# Nevada 2026 candidates

## Sources (official only; Nevada Secretary of State, saved files)
- 2026 Primary Election Statewide Certified List of Candidates (Jun 9 primary): 479 rows, 146 in scope.
- 2026 General Election Statewide Certified List of Candidates (Nov 3): 126 in-scope rows.
- Realtime candidate filing list, downloaded 2026-10-30 (1102 rows; 1101 `Filed`, 1 `Challenged Successfully`).
- Index: https://www.nvsos.gov/sos/elections/election-information/2026-election-information

## Scope and modeling
- **Offices:** Governor (new office), the existing Lt. Governor, Secretary of State, Treasurer, Controller, Attorney General and U.S. House CD1–4 offices, and new State Senate (11 districts) and Assembly (all 42 districts) offices with their districts and general elections.
- **Primary races:** one nomination office and Jun 9 primary race per party contest on the certified primary list (46 contests; Democratic and Republican only). Under Nevada law a party contest with one candidate is not on the primary ballot; every primary-list row is `In Primary = Y`. So 62 D/R general nominees get no primary race (Mike's rule: no primary for unopposed nominees).
- **General candidacies:** party lines for Democratic, Republican, Libertarian Party of Nevada and Independent American Party. The 6 No Political Party candidates get the ballot label `No Political Party`, kind `petition`: William Johnson (CD4), Afzal Khan and Steven St John (CD1), Danielle Ford (Governor), Steven Samuel Cohen (SD8), Katherine Duncan (AD6).
- **Federal people:** the 14 existing U.S. House general candidacies are referenced and their people reused for primary candidacies when district, party, surname and first initial match.
- **Names:** taken from the "Candidate Name" column, with the ballot name ("Last, First") deciding the surname (e.g. Guzman Fralick, Bachman Dodge, La Rue Hatch). Nicknames and suffixes are dropped from name parts.
- **No inference:** nominees come from the general certified list, not from results. Every D/R nominee in a contested primary is on that party's primary list. Incumbency is not recorded.

## Flags
- **Withdrawals/removals:** the only `Challenged Successfully` row (Major Benjamin David Samia, Clark County Sheriff) is out of scope; the general list's two `Successfully Challenged` notes are a Family Court judge and a GID seat, also out of scope. No in-scope removals; the sources give no withdrawal dates.
- **Same surname, kept distinct:** Ira D Hansen (SD14 R) and Irina Hansen (Governor primary); Aaron D. Ford (Governor D) and Danielle Ford (Governor NPP).
- **Name codes shared with other states:** 9 people (e.g. Brittney M. Miller, Steven Samuel Cohen, Charlene Young) got new codes (`--new`) with no link.
- **Not in scope:** county, city, judicial, school board, Board of Regents and other nonpartisan offices (831 primary-list/general-list rows skipped).
