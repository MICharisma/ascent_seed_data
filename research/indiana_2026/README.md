# Indiana 2026: state candidate seed (ascent-clerk)

## Sources (official only, Indiana Election Division)
- **2026 Primary Election (May 5) candidate list, as of 3/25/2026:** https://www.in.gov/dA/916c64d0f5/Primary-Candidate-List-3.25.26.xlsx?language_id=1
- **2026 General Election candidate list (abbreviated), as of 9/22/2026:** https://www.in.gov/sos/elections/files/Candidate_List_Abbreviated_20260922_011251PM.xlsx
- Both are linked from https://www.in.gov/sos/elections/candidate-information/

## Scope
- U.S. House 1-9 (primaries only; the general candidacies already exist in federal_candidates_2026.yml).
- Secretary of State, State Comptroller and Treasurer of State: general only, since these nominees are chosen at party conventions. The existing statewide races were reused.
- State Senate (25 districts) and State House (all 100 districts).
- **Not included:** county, township, town, city, school, judicial, prosecutor and convention delegate/precinct committee rows (19,055 rows).

## Counts
- 3 parties: Democratic, Republican, Libertarian.
- 125 districts and 125 elections.
- 360 offices and 360 races: 125 general and 235 primary nomination contests.
- 374 persons and 607 candidacies: 357 primary and 271 general. 21 U.S. House general candidacies were reused.
- **General ballot lines:**
  - 132 Democratic, 116 Republican, 10 Libertarian (party)
  - 3 Independent, 1 Lincoln Party, 1 Socialist Party of Indiana, 1 Green (petition)
  - 7 declared write-ins (write_in)

## Modeling notes
- **Primaries:** Indiana prints unopposed candidates on the primary ballot, so every listed primary candidate has a nomination candidacy.
- **Libertarian** nominees are chosen at convention, so they have general lines only.
- **Petition parties:** minor parties without ballot status (Lincoln, Socialist Party of Indiana, Green) and independents are `petition` lines with no party code.
- **Write-ins:** declared write-in candidates are `write_in` lines with the label "Write-in". The listed affiliation is kept in the notes.
- Winners, incumbency and party were not inferred beyond the listed label.

## Flags for review
- **Ballot vacancies filled after the primary.** These 9 general nominees were not in that party's primary list, presumably named by party caucus or chair. They have a general candidacy only:
  - HD8 Eric Harris (R)
  - HD32 Paul G. Nix (R)
  - HD42 Brandi Vandivier (D)
  - HD52 Joseph Trost (D)
  - HD54 Nan Polk (D)
  - HD59 Josh Burbrink (D)
  - HD74 Lena Goffinet (D)
  - HD75 Mason Barclay (D)
  - HD90 David Lawrence Boyd (D)
- **Same name in two Indiana contests, kept as separate people** (not linked; please confirm or merge):
  - David Lawrence Boyd: CD6 Democratic primary and the HD90 general.
  - Coumba Kebe: HD29 Democratic primary and the Treasurer of State general (convention nominee).
  - Earl Harris, Jr. (HD2) and Eric Harris (HD8) share a name code but are different people.
  - John E Bartlett (HD33) and John L. Bartlett (HD95) share a name code but are different people.
- **Withdrawals are not recorded.** Neither list reports withdrawals. The primary list post-dates the withdrawal deadline, and candidates who dropped after the primary simply don't appear on the general list.
- **Name parsing:**
  - Nicknames in parentheses were dropped, e.g. "Cynthia (Cinde) Wirth".
  - Generational suffixes were dropped (the contract has no suffix field).
- **14 name codes match people elsewhere in the repo.** They were minted as new people with no link.

CI is disabled for this repo, so it was not run. All local checks pass: validate, unittest, accounts, export-catalog --check.
