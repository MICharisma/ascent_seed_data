# Contributing seed data to Ascent

Ascent's reference data — places, offices, elections, races, candidates, the issue library, and campaign communications — lives here as `micharisma-seeds/v1` manifests. Contributions arrive as pull requests that add manifests.

## Where to put a contribution

- `manifests/contributions/<your-organization>/` for stances, communications, stance evidence, channels, and new approaches. File names carry no meaning; organize them however suits you.
- Do not edit `manifests/2026/` or `conversion/`: they are generated from the sourced ballot rows in `races/`. Report a problem with those rows instead.

## Writing a manifest

Every file starts with the envelope and lists records by type and code:

```yaml
format: micharisma-seeds/v1
namespace: MIC
catalog: ASC
source:
  contributor: Your Organization
  url: https://example.org/where-you-found-it
  captured_on: "2026-10-15"
records:
  - type: StanceEvidence
    code: EVIDENCE-...
    attributes: {relation: states, quote: "A short quote.", offset_seconds: 102}
    references:
      stance: STANCE-...
      communication: COMMUNICATION-...
```

- **Refer to existing records by their codes.** Candidacies, races, people, and approaches already have codes in this repository; never use database IDs.
- **Codes** are uppercase letters, digits, dashes, and underscores. The recipes are in `doc/entity_code_plan.md` and `doc/communications_plan.md` in the Ascent repository: for example `STANCE-{candidacy path}-{approach path}` and `COMMUNICATION-{channel path}-{date}-{slug}`.
- **Each piece of evidence is its own record**, so you can add evidence to an existing stance without redefining it.
- **Allowed types, fields, and values** are listed in `schemas/asc.contract.json` and enforced by `schemas/v1/asc.schema.json`.

## Sources and content

- Stances, communications, and evidence need a source in the `source` block.
- Link to communications; never upload video or full transcripts. Quotes are at most 300 characters. Record a deleted or edited post with `availability: removed` or `edited` and an `archived_url`.
- Never attach invented positions or quotes to a real person.

## Checking your files

Validate each manifest against `schemas/v1/asc.schema.json` with any JSON Schema (Draft 2020-12) validator; YAML files can be converted to JSON first. Maintainers also run Ascent's `bin/rails seed_library:validate`, which additionally checks references and contradictory definitions.

## What happens on merge

The importer creates records that don't exist yet, never overwrites a reviewed value, and reports any disagreement for a maintainer to resolve.
