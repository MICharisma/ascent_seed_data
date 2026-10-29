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

## Person codes and the 28 shared name codes

Every new Person has a full code minted with `tools/seed_contract.py mint` (in-process, same function), facts `PA | <first appearance date> | <DoS printed name, LAST, FIRST> | <DoS office - district>`; the first appearance is the May 19 primary for anyone who ran in it, otherwise Nov 3. Because the DoS prints `LAST SUFFIX, FIRST MIDDLE`, the name-code base was passed explicitly (`--name-code`) from the parsed surname and given name rather than letting `mint` split the printed text by word order; multi-word surnames keep the whole surname (e.g. `DEAN_CUNNANE` would apply, but she is the existing `PERSON-DEAN_MD_8E`). Each Person carries `username` = lowercased code and `username_status: provisional`. The full list with facts is in `minted.json` beside the build scripts (not in the repo); the CSV has `person_code` and `mint_resolution`.

PR #15's first version left out 28 people whose name codes were shared. All 28 are now included. Each was compared with every existing person sharing the name code (name, state, race); none is the same person, so each was minted with `--new`:

| Race | Candidate (ballot) | New code | Shares name code with | Why distinct |
|---|---|---|---|---|
| State Senate District 20 | BAKER, ELISABETH J | PERSON-BAKER_EL_4V | PERSON-BAKER_EL_6G Elizabeth Baker (RACE-USA-FL-TITUSVILLE-COUNCIL_MEMBER-SEAT_1-2026_GENERAL) | different given name |
| State Senate District 20 | BAKER, JACLYN ESTELLE | PERSON-BAKER_JC_3X | PERSON-BAKER_JC_2Z Jack Baker Jr. (RACE-USA-FL-COUNTY_BAKER-SCHOOL_BOARD_MEMBER-DISTRICT_2-2026_GENERAL) | different given name |
| State Senate District 36 | JONES, THOMAS MATTHEW | PERSON-JONES_TH_9T | PERSON-JONES_TH_6F Thomas H. Jones, Jr. (RACE-USA-VA-WAVERLY-COUNCIL_MEMBER-2026_GENERAL) | same given name but a different state and office; no source links them |
| State House District 6 | WALKER, MICHAEL C | PERSON-WALKER_MC_7H | PERSON-WALKER_MC_4H Michelle Walker (RACE-USA-FL-COUNTY_LEE-LIBRARY_TRUSTEE-SANIBEL_PUBLIC_LIBRARY_SEAT_3-2026_GENERAL); PERSON-WALKER_MC_8R Michael Emke Walker (RACE-USA-NY-VILLENOVA-HIGHWAY_SUPERINTENDENT-UNEXPIRED_TERM-2026_GENERAL) | same given name but a different state and office; no source links them |
| State House District 9 | BROWN, MARLA ANN | PERSON-BROWN_MR_7A | PERSON-BROWN_MR_3Y Maurice Mo Brown (RACE-USA-NY-ASSEMBLY-AD_129-2026_GENERAL); PERSON-BROWN_MR_9F Marcus A. Brown (RACE-USA-CT-HOUSE-HD_127-2026_GENERAL) | different given name |
| State House District 10 | BROWN, AMEN | PERSON-BROWN_AM_6C | PERSON-BROWN_AM_7R Amy Brown (RACE-USA-FL-COUNTY_HILLSBOROUGH-COMMUNITY_DEVELOPMENT_DISTRICT_SUPERVISOR-OAKS_AT_SHADY_CREEK_CDD_SEAT_3-2026_GENERAL) | different given name |
| State House District 22 | SMITH JR, ROBERT E | PERSON-SMITH_RB_8L | PERSON-SMITH_RB_3D Robert Smith (RACE-USA-NY-POLAND_TOWN-TOWN_SUPERVISOR-2026_GENERAL) | same given name but a different state and office; no source links them |
| State House District 24 | ANDERSON , WILLIAM | PERSON-ANDERSON_WL_5U | PERSON-ANDERSON_WL_5B William P. "Bill" Anderson (RACE-USA-VA-ABINGDON-COUNCIL_MEMBER-2026_GENERAL) | same given name but a different state and office; no source links them |
| State House District 41 | MILLER, BRETT R | PERSON-MILLER_BR_4B | PERSON-MILLER_BR_2L Bronwyn Catherine Miller (RACE-USA-FL-APPEAL-DCA_3-APPELLATE_JUDGE-RETENTION_OF_BRONWYN_CATHERINE_MILLER-2026_GENERAL); PERSON-MILLER_BR_3U Brian J. Miller (RACE-USA-MT-CONGRESS-CD_2-2026_GENERAL); PERSON-MILLER_BR_8Z Brian D. Miller (RACE-USA-NY-ASSEMBLY-AD_122-2026_GENERAL) | different given name |
| State House District 54 | SCOTT, GREGORY | PERSON-SCOTT_GR_4Q | PERSON-SCOTT_GR_8S Gordon D. Scott (RACE-USA-VA-NORTON-SCHOOL_BOARD_MEMBER-NORTON_CITY-2026_GENERAL) | different given name |
| State House District 58 | ROGERS, CHERRI | PERSON-ROGERS_CH_5G | PERSON-ROGERS_CH_8J Chris Rogers (RACE-USA-CA-ASSEMBLY-AD_2-2026_GENERAL) | different given name |
| State House District 62 | JONES, TRAJAN WILLIAM | PERSON-JONES_TR_7H | PERSON-JONES_TR_2C Travis W. Jones (RACE-USA-VA-FRIES-COUNCIL_MEMBER-2026_GENERAL) | different given name |
| State House District 66 | SMITH, BRIAN A | PERSON-SMITH_BR_8T | PERSON-SMITH_BR_4M Brandon Smith (RACE-USA-FL-WEST_PARK-COMMISSIONER-SEAT_2-2026_GENERAL); PERSON-SMITH_BR_7M Brendalee A. Smith (RACE-USA-MA-HOUSE-TENTH_BRISTOL-2026_GENERAL); PERSON-SMITH_BR_7V Brigitte Smith (RACE-USA-FL-COUNTY_MARION-SCHOOL_BOARD_MEMBER-DISTRICT_4-2026_GENERAL); PERSON-SMITH_BR_8H Brent Smith (RACE-USA-FL-COUNTY_COLLIER-COMMUNITY_DEVELOPMENT_DISTRICT_SUPERVISOR-PELICAN_MARSH_CDD_SEAT_3-2026_GENERAL); PERSON-SMITH_BR_9H Brad Smith (RACE-USA-WI-CONGRESS-CD_6-2026_GENERAL); PERSON-SMITH_BR_9R Brian Conway Smith (RACE-USA-MA-COUNTY_DUKES-REGIONAL_COMMISSION_MEMBER-2026_GENERAL) | same given name but a different state and office; no source links them |
| State House District 74 | WILLIAMS, DAN K | PERSON-WILLIAMS_DN_2R | PERSON-WILLIAMS_DN_7W Danny R. Williams (RACE-USA-VA-COURTLAND-MAYOR-2026_GENERAL) | different given name |
| State House District 90 | REICHARD, CHAD G | PERSON-REICHARD_CH_4K | PERSON-REICHARD_CH_6J Chris Reichard (RACE-USA-MO-CONGRESS-CD_8-2026_GENERAL) | different given name |
| State House District 92 | ANDERSON, KRISTA JEAN | PERSON-ANDERSON_KR_4Q | PERSON-ANDERSON_KR_5N Kristof Von Anderson (RACE-USA-FL-DANIA_BEACH-COMMISSIONER-2026_GENERAL); PERSON-ANDERSON_KR_6D Kristen Anderson (RACE-USA-FL-COUNTY_POLK-COMMUNITY_DEVELOPMENT_DISTRICT_SUPERVISOR-HIGHLAND_MEADOWS_II_CDD_SEAT_2-2026_GENERAL) | different given name |
| State House District 92 | ANDERSON, MARC S | PERSON-ANDERSON_MR_5B | PERSON-ANDERSON_MR_5G Mark W. Anderson (RACE-USA-CT-HOUSE-HD_62-2026_GENERAL) | different given name |
| State House District 93 | JONES, PAUL MICHAEL | PERSON-JONES_PL_5K | PERSON-JONES_PL_8K Paul J. "PJ" Jones (RACE-USA-VA-KILMARNOCK-COUNCIL_MEMBER-2026_GENERAL); PERSON-JONES_PL_9Y Paul Irving Jones (RACE-USA-CA-ASSEMBLY-AD_62-2026_GENERAL) | same given name but a different state and office; no source links them |
| State House District 95 | RIVERA, JASMINE | PERSON-RIVERA_JS_5Q | PERSON-RIVERA_JS_9N Jasmine Rivera (RACE-USA-FL-NORTH_MIAMI_BEACH-COMMISSIONER-GROUP_2-2026_GENERAL) | same given name but a different state and office; no source links them |
| State House District 128 | WAGNER, ANDREW | PERSON-WAGNER_AN_9K | PERSON-WAGNER_AN_3A Ann Wagner (RACE-USA-MO-CONGRESS-CD_2-2026_GENERAL) | different given name |
| State House District 135 | SAMUELSON, STEPHEN P | PERSON-SAMUELSON_ST_8J | PERSON-SAMUELSON_ST_3M Stephen Samuelson (RACE-USA-TX-GOVERNOR-NOMINEE_REPUBLICAN-2026_PRIMARY) | same given name but a different state and office; no source links them |
| State House District 136 | FREEMAN, ROBERT | PERSON-FREEMAN_RB_5Y | PERSON-FREEMAN_RB_8Q Robert Teron Freeman (RACE-USA-VA-QUANTICO-COUNCIL_MEMBER-2026_GENERAL) | same given name but a different state and office; no source links them |
| State House District 144 | MURPHY, MICHAEL J | PERSON-MURPHY_MC_7D | other PA candidate MURPHY, MICHAEL E (State House District 162) | different middle initial, county and district |
| State House District 162 | MURPHY, MICHAEL E | PERSON-MURPHY_MC_4V | other PA candidate MURPHY, MICHAEL J (State House District 144) | different middle initial, county and district |
| State House District 167 | LEWIS, JOSEPH M | PERSON-LEWIS_JS_3X | PERSON-LEWIS_JS_2U Joseph Lewis Jr. (RACE-USA-FL-APPEAL-DCA_1-APPELLATE_JUDGE-RETENTION_OF_JOSEPH_LEWIS_JR-2026_GENERAL) | same given name but a different state and office; no source links them |
| State House District 172 | DOUGHERTY, SEAN MICHAEL | PERSON-DOUGHERTY_SN_6H | PERSON-DOUGHERTY_SN_5X Sean Dougherty (RACE-USA-CA-CONGRESS-CD_19-NOMINEE_TOP_TWO-2026_PRIMARY) | same given name but a different state and office; no source links them |
| State House District 186 | HARRIS, JORDAN ALEXANDER | PERSON-HARRIS_JR_8X | PERSON-HARRIS_JR_7L Jerry L. Harris (RACE-USA-VA-JONESVILLE-MAYOR-2026_GENERAL) | different given name |
| State House District 200 | JOHNSON, CHRISTOPHER | PERSON-JOHNSON_CH_4V | PERSON-JOHNSON_CH_5X Chris Johnson (RACE-USA-FL-COUNTY_JACKSON-SCHOOL_BOARD_MEMBER-DISTRICT_4-2026_GENERAL); PERSON-JOHNSON_CH_8L Chad Johnson (RACE-USA-FL-HOUSE-HD_22-2026_GENERAL) | different given name |

## Candidate websites

The Department of State list has no website field, and no website was guessed or found by search. For the 34 US House nominees, the website on each principal campaign committee's FEC record was fetched on 2026-10-29. A site was kept only when it returned HTTP 200 and its page named the candidate. That gave {len(CH)} website Channels, each owned by the existing PR #7 general Candidacy with `official: true` and its own `source`. State-office candidates have no official website source, so they have none. Omitted:

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
