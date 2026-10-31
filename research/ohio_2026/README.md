# Ohio 2026 candidates (May 5 primary + Nov 3 general)

## Sources
- **Ohio Secretary of State, May 5, 2026 Primary/Special Election Official Canvass** (https://data.ohiosos.gov/portal/past-election-results): `summary-level-official-results-2026-primary---{republican,democratic,libertarian}.xlsx`, sheets Statewide Offices, Justice of the Supreme Court, U.S. Congress and General Assembly. These were saved by a browser because ohiosos.gov is behind a JS challenge.
- **Franklin County Board of Elections, "2026 General Election Candidates"** (revised Oct 16, 2026; `franklin_2026_General_Candidate_List.pdf`). Used to cross-check nominees, for general-only independents, and for one replacement nominee.

## Scope and modeling
- **Offices:**
  - Governor is a new office. Ohio elects it jointly with the Lieutenant Governor.
  - New Ohio Supreme Court offices for the two seats on the ballot: the term starting 1/1/2027 and the term starting 1/2/2027.
  - New State Senate and State House offices for every district with a primary candidate, with their general elections: 116 districts.
  - Existing offices reused: U.S. Senate (unexpired term), CD1–15, Lieutenant Governor, Attorney General, Auditor, Secretary of State and Treasurer.
- **Primary:** one nomination office and May 5 primary race per party contest in the official canvass, with 408 primary candidacies across the R, D and L primaries.
  - Ohio prints unopposed candidates on the primary ballot, so they are included.
  - Write-in candidates marked (WI) in the canvass get `write_in` ballot lines.
  - Governor primary candidacies go on the governor half of the ticket. The canvass lists running mates as "A and B", and the note records the full ticket.
- **Nov 3 nominees:** each party contest's plurality winner in the certified official canvass is the nominee. Ohio has no primary runoff. Media calls were not used. Each general candidacy is labelled "Nov 3 nominee per the certified official May 5, 2026 primary results" with its vote counts.
  - For governor, each winning ticket also gets a Lieutenant Governor general candidacy for the running mate, in the existing LTG race.
  - The 36 existing U.S. Senate and U.S. House general candidacies on main are referenced, not duplicated. Their people are reused for the federal primary candidacies.
- **Write-in winners:** a contest won only by a write-in gets a general candidacy only when an official list confirms it. Confirmed: Franklin list (HD3 R Kent, HD5 R Cole, HD8 R Hunter-Kalagidis) or the existing federal file (CD5 L Veloff). The rest are flagged below. Ohio can require write-in nominees to reach a minimum vote, and I didn't check that.
- **Independents:** general-only, from the Franklin list (party "N/A" or "nonparty", not write-ins). They are Gary Josephson (CD15, already-modeled race) and Cameron Koffel (HD7). Both get `Independent` lines of kind `petition`. Registered general write-ins on the Franklin list are excluded: 3 governor tickets, 3 U.S. Senate, CD15 Ronan, SD25 Angus, HD3 Afriyie and HD5 Eldridge.
- **Totals:**

  | Record | Count |
  | --- | --- |
  | Parties | 3 |
  | Districts and elections | 116 |
  | Offices | 415 |
  | Races | 415 |
  | Persons | 378 |
  | Candidacies | 653 |

  The 653 candidacies are 408 primary and 245 new general. Another 36 federal general candidacies are reused.

## Flags (need review)
- **Statewide independents and third parties are unverified.** Only Franklin County's list was available, so independents in multi-county or other-county legislative districts are not covered. These existing main candidacies were not confirmed by any source used here: Greg Levy (U.S. Senate, "Other"), Nathan Weise (CD1, Libertarian; the L primary there had only write-in Jason Stoops), Tracey Tackett (CD4, Independent) and Sandeep Dixit (CD13, No Party). They were left as they are.
- **HD12 D:** Liam N. Strausbaugh won the certified primary, but the Franklin list shows Lee Yarsky as the Democratic candidate. The general candidacy is Yarsky's, sourced to the Franklin list. Strausbaugh keeps only his primary candidacy. No source gives the withdrawal or replacement timing.
- **Write-in-only primary winners with no general candidacy** (not confirmed on an official general list):
  - CD7 L Duvall-Gambino (23 votes)
  - Auditor L Jeffery (441)
  - SD5 D Harris (584)
  - SD9 R Matthews (214)
  - SD29 L Moore (3)
  - HD2 L Dodge (6)
  - HD6 L Crayton (5)
  - HD9 L Linnabary (4)
  - HD14 R Morgan (390)
  - HD21 R Barhams (178)
  - HD31 L Miller (13)
  - HD32 D Popovic (575)
  - HD40 D Hornbacker (289)
  - HD41 D White (1,910)
  - HD41 L Watkins (4)
  - HD42 R McMahon (100)
  - HD82 D McCray (269)
  - HD87 D Covrett (186)
  - HD88 L Machoukas (15)
  - HD92 D Senff (396)
- **Libertarian governor primary:** the canvass also lists write-in ticket Travis Jon Vought and Christy Jo Orr. Don Kissick and James L. Mills won.
- **Same names kept separate:** Sherrod Brown (U.S. Senate) and Shontel M. Brown (CD11); Andrew King (Supreme Court) and Angie King (HD84).
- **Name codes shared with other states (11, `--new`, not linked):** Todd Wilson, Anthony Bruce Campbell, Andrew King, Jesse Baker, Thomas West (the same name as an existing Thomas West; no source links them), Rachel Baker, Andrea White, Nick Morris, Angie King, James Antoni Joyce and Louis Murphy.
- **No withdrawal data** in the canvass. The only replacement seen is HD12 D above.
- **Not in scope:** Court of Appeals, State Central Committee and county offices.

## Checks
validate, unittest, accounts, export-catalog and `--check` all pass locally. CI stays disabled. Not merged.

## Local integration corrections

Removed invalid party associations from 28 write-in ballot lines. Source labels and `kind: write_in` are preserved; only party-kind lines may carry a party association.
