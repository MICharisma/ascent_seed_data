# Missouri 2026 candidates

## Sources (official only; saved from the Missouri Secretary of State)
- Certified Candidate List, 2026 Primary Election (Aug 4): https://s1.sos.mo.gov/CandidatesOnWeb/DisplayCandidatesPlacement.aspx?ElectionCode=750006905. It has 510 candidates; 500 are in scope after skipping the 10 Circuit Judge candidates.
- Candidates Withdrawn/Removed, 2026 Primary: https://s1.sos.mo.gov/CandidatesOnWeb/CandidatesRemoved.aspx?ElectionCode=750006905 (23 entries).
- 2026 General Election Certification of Candidates and Party Emblems, certified Aug 25, 2026 by Secretary of State Denny Hoskins: https://www.sos.mo.gov/elections/candidates/

## Scope and modeling
- **Offices:** State Auditor and U.S. House CD1–8 (both existing offices), plus State Senate (17 even-numbered districts) and State House (163 districts with candidates). The new districts come with their general elections.
- **Primary races:** one nomination office and Aug 4 primary race per party contest that appears on the certified primary list. Missouri prints unopposed candidates on the primary ballot, so they are included. No primary is created where the official list has none.
- **General candidacies:** one per certified general candidate. Republican, Democratic and Libertarian candidates get party lines. The two independents (HD127 Racheal Martin, HD128 Shane Sawyer) get `Independent` lines of kind `petition`.
- **Federal people:** the 24 U.S. House general candidacies already in `federal_candidates_2026.yml` are referenced, and their people are reused for their primary candidacies.
- **No inference:** every general party nominee on the certification also appears on that party's primary list. Nominees are taken from the certification, not from results. Incumbency is not recorded.

## Flags
- **Withdrawals:** 23 are classified as `before-primary-ballot (withdrew)`. The removal dates run from 3/11/2026 to 6/9/2026, all before the Aug 4 primary, and none of these people is on the certified primary list. The source is the Withdrawn/Removed page.
  - Sean Smith (R) withdrew from CD5 and Mike Jones (R) withdrew from HD12. A Sean Smith is the certified R nominee in HD34 and a Mike Jones in SD34, but the withdrawal rows are not linked to those people because the source does not say they are the same person.
- **Same-name pairs kept as different people:** Chris Brown (HD16) and Chris Brown (HD75); Chad Perkins (HD40) and Cheryle Perkins (HD160).
- **Name codes shared with other states:** 27 people share a name code with an existing person. Each got a new code (`--new`), with no link.
- **Not in scope:** Circuit Judge partisan primaries and the judicial retention list.
- **Name handling:** nicknames in parentheses and suffixes (Jr, Sr, III) are dropped from the name parts but kept in the ballot name.
