# Tennessee 2026 candidates (general only)

## Sources
These are official Tennessee Secretary of State, Division of Elections general-election candidate lists for Nov 3, 2026. They were generated Sep 3, 2026 and published at https://sos.tn.gov/elections/2026-candidate-lists:
- Governor_Nov2026.pdf
- USSenate_Nov2026.pdf
- USHouse_Nov2026.pdf
- TNSenate_Nov2026.pdf
- TNHouse_Nov2026.pdf

## Scope and modeling
- **Offices and districts:**
  - Governor is a new office.
  - The U.S. Senate and U.S. House CD1–9 offices already exist.
  - The new districts, with their general elections, are State Senate (the 17 odd-numbered districts) and State House (98 districts with candidates).
- **Party lines:**
  - Republican and Democratic candidates get party lines.
  - Candidates listed as "Independent" get `Independent` lines of kind `petition`.
- **Federal people:** the 56 U.S. Senate and U.S. House general candidacies already in `federal_candidates_2026.yml` are referenced.

## Flags
- **No Aug 6 primary.** There are no primary candidacies, nomination offices or primary races. The four "Tennessee" PDFs found in /workspace/ascent/az-2026/raw/ were checked and are Arizona Secretary of State files, so they were not used:
  - partisan filing list, Feb 23–Mar 23
  - primary write-in/withdrawn list for the July 21 primary
  - "STATE OF ARIZONA OFFICIAL CANVASS"
  - general write-in/withdrawn list

  No official Tennessee primary list was available. Nominees are taken from the general list, not inferred.
- **No withdrawal data:** the general lists include only qualified candidates.
- **HD93:** "No Candidate Qualified", so no race was created.
- **Same names on two general ballots:** "Brent Taylor" appears in CD9 and SD31, and "Justin J. Pearson" appears in CD9 and HD86, exactly as printed. Each was minted as two distinct people because the source gives nothing to link them. This should be checked.
- **Name codes shared with other states:** 19 people share a name code with an existing person in another state. Each got a new code (`--new`), with no link.
- **Name handling:** nicknames in quotes and suffixes are dropped from the name parts but kept in the ballot name.
