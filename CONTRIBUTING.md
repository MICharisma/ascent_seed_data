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
- **Codes** are uppercase letters, digits, dashes, and underscores. The recipes are in `doc/entity_code_plan.md` in the Ascent repository, for example `STANCE-{candidacy path}-{approach path}`; social media codes are below.
- **A code is the record's identity.** Its entity URI is the code qualified by namespace and catalog, `MIC-ASC-{code}`. Two records with different codes are two records, however alike their names; if you need a second code for an existing record, list it under that record's `aliases`.
- **Each piece of evidence is its own record**, so you can add evidence to an existing stance without redefining it.
- **Allowed types, fields, and values** are listed in `schemas/asc.contract.json` and enforced by `schemas/v1/asc.schema.json`.

## People

A person's code is a version of their name and a disambiguator Ascent issues to everyone in advance: Letitia James is `PERSON-JAMES_LT_6J`.

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

Two types record what candidates, campaigns, and parties publish online: a **Channel** is one account on one platform, and a **Communication** is one thing published there. Ascent keeps links, platform IDs, dates, short summaries, and quotes, never the posts, images, or video themselves. `examples/candidate_social_media.yml` shows a complete fictional example; that folder is not imported.

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

## Sources and content

- Stances, communications, and evidence need a source in the `source` block.
- Link to communications; never upload video or full transcripts. Quotes are at most 300 characters. Record a deleted or edited post with `availability: removed` or `edited` and an `archived_url`.
- Never attach invented positions or quotes to a real person.

## Checking your files

Validate each manifest against `schemas/v1/asc.schema.json` with any JSON Schema (Draft 2020-12) validator; YAML files can be converted to JSON first. Maintainers also run Ascent's `bin/rails seed_library:validate`, which additionally checks references and contradictory definitions.

## What happens on merge

The importer creates records that don't exist yet, never overwrites a reviewed value, and reports any disagreement for a maintainer to resolve. It recognizes an existing record by its code or a listed alias, never by its name.
