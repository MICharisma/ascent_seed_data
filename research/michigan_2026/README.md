# Michigan 2026: state candidate seed (ascent-clerk)

## Sources (official only)
The Michigan Department of State, Bureau of Elections publishes an Official Candidate Listing covering all state and judicial offices. It is linked from https://www.michigan.gov/sos/elections/election-results-and-data. The mvic.sos.state.mi.us mirror returns 403 to this box, so it was not used.
- **Primary (Aug 4, 2026):** https://mi-boe.entellitrak.com/etk-mi-boe-prod/page.request.do?page=page.miboePublicReport&electionType=PRI&electionYear=2026
- **General (Nov 3, 2026):** https://mi-boe.entellitrak.com/etk-mi-boe-prod/page.request.do?page=page.miboePublicReport&electionType=GEN&electionYear=2026
- The listings include status (WITHD or DISQ), party, filing date and filing method (Filing Fee, Petitions, Convention, Affidavit, Advanced Write-in).
- Rows repeated under per-county "Files In" headings were de-duplicated.

## Scope
- Governor (new office `OFFICE-USA-MI-GOVERNOR` with a general race).
- U.S. Senate and U.S. House 1-13: primaries here; the general candidacies already exist in the federal file.
- Secretary of State and Attorney General: convention nominees, general only, on the existing races.
- State Senate 1-38 and State House 1-110.
- **Not included:**
  - Lieutenant Governor running mates. They are on a joint ticket with the Governor, and each name is recorded in the review CSV notes.
  - The 2-seat statewide education boards (State Board of Education, UM Regents, MSU Trustees, WSU Governors).
  - Supreme Court and all judicial seats.

## Counts
- 7 parties: Democratic, Republican, Libertarian, Green, U.S. Taxpayers, Working Class, Natural Law.
- 148 districts and 148 elections.
- 473 offices and 473 races: 149 general and 324 primary nomination contests.
- 539 persons and 862 candidacies: 517 primary candidacy rows and 413 general entries. 68 U.S. Senate and House general candidacies were reused.
- **General ballot lines:** 165 D, 165 R, 25 Green, 23 Libertarian, 14 Working Class, 13 U.S. Taxpayers, 3 Natural Law, 5 No Party Affiliation (petition).

## Modeling notes
- Michigan prints unopposed candidates on the primary ballot, so every listed primary candidate on the ballot is modeled.
- Minor-party nominees (filing method "Convention") have general lines only.
- No Party Affiliation candidates are `petition` lines.
- Names are listed as "Last, First Middle". Generational suffixes (Jr., Sr., II) are part of the display name but are not split into a field.

## Withdrawals and disqualifications (with official listing citation)
- **Before the primary ballot:** 45 withdrew and 16 were disqualified.
- **Before the general ballot:**
  - Disqualified: 2 independent U.S. House filers in CD13, D. Etta Wilcoxon (Green, CD13) and Felix Thibodeau (Working Class, CD7).
  - Disqualified: HD3 Debra Davis (NPA) and HD9 Danetta L. Simpson (NPA).
  - Withdrew: Jay DeBoyer (R, HD63). He is the Republican Lt. Governor running mate.

## Flags for review
- **HD63:** Pamela Hornberger is the Republican general nominee but was not on the primary ballot. This is presumably a party-filled vacancy after DeBoyer's withdrawal. She has a general candidacy only.
- **SD36:** Mark W. Yonkman was disqualified from the Democratic primary but is the Democratic general nominee. This is presumably a vacancy fill. He has a general candidacy only; the primary disqualification is in WD.
- **HD34:** John Dahlgren was disqualified from the primary but won the Democratic line as an "Advanced Write-in", per the filing method. He has a general Democratic line only.
- **Same name code, kept as separate people:**
  - Brendan Johnson (SD9) and Brendan J. Johnson (SD26).
  - John P. Ludtke (HD76) and John Perry Ludtke Jr. (Attorney General). These may be the same person but were not linked.
- **16 name codes match people elsewhere in the repo**, all from other states. They were minted as new people with no link.
- Winners, incumbency and party were not inferred.

CI is disabled for this repo, so it was not run. All local checks pass: validate, unittest, accounts, export-catalog --check.

## Local integration corrections

Re-minted Larry Johnson as `PERSON-JOHNSON_LR_2N` with provisional username `johnson_lr_2n`. `PERSON-JOHNSON_LR_2M` remains with Kansas Laura Johnson; no alias links these different people.
