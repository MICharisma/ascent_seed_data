#!/usr/bin/env python3
"""Validate seed contributions and export candidate owner codes without Rails."""

import argparse
import datetime
import hashlib
import json
import math
from pathlib import Path
import re
import sys
import unicodedata

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

import reference_catalog

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas" / "v1"
PERSON_CODE_RE = re.compile(r"^PERSON-[A-Z0-9]+(?:_[A-Z0-9]+)*_[2-9][A-HJ-NP-Z]$")
DISAMBIGUATORS = [f"{digit}{letter}" for digit in "23456789" for letter in "abcdefghjklmnpqrstuvwxyz"]
SUFFIX_RE = re.compile(r"^(?:jr|sr|ii|iii|iv|v|esq|esquire)\.?$", re.I)
TRANSLIT = str.maketrans({"ł": "l", "Ł": "L", "ø": "o", "Ø": "O", "ß": "ss", "æ": "ae", "Æ": "AE", "œ": "oe", "Œ": "OE", "đ": "d", "Đ": "D"})


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
        if "*" in text and any(isinstance(event, yaml.AliasEvent) for event in yaml.parse(text, Loader=StrictLoader)):
            raise ValueError("YAML aliases are unsupported; use scope/groups")
        value = yaml.load(text, Loader=StrictLoader)
    return portable(value)


def validator(name):
    schema = json.loads((SCHEMAS / name).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    resources = [json.loads(path.read_text()) for path in SCHEMAS.glob("*.schema.json")]
    registry = Registry().with_resources((item["$id"], Resource.from_contents(item)) for item in resources)
    return Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())


def validate_person_record(row):
    code = row.get("code", "")
    if not PERSON_CODE_RE.match(code):
        raise ValueError(f"Person definition {code} requires a disambiguator; bare name codes are allowed only as references")
    username = row.get("attributes", {}).get("username")
    expected_username = code.removeprefix("PERSON-").lower()
    if username is not None and username != expected_username:
        raise ValueError(f"Person definition {code} username {username!r} must match {expected_username!r}")


def iter_person_records(container):
    for row in container.get("records", []):
        if row.get("type") == "Person":
            yield row
    for group in container.get("groups", []):
        yield from iter_person_records(group)


def validate_people(document):
    seen = set()
    for row in iter_person_records(document):
        validate_person_record(row)
        code = row["code"]
        if code in seen:
            raise ValueError(f"duplicate Person definition {code}")
        seen.add(code)


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
    validate_people(document)
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
            if row["type"] == "Person":
                validate_person_record(row)
            entry = index.setdefault(code, {"code": code, "type": row["type"], "attributes": {},
                                            "references": {}, "aliases": [], "files": []})
            if entry["type"] != row["type"]:
                raise ValueError(f"{code} names multiple entity types")
            if row["type"] == "Person" and entry["files"]:
                raise ValueError(f"{path}: duplicate Person definition {code} (already defined in {entry['files'][0]})")
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


def person_full_name(attributes):
    return " ".join(attributes[key] for key in ("first_name", "middle_name", "last_name") if attributes.get(key))


def slug(text):
    decomposed = "".join(c for c in unicodedata.normalize("NFKD", str(text or "").translate(TRANSLIT)) if not unicodedata.combining(c))
    ascii_text = decomposed.encode("ascii", "replace").decode("ascii").lower().replace("'", "")
    return re.sub(r"[^a-z0-9]+", "_", ascii_text).strip("_")


def name_parts(printed_name):
    words = str(printed_name or "").split()
    if not words:
        raise ValueError("printed name is required")
    suffix = words.pop() if len(words) > 2 and SUFFIX_RE.match(words[-1]) else None
    last_word = words.pop()
    last_name = f"{last_word} {suffix}" if suffix else last_word
    first_name = words.pop(0) if words else None
    middle_name = " ".join(words) or None
    return {"first_name": first_name, "middle_name": middle_name, "last_name": last_name}


def given_letters(first_name):
    letters = slug(first_name).replace("_", "")
    if not letters:
        return ""
    consonant = next((ch for ch in letters[1:] if ch not in "aeiou0123456789"), None)
    return letters[0] + (consonant if consonant is not None else letters[1:2])


def name_code(printed_name):
    parts = name_parts(printed_name) if isinstance(printed_name, str) else printed_name
    surname_words = (parts.get("last_name") or "").replace(",", "").split()
    if len(surname_words) > 1 and SUFFIX_RE.match(surname_words[-1]):
        surname_words.pop()
    surname = slug(surname_words[-1] if surname_words else "")
    given = given_letters(parts.get("first_name"))
    return "_".join(part for part in (surname, given) if part)


def first_appearance_facts(state, election_date, printed_name, printed_office):
    state_code = str(state or "").strip().upper().removeprefix("STATE-USA-")
    date_text = " ".join(str(election_date or "").split())
    name_text = " ".join(str(printed_name or "").split())
    office_text = " ".join(str(printed_office or "").split())
    if not state_code or not date_text or not name_text or not office_text:
        raise ValueError("state, election_date, printed_name, and printed_office are required")
    return f"{state_code} | {date_text} | {name_text} | {office_text}"


def mint_username(base, state, election_date, printed_name, printed_office, taken=()):
    normalized_base = str(base or "").strip().removeprefix("PERSON-").lower()
    if not re.match(r"^[a-z0-9]+(?:_[a-z0-9]+)*$", normalized_base) or PERSON_CODE_RE.match(f"PERSON-{normalized_base.upper()}"):
        raise ValueError(f"invalid name code {base!r}")
    facts = first_appearance_facts(state, election_date, printed_name, printed_office)
    taken_set = {str(item).strip().removeprefix("PERSON-").lower() for item in taken}
    start = int(hashlib.sha256(facts.encode("utf-8")).hexdigest(), 16) % len(DISAMBIGUATORS)
    for offset in range(len(DISAMBIGUATORS)):
        candidate = f"{normalized_base}_{DISAMBIGUATORS[(start + offset) % len(DISAMBIGUATORS)]}"
        if candidate not in taken_set:
            return candidate
    raise ValueError(f"All {len(DISAMBIGUATORS)} disambiguators are taken for PERSON-{normalized_base.upper()}")


def taken_usernames(root=ROOT, index=None):
    index = catalog(root / "manifests") if index is None else index
    taken = set()
    for code, row in index.items():
        if row["type"] == "Person":
            taken.add(code.removeprefix("PERSON-").lower())
            for alias in row.get("aliases", []):
                if alias.startswith("PERSON-"):
                    taken.add(alias.removeprefix("PERSON-").lower())
    conversion = root / "conversion"
    if conversion.is_dir():
        for path in sorted(conversion.glob("*/*/usernames.yml")):
            mapping = load_document(path) or {}
            taken.update(str(value).strip().removeprefix("PERSON-").lower() for value in mapping.values())
    return taken


def existing_people_for_name_code(index, base):
    prefix = f"PERSON-{str(base).strip().removeprefix('PERSON-').upper()}"
    races_by_person = {}
    for row in index.values():
        if row["type"] == "Candidacy":
            person_code = reference_code(row["references"].get("person"))
            race_code = reference_code(row["references"].get("race"))
            if person_code and race_code:
                races_by_person.setdefault(person_code, set()).add(race_code)
    matches = []
    for code, row in sorted(index.items()):
        if row["type"] == "Person" and code.rsplit("_", 1)[0] == prefix and PERSON_CODE_RE.match(code):
            matches.append({
                "code": code,
                "username": code.removeprefix("PERSON-").lower(),
                "name": person_full_name(row.get("attributes", {})),
                "races": sorted(races_by_person.get(code, ())),
                "files": sorted(set(row.get("files", ()))),
            })
    return matches


def format_existing_people(base_code, existing):
    lines = [f"Existing people sharing {base_code}:"]
    for item in existing:
        races = ", ".join(item["races"]) if item["races"] else "no candidacy recorded"
        lines.append(f"  - {item['code']}: {item['name']} ({races})")
    return "\n".join(lines)


def mint_person_code(state, election_date, printed_name, printed_office, base=None,
                     is_new=False, same_as=None, index=None, taken=None, interactive=False):
    if is_new and same_as:
        raise ValueError("Pass either --new or --same-as, not both")
    index = catalog(ROOT / "manifests") if index is None else index
    resolved_base = (base.strip().removeprefix("PERSON-").lower() if base else name_code(printed_name))
    base_code = f"PERSON-{resolved_base.upper()}"
    facts = first_appearance_facts(state, election_date, printed_name, printed_office)
    existing = existing_people_for_name_code(index, resolved_base)
    if same_as:
        target = same_as.strip().upper()
        if not target.startswith("PERSON-"):
            target = f"PERSON-{target}"
        matched = next((item for item in existing if item["code"] == target), None)
        if not matched:
            raise ValueError(f"{target} is not an existing Person sharing {base_code}")
        return {"code": matched["code"], "username": matched["username"], "name_code": base_code,
                "facts": facts, "resolution": "existing", "existing": existing}
    if existing and not is_new:
        summary = format_existing_people(base_code, existing)
        if interactive:
            print(summary, file=sys.stderr)
            print("Enter 'new' or an existing PERSON-... code: ", end="", file=sys.stderr, flush=True)
            answer = sys.stdin.readline().strip()
            normalized = re.sub(r"^same\s+as\s+", "", answer, flags=re.I).strip()
            if normalized.lower() == "new":
                is_new = True
            else:
                target = normalized.upper()
                if target and not target.startswith("PERSON-"):
                    target = f"PERSON-{target}"
                matched = next((item for item in existing if item["code"] == target), None)
                if matched:
                    return {"code": matched["code"], "username": matched["username"], "name_code": base_code,
                            "facts": facts, "resolution": "existing", "existing": existing}
                raise ValueError(f"{summary}\nSpecify --new or --same-as PERSON-...")
        else:
            raise ValueError(f"{summary}\nSpecify --new or --same-as PERSON-...")
    all_taken = taken_usernames(ROOT, index=index) if taken is None else set(taken)
    all_taken.update(item["username"] for item in existing)
    username = mint_username(resolved_base, state, election_date, printed_name, printed_office, taken=all_taken)
    return {"code": f"PERSON-{username.upper()}", "username": username, "name_code": base_code,
            "facts": facts, "resolution": "new", "existing": existing}


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


def check_duplicate_people(documents):
    seen = {}
    examples_root = (ROOT / "examples").resolve()
    for path, document in documents:
        resolved = path.resolve()
        if resolved.is_relative_to(examples_root):
            continue
        for row in iter_person_records(document):
            code = row["code"]
            if code in seen and seen[code].with_suffix("") != resolved.with_suffix(""):
                raise ValueError(f"{path}: duplicate Person definition {code} (already defined in {seen[code]})")
            seen[code] = resolved


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
    mint = commands.add_parser("mint")
    mint.add_argument("--state", required=True)
    mint.add_argument("--date", dest="election_date", required=True)
    mint.add_argument("--name", dest="printed_name", required=True)
    mint.add_argument("--office", dest="printed_office", required=True)
    mint.add_argument("--name-code", dest="base")
    resolution = mint.add_mutually_exclusive_group()
    resolution.add_argument("--new", dest="is_new", action="store_true")
    resolution.add_argument("--same-as")
    mint.add_argument("--format", choices=("text", "json"), default="text")
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
    if args.command == "mint":
        result = mint_person_code(
            args.state, args.election_date, args.printed_name, args.printed_office,
            base=args.base, is_new=args.is_new, same_as=args.same_as, interactive=sys.stdin.isatty()
        )
        if args.format == "json":
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(result["code"])
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
    if not failed:
        try:
            check_duplicate_people(documents)
            manifests_root = (ROOT / "manifests").resolve()
            in_manifests = any(path.resolve().is_relative_to(manifests_root) for path, _ in documents)
            if account_documents or in_manifests:
                index = catalog(ROOT / "manifests")
                if account_documents:
                    check_accounts(account_documents, index)
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
