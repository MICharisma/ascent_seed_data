# South Carolina 2026 general and primary candidacies

Built by Ascent Clerk (overnight worker B) on 2026-10-29 in micharisma-seeds/v1 under the current AGENTS.md / CONTRIBUTING.md / WORKERS.md contract.

## Sources (official first)

- South Carolina Election Commission (VREMS) candidate search, 2026 Statewide General Election, all offices: https://vrems.scvotes.sc.gov/Candidate/CandidateSearch?electionId=22596
- CSV export of that search (used locally; raw personal-data export is not committed): https://vrems.scvotes.sc.gov/Candidate/ExportSearchResults (CSV export of the search above, all offices). Pulled 2026-10-29.
- Existing repo records reused: federal_candidates_2026.yml, statewide_races_2026.yml, elections_2026.yml, federal_races_2026.yml.

## Scope

- In: US Senate, 7 US House seats, Governor/Lt. Governor, Secretary of State, Treasurer, Attorney General, Comptroller General, Superintendent of Education, Commissioner of Agriculture, all 124 State House seats, and the June 9 Democratic and Republican primaries. The State Senate is not elected in 2026 (next in 2028).
- Deferred: local/county offices (475), School Board (192), not a nominee: Defeated In Primary (115), Soil and Water District Commission (86), Watershed Conservation District (54), School Trustee (36), Fire District Commissioner (32), School Trustee District (24), School District At Large (17), School Board At Large (16), Public Service District (11), County Council District (9), Commissioner of Public Works (8), Fort Mill School District Trustees (7), School Board of Trustees District 3 (6), Board of Education (6), James Island Public Service District (5), School Board of Trustees District 1 (4), School Board of Trustees District 7 (4), Clover School District Trustee At-Large (4), School Board At Large District 9 (3), Rock Hill School District Trustee Seat 2 (3), Rock Hill School District Trustee Seat 4 (3), Solicitor Circuit 12 (2), School Board of Trustees District 5 (2), School Board of Trustees District 9 (2), Clover School District Trustee Seat 2 (2), Rock Hill School District Trustee At-Large (2), District 5 (Unexpired Term) (2), not a nominee: Petition Failed (1), not a nominee: Defeated At Convention (1), Solicitor Circuit 3 (1), Solicitor Circuit 5 (1), Solicitor Circuit 6 (1), Solicitor Circuit 13 (1), Solicitor Circuit 15 (1), York School District Trustee Seat 2 (1), York School District Trustee Seat 4 (1), York School District Trustee At-Large (1), Clover School District Trustee Seat 1 (1), Clover School District Trustee Seat 5 (1), St Andrews Public Service District Section 1 (1), St Andrews Public Service District At Large (1), St Andrews Public Service District Section 2 (1).

## Counts

- General contests: 140; party primary races: 73
- General candidate entries: 283; primary candidate entries: 189
- Records: 450 Candidacy, 124 District, 124 Election, 198 Office, 2 Party, 377 Person, 198 Race
- General candidates reused unchanged from existing repo files: 22
- New people whose name code was already used elsewhere (minted with --new; no cross-state or same-person link): 21

## Modeling

- Every Person definition has a full code from `tools/seed_contract.py mint` and a matching provisional username. All three manifests carry document-level `scope: state: STATE-USA-SC`, so districts nest under the state.
- Primaries are nominations: each party+contest on the official primary list gets a POSITION-NOMINEE office (nominee_for the general office, nominating_organization the party) and a race in ELECTION-USA-SC-2026_PRIMARY. Contests/parties absent from the official primary list get no primary.
- Party labels are as printed by the official source. No winner, incumbency or vote total is recorded.
- There is no separate official primary candidate list in VREMS for 2026; the general-election candidate file keeps primary losers with status "Defeated In Primary". A primary race is built only where two or more same-party candidates reached the primary ballot; a lone filer is nominated without a printed primary (S.C. Code 7-11-50), so no primary race.
- Runoffs (June 23) are not separate races; runoff participants are in the single primary race. Primary results/winners are not stated (the general candidacy shows the nominee).
- Minor-party nominees (Libertarian, Forward, United Citizens, Workers, Green, Alliance, Constitution) are nominated by convention: general candidacy only, kind unclassified. Petition candidates use kind designation.
- Names use the official split first/middle/last/suffix fields; ballot names are as printed. Lt. Governor running-mate names come from the Running Mate field and are split heuristically.
- Withdrawals classified from the official status and status date: before-primary-ballot: 11, after-primary: 6.
- No websites: the VREMS export has no website field (only contact phone/email, not used).

## Flags for review

- Review fusion: SC allows fusion; this file has one row per filing, so a candidate nominated by two parties would appear twice; check conflicts.md for multi-line candidacies.
- "Withdrew" (unqualified) statuses were classified by date.
- Party primaries with no same-party nominee on the general list: 0; general nominees with no matching primary candidacy: 0; names in more than one contest: 1; existing repo candidacies not matched: 0. Details in conflicts.md.

## Files

- `sc_2026_review.csv`: one row per candidate entry with person code, mint facts/resolution, candidacy code, withdrawal class and source.
- `district_crosswalk.csv`: legislative district codes to TIGER 2024 GEOIDs.
- `conflicts.md`: automatic and manual flags.
