# Tennessee 2026 candidates (Aug 6 primary + Nov 3 general)

## Sources (official Tennessee Secretary of State, Division of Elections)
- Nov 3, 2026 general candidate lists (generated Sep 3, 2026), https://sos.tn.gov/elections/2026-candidate-lists: Governor_Nov2026.pdf, USSenate_Nov2026.pdf, USHouse_Nov2026.pdf, TNSenate_Nov2026.pdf, TNHouse_Nov2026.pdf.
- Aug 6, 2026 official primary results, listed under "2026 Election Results" at https://sos.tn.gov/elections/results:
  - https://sos-prod.tnsosgovfiles.com/s3fs-public/document/20260806RepublicanPrimarybyCounty.pdf
  - https://sos-prod.tnsosgovfiles.com/s3fs-public/document/20260806DemocraticPrimarybyCounty.pdf
  - (also saved: 20260806AllbyPrecinct.xlsx)
- The pre-primary candidate lists are no longer posted (the candidate-lists page now has only the Nov lists), so primary candidates come from the official results, which list every candidate on each primary ballot.

## Scope and modeling
- **Offices and districts:** Governor (new office); existing U.S. Senate and U.S. House CD1–9 offices; new State Senate (17 odd-numbered districts) and State House (98 districts with candidates) offices with their general elections.
- **Primary races:** one nomination office and Aug 6 primary race per party contest with at least one ballot candidate in the official results: 204 contests, 293 primary candidacies. Tennessee prints unopposed candidates on the primary ballot (they get votes in the results), so they are included, as in Missouri. 49 party contests show "No Candidate Qualified" and get no primary.
- **Registered write-ins excluded** from primary candidacies (5): David Fey (R: Governor, U.S. Senate, CD3), Lore Bergman (D, CD7), Britney Thornton (D, HD93).
- **General candidacies:** from the Nov lists only; nominees are not inferred from vote totals. Republican and Democratic candidates get party lines; "Independent" candidates get `Independent` lines of kind `petition`.
- **Federal people:** the 56 existing U.S. Senate and U.S. House general candidacies are referenced, and their people are reused for primary candidacies (district, party, surname and first initial match).

## Flags
- **HD84 D:** the official primary results list Kyler L. Gilkey and Joe Towns Jr., but the Nov list's Democratic nominee is Matthew Szalaj. Szalaj has no primary candidacy; the source gives no reason (possible replacement nominee). Needs review.
- **HD26 D:** primary between Nathan B. Denton and Lucian Lafae, but the Nov list has no Democratic candidate. No general candidacy created.
- **HD93:** Republican "No Candidate Qualified"; Democratic primary had only write-in Britney Thornton; the Nov list says no candidate qualified, so no general race.
- **Same names in two contests, kept as different people:** the official lists and results give no statement that these are the same person, so nothing is linked (same name and same city on the Nov lists for Taylor/Pearson): Brent Taylor (CD9 R / SD31 R, both Eads), Justin J. Pearson (CD9 D / HD86 D, both Memphis), London Lamar (CD9 D primary / SD33 D), Vincent Dixie (CD7 / HD54), Todd Warner (CD9 R primary / HD92), Kevin Lee McCants (Governor D / U.S. Senate D primaries). Needs review.
- **No withdrawal data:** neither source lists withdrawals.
- **The four "Tennessee" PDFs in az-2026/raw** are Arizona Secretary of State files and were not used.
- **Name codes shared with other states:** 24 people got new codes (`--new`), with no link.
- **Name handling:** nicknames in quotes or parentheses and suffixes are dropped from the name parts but kept in the ballot name.
