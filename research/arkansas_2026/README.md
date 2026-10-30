# Arkansas 2026 (Ascent Clerk)

Built 2026-10-30 from official Arkansas Secretary of State sources only. The results API was read with the browser user agent on public, unauthenticated endpoints. No embedded tokens were used.

| Source | URL |
|---|---|
| Election Night Reporting (ENR) ballot setup for the 2026 General Election & Judicial Runoff (Nov 3, 2026): contests and candidates with party | https://arkansas.tally-enr.com/#election=11b07106-031e-4d7c-911a-d01fb473d6dd (API: https://enr-results-api.totalresults.com/Contest/GetContestSearchList?cid=arkansas&electionID=11b07106-031e-4d7c-911a-d01fb473d6dd) |
| Mar 3, 2026 Preferential Primary, official results (marked "Official", last updated 07/02/2026, 2,897 of 2,897 precincts) | https://arkansas.tally-enr.com/#election=7f77a178-af02-40ec-92db-c5cc50882c68 (API: `Contest/GetContestResults?cId=arkansas&electionID=7f77a178-...&contestType=Federal\|Statewide\|State%20Senate\|State%20Representative`) |
| Mar 31, 2026 Primary Runoff results | https://arkansas.tally-enr.com/#election=b412bdef-f97a-45bc-b3ec-6761d28caf9e |
| SoS candidate filings (198 state and federal filers), used only for the withdrawal cross-check | https://candidates.arkansas.gov/ |

## Model

- **Primaries:** one POSITION-NOMINEE office and one `-2026_PRIMARY` race for each of the 37 contested primaries in the official results (Republican and Democratic, plus SD26, which the results list as "Non Partisan" and which is modeled as `-NOMINEE_NONPARTISAN`).
  - Unopposed nominees are not on Arkansas's primary ballot, so they have only a general candidacy.
  - Runoff vote totals (7 runoffs) are recorded in the candidacy notes.
- **Nominee flag:** Y means the candidate appears on the SoS 2026 General ballot for that party and office. It is not inferred from vote share. The ENR `isWinner` flags are all false, so they were not used.
- **General:** every candidate in the ENR General ballot setup for U.S. Senate, U.S. House, the seven statewide offices, State Senate and State House.
  - Party comes from the ENR party ID.
  - Independents use the designation line "Independent".
  - There are no write-ins.
- **Names:** the party prefix ("REP", "DEM", "LIB", "IND") and incumbency or office titles on the ballot are stripped from the person name. These include "State Representative", "Senator", "Rep." and "JP" (Justice of the Peace, per the filings list). The exact ballot name is kept in each candidacy note. Titles are not used to set incumbency.
- **Legislature:** 18 Senate and 101 House districts with a 2026 contest (`DISTRICT-USA-AR-SENATE-SD_n`, `-HOUSE-HD_n`).
  - HD8 also has a special election for the unexpired term. It is a separate new office, `OFFICE-USA-AR-HOUSE-HD_8-UNEXPIRED_TERM`, with seat `HD_8_UNEXPIRED_TERM`.
  - SD26 has a primary but no general contest.
- **New:** the Governor office and race (POSITION-GOVERNOR) and 3 Parties (Republican, Democratic, Libertarian). No new Positions.
- **Reused unchanged:** the existing Lt. Governor, Secretary of State, Attorney General, Treasurer, Auditor and Land Commissioner offices and races, and the federal offices, races and 13 general candidacies.
- **Counts:** 230 people and 266 candidacies (89 primary and 177 new general).

## Not included

Judicial contests, county, city and school contests, and ballot issues.

## Websites

None verified, so `candidate_accounts/` is untouched.

## Local integration corrections

Added `ORGANIZATION-USA-AR-NONPARTISAN_PRIMARY` as a placeholder Organization with `kind: nonpartisan_primary` and linked all 1 nonpartisan nomination offices to it. This models the nomination process without assigning a political party or changing the source ballot labels.
