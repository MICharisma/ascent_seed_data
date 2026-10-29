# Contributing seed data to Ascent

Ascent's reference data includes places, offices, elections, races, candidates, the issue library, campaign communications, and image metadata. It lives here as JSON or YAML `micharisma-seeds/v1` manifests. Contributions arrive as pull requests that add manifests. Start with [WORKERS.md](WORKERS.md) for the account and image workflow.

For a new election graph, start with the paired [minimum YAML/JSON examples](examples/README.md#minimum-election-graph). They cover the place hierarchy, branch, office, election, race, person, candidacy, and account dependencies. The example guide also documents the existing Year prerequisite and all three branch values.

## Where to put a contribution

- `manifests/contributions/<your-worker>/candidate_accounts/` for verified official Channel records under the stricter worker account contract.
- `manifests/contributions/<your-worker>/profile_images/` for Image and ImagePlacement records under the general Ascent contract.
- Other folders under `manifests/contributions/<your-organization>/` for new place and election graphs, stances, communications, stance evidence, party channels, and new approaches. File names carry no meaning; the `candidate_accounts/` directory selects the stricter account checks.
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
- **Codes** are uppercase letters, digits, dashes, and underscores. The recipes are in `doc/entity_code_plan.md` in the Ascent repository, for example `STANCE-{candidacy path}-{approach path}`; social media codes are below.
- **A code is the record's identity.** Its entity URI is the code qualified by namespace and catalog, `MIC-ASC-{code}`. Two records with different codes are two records, however alike their names; if you need a second code for an existing record, list it under that record's `aliases`.
- **Each piece of evidence is its own record**, so you can add evidence to an existing stance without redefining it.
- **Allowed types, fields, and values** are listed in `schemas/asc.contract.json` and enforced by `schemas/v1/asc.schema.json`.

## Find existing records

Use the [entity catalog](catalog/README.md) to browse records by type and state. The CSV files include entity codes, names, state codes, FIPS, aliases, references, and source paths. Each catalog group links to its source manifests.

After the Python setup in [WORKERS.md](WORKERS.md#set-up-validation), use the offline lookup:

```sh
.venv/bin/python tools/seed_contract.py lookup Albany --state NY
.venv/bin/python tools/seed_contract.py lookup Mayor --type Position
.venv/bin/python tools/seed_contract.py lookup Albany --type Office --format json
```

A nonzero exit means the lookup failed or no records matched. Queries match names, entity codes, aliases, and FIPS without regard to letter case. `--type` takes an entity type such as County, Position, Office, or Candidacy. `--state` accepts `NY` or `STATE-USA-NY`. Omit the query to list all records matching the filters.

A Position describes a role, such as Mayor. An Office connects that role to a jurisdiction. A Race connects the office to an Election, and a Candidacy connects a Person to the race. Reuse each existing code when adding data to that record.

State filters follow manifest scope and references. A person's state association does not establish residence. Catalog entries describe repository definitions, independent of whether a database has imported them.

## County FIPS

A record's top-level `code` is its Ascent entity code. A county's external geographic identifier is `attributes.fips`:

```yaml
type: County
code: COUNTY-USA-AL-AUTAUGA
attributes:
  name: Autauga County
  fips: "01001"
references:
  state: STATE-USA-AL
```

FIPS is optional and, when present, must be a quoted five-digit string. Keep leading zeros. Replace the former County `attributes.code` with `attributes.fips`; the old attribute is rejected. Country and State `attributes.code` retain their existing meanings.

In the app, a county's FIPS must agree with its jurisdiction's Census GEOID when both are present. Boundary imports match counties by FIPS and fill missing FIPS from the county feature.

## Refresh the catalog

After changing a manifest, regenerate the catalog from this repository root:

```sh
.venv/bin/python tools/seed_contract.py export-catalog
```

A nonzero exit means generation failed. The command reports the unique record count and writes generated CSV files and their index under `catalog/`. Edit definitions in `manifests/`, then commit the resulting catalog changes with them. The exporter rejects contradictory attributes and alias collisions.

Check the generated files without changing them:

```sh
.venv/bin/python tools/seed_contract.py export-catalog --check
```

A nonzero exit means the catalog is missing, stale, or has unexpected files. This check runs in CI.

## People

A person's code is a version of their name and a disambiguator Ascent issues to everyone in advance: Letitia James is `PERSON-JAMES_LT_5Y` in the current manifests. Use the owner export in [WORKERS.md](WORKERS.md#find-the-owner-codes) to find current full codes.

- **The name code** is the surname, then the given name's first letter and its next consonant: Letitia → `LT`, Clyde → `CL`, Ann → `AN`. A person printed with only a surname has the surname alone.
- **The disambiguator** is a digit and a letter, such as `6J`. Ascent assigns it once and never changes it.
- **In a submission you may use the name code alone**, such as `PERSON-JAMES_LT`, when you don't know the disambiguator. The importer resolves it to the one person with that name code; if two people share it, the import stops and lists both full codes.
- A code names no state or office, because a person may later run somewhere else. Social media handles go in the person's Channel records, not their code.

## Organizations

An Organization is an institution that endorses or nominates candidacies: a union, an advocacy group, a business, a newspaper, a civic group. Its code is `ORGANIZATION-{jurisdiction path}-{NAME}`, such as `ORGANIZATION-USA-GA-AFL_CIO`, with a `name`, an optional `abbreviation`, a `kind` (`union`, `advocacy`, `business`, `media`, `civic`, `nonpartisan_primary`, or `other`), and a `state` reference when it works within one state.

A party is an Organization too, recorded as a `Party` with its own codes (`PARTY-USA-GA-DEMOCRATIC`) and no kind. A `Party` must belong to a state. Anywhere an organization can be named, such as a channel's owner or a nomination's organization, a party's code works.

## Primaries and nominations

A primary is a race for a nomination: a place on the general-election ballot for one office. Each nomination is an Office of its own.

| Field | Required | Meaning |
|---|---|---|
| `code` | yes | `OFFICE-{office path}-NOMINEE_{ORGANIZATION}`: the Georgia Democratic nomination for the 5th district is `OFFICE-USA-GA-CONGRESS-CD_5-NOMINEE_DEMOCRATIC` |
| `position` | yes | `POSITION-NOMINEE` |
| `jurisdiction` | yes | The nominated office's jurisdiction |
| `nominee_for` | yes | The nominated office, such as `OFFICE-USA-GA-CONGRESS-CD_5` |
| `nominating_organization` | yes | The party, or the placeholder Organization for a nonpartisan primary |
| `nominee_count` | yes | How many the primary sends to the general: 1 for a party primary, 2 for a top-two primary, 4 for Alaska's top-four |

The race for it sits in the state's primary election from `elections_2026.yml`, even when the nomination is for a district: `RACE-USA-GA-CONGRESS-CD_5-NOMINEE_DEMOCRATIC-2026_PRIMARY` in `ELECTION-USA-GA-2026_PRIMARY`. A primary runoff is a race for the same nomination in the `..._2026_PRIMARY_RUNOFF` election. Primary candidates are ordinary Candidacy records in that race, with the people's codes as described above.

Nonpartisan primaries nominate through placeholder Organizations in `manifests/contributions/ascent/nominations.yml`: `ORGANIZATION-USA-CA-TOP_TWO_PRIMARY`, `ORGANIZATION-USA-WA-TOP_TWO_PRIMARY`, and `ORGANIZATION-USA-AK-TOP_FOUR_PRIMARY`. Their nomination codes end in `NOMINEE_TOP_TWO` or `NOMINEE_TOP_FOUR`.

Record every candidate who ran, including those who lost: Ascent can put a whole primary field on one simulated general-election ballot, where approval voting may favor a candidate the primary eliminated.

## Candidates' social media accounts and posts

For workers adding accounts to existing candidates, start with [WORKERS.md](WORKERS.md). It provides equivalent JSON and YAML templates, an export of existing owner codes, and offline validation. Put those submissions in `manifests/contributions/<your-worker>/candidate_accounts/` to apply the stricter account contract.

Two types record what candidates, campaigns, and parties publish online: a **Channel** is one account on one platform, and a **Communication** is one thing published there. Communication seeds hold links, platform IDs, dates, short summaries, and quotes. They do not copy posts or video. Separately, the app stores profile image files through Active Storage. `examples/candidate_social_media.yml` shows a complete fictional example; that folder is not imported.

### Channel: one account

| Field | Required | Meaning |
|---|---|---|
| `code` | yes | `CHANNEL-{PLATFORM}-{HANDLE}`: a platform token (`WEB`, `YT`, `IG`, `TT`, `X`, `BSKY`, `FB`, or `THR`, or a 2–4 letter abbreviation for another platform), then the handle in code form. `avery.example.com` on Bluesky is `CHANNEL-BSKY-AVERY_EXAMPLE_COM` |
| `platform` | yes | `website`, `youtube`, `instagram`, `tiktok`, `x`, `bluesky`, `facebook`, `threads`, or `other` |
| `handle` | yes | The handle as the platform shows it, without `@`; for a website, its host and any path |
| `url` | no | The account's profile or home page |
| `official` | no | `true` when the person, campaign, or party runs the account; `false`, the default, for supporters' and unofficial accounts |
| `owner` | no | A reference to a `PERSON-…`, a `CANDIDACY-…` for one campaign's account, or a `PARTY-…` |

A platform and handle name exactly one account. The importer refuses a second code for an account it already has; use the existing code or list yours under its `aliases`.

### Communication: one post, video, or other publication

| Field | Required | Meaning |
|---|---|---|
| `code` | yes | `COMMUNICATION-{channel path}-{YYYY_MM_DD}-{SLUG}`, where the channel path is the channel's code without `CHANNEL-`: `COMMUNICATION-BSKY-AVERY_EXAMPLE_COM-2026_10_02-TRANSIT_FUNDING` |
| `kind` | yes | `post` for a social media post; also `video`, `ad`, `speech`, `debate`, `interview`, `platform`, `press_release`, `mailer`, or `other` |
| `published_on` | yes | The date it was published, `YYYY-MM-DD` |
| `url` | yes | Its permanent link. One URL is one communication |
| `platform_id` | no | The platform's own ID for it, such as a YouTube video ID, an X post ID, an Instagram shortcode, or a Bluesky record key |
| `archived_url` | no | An archived copy, such as a Wayback Machine link; expected whenever `availability` is `edited` or `removed` |
| `availability` | no | `available` (the default), `edited`, or `removed` |
| `title` | no | Its title, when it has one |
| `summary` | no | A sentence or two in your own words |
| `duration_seconds` | no | Length of a video or audio recording |
| `language` | no | A language tag such as `en` or `es` |
| `featured_candidacies` | no | Codes of the candidacies it features or promotes; later contributions can add more |
| `channel` | no | A reference to the `CHANNEL-…` that published it |

A quote from a communication belongs in a `StanceEvidence` record that links it to a stance, at most 300 characters.

## Shared profile images

An `Image` is a reusable image with `alt_text`, `credit`, and `source_url`. Seed manifests identify its original external image with `url`. An `ImagePlacement` links that image to a Person or Candidacy. One person can have many images, and one image can appear on several people and campaigns. The equivalent [YAML example](examples/profile_images.yml) and [JSON example](examples/profile_images.json) show both relationships. Their subject codes are placeholders; replace them with exported full codes before import.

The app stores uploaded image files in Active Storage. Manifest `url` values identify original external images; importing a manifest does not download those files or create blobs. Admins can attach a file to the shared Image. Attached files use named avatar, thumbnail, portrait, and large variants. Blob IDs, signed upload IDs, files, and variant records are not manifest attributes. OpenAI portrait generation remains disabled pending legal review and cannot be triggered through a seed manifest.

Create an `IMAGE-...` code for the image and an `IMAGE_PLACEMENT-...` code for each use. Image URLs are unique. Reuse the existing Image code for the same URL. Each placement requires `references.image` and `references.subject`, using full local entity codes. The subject must be a Person or Candidacy. A subject can use a given image only once.

| Record | Field | Meaning |
|---|---|---|
| Image | `attributes.url` | Original image URL; required to create an Image from a manifest without an attachment |
| Image | `attributes.alt_text` | Description of the image |
| Image | `attributes.credit` | Image attribution |
| Image | `attributes.source_url` | The source page where the image and attribution were found |
| ImagePlacement | `references.image` | The shared `IMAGE-...` code |
| ImagePlacement | `references.subject` | An exported Person or Candidacy code |
| ImagePlacement | `attributes.position` | Nonnegative display order, default 0 |

The app creates these variants from attached originals; contributors do not seed variant dimensions or files:

| Variant | Size | Treatment |
|---|---|---|
| avatar | 96×96 | Crop |
| thumbnail | within 320×320 | Preserve proportions |
| portrait | 800×1000 | Crop |
| large | within 1600×1600 | Preserve proportions |

`ImagePlacement.attributes.position` is a nonnegative integer, defaulting to 0. Lower values appear first; equal values use placement database ID order. Set distinct positions when the order matters. Candidacy profiles show their campaign images before the person's images and remove duplicates. The person page shows that person's images. The first image appears in the header, and additional images appear under Photos.

Include image-source evidence in `source`, and retain the source page in `Image.attributes.source_url`. Store image links rather than uploading image files to this data repository. The image's description and attribution are shared across its placements. Removing a placement leaves the shared Image intact. Seed replay preserves existing values and reports disagreements, including order changes, for maintainer review.

Person attributes `portrait_url`, `portrait_credit`, and `portrait_source_url` are no longer accepted. Replace them with Image attributes `url`, `credit`, and `source_url`, plus a placement referencing that Person. Put image contributions outside the `candidate_accounts/` worker subset, such as `manifests/contributions/<your-worker>/profile_images/`.

OpenAI portrait generation is disabled pending legal review. Seed contributions must leave activation flags and disabled controls unchanged and must not introduce automatic portrait-generation calls. Image-source contribution and Active Storage attachment do not activate generation.

## Sources and content

- Stances, communications, evidence, and images need a source in the `source` block. Include the contributor, source-page URL, and capture date. The worker account subset requires a per-record source and ownership-verification note.
- Link to communications; never upload video or full transcripts. Quotes are at most 300 characters. Record a deleted or edited post with `availability: removed` or `edited` and an `archived_url`.
- Never attach invented positions or quotes to a real person.

## Checking your files

Use the offline validator described in [WORKERS.md](WORKERS.md#validate-before-submission), or validate each manifest against `schemas/v1/asc.schema.json` with any JSON Schema (Draft 2020-12) validator. YAML files can be converted to JSON first. Maintainers also run Ascent's `bin/rails seed_library:validate` for catalog definitions and contradictions. The import step resolves dependencies and checks model validations, identity collisions, and conflicts with database values.

## Import behavior

Reviewing a data pull request and importing its manifests into the app are separate steps. An app maintainer handles the import. The importer creates records that don't exist yet, never overwrites a reviewed value, and reports any disagreement for a maintainer to resolve. It recognizes an existing record by its code or a listed alias, never by its name.
