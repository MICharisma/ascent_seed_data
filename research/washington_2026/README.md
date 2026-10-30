# Washington 2026: state legislative candidate seed, top-two (ascent-clerk)

## Sources (official only)
- Secretary of State candidate list, https://voter.votewa.gov/CandidateList.aspx, "Export to CSV":
  - `?e=898` PRIMARY 2026 (08/04/2026): 1,108 rows statewide (all offices)
  - `?e=899` GENERAL 2026 (11/03/2026): 887 rows
- Each multi-county legislative district shows up twice: once as `Legislative` and once in a county-filed uppercase `LEGISLATIVE` copy. These were de-duplicated by district, race and name.

## Scope
State Senate (24 districts with 2026 seats), State Representative Pos. 1 and Pos. 2 in all 49 legislative districts, and the U.S. House 1-10 top-two primaries. Washington has no statewide executive or U.S. Senate contest in 2026.
**Not included (nonpartisan or local):** judicial, county, city, PUD, port and other local contests. 1,384 rows were skipped.

## Model (same as California, PR #11)
- `ORGANIZATION-USA-WA-TOP_TWO_PRIMARY` (already in the repo) is the nominating organization. Each contest gets an `OFFICE-...-NOMINEE_TOP_TWO` office with `nominee_count: 2` and a race `...-NOMINEE_TOP_TWO-2026_PRIMARY` in `ELECTION-USA-WA-2026_PRIMARY`.
- **Every active primary filer gets a top-two candidacy.** Washington prints every candidate on the top-two ballot, including sole filers, so a sole filer is a real primary contest (not an unopposed nominee declared without a primary).
- **Party preference ballot lines:**
  - DEMOCRATIC or DEMOCRAT becomes `Democratic` (kind party, PARTY-USA-WA-DEMOCRATIC, new).
  - REPUBLICAN becomes `Republican` (kind party, PARTY-USA-WA-REPUBLICAN, new).
  - Any other preference, such as "Prefers Independent Party", "Prefers Trump Republican Party", "Prefers Cascade Party" or "Prefers No Kings Party", becomes a `designation` with no party.
  - "States No Party Preference" and "Nonpartisan" also become `designation`.
  - A preference is self-declared and doesn't imply party nomination. The raw preference string is kept in the review CSV notes.
- **Office structure:**
  - Each legislative district is one new district (`DISTRICT-USA-WA-LEGISLATIVE-LD_n`) with one general election. TIGER sldu GEOIDs are in district_crosswalk.csv.
  - House seats are separate offices: `OFFICE-USA-WA-HOUSE-LD_n-POS_1` and `-POS_2`.
  - The Senate office is `OFFICE-USA-WA-SENATE-LD_n`.

## Counts
- 2 parties, 49 districts and 49 elections.
- 254 offices and 254 races: 122 general (24 Senate + 98 House positions) and 132 top-two nomination contests (122 legislative + 10 U.S. House).
- 340 persons and 584 candidacies: 359 top-two primary and 245 general. 20 U.S. House general candidacies were reused from federal_candidates_2026.yml.

## Flags for review
- **Primary "Election Status" is stale.** In the official primary export, most rows still say "In Primary" instead of "Advanced to General". The general candidate list was therefore used as the authority for who is on the Nov 3 ballot. Winners and vote totals are not modeled.
- **LD5 Pos. 1** is listed as "Short & Full": one race for both the unexpired and the full term (Zach Hall, Michelle Bennett). This is noted in the race description.
- **7 primary withdrawals** are classified `before-primary-ballot (withdrew)` with the SoS citation:
  - Julia Payne (LD6 Pos. 1)
  - Douglas McKinley (LD8 Senate)
  - Joel Ard (LD23 Pos. 1)
  - Brett Johnson (LD29 Pos. 1)
  - Emijah Smith (LD37 Senate)
  - Raymond Pelletti (CD2)
  - Mike Gahvarehchee (CD5)
- **Name splits:**
  - Nicknames in quotes or parentheses were dropped, e.g. Thomas (Jeff) Kelly, Juan "Jerry" Garcia, Rodney 'Star' Thornley.
  - Suffix "III" was dropped from Luc Jasmin III (the contract has no suffix field).
  - **Read as two-word surnames (please confirm):** Hernandez Greenfield, Alvarez Shepard, Jurado Stonier, Gluesenkamp Perez.
  - **Read as middle names:** Tomiko (Sharon Tomiko Santos), Grant (Julia Grant Reed), Su-Ling (Mia Su-Ling Gregerson).
- **14 name codes match people already in the repo**, all from other states or different people. They were minted as new people with no link.
- The ballot-name-only source has no residence data, so people are keyed by name and contest.

CI is disabled for this repo, so it was not run. All local checks pass: validate, unittest, accounts, export-catalog --check.
