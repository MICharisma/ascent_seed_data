# California 2026: sources, conflicts and gaps

Contributor: Ascent Clerk. Captured 2026-10-27 (America/New_York). Files: `manifests/contributions/ascent-clerk/ca_2026_{foundation,races,candidates}.yml` and `manifests/contributions/ascent-clerk/candidate_accounts/ca_2026_sos_contact_list_websites.yml`. `POSITION-BOARD_OF_EQUALIZATION_MEMBER` is defined in `manifests/foundation.yml`.

## Sources (in order of authority)

1. California Secretary of State, Official Certified List of Candidates, Nov 3, 2026 General Election, certified 8/27/2026: https://elections.cdn.sos.ca.gov/statewide-elections/2026-general/cert-list-candidates.pdf (nominees, party preference exactly as printed, ballot designation, `*` incumbent marks on statewide/legislative/BOE contests).
2. California Secretary of State, Statement of Vote, June 2, 2026 Primary, certified 7/10/2026: https://elections.cdn.sos.ca.gov/sov/2026-primary/sov/complete-sov.pdf and the `csv-voter-nominated.xlsx` workbook from https://www.sos.ca.gov/elections/prior-elections/statewide-election-results/primary-election-june-2-2026/statement-vote (every primary candidate, incl. 24 qualified write-ins; party; Incumbent Flag; votes; counties reporting).
3. California Secretary of State, Official Candidate Contact List, 9/23/2026: https://elections.cdn.sos.ca.gov/statewide-elections/2026-general/contact-list.pdf (candidate-supplied `WEBSITE:` lines only; no emails or addresses were taken).
4. FEC candidate master `cn26.zip` (https://www.fec.gov/files/bulk-downloads/2026/cn26.zip), House / CA / 2026: FEC candidate IDs in the review CSV only.
5. The Green Papers, https://www.thegreenpapers.com/G26/CA: cross-check only (statewide and US House). Ballotpedia was not used.
6. Census TIGER/Line 2024 (cd119, sldu, sldl for state 06): GEOIDs in `district_crosswalk.csv`.

## What was cross-checked

* Certified list vs Statement of Vote: all 324 general nominees matched a primary candidate by name; party labels agree; the two top vote-getters in every contest equal the two nominees; the incumbent marks agree for every non-US House contest.
* The Green Papers page: the surname of every US House and statewide nominee on the certified list appears on it; the FEC IDs it prints for US House nominees agree with cn26.

## Conflicts and judgment calls

1. **Odd or even state Senate districts.** SoS press release PR26-112 (Aug 27, 2026) says "20 odd-numbered State Senate district" seats are up. The certified list and the Statement of Vote ("even-numbered districts only") show the 20 **even** districts (2-40). Followed the certified list.
2. **US House district lines.** 2026 races are run on the Proposition 50 map. TIGER 2024 `cd119` is the older map, so `district_crosswalk.csv` GEOIDs (06 + district number) identify the district by number only; boundaries and county lists are those reported in the Statement of Vote, not TIGER. Board of Equalization districts have no TIGER layer.
3. **US House incumbent flag.** The Statement of Vote marks every US House candidate `N` and the certified list has no `*` for US House, even for sitting members. The review CSV leaves the flag blank for US House rows; nothing was inferred. For other offices it is the SoS flag.
4. **Party labels in PR #7 vs the SoS.** `federal_candidates_2026.yml` labels 59 CA Democrats "Democrat" (SoS prints "Democratic"), and labels Kevin Kiley (CD 6, `CANDIDACY-USA-CA-CONGRESS-CD_6-2026_GENERAL-KILEY_KV_6M`) "Independent"; the SoS prints "No Party Preference" (The Green Papers says he switched to Independent in March 2026 but is running under "No Party Preference"). Those records were not edited; the new primary candidacies use the SoS text.
5. **Name differences with PR #7.** The SoS prints Gil Cisneros (PR #7: Gilbert Ray Cisneros, CD 31) and Lou Correa (PR #7: J. Luis Correa, CD 46). Middle initials differ for Matsui, Liccardo, Carbajal, Rivas, Lieu, Sánchez, Vo and Peters. Existing person codes are reused.
6. **Single-nominee Assembly races.** AD 4, 8, 22 and 32 have one nominee on the Nov 3 ballot (only one non-write-in candidate ran in the primary). Nomination offices still carry `nominee_count: 2` as the top-two contract defines.
7. **US Senate.** No US Senate race is on California's Nov 3, 2026 ballot (the SoS list has none). The Green Papers page lists three early FEC registrants for the 2028 Class 3 seat; ignored.
8. **Special elections.** The Green Papers shows special elections for CD 1 (special primary June 2, 2026) and CD 14 (June 16 and Aug 18, 2026). Not recorded here; they are not on the Nov 3 ballot.
9. **Race in the primary election.** Per CONTRIBUTING.md, district nomination races sit in `ELECTION-USA-CA-2026_PRIMARY` although the nomination office's jurisdiction is the district.

## Name-code collisions: 21 candidates NOT in the YAML

CONTRIBUTING.md allows a name code alone (e.g. `PERSON-SHEA_JS`) only when it resolves to one person; the importer stops if two share it. These 21 ballot names produce a name code already used by a person in this repository (listed with the existing full codes). I cannot tell whether they are the same people, and Ascent issues the disambiguators, so these people, their primary candidacies, their 7 general candidacies and 5 websites are **left out** and listed in `ca_2026_review.csv` (`in_pr = N`). Once Ascent issues codes, they need adding.

| Race | Candidate | On Nov 3 ballot | Name code | Existing repo codes |
|---|---|---|---|---|
| Governor | Matthew Chase Levy (Democratic) | N | PERSON-LEVY_MT | PERSON-LEVY_MT_2Q |
| Governor | Mauro Alberto Orozco (No Party Preference) | N | PERSON-OROZCO_MR | PERSON-OROZCO_MR_6D |
| State Assembly District 18 | Michael Goldstein (Green) | N | PERSON-GOLDSTEIN_MC | PERSON-GOLDSTEIN_MC_4F |
| U.S. House District 1 | Timothy Sean Kelly (No Party Preference) | N | PERSON-KELLY_TM | PERSON-KELLY_TM_6K |
| U.S. House District 4 | Sharon Brown (Republican) | N | PERSON-BROWN_SH | PERSON-BROWN_SH_5Q, PERSON-BROWN_SH_7R, PERSON-BROWN_SH_8Q |
| State Assembly District 11 | Rochelle Conner (No Party Preference) | N | PERSON-CONNER_RC | PERSON-CONNER_RC_2W |
| U.S. House District 20 | Jeremy Fox (No Party Preference) | N | PERSON-FOX_JR | PERSON-FOX_JR_4U |
| U.S. House District 26 | Daniel Miller (Republican) | N | PERSON-MILLER_DN | PERSON-MILLER_DN_7C |
| U.S. House District 32 | Doug Smith (No Party Preference) | N | PERSON-SMITH_DG | PERSON-SMITH_DG_2Y, PERSON-SMITH_DG_9A |
| U.S. House District 37 | John Thompson Parker (Peace and Freedom) | N | PERSON-PARKER_JH | PERSON-PARKER_JH_7H |
| U.S. House District 41 | Shonique Williams (Democratic) | N | PERSON-WILLIAMS_SH | PERSON-WILLIAMS_SH_3Y |
| U.S. House District 44 | Mark Stewart Greenstein (Democratic) | N | PERSON-GREENSTEIN_MR | PERSON-GREENSTEIN_MR_8Q |
| State Assembly District 43 | Celeste Rodriguez (Democratic) | Y | PERSON-RODRIGUEZ_CL | PERSON-RODRIGUEZ_CL_6E |
| State Assembly District 52 | Andrea Lee Anderson (Republican) | Y | PERSON-ANDERSON_AN | PERSON-ANDERSON_AN_8R |
| State Assembly District 54 | Mark Gonzalez (Democratic) | Y | PERSON-GONZALEZ_MR | PERSON-GONZALEZ_MR_9A |
| State Assembly District 55 | Ashley M. Brown (Democratic) | Y | PERSON-BROWN_AS | PERSON-BROWN_AS_6D |
| State Assembly District 56 | Jessica Martinez (Republican) | Y | PERSON-MARTINEZ_JS | PERSON-MARTINEZ_JS_5K |
| State Assembly District 62 | Paul Irving Jones (Republican) | Y | PERSON-JONES_PL | PERSON-JONES_PL_8K |
| State Assembly District 50 | Robert Garcia (Democratic) | Y | PERSON-GARCIA_RB | PERSON-GARCIA_RB_5M |
| U.S. House District 50 | Joseph "Joe" Shea (Libertarian) | N | PERSON-SHEA_JS | PERSON-SHEA_JS_7C |
| U.S. House District 16 | Kevin Johnson (Republican) | N | PERSON-JOHNSON_KV | PERSON-JOHNSON_KV_4H, PERSON-JOHNSON_KV_5D |

## Not included

* Local races (county, city, school and special-district contests): not collected.
* Judicial retention contests (Supreme Court, Courts of Appeal) on the certified list.
* Social media handles: the SoS contact list gives websites only; none were looked up elsewhere. Websites are `Channel` records owned by the candidate's person, `official: true` because the candidate supplied them to the SoS. The URL scheme is `https://`, which the SoS list does not state.
* Winners, advancement and incumbency are not recorded in the YAML (no field). Primary vote totals and SoS incumbent flags are in `ca_2026_review.csv` only.
* FEC IDs: 257 of 297 US House primary candidates matched in cn26 (all 104 general nominees); the rest are not in cn26 under that district. Six people have more than one candidate ID, listed all in the CSV.

## Files here

* `ca_2026_review.csv`: one row per primary candidate (733), flagged for the 324 on the Nov 3 ballot.
* `district_crosswalk.csv`: district code, TIGER 2024 GEOID where one exists, and county codes and FIPS (counties that reported votes in the contest).

## Candidate websites (worker contract, reworked 2026-10-28)

202 website Channels are in `candidate_accounts/`. Each is owned by the candidate's 2026 general Candidacy, because the SoS contact list is a campaign filing. Each has `official: true` and its own `source` citing the contact list. Each site was fetched on 2026-10-28; a site was kept only when it returned HTTP 200 and its page named the candidate.

These 11 contact-list websites were omitted because that check failed (HTTP status, or surname not found in the page):

| Channel | Owner person | Result |
|---|---|---|
| hawksforus.com | PERSON-HAWKS_JN | no response |
| harderforcongress.com | PERSON-HARDER_JS_2S | HTTP 500 |
| souleforcongress.com | PERSON-SOULE_PT_9S | 200, name not found (likely script-rendered) |
| rokhanna.com | PERSON-KHANNA_RO_8D | HTTP 403 |
| bobsmithforcongress.com | PERSON-SMITH_BB_4D | 200, name not found |
| gilonthehill.com | PERSON-CISNEROS_GL_2A | HTTP 403 |
| tief4casenate.com | PERSON-GIBBS_TF | no response |
| seyartoforsenate.com | PERSON-SEYARTO_KL | no response |
| adams4assembly.com | PERSON-ADAMS_MT | no response |
| andresandfordforassembly.com | PERSON-SANDFORD_AN | 200, name not found |
| vote4lydia.com | PERSON-GUTIERREZ_LY | no response |

The 5 websites of the name-code-collision general nominees stay excluded with those candidates. The contract still has no way to submit a person whose name code is already taken, so the 21 collisions are reported only.
