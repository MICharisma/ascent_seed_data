# Texas 2026: sources, conflicts and gaps

Contributor: Ascent Clerk. Captured 2026-10-29 (America/New_York). Files: `manifests/contributions/ascent-clerk/tx_2026_{foundation,races,candidates}.yml` and `manifests/contributions/ascent-clerk/candidate_accounts/tx_2026_sos_candidate_websites.yml`. No new Position was needed.

## Sources (in order of authority)

1. Texas Secretary of State, 2026 General Election Ballot Certification, dated 8/28/2026: https://www.sos.texas.gov/elections/forms/2026-ballot-cert.pdf (Nov 3 nominees and party for every in-scope contest).
2. Texas Secretary of State, 2026 General Election declared write-in candidate certification: https://www.sos.texas.gov/elections/forms/2026-write-In-ballot-cert.pdf (14 in-scope write-ins: US Senate 4, CD 27, CD 33, Governor 4, Lieutenant Governor 2, SBOE 6, HD 124).
3. Texas Secretary of State Candidate Bio Portal (https://goelect.txelections.civixapps.com/ivis-cbp-ui/; data from `https://goelect.txelections.civixapps.com/api-ivis-cbp/api/cbp/findQualifiedCandidates`), election lists 53815 (2026 General), 53814 (2026 Democratic Primary), 53813 (2026 Republican Primary), 58314 (Democratic Primary Runoff), 58315 (Republican Primary Runoff). Used for primary and runoff candidates (filing status IP/IR/LP/CG kept; R = rejected, W = withdrawn, DI = declared ineligible dropped), structured name fields, the general-election incumbent flag (CSV only) and `txWebsiteUrl`. Emails and addresses were not taken.
4. FEC candidate master `cn26.zip` (https://www.fec.gov/files/bulk-downloads/2026/cn26.zip), TX House and Senate: FEC IDs in the review CSV only.
5. The Green Papers, https://www.thegreenpapers.com/G26/TX: cross-check only. Ballotpedia was not used.

## What was cross-checked

* Ballot certification vs Bio Portal general list: all 231 in-scope contests and 468 party/independent nominees agree (only office-name formatting differs, e.g. "(UNEXPIRED TERM)" vs "- UNEXPIRED TERM").
* Every Democratic and Republican nominee is in that party's primary list for the same office, and in the runoff list where a runoff was held, except the four in conflict 3.
* The Green Papers: the surname of every US Senate, US House and statewide nominee appears on its TX page; its list of runoff contests matches the Bio Portal runoff lists for federal and statewide offices.

## Conflicts and judgment calls

1. **Primary and runoff vote totals are not included.** The official results site (results.texas-election.com) is behind a bot challenge and could not be read. Winners are not recorded anyway; nominees come from the ballot certification, and runoff candidates from the Bio Portal runoff lists. Primary races have `status: completed` and no `certification_status`.
2. **Cancelled runoffs.** The Bio Portal Republican runoff list still has CD 23 (Brandon Herrera `IR`, Tony Gonzales withdrawn) and CD 32 (Jace Yarbrough `IR`, Ryan Binkley withdrawn). The Green Papers says both runoffs were cancelled after the withdrawals, and its runoff list omits them. No runoff race or candidacy was created for CD 23 or CD 32.
3. **Nominees missing from the primary lists.** Tom Luck (D, HD 19), Carlos (Charlie) Garza (R, SBOE 13), Coretta Mallet-Fontenot (D, SBOE 4 unexpired) and Tammie Nielsen (R, SBOE 4 unexpired) are on the ballot certification but in no 2026 primary list for that office. They were probably nominated by party executive committees, but that is not stated, so it is not recorded. They have general candidacies only.
4. **Libertarian and Green nominees** are chosen by convention, not primary, so they get general candidacies only. No nomination office or race was created for them.
5. **Same name in two contests.** Avery Ayers (US Senate write-in; Republican primary CD 38), Arturo Espinosa and Stephen Samuelson (Lieutenant Governor write-ins; Republican primary for Governor) appear with identical ballot names in two contests. Each is treated as one person with two candidacies. Split them if they are different people.
6. **Party label in PR #7.** `federal_candidates_2026.yml` labels TX Democrats "Democrat" (the SoS prints "DEM"/Democratic) and uses `kind: unclassified`. Those records were not edited; new TX candidacies use `Democratic`/`Republican`/`Libertarian`/`Green` party lines that reference `PARTY-USA-TX-*`, and "Independent" (Ben Mendoza, CD 23, existing record) is a designation.
7. **Court of Criminal Appeals judges** use the shared `POSITION-JUSTICE` (court of last resort for criminal cases); an Office note says so. 15th Court of Appeals offices use `POSITION-APPELLATE_JUDGE` under a statewide district `DISTRICT-USA-TX-APPEAL-COA_15`.
8. **Unexpired terms.** Supreme Court Place 2 and SBOE District 4 are unexpired-term contests; it is in the race descriptions.
9. **Names.** The SoS prints names in capitals. They were converted mechanically (Mc, O', hyphens, initials kept). Nicknames in quotes or parentheses and suffixes (Jr, III) were dropped from Person attributes; the exact ballot text is in the CSV. Surnames follow the Bio Portal's last-name field (e.g. `RODRIGUEZ_PRILLIMAN`). Existing federal persons keep their PR #7 names and codes.
10. **Incumbency** is not in the YAML. The Bio Portal general-election incumbent flag is in the CSV (`sos_incumbent_flag`), blank where the SoS left it empty.
11. **Races in the state primary election.** Per CONTRIBUTING.md, district nomination races sit in `ELECTION-USA-TX-2026_PRIMARY` / `_PRIMARY_RUNOFF` even though the nomination office's jurisdiction is the district.

## Name-code collisions: 40 candidates NOT in the YAML

These ballot names produce a name code already used in this repository (main, or the California PR #11 branch), or shared by two different TX candidates. Ascent issues the disambiguators, so these people and all their candidacies (68 rows in the CSV, 25 of them Nov 3 nominees) are left out and listed in `tx_2026_review.csv` with `in_pr = N`.

| Race | Candidate (ballot) | Candidacies | Name code | Existing codes |
|---|---|---|---|---|
| Attorney General | NATHAN JOHNSON | general (Democratic); Dem primary; Dem runoff | PERSON-JOHNSON_NT | PERSON-JOHNSON_NT |
| Court of Criminal Appeals, Judge, Place 3 | THOMAS SMITH | general (Republican); Rep primary; Rep runoff | PERSON-SMITH_TH | PERSON-SMITH_TH_7E |
| State Board of Education District 6 | MARGO JORDAN | general (write-in) | PERSON-JORDAN_MR | PERSON-JORDAN_MR_8S |
| State Board of Education District 14 | AMY TAYLOR | general (Democratic); Dem primary | PERSON-TAYLOR_AM | PERSON-TAYLOR_AM_4F, PERSON-TAYLOR_AM_6K |
| State House District 15 | MONIQUA' S. SCOTT | general (Democratic); Dem primary | PERSON-SCOTT_MN | PERSON-SCOTT_MN_2Y |
| State House District 20 | TERRY M. WILSON | general (Republican); Rep primary | PERSON-WILSON_TR | other TX candidate: TERRI LEO WILSON |
| State House District 23 | CHERYL LYNN CLARK | general (Democratic); Dem primary | PERSON-CLARK_CH | PERSON-CLARK_CH_8A, PERSON-CLARK_CH_8Q |
| State House District 23 | TERRI LEO WILSON | general (Republican); Rep primary | PERSON-WILSON_TR | other TX candidate: TERRY M. WILSON |
| State House District 39 | ARMANDO MANDO MARTINEZ | general (Democratic); Dem primary | PERSON-MARTINEZ_AR | PERSON-MARTINEZ_AR |
| State House District 51 | MARIA LUISA "LULU" FLORES | general (Democratic); Dem primary | PERSON-FLORES_MR | PERSON-FLORES_MR_9A |
| State House District 51 | JESSICA MARTINEZ | general (Republican); Rep primary | PERSON-MARTINEZ_JS | PERSON-MARTINEZ_JS_5K |
| State House District 57 | RICHARD HAYES | general (Republican); Rep primary | PERSON-HAYES_RC | PERSON-HAYES_RC |
| State House District 64 | ANDY HOPPER | general (Republican); Rep primary | PERSON-HOPPER_AN | PERSON-HOPPER_AN_8L |
| State House District 65 | MITCH LITTLE | general (Republican); Rep primary | PERSON-LITTLE_MT | PERSON-LITTLE_MT_2E |
| State House District 75 | MARY E GONZALEZ | general (Democratic); Dem primary | PERSON-GONZALEZ_MR | PERSON-GONZALEZ_MR_9A |
| State House District 104 | JESSICA GONZALEZ | general (Democratic); Dem primary | PERSON-GONZALEZ_JS | PERSON-GONZALEZ_JS_3C |
| State House District 107 | LINDA GARCIA | general (Democratic); Dem primary | PERSON-GARCIA_LN | PERSON-GARCIA_LN_2J |
| State House District 108 | MORGAN MEYER | general (Republican); Rep primary | PERSON-MEYER_MR | other TX candidate: MARC M. MEYER |
| State House District 109 | WILL CAMPBELL | general (Republican); Rep primary | PERSON-CAMPBELL_WL | PERSON-CAMPBELL_WL |
| State House District 125 | RICARDO 'RICK' MARTINEZ | general (Republican); Rep primary | PERSON-MARTINEZ_RC | PERSON-MARTINEZ_RC_5W |
| State House District 127 | MICHELLE WILLIAMS | general (Democratic); Dem primary | PERSON-WILLIAMS_MC | PERSON-WILLIAMS_MC_6F, PERSON-WILLIAMS_MC_9U |
| State House District 139 | CHARLENE WARD JOHNSON | general (Democratic); Dem primary | PERSON-JOHNSON_CH | PERSON-JOHNSON_CH_5X, PERSON-JOHNSON_CH_8L |
| State House District 142 | HEIDI HALL | general (Republican); Rep primary | PERSON-HALL_HD | PERSON-HALL_HD |
| State House District 144 | MARY ANN PEREZ | general (Democratic); Dem primary | PERSON-PEREZ_MR | PERSON-PEREZ_MR_4M |
| 15th Court of Appeals, Justice, Place 3 | MARC M. MEYER | general (Democratic); Dem primary | PERSON-MEYER_MR | other TX candidate: MORGAN MEYER |
| U.S. House District 5 | RUTH "TRUTH" TORRES | Dem primary; Dem runoff | PERSON-TORRES_RT | PERSON-TORRES_RT_4S |
| U.S. House District 18 | AL GREEN | Dem primary; Dem runoff | PERSON-GREEN_AL | PERSON-GREEN_AL_4P |
| U.S. House District 18 | GRETCHEN BROWN | Dem primary | PERSON-BROWN_GR | PERSON-BROWN_GR_9E |
| U.S. House District 21 | GARY TAYLOR | Dem primary | PERSON-TAYLOR_GR | PERSON-TAYLOR_GR_4J, PERSON-TAYLOR_GR_9D |
| State Senate District 21 | CORTNEY JONES | Dem primary | PERSON-JONES_CR | PERSON-JONES_CR_9A |
| State House District 64 | CHRISTIE WOOD | Dem primary | PERSON-WOOD_CH | PERSON-WOOD_CH_3Q |
| State House District 120 | JORDAN BROWN | Dem primary | PERSON-BROWN_JR | PERSON-BROWN_JR_9G |
| State House District 125 | DONOVON RODRIGUEZ | Dem primary | PERSON-RODRIGUEZ_DN | PERSON-RODRIGUEZ_DN |
| U.S. House District 16 | MARCY CHAVEZ | Rep primary | PERSON-CHAVEZ_MR | PERSON-CHAVEZ_MR_3R |
| U.S. House District 32 | GORDON HESLOP | Rep primary | PERSON-HESLOP_GR | PERSON-HESLOP_GR_6V |
| U.S. House District 35 | JOSH CORTEZ | Rep primary | PERSON-CORTEZ_JS | PERSON-CORTEZ_JS_5C |
| State Board of Education District 2 | CARRIE MOORE | Rep primary | PERSON-MOORE_CR | PERSON-MOORE_CR_6G |
| State Senate District 4 | CHARLIE MILLER | Rep primary | PERSON-MILLER_CH | PERSON-MILLER_CH_4L, PERSON-MILLER_CH_7N |
| State House District 8 | DANIEL HUNT | Rep primary | PERSON-HUNT_DN | PERSON-HUNT_DN_8K |
| State House District 86 | JAMIE HAYNES | Rep primary | PERSON-HAYNES_JM | PERSON-HAYNES_JM_3F |

## Not included

* Local, county, district court, justice of the peace, party offices, and special elections.
* Social media handles: none were looked up.
* Winners, advancement, vote totals and incumbency (see conflicts 1 and 10).

## Candidate websites

9 website Channels are in `candidate_accounts/`, each owned by the candidate's 2026 general Candidacy (the existing PR #7 Candidacy for federal nominees), with `official: true` and its own `source`. The Bio Portal had a website for only 11 in-scope general nominees. Each site was fetched on 2026-10-29; a site was kept only when it returned HTTP 200 and its page named the candidate. Omitted:

| Candidate | Given URL | Reason |
|---|---|---|
| MICHAEL MYERS | https://www.facebook.com/profile.php?id=61583624363660 | Facebook profile, not a website (social accounts are out of scope) |
| HUMBERTO PEREZ | Perez for Texas.com | malformed URL / no response |

## Files here

* `tx_2026_review.csv`: one row per candidacy (1391: general 482, primaries and runoffs 909).
* `district_crosswalk.csv`: new and existing district codes with the TIGER 2024 GEOID (state 48 + district number) where a layer exists. SBOE and Court of Appeals districts have none.
