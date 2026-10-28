# Ascent seed data

This repository holds sourced reference data as JSON and YAML `micharisma-seeds/v1` manifests.

Start with these contributor instructions:

- [Minimum working examples](examples/README.md) for countries, states, districts, branches, offices, elections, races, people, candidacies, and accounts in YAML and JSON.
- [WORKERS.md](WORKERS.md) for the account and image contribution workflow, owner-code export, and validation commands.
- [CONTRIBUTING.md](CONTRIBUTING.md) for record fields, entity-code rules, source requirements, and import behavior.
- [Published schemas](schemas/README.md) for the machine-readable contract and maintainer regeneration.
- [AGENTS.md](AGENTS.md) for automated contributors' working instructions.

Image contributors submit original image URLs and `ImagePlacement` records. The app stores uploaded files and creates thumbnails through Active Storage. OpenAI portrait generation remains disabled pending legal review.
