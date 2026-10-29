"""Build contributor lookups from manifests, independently of any app database."""

import csv
import io
import json
from collections import defaultdict
from pathlib import Path


def entries(index):
    bindings = {code: code for code in index}
    for code, row in index.items():
        for alias in row.get("aliases", []):
            if alias in bindings and bindings[alias] != code:
                raise ValueError(f"Alias {alias} identifies both {bindings[alias]} and {code}")
            bindings[alias] = code

    def resolve(code):
        return index.get(bindings.get(code, code), {})

    def name(code, visited=frozenset()):
        if code in visited:
            return code
        row = resolve(code)
        attributes = row.get("attributes", {})
        if row.get("type") == "Person":
            return " ".join(attributes[key] for key in ("first_name", "middle_name", "last_name") if attributes.get(key)) or code
        for key in ("name", "title", "alt_text", "handle"):
            if attributes.get(key):
                return str(attributes[key])
        refs = references(row)
        keys = {"Office": ("position", "jurisdiction"), "Race": ("office", "election"),
                "Candidacy": ("person", "race"), "ImagePlacement": ("image", "subject")}.get(row.get("type"), ())
        parts = [name(refs[key], visited | {code}) for key in keys if refs.get(key)]
        return " · ".join(parts) or code

    def states(code, visited=frozenset()):
        if code in visited:
            return set()
        row = resolve(code)
        if row.get("type") == "State":
            return {row["code"]}
        return set().union(*(states(value, visited | {code}) for value in references(row).values()))

    result = []
    for code, row in sorted(index.items()):
        result.append({"code": code, "type": row["type"], "name": name(code),
                       "states": sorted(states(code)), "fips": row["attributes"].get("fips"),
                       "aliases": sorted(row.get("aliases", [])), "references": references(row),
                       "files": sorted({f"manifests/{path}" for path in row["files"]})})
    return result


def references(row):
    return {key: value.get("code") if isinstance(value, dict) else value
            for key, value in sorted(row.get("references", {}).items()) if value}


def export(index, directory, check=False):
    rows = entries(index)
    if not rows:
        raise ValueError("Cannot export an empty catalog")
    outputs = {}
    groups = defaultdict(list)
    for row in rows:
        for state in row["states"] or ["all"]:
            groups[(row["type"], state)].append(row)
    summary = ["# Entity catalog", "", "Generated from the seed manifests. Edit the source manifests, then run",
               "`.venv/bin/python tools/seed_contract.py export-catalog` from the repository root.",
               "Use the [Python setup](../WORKERS.md#set-up-validation) before running these commands.", "",
               "These records are defined in the repository. This catalog does not report database imports.", "",
               "Search with `.venv/bin/python tools/seed_contract.py lookup Albany --type County --state NY`.",
               "State filters follow manifest scope and references. For people, they do not establish residence.", "",
               "Each CSV includes entity codes, names, state codes, FIPS, aliases, references, and source paths.",
               "Use `--format json` with `lookup` to export matching records as JSON.", "",
               "| Type | State entity code | Records | Browse | Sources |",
               "| --- | --- | ---: | --- | --- |"]
    for (entity_type, state), selected in sorted(groups.items()):
        relative = f"{entity_type}/{state}.csv"
        stream = io.StringIO(newline="")
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["Entity code", "Name", "State entity codes", "FIPS", "Aliases", "References and scope", "Source files"])
        for row in selected:
            writer.writerow([row["code"], row["name"], "; ".join(row["states"]), row["fips"], "; ".join(row["aliases"]),
                             json.dumps(row["references"], ensure_ascii=False, sort_keys=True), "; ".join(row["files"])])
        outputs[relative] = stream.getvalue()
        sources = sorted({source for row in selected for source in row["files"]})
        links = ", ".join(f"[{source.removeprefix('manifests/')}](../{source})" for source in sources)
        summary.append(f"| {entity_type} | {state if state != 'all' else 'Unscoped'} | {len(selected)} | [CSV]({relative}) | {links} |")
    outputs["README.md"] = "\n".join(summary) + "\n"
    directory = Path(directory)
    existing = {path.relative_to(directory).as_posix() for path in directory.rglob("*") if path.is_file()}
    if check:
        stale = [path for path, content in outputs.items() if not (directory / path).is_file()
                 or (directory / path).read_text() != content]
        stale.extend(existing - outputs.keys())
        if stale:
            raise ValueError("Stale catalog files: " + ", ".join(sorted(stale)))
    else:
        for path in existing - outputs.keys():
            (directory / path).unlink()
        for path, content in outputs.items():
            target = directory / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
    return len(rows)


def lookup(path, query="", entity_type=None, state=None):
    rows_by_code = {}
    for file in sorted(Path(path).glob("*/*.csv")):
        with file.open(newline="") as stream:
            for row in csv.DictReader(stream):
                rows_by_code[row["Entity code"]] = {"code": row["Entity code"], "type": file.parent.name, "name": row["Name"],
                    "states": row["State entity codes"].split("; ") if row["State entity codes"] else [],
                    "fips": row["FIPS"] or None, "aliases": row["Aliases"].split("; ") if row["Aliases"] else [],
                    "references": json.loads(row["References and scope"]), "files": row["Source files"].split("; ")}
    rows = [row for _, row in sorted(rows_by_code.items())]
    if not rows:
        raise ValueError("Catalog is missing or empty; run export-catalog")
    types = {row["type"].casefold() for row in rows}
    if entity_type and entity_type.casefold() not in types:
        raise ValueError(f"Unknown entity type {entity_type}")
    states = {code for row in rows for code in row["states"]}
    matching_states = {code for code in states if state and (code.casefold() == state.casefold()
                      or code.rsplit("-", 1)[-1].casefold() == state.casefold())}
    if state and not matching_states:
        raise ValueError(f"Unknown state {state}")
    return [row for row in rows if (not entity_type or row["type"].casefold() == entity_type.casefold())
            and (not state or matching_states.intersection(row["states"]))
            and query.casefold() in " ".join([row["code"], row["name"], row["fips"] or "", *row["aliases"]]).casefold()]


def display(rows, format):
    if format == "json":
        return json.dumps(rows, ensure_ascii=False, indent=2)
    lines = ["Entity code\tName\tState entity codes\tFIPS\tSource files"]
    lines.extend("\t".join([row["code"], row["name"], ", ".join(row["states"]), row["fips"] or "", ", ".join(row["files"])]) for row in rows)
    return "\n".join(lines)
