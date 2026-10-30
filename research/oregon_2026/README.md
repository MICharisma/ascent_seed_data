# Oregon 2026: state candidate seed (ascent-clerk)

## Sources (official only)
- ORESTAR candidate filings export, Secretary of State Elections Division: https://secure.sos.state.or.us/orestar/CFSearchPage.do
  - 2026 Primary Election (election id 1451, 2026-05-19): 350 rows
  - 2026 General Election (election id 1453, 2026-11-03): 263 rows
  - Export: `XcelCFSearch?ut=2&...&cfElection={1451|1453}&cfDisqualifiedCandidates=true` (includes disqualified/withdrawn filers)

## Scope
Governor, U.S. Senate, U.S. House 1-6, State Senate (odd-cycle seats on 2026 ballot), State House 1-60.
**Skipped (nonpartisan, noted only):** Circuit Court, Court of Appeals, Supreme Court, District Attorney, BOLI Commissioner. ORESTAR has no general rows for BOLI, Supreme Court or Court of Appeals; the existing BOLI general race in the repo was left as is (gap).

## Counts
- 7 parties: Democratic, Republican, Working Families, Independent Party of Oregon, Libertarian, Pacific Green, Progressive
- 75 districts + 75 elections; 227 offices / 227 races (76 general, 151 nomination contests)
- 246 persons, 396 candidacies (247 primary, 245 general); 18 federal candidacies reused from federal_candidates_2026.yml
- 63 general candidacies carry fusion (multiple nominating-party ballot lines on one candidacy)

## Modeling notes
- Oregon prints unopposed candidates on the closed primary ballot, so every primary filer gets a nomination candidacy (this is not the "unopposed without primary" case).
- General nominations won by **write-in in the primary** (ORESTAR filetype "Write In", e.g. Gomberg HD10 REP, Kaufmann HD18 DEM, Prozanski SD4 REP, Osborne HD2 DEM, Dobson HD39 REP, McDonald HD16 REP, Nguyen HD38 REP, Schimmel HD29 REP) are modeled as `party` ballot lines on the general candidacy with the ORESTAR filing date in notes. No primary candidacy was created for them, since they weren't on the printed primary ballot.
- Minor-party nominees (WFP, IPO, Libertarian, Pacific Green, Progressive) are chosen by party process, not the state primary, so they have general ballot lines only.
- Party, winner and incumbency are not inferred. No handles.

## Flags for review
- **HD24 Democratic:** Andrew Brunello was on the DEM primary ballot, but ORESTAR lists no DEM general nominee. Results weren't checked against the official canvass, and no withdrawal is recorded.
- **Federal fusion:** existing federal candidacies hold one ballot line; ORESTAR shows additional cross-nominations for some. These are in the review CSV notes; federal_candidates_2026.yml was not edited.
- **Withdrawn or not qualified:** 6 before the primary ballot and 1 before the general, classified with ORESTAR citations in or_2026_review.csv.
- **Internal name-code check:** Elvis Clark (HD41) and Ruby M Clark (HD20) are distinct people.
- No cross-state links were made for same-year candidates.
- **OFFICE-USA-OR-GOVERNOR** was not in the repo and is minted here.

## Files
or_2026_foundation.yml, or_2026_races.yml, or_2026_candidates.yml; research/oregon_2026/or_2026_review.csv, district_crosswalk.csv.

CI is disabled for this repo, so it was not run. All local checks pass: validate, unittest, accounts, export-catalog --check.
