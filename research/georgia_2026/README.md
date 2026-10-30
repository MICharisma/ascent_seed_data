# Georgia 2026 candidates (primary and runoff)

## Sources (official only)
- May 19, 2026 General Primary, Georgia Secretary of State official results: https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926 (JSON: https://results.sos.ga.gov/results/public/api/elections/Georgia/GeneralPrimary51926/data)
- June 16, 2026 General Primary Runoff, official results: https://results.sos.ga.gov/results/public/Georgia/elections/06162026GeneralPrimaryRunoff (JSON: .../api/elections/Georgia/06162026GeneralPrimaryRunoff/data)

The candidate names come from the ballot options in those results. Vote counts are not used, and nothing is inferred from them: no winners, no nominees, no incumbency. The "(I)" marker on the results is removed and not recorded.

- **Qualifying lists** (saved from the Georgia Secretary of State's qualifying-candidate site, mvp.sos.ga.gov):
  - May 19, 2026 General Primary: 2,385 records; 697 are in scope.
  - Nov 3, 2026 General: 311 records.

## Scope
- Statewide offices: U.S. Senate, Governor (new office), Lt. Governor, Secretary of State, Attorney General, Agriculture, Insurance, School Superintendent, Labor
- PSC Districts 3 and 5. These are new offices, elected statewide; each candidate must live in the district.
- U.S. House CD1–14
- State Senate SD1–56 and State House HD1–180. New districts and their general elections are added.
- Each party contest gets a nomination office and a May 19 primary race. Unopposed candidates are included because Georgia prints them on the primary ballot.
- Each of the 26 party runoffs gets a `-2026_PRIMARY_RUNOFF` race on the same nomination office (the TX precedent), with candidacies for the two runoff candidates.

## Gaps and flags
- **Still no general-election candidacies.** The Nov 3 qualifying list has 311 records, but it covers only candidates who qualify for the general itself: independents, political-body candidates, specials and local contests. Party nominees are not on it. The in-scope records are:
  - **Disqualified (7, not added; classified `before-general-ballot (disqualified)`):**
    - Libertarians: Allen Buckley (U.S. Senate), Andrew Paul Underwood (CD14), Chase Russell Oliver (Governor), Colin McKinney (Insurance), Thomas Michael Blooming (PSC 5)
    - Independents: Stephen Matthew Acorn (HD137), Christina Potts (SD6)
  - **Not added:** Travis Terrell Lockhart (Independent, HD151) has the status "QUALIFIED - SIGNATURES REQUIRED", meaning his nominating petition is not shown as accepted. He is classified `unresolved`.
  - The other 5 disqualified records on the list are local contests, which are out of scope.

  No Democratic or Republican general candidacies are created, because that would mean inferring nominees from results.
- **Not included:**
  - The special election for State Senate District 7 (all-party special, held with the primary and runoff)
  - Judicial contests, district attorneys and party questions
  - Local contests
- **Cross-check against the primary qualifying list:** every candidate in the results matches a QUALIFIED record by contest, party and surname, except for the items below.
  - **HD108 (R):** the results print "Davila", but the qualifying list has ELVIA DAVILA-PELAYO. The surname is set to Davila-Pelayo.
  - **David Scott (CD13, D) and Lisa J Anderson (SD33, D):** both are QUALIFIED on the qualifying list but absent from the results ballot. Neither source gives a reason. They are classified `not-on-primary-ballot (reason not stated)` and have no candidacy.
  - **Withdrawals and disqualifications:** 14 withdrew and 3 were disqualified before the primary ballot, per the qualifying-list status. None of them is on the results. No withdrawal or disqualification date is given.
- **Federal people reused:** 30 federal people in `federal_candidates_2026.yml` are linked to their primary candidacies (matched on same district, same party, and the same last name and first initial).
- **Shared name codes:** these same-name-code pairs are distinct people in different contests, and each got its own minted code:
  - Mathis: DeAndre / Danny
  - Clark: Jasmine / Josh
  - Williams: Alyssa Nia / Al
  - Thomas: Gregory / George
  - Anderson: Brian / Bradley B.
  - Harris: William (HD82) / William C. (HD126)
- **Name handling:** nicknames in quotes and suffixes are dropped from the name parts but kept in the ballot name in the review CSV.
