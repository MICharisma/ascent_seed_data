#!/usr/bin/env python3
"""Validate seed contributions and export candidate owner codes without Rails."""

import argparse
import datetime
import json
import math
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

import reference_catalog

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas" / "v1"


class StrictLoader(getattr(yaml, "CSafeLoader", yaml.SafeLoader)):
    def construct_mapping(self, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            if key_node.value == "<<":
                raise ValueError("YAML merge keys are unsupported; use scope/groups")
            key = self.construct_object(key_node, deep=deep)
            if type(key) not in (str, int):
                raise ValueError("mapping keys must be strings (registry numbers may be integers)")
            if key in result:
                raise ValueError(f"duplicate key {key!r} at line {key_node.start_mark.line + 1}")
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def portable(value):
    if isinstance(value, dict):
        result = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError("manifest mapping keys must be strings; quote numeric keys")
            result[key] = portable(item)
        return result
    if isinstance(value, list):
        return [portable(item) for item in value]
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("non-finite numbers are unsupported")
    if type(value) not in (str, int, float, bool, type(None)):
        raise ValueError(f"unsupported value type {type(value).__name__}")
    return value


def load_document(path):
    text = Path(path).read_text(encoding="utf-8")
    if "<%" in text:
        raise ValueError("ERB is unsupported")
    if Path(path).suffix.lower() == ".json":
        value = json.loads(text, object_pairs_hook=unique_object)
    else:
        if any(isinstance(event, yaml.AliasEvent) for event in yaml.parse(text, Loader=StrictLoader)):
            raise ValueError("YAML aliases are unsupported; use scope/groups")
        value = yaml.load(text, Loader=StrictLoader)
    return portable(value)


def validator(name):
    schema = json.loads((SCHEMAS / name).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    resources = [json.loads(path.read_text()) for path in SCHEMAS.glob("*.schema.json")]
    registry = Registry().with_resources((item["$id"], Resource.from_contents(item)) for item in resources)
    return Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())


def validate_file(path, schema):
    document = load_document(path)
    errors = list(schema.iter_errors(document))
    if errors:
        diagnostics = []
        for error in errors:
            if error.validator == "oneOf" and isinstance(error.instance, dict):
                selected = next((i for i, branch in enumerate(error.schema["oneOf"])
                                 if branch.get("properties", {}).get("type", {}).get("const") == error.instance.get("type")), None)
                children = [child for child in error.context if child.schema_path[0] == selected]
                diagnostics.extend(children or [error])
            else:
                diagnostics.append(error)
        for error in diagnostics[:8]:
            pointer = "/" + "/".join(map(str, error.absolute_path))
            print(f"{path}:{pointer}: {error.message[:240]}", file=sys.stderr)
        raise ValueError(f"{len(errors)} schema violation(s)")
    return document


def manifest_files(paths):
    files = set()
    for path in paths:
        files.update(item for item in (path.rglob("*") if path.is_dir() else [path])
                     if item.suffix.lower() in {".json", ".yaml", ".yml"})
    return sorted(files)


def catalog(root):
    index = {}

    def collect(container, path, scope):
        scope = scope | container.get("scope", {})
        for row in container.get("records", []):
            code = row["code"]
            entry = index.setdefault(code, {"code": code, "type": row["type"], "attributes": {},
                                            "references": {}, "aliases": [], "files": []})
            if entry["type"] != row["type"]:
                raise ValueError(f"{code} names multiple entity types")
            if row["type"] == "Channel":
                owner = (scope | row.get("scope", {}) | row.get("references", {})).get("owner")
                existing_owner = entry["references"].get("owner")
                if existing_owner and owner and reference_code(existing_owner) != reference_code(owner):
                    raise ValueError(f"{path}: contradictory {code} owner across seed definitions")
            for field, value in row.get("attributes", {}).items():
                if field in entry["attributes"] and entry["attributes"][field] != value:
                    raise ValueError(f"{path}: contradictory {code} attribute {field} across seed definitions")
                entry["attributes"][field] = value
            entry["references"].update(scope | row.get("scope", {}) | row.get("references", {}))
            entry["aliases"] = sorted(set(entry["aliases"]) | set(row.get("aliases", [])))
            entry["files"].append(str(path.relative_to(root)))
        for group in container.get("groups", []):
            collect(group, path, scope)

    files = manifest_files([root])
    if not files:
        raise ValueError(f"No catalog manifests found in {root}")
    for path in files:
        document = load_document(path)
        if document.get("format") != "micharisma-seeds/v1" or document.get("catalog") != "ASC" or document.get("namespace") != "MIC":
            raise ValueError(f"{path}: expected an MIC/ASC seed manifest")
        collect(document, path, {})
    accounts = {}
    for code, row in index.items():
        if row["type"] == "Channel":
            key = tuple(row["attributes"].get(field) for field in ("platform", "handle"))
            if key in accounts and accounts[key] != code:
                raise ValueError(f"Account has multiple codes {accounts[key]} and {code}; request maintainer review")
            accounts[key] = code
    return index


def reference_code(value):
    return value.get("code") if isinstance(value, dict) else value


def owners(index):
    for code, row in sorted(index.items()):
        if row["type"] not in {"Person", "Candidacy"}:
            continue
        person_code = code if row["type"] == "Person" else reference_code(row["references"].get("person"))
        person = index.get(person_code, {}).get("attributes", {})
        yield {"code": code, "type": row["type"],
               "name": " ".join(person[key] for key in ("first_name", "middle_name", "last_name") if person.get(key)),
               "person": person_code, "race": reference_code(row["references"].get("race")),
               "files": sorted(set(row["files"]))}


def check_accounts(documents, index):
    channels = {code: row for code, row in index.items() if row["type"] == "Channel"}
    accounts = {(row["attributes"].get("platform"), row["attributes"].get("handle")): code
                for code, row in channels.items()}
    seen = set()
    for path, document in documents:
        for row in document["records"]:
            code = row["code"]
            owner = row["references"]["owner"]
            if owner not in index or index[owner]["type"] not in {"Person", "Candidacy"}:
                raise ValueError(f"{path}: {owner} is not an existing full Person or Candidacy code")
            if code in seen:
                raise ValueError(f"{path}: duplicate submitted channel code {code}")
            seen.add(code)
            if code in index and index[code]["type"] != "Channel":
                raise ValueError(f"{path}: {code} already names another entity type")
            key = tuple(row["attributes"][field] for field in ("platform", "handle"))
            if key in accounts and accounts[key] != code:
                raise ValueError(f"{path}: account already uses {accounts[key]}; reuse that code")
            existing = channels.get(code)
            if existing:
                for field, value in row["attributes"].items():
                    current = existing["attributes"].get(field)
                    if current is not None and current != value:
                        raise ValueError(f"{path}: {code} conflicts with existing {field}; request maintainer review")
                current_owner = reference_code(existing["references"].get("owner"))
                if current_owner and current_owner != owner:
                    raise ValueError(f"{path}: {code} already belongs to {current_owner}; request maintainer review")
            channels[code] = row
            accounts[key] = code


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "accounts"):
        check = commands.add_parser(command)
        check.add_argument("paths", nargs="+", type=Path)
    commands.add_parser("owners")
    export = commands.add_parser("export-catalog")
    export.add_argument("--check", action="store_true")
    lookup = commands.add_parser("lookup")
    lookup.add_argument("query", nargs="?", default="")
    lookup.add_argument("--type", dest="entity_type")
    lookup.add_argument("--state")
    lookup.add_argument("--format", choices=("table", "json"), default="table")
    args = parser.parse_args(argv)
    if args.command == "export-catalog":
        count = reference_catalog.export(catalog(ROOT / "manifests"), ROOT / "catalog", check=args.check)
        print(f"{'Checked' if args.check else 'Exported'} {count} catalog records.")
        return 0
    if args.command == "lookup":
        rows = reference_catalog.lookup(ROOT / "catalog", args.query, args.entity_type, args.state)
        if not rows:
            print("No catalog records match.", file=sys.stderr)
            return 1
        print(reference_catalog.display(rows, args.format))
        return 0
    if args.command == "owners":
        rows = list(owners(catalog(ROOT / "manifests")))
        if not rows:
            raise ValueError("No candidate owners found")
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return 0
    files = manifest_files(args.paths)
    if not files:
        print("No manifest files found.", file=sys.stderr)
        return 1
    schema = validator("asc.schema.json")
    account_schema = validator("candidate-accounts.schema.json")
    documents = []
    account_documents = []
    failed = 0
    for path in files:
        try:
            is_account = args.command == "accounts" or "candidate_accounts" in path.parts
            document = validate_file(path, account_schema if is_account else schema)
            documents.append((path, document))
            if is_account:
                account_documents.append((path, document))
        except (ValueError, yaml.YAMLError, OSError) as error:
            print(f"{path}: {error}", file=sys.stderr)
            failed += 1
    if account_documents and not failed:
        try:
            check_accounts(account_documents, catalog(ROOT / "manifests"))
        except (ValueError, yaml.YAMLError, OSError) as error:
            print(str(error), file=sys.stderr)
            failed += 1
    print(f"Checked {len(files)} manifest(s), {sum(len(doc.get('records', [])) for _, doc in documents)} top-level record(s); {failed} failed. No data was imported.")
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, yaml.YAMLError, OSError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
