# Ascent seed data

This repository holds sourced reference data as JSON and YAML `micharisma-seeds/v1` manifests.

Start with these contributor instructions:

- [Entity catalog](catalog/README.md) to find existing codes by entity type and state, with source-file links.
- [Minimum working examples](examples/README.md) for countries, states, districts, branches, offices, elections, races, people, candidacies, and accounts in YAML and JSON.
- [WORKERS.md](WORKERS.md) for the account and image contribution workflow, owner-code export, and validation commands.
- [CONTRIBUTING.md](CONTRIBUTING.md) for record fields, entity-code rules, source requirements, and import behavior.
- [Published schemas](schemas/README.md) for the machine-readable contract and maintainer regeneration.
- [AGENTS.md](AGENTS.md) for automated contributors' working instructions.

Image contributors submit original image URLs and `ImagePlacement` records. The app stores uploaded files and creates thumbnails through Active Storage. OpenAI portrait generation remains disabled pending legal review.

After the Python setup in [WORKERS.md](WORKERS.md#set-up-validation), search without Rails or a database:

```sh
.venv/bin/python tools/seed_contract.py lookup Albany --type County --state NY
.venv/bin/python tools/seed_contract.py lookup 01001 --type County --format json
```

A nonzero exit means the lookup failed or no records matched. The first command returns Albany County's entity code and FIPS. The second returns Autauga County with `fips: "01001"`.
