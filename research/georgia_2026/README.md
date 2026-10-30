# Georgia 2026 candidates (primary and runoff)

## Sources (official only)
- May 19, 2026 General Primary, Georgia Secretary of State official results: https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926 (JSON: https://results.sos.ga.gov/results/public/api/elections/Georgia/GeneralPrimary51926/data)
- June 16, 2026 General Primary Runoff, official results: https://results.sos.ga.gov/results/public/Georgia/elections/06162026GeneralPrimaryRunoff (JSON: .../api/elections/Georgia/06162026GeneralPrimaryRunoff/data)

The candidate names come from the ballot options in those results. Vote counts are not used, and nothing is inferred from them: no winners, no nominees, no incumbency. The "(I)" marker on the results is removed and not recorded.

## Scope
- Statewide offices: U.S. Senate, Governor (new office), Lt. Governor, Secretary of State, Attorney General, Agriculture, Insurance, School Superintendent, Labor
- PSC Districts 3 and 5. These are new offices, elected statewide; each candidate must live in the district.
- U.S. House CD1–14
- State Senate SD1–56 and State House HD1–180. New districts and their general elections are added.
- Each party contest gets a nomination office and a May 19 primary race. Unopposed candidates are included because Georgia prints them on the primary ballot.
- Each of the 26 party runoffs gets a `-2026_PRIMARY_RUNOFF` race on the same nomination office (the TX precedent), with candidacies for the two runoff candidates.

## Gaps and flags
- **No general-election candidacies.** No reachable official general candidate list was found, because sos.ga.gov and mvp.sos.ga.gov return 403 to this environment. Primary results are not used to infer nominees. The general races exist so that candidacies can be added later from https://sos.ga.gov (2026 General Election qualified candidates list).
- **Not included:**
  - The special election for State Senate District 7 (all-party special, held with the primary and runoff)
  - Judicial contests, district attorneys and party questions
  - Local contests
- **No withdrawal data:** the results show only the candidates who were on the ballot.
- **Federal people reused:** 30 federal people in `federal_candidates_2026.yml` are linked to their primary candidacies (matched on same district, same party, and the same last name and first initial).
- **Shared name codes:** these same-name-code pairs are distinct people in different contests, and each got its own minted code:
  - Mathis: DeAndre / Danny
  - Clark: Jasmine / Josh
  - Williams: Alyssa Nia / Al
  - Thomas: Gregory / George
  - Anderson: Brian / Bradley B.
  - Harris: William (HD82) / William C. (HD126)
- **Name handling:** nicknames in quotes and suffixes are dropped from the name parts but kept in the ballot name in the review CSV.
