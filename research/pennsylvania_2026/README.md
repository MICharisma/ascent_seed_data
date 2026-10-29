# Pennsylvania 2026: sources, conflicts and gaps

Contributor: Ascent Clerk. Captured 2026-10-29 (America/New_York). Files: `manifests/contributions/ascent-clerk/pa_2026_{foundation,races,candidates}.yml` and `manifests/contributions/ascent-clerk/candidate_accounts/pa_2026_fec_committee_websites.yml`. The Lieutenant Governor race description in `statewide_races_2026.yml` (an earlier Ascent Clerk file) was updated to cite the Department of State and the joint election. No new Position was needed.

## Scope

247 contests on the Nov 3, 2026 ballot: Governor, Lieutenant Governor, US House districts 1 to 17, the 25 even-numbered state Senate districts, and all 203 state House districts.

* **No US Senate race.** The Green Papers lists McCormick (Class 1, up 2030) and Fetterman (Class 3, up 2028), and the Department of State list has no US Senate contest.
* **No statewide judicial or retention races.** The Department of State 2026 general list has none. Pennsylvania's appellate elections and retentions happen in odd-numbered years.
* **State Senate.** The Department of State list has exactly the 25 even-numbered districts (2 to 50), which matches the brief.

## Sources (in order of authority)

1. Pennsylvania Department of State, PA Voter Services candidate list for the "2026 General Election (11/03/2026)": https://www.pavoterservices.pa.gov/ElectionInfo/ElectionInfo.aspx. The page embeds the list as `dataJson`; the copy captured 2026-10-29 had 1,298 rows. State committee rows were dropped, and exact duplicate rows were collapsed (Richey, Amen Brown, Magwood, Stehr and Vasquez each appear twice). From each row we used the name, party, candidate type (Petition, Paper, Write-in, Substitute), status (Approved, Withdrawn, Inactive-CrossFiled), `PrimaryResult` and county.
2. FEC candidate master `cn26.zip` (https://www.fec.gov/files/bulk-downloads/2026/cn26.zip) for the FEC IDs of US House candidates (in the CSV only), and the FEC committee API (`https://api.open.fec.gov/v1/committee/<id>/`) for each US House nominee's principal campaign committee website.
3. The Green Papers, https://www.thegreenpapers.com/G26/PA, as a cross-check: every Governor, Lieutenant Governor and US House nominee's surname appears on that page. Ballotpedia was not used.

## How the list was modelled

* **Primary (May 19, 2026, closed).** Each Democratic and Republican field is a nomination Office (`POSITION-NOMINEE`, `nominee_count: 1`, `nominating_organization` = the party) with a race in `ELECTION-USA-PA-2026_PRIMARY`. Approved petition candidates are the people on the primary ballot. Write-in rows with `PrimaryResult = true` are people who won the nomination by write-in; they get a primary candidacy with a `write_in` ballot line. That covers 24 write-in primary candidacies. The Department of State does not list losing write-ins.
* **General (Nov 3).** The nominees are the Approved rows with `PrimaryResult = true`, Approved Paper (minor party or political body) candidates, and one Approved Substitute. Libertarian candidates use a new `PARTY-USA-PA-LIBERTARIAN` line. Political bodies get `designation` lines with the Department of State's own label: The Independent Party, Independent Party, Independent, Forward Independent, Progress for Pennsylvania and Green. The Green Party has no `Party` record here because its only remaining candidate (SD 24) filed by paper.
* **Governor and Lieutenant Governor.** These are nominated in separate primaries but elected jointly in November: one vote goes to a party's Governor and Lieutenant Governor together (Pa. Const. art. IV, sec. 4). Ascent has no ticket or running-mate record, so the two offices keep separate general races and candidacies, paired by party line. Both race descriptions say so. `OFFICE-USA-PA-GOVERNOR` and its race are new; Lieutenant Governor reuses the existing office and race.
* **Results.** Candidacies record no winner, vote total or incumbency. The Department of State's `PrimaryResult` flag is in the CSV (`dos_primary_result`). Primary vote totals were not collected; electionreturns.pa.gov was not used.

## Conflicts and judgment calls

1. **Withdrawn before the primary.** 27 Withdrawn rows without a primary win were left out entirely: the Green Governor and Lieutenant Governor candidates (Dastra, Bolton), the Green CD 7 candidate (Tupone), and 24 petition candidates, including five in the CD 3 Democratic primary. The Department of State gives no withdrawal dates, so I assumed these people were not on the primary ballot. They are not in the CSV.
2. **SD 26 (Republican).** Alfeia DeVaughn-Goodwin won the Republican primary (`PrimaryResult = true`) and then withdrew. Gail R. Scott is the Approved **Substitute** nominee. DeVaughn-Goodwin keeps her primary candidacy. Scott has only a general candidacy, because she did not run in the primary.
3. **HD 145 (Democratic).** Les Mavus won the Democratic primary and then withdrew, and the list shows no Democratic substitute. The general race has only Craig Staats (R) and Rebecca Prendergast (Independent Party). Check this if a substitute is named later.
4. **HD 2, Robert Merski, cross-filed.** He has a Democratic petition row and a Republican write-in row (`Inactive-CrossFiled`, `PrimaryResult = true`), and the general row is party "Democratic / Republican". He is one Person with a Democratic primary candidacy, a Republican write-in primary candidacy, and one general candidacy with both a Democratic and a Republican party line.
5. **US House names from PR #7.** All 34 existing `federal_candidates_2026.yml` general candidacies match a Department of State nominee and were reused unchanged. Some differences from the state's ballot names: CD 4 "DEAN CUNNANE, MADELEINE" is PR #7's Madeleine Dean; CD 16 "KELLY JR., GEORGE JOSEPH" is PR #7's Mike Kelly; CD 7 "BROOKS, ROBERT R" is Bob Brooks; CD 17 "GUY, ANTHONY G" is Tony Guy. PR #7 also labels Democrats "Democrat" (the state prints "Democratic"), labels Dennis Mahoney (CD 3) "Independent" where the state has "The Independent Party", and uses `kind: unclassified`. Those records were not edited.
6. **Primary candidates for federal nominees** use the PR #7 person codes. US House primary losers are new people.
7. **Names.** The Department of State prints "LAST SUFFIX, FIRST MIDDLE" in capitals. Names were converted mechanically: suffixes were dropped, single-letter middles became initials, and Mc and O' were handled. The exact ballot text is in the CSV.
8. **Joint ticket.** See above. If Ascent adds a ticket or running-mate record, the Governor and Lieutenant Governor general candidacies should be linked by party.

## Name-code collisions: 28 candidates NOT in the YAML

These people's name codes are already used in this repository (on main, including Texas, or on the California PR #11 branch), or are shared by two different Pennsylvania candidates. Ascent issues the disambiguators, so these people and all their candidacies are left out. That is 55 CSV rows with `in_pr = N`, 27 of them Nov 3 nominees.

| Race | Candidate (ballot) | Candidacies | Name code | Existing codes |
|---|---|---|---|---|
| State Senate District 20 | BAKER, ELISABETH J | Rep primary; general (Republican) | PERSON-BAKER_EL | PERSON-BAKER_EL_6G |
| State Senate District 20 | BAKER, JACLYN ESTELLE | Dem primary; general (Democratic) | PERSON-BAKER_JC | PERSON-BAKER_JC_2Z |
| State Senate District 36 | JONES, THOMAS MATTHEW | Rep primary; general (Republican) | PERSON-JONES_TH | PERSON-JONES_TH_6F |
| State House District 6 | WALKER, MICHAEL C | Dem primary; general (Democratic) | PERSON-WALKER_MC | PERSON-WALKER_MC_4H, PERSON-WALKER_MC_8R |
| State House District 9 | BROWN, MARLA ANN | Rep primary; general (Republican) | PERSON-BROWN_MR | PERSON-BROWN_MR_3Y, PERSON-BROWN_MR_9F |
| State House District 10 | BROWN, AMEN | Dem primary; general (Democratic) | PERSON-BROWN_AM | PERSON-BROWN_AM_7R |
| State House District 22 | SMITH JR, ROBERT E | Rep primary; general (Republican) | PERSON-SMITH_RB | PERSON-SMITH_RB_3D |
| State House District 24 | ANDERSON , WILLIAM | Dem primary | PERSON-ANDERSON_WL | PERSON-ANDERSON_WL_5B |
| State House District 41 | MILLER, BRETT R | Rep primary; general (Republican) | PERSON-MILLER_BR | PERSON-MILLER_BR_2L, PERSON-MILLER_BR_3U, PERSON-MILLER_BR_8Z |
| State House District 54 | SCOTT, GREGORY | Dem primary; general (Democratic) | PERSON-SCOTT_GR | PERSON-SCOTT_GR_8S |
| State House District 58 | ROGERS, CHERRI | Dem primary; general (Democratic) | PERSON-ROGERS_CH | PERSON-ROGERS_CH_8J |
| State House District 62 | JONES, TRAJAN WILLIAM | Dem primary; general (Democratic) | PERSON-JONES_TR | PERSON-JONES_TR_2C |
| State House District 66 | SMITH, BRIAN A | Rep primary; general (Republican) | PERSON-SMITH_BR | PERSON-SMITH_BR_4M, PERSON-SMITH_BR_7M, PERSON-SMITH_BR_7V, PERSON-SMITH_BR_8H, PERSON-SMITH_BR_9H, PERSON-SMITH_BR_9R |
| State House District 74 | WILLIAMS, DAN K | Dem primary; general (Democratic) | PERSON-WILLIAMS_DN | PERSON-WILLIAMS_DN_7W |
| State House District 90 | REICHARD, CHAD G | Rep primary; general (Republican) | PERSON-REICHARD_CH | PERSON-REICHARD_CH_6J |
| State House District 92 | ANDERSON, KRISTA JEAN | Dem primary; general (Democratic) | PERSON-ANDERSON_KR | PERSON-ANDERSON_KR_5N, PERSON-ANDERSON_KR_6D |
| State House District 92 | ANDERSON, MARC S | Rep primary; general (Republican) | PERSON-ANDERSON_MR | PERSON-ANDERSON_MR_5G |
| State House District 93 | JONES, PAUL MICHAEL | Rep primary; general (Republican) | PERSON-JONES_PL | PERSON-JONES_PL_8K, PERSON-JONES_PL_9Y |
| State House District 95 | RIVERA, JASMINE | Rep primary; general (Republican) | PERSON-RIVERA_JS | PERSON-RIVERA_JS_9N |
| State House District 128 | WAGNER, ANDREW | Dem primary; general (Democratic) | PERSON-WAGNER_AN | PERSON-WAGNER_AN_3A |
| State House District 135 | SAMUELSON, STEPHEN P | Dem primary; general (Democratic) | PERSON-SAMUELSON_ST | PERSON-SAMUELSON_ST |
| State House District 136 | FREEMAN, ROBERT | Dem primary; general (Democratic) | PERSON-FREEMAN_RB | PERSON-FREEMAN_RB_8Q |
| State House District 144 | MURPHY, MICHAEL J | Rep primary; general (Republican) | PERSON-MURPHY_MC | other PA candidate: MURPHY, MICHAEL E |
| State House District 162 | MURPHY, MICHAEL E | Rep primary; general (Republican) | PERSON-MURPHY_MC | other PA candidate: MURPHY, MICHAEL J |
| State House District 167 | LEWIS, JOSEPH M | Rep primary; general (Republican) | PERSON-LEWIS_JS | PERSON-LEWIS_JS_2U |
| State House District 172 | DOUGHERTY, SEAN MICHAEL | Dem primary; general (Democratic) | PERSON-DOUGHERTY_SN | PERSON-DOUGHERTY_SN_5X |
| State House District 186 | HARRIS, JORDAN ALEXANDER | Dem primary; general (Democratic) | PERSON-HARRIS_JR | PERSON-HARRIS_JR_7L |
| State House District 200 | JOHNSON, CHRISTOPHER | Dem primary; general (Democratic) | PERSON-JOHNSON_CH | PERSON-JOHNSON_CH_5X, PERSON-JOHNSON_CH_8L |

## Candidate websites

The Department of State list has no website field, and no website was guessed or found by search. For the 34 US House nominees, the website on each principal campaign committee's FEC record was fetched on 2026-10-29. A site was kept only when it returned HTTP 200 and its page named the candidate. That gave 26 website Channels, each owned by the existing PR #7 general Candidacy with `official: true` and its own `source`. State-office candidates have no official website source, so they have none. Omitted:

| Candidate | FEC website | Reason |
|---|---|---|
| ARRIAGA, JESSICA |  | no website on the FEC committee record |
| BOYLE, BRENDAN F | HTTP://WWW.VOTEBOYLE.COM | HTTP 500 |
| MAHONEY, DENNIS JOSEPH |  | no website on the FEC committee record |
| BROOKS, ROBERT R |  | no website on the FEC committee record |
| SMUCKER, LLOYD K |  | no website on the FEC committee record |
| JOYCE, JOHN |  | no website on the FEC committee record |
| BILGER, RAY |  | no website on the FEC committee record |
| GUY, ANTHONY G | WWW.TONYGUYFORCONGRESS.COM | no response (TLS/connection error) |

## Not included

* Local offices, party state committee members, and special elections.
* Social media handles: none were looked up.
* Winners, vote totals and incumbency.

## Files here

* `pa_2026_review.csv`: one row per candidacy, 917 in all: 436 general and 481 primary.
* `district_crosswalk.csv`: each district code with its TIGER 2024 layer and GEOID (state FIPS 42 plus the district number).
