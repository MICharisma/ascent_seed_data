# Add existing candidates' accounts

Use this guide to submit verified websites and social accounts for people already in Ascent. The files use the existing `micharisma-seeds/v1` format and import as `Channel` records.

## Set up validation

Run these commands from this data repository with Python 3.10 or later:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r tools/requirements.txt
```

These commands create a local environment and install the validator's dependencies. A nonzero exit means setup failed. Validation runs offline after installation, with no Rails checkout, private library, credentials, or database.

## Find the owner codes

Export the current repository's people and candidacies:

```sh
.venv/bin/python tools/seed_contract.py owners > /tmp/ascent-candidate-owners.json
```

A nonzero exit means export failed. The output is a nonempty JSON array with `code`, `type`, `name`, `person`, `race`, and source `files`. Use `race` to distinguish a person's campaigns. For example, the current New York statewide manifest defines `PERSON-JAMES_LT_5Y` and `CANDIDACY-USA-NY-ATTORNEY_GENERAL-2026_GENERAL-JAMES_LT_5Y`. Read the current export rather than copying codes from prose.

Use the full local code, including the person's disambiguator. Do not use database IDs, page URLs, name-only shortcuts, or the `MIC-ASC-` URI prefix. Do not create another Person or Candidacy to attach an account. If the owner is missing or ambiguous, report that gap to the maintainer.

## Verify each account

Read the candidate's official website, campaign website, or another first-party source that links to the account. Record that source URL, the date you inspected it, and a short `verification_note` describing the evidence. A matching name or platform badge alone does not establish ownership.

Choose the owner according to the account's scope:

- Use a `PERSON-...` code for the person's continuing public account, including an account they use across campaigns.
- Use a `CANDIDACY-...` code when the account belongs to that specific campaign. Verify the office and election year.

Keep one account under one owner. Do not duplicate the same personal account for every campaign. The candidacy page already includes its person's official accounts alongside the campaign's accounts.

Submit only verified official accounts through this worker contract. Omit accounts you cannot verify and report the reason separately. Do not guess handles, invent websites, treat supporter accounts as official, or infer positions or endorsements from an account's existence. Source accuracy and the Person-versus-Candidacy choice require human review; validation cannot establish either.

## Write the contribution

Copy [the YAML template](examples/candidate_accounts.yml) or [the equivalent JSON template](examples/candidate_accounts.json). Both templates are fictional and live outside the imported `manifests/` tree. Replace every example account, owner, source, and verification note before submission. Their owners intentionally do not exist in the catalog, so the `accounts` check rejects the unchanged templates.

Put the completed files in `manifests/contributions/<your-worker>/candidate_accounts/`. Use any file names with `.yml`, `.yaml`, or `.json` extensions. Keep all account submissions in that directory so the repository check applies the worker contract automatically.

Each record requires:

- `type: Channel` and an uppercase `CHANNEL-...` code. Follow the platform and handle code recipes in [CONTRIBUTING.md](CONTRIBUTING.md#channel-one-account).
- `attributes.platform`, `attributes.handle`, `attributes.url`, and `attributes.official: true`. The supported platforms come from the general Ascent schema. Use `other` for a platform outside that list.
- `references.owner` containing an existing full Person or Candidacy code.
- A per-record `source` with `contributor`, `url`, `captured_on` in `YYYY-MM-DD` form, and `verification_note`.

Preserve the handle's spelling and case, without its leading `@`. A website's handle is its host and any path. Use an HTTP or HTTPS profile URL, rather than a single post. The account URL and evidence URL can differ.

Search existing Channel records before choosing a code. The pair `platform` and `handle` identifies an account, and the validator compares that pair exactly, as the importer does. Reuse an existing account's code. An unchanged record can be imported repeatedly. If an existing owner, handle, URL, or official status disagrees, request maintainer review instead of inventing another code or moving the account. Alias changes require the general contribution workflow.

The worker subset permits only flat Channel records with explicit owners and per-record sources. Use [the general contract](CONTRIBUTING.md) for posts, videos, party accounts, new people, aliases, and stance evidence. An account by itself does not create a Communication or a stance.

## Validate before submission

Check your completed folder, replacing `your-worker` with its actual name:

```sh
.venv/bin/python tools/seed_contract.py accounts manifests/contributions/your-worker/candidate_accounts
```

A nonzero exit or a nonzero `failed` count means validation failed. The command reports the number of files and records checked, and rejects an empty or missing selection. It checks the published schema, existing full owner codes, duplicate submitted codes, duplicate accounts, and conflicts with existing Channels. It does not modify or import data.

Check all manifests and examples before opening a pull request:

```sh
.venv/bin/python tools/seed_contract.py validate manifests examples
```

A nonzero exit or a nonzero `failed` count means validation failed. Files in a `candidate_accounts` directory receive the stricter account checks. Other files receive the general Ascent schema checks. GitHub Actions runs this command and the validator tests on pull requests.

The parser rejects duplicate keys, YAML aliases and merge keys, custom tags, multiple YAML documents, ERB, and non-finite numbers. YAML and JSON use the same schema. The worker schema is [schemas/v1/candidate-accounts.schema.json](schemas/v1/candidate-accounts.schema.json), a stricter subset of the generated Ascent schema. Do not edit the generated general schema to bypass an error.

Submit the new files in a pull request to this data repository. Leave generated ballot manifests unchanged. Maintainers run the Rails importer checks and review ownership evidence before importing. Source metadata stays in the seed file; Channel stores the profile fields and owner, not a separate database verification record.
