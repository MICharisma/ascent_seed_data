# Seed contribution instructions

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [WORKERS.md](WORKERS.md) before writing manifests. These documents and the published schemas define the contribution format.

- Use the [minimum working examples](examples/README.md) when defining a new place or election graph. The account and image workflows in WORKERS.md attach data to candidates that already exist.
- Put contributions under `manifests/contributions/<your-worker>/`. Keep verified official Channel records in `candidate_accounts/`; keep Image and ImagePlacement records in `profile_images/`.
- Export and reuse existing full Person and Candidacy entity codes. When adding a new `Person` definition, mint a full disambiguated code with `tools/seed_contract.py mint --state <STATE> --date <YYYY-MM-DD> --name "<Printed Name>" --office "<Printed Office>"` (`--new` or `--same-as PERSON-...` when the name code is shared); bare name codes are allowed only as references, never on `Person` definitions. Do not use database IDs or create duplicate owners to attach accounts or images. Report missing or ambiguous owners.
- Use `tools/seed_contract.py lookup` or `catalog/README.md` for existing place, position, office, race, and policy codes. County geographic identifiers use `attributes.fips`, as quoted five-digit strings.
- Regenerate `catalog/` with `tools/seed_contract.py export-catalog` after manifest changes. Do not hand-edit generated catalog files. Run `export-catalog --check` before submission.
- Check existing account and image records before choosing codes. Reuse a Channel for the same platform and handle, and an Image for the same original URL. Add a distinct ImagePlacement for each subject using an image.
- Record the source URL, contributor, and capture date. Verify account ownership from first-party evidence. Preserve image credits and source-page URLs. Do not invent positions, quotes, or endorsements.
- Submit original image links and metadata. Do not commit image binaries, thumbnails, blobs, signed upload IDs, API keys, or local storage paths to this data repository. Active Storage attachments belong to the app.
- Keep OpenAI portrait generation disabled pending legal review. Do not change activation flags or add portrait-generation API calls, jobs, or scripts as part of a seed contribution.
- Leave generated `manifests/2026/`, `conversion/`, and generated schema files unchanged. Report source-data problems or contract gaps to the maintainer.
- Run the applicable checks in WORKERS.md before submission. Report which files and records were checked, unresolved references, and verification gaps. General schema validation does not establish image ownership, confirm image references exist, download images, or import records.
