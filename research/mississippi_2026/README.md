# Mississippi 2026 (Ascent Clerk)

Built 2026-10-29 from official Mississippi Secretary of State files only:

| File | URL |
|---|---|
| Sample Official Election Ballot, Federal and Judicial Election, Nov 3, 2026 (dated 9-9-26) | https://www.sos.ms.gov/content/documents/Elections/2026/Sample%20Ballot%209-9-26.pdf |
| Official Recapitulation, Federal Primary Election (Democratic), Mar 10, 2026 | https://www.sos.ms.gov/content/documents/elections/2026/Recap%20report%20Democratic%20Primary%202026.pdf |
| Official Recapitulation, Federal Primary Election (Republican), Mar 10, 2026 | https://www.sos.ms.gov/content/documents/elections/2026/republican%20primary%202026.pdf |
| Candidate Qualifying List (current on-file list) | https://sos.ms.gov/content/CandidateQualifying/default.aspx |

## What is in the PR

- **U.S. Senate and U.S. House 1-4:** the general races and all 15 general candidacies already exist in `federal_candidates_2026.yml` and are referenced unchanged. This PR adds a party nomination office (POSITION-NOMINEE) and a March 10 primary race for each contest and party on the official recaps (10 races, 20 primary candidacies, with recap vote totals in the review CSV). The nominee flag comes from the Nov 3 sample ballot, not from vote counts.
- **State House specials, HD 70 and HD 77:** nonpartisan special elections (ballot prints "Independent"), 3 and 4 candidates. No primaries.
- **Court of Appeals:** the five seats on the sample ballot (D1 P1, D1 P2, D2 P1, D4 P2, D5 P1), nonpartisan, no primaries. POSITION-APPELLATE_JUDGE.
- No new Positions.

## No regular legislative races

Mississippi elects its whole Legislature in odd years (last 2023, next 2027). The SoS 2026 sample ballot is titled "Federal and Judicial Election" and contains no regular State Senate or House contests, only the HD 70 and HD 77 specials. Verified against that official ballot.

## Not included (flags)

- **State Senate District 34 special:** the qualifying list has a "Candidates for State Senate 34" section (Johnny DuPree, Kenneth Keyes, Tiffany Anne Lindsey, Daryl A. McKines Jr., Bruce D. Pilgrim, Nellie "Cookie" Satcher) with no election date, and the race is not on the Nov 3 sample ballot. Left out until the SoS publishes its date and ballot.
- **Chancery, circuit court and District Attorney 7 (special):** local trial-court and district offices; on the sample ballot but outside this batch's scope (statewide, federal, legislative and appellate). Can be added from the same PDF.
- **Libertarian nominees** (Baucom CD 1, Kiehle CD 3) and the independents (Pinkins, Foster, Boyanton) reached the ballot without a primary, so they have general candidacies only (already in the federal file).
- **Websites:** no official Mississippi source lists candidate websites, so `candidate_accounts/` is not touched.
- **Party labels:** the SoS prints "Democrat"; ballot line labels use that wording. The party record is PARTY-USA-MS-DEMOCRATIC.

## Withdrawals

None. Everyone on the official primary recaps appears in this PR; no withdrawal is recorded on any captured SoS file.

## Names

All names are as printed on the sample ballot or recap. Middle names/initials go in `middle_name`; generational suffixes stay with the surname. "Dianne McNair Gaddis": McNair is treated as a middle name (surname Gaddis, as the qualifying list sorts her) -- confirm. Nicknames in quotes (Chris Dunn, Tony Lawrence) are not stored as names.

## Codes

All 23 new people minted with `tools/seed_contract.py mint`. One shared name code: Craig T. Williams (HD 77) shares WILLIAMS_CR with people in FL and VA; minted `--new` (no in-state evidence of the same person). Federal people from `federal_candidates_2026.yml` are reused unchanged.

## Rails import checks

- HD 70/77 races use `-2026_SPECIAL` race codes inside district elections named "... Special Election 2026" (kind general, Nov 3).
- Court of Appeals districts have no TIGER layer (county-defined, Miss. Code 9-4-5); see `district_crosswalk.csv`.
- Provisional usernames may collide with other parallel state PRs not yet on main.
