# Colorado 2026 general and primary candidacies

Built by Ascent Clerk (overnight worker B) on 2026-10-29 in micharisma-seeds/v1 under the current AGENTS.md / CONTRIBUTING.md / WORKERS.md contract.

## Sources (official first)

- Colorado Secretary of State, 2026 Primary Election official candidate list: https://www.coloradosos.gov/pubs/elections/vote/files/2026/2026PrimaryCandidateListOfficial.xlsx (page https://www.coloradosos.gov/pubs/elections/vote/primaryCandidates.html)
- Colorado Secretary of State, 2026 General Election official candidate list: https://www.coloradosos.gov/pubs/elections/vote/files/2026/2026GeneralCandidateListOfficial.xlsx (page https://www.coloradosos.gov/pubs/elections/vote/generalCandidates.html)
- Existing repo records reused: federal_candidates_2026.yml (US Senate/House general candidacies), statewide_races_2026.yml, elections_2026.yml, federal_races_2026.yml.

## Scope

- In: US Senate, 8 US House seats, Governor, Lieutenant Governor, Attorney General, Secretary of State, State Treasurer, State Senate and State House seats on the 2026 ballot, and the June 30 primaries.
- Deferred (not built): State Board of Education (2 entries), University of Colorado Board of Regents (2 entries), RTD Board of Directors (1 entries), Colorado Supreme Court (1 entries), Colorado Court of Appeals (1 entries), District Court (1 entries), District Court - Denver Juvenile Court (1 entries), Distirct Court - Denver Probate Court (1 entries), County Court (1 entries), Associate County Court (1 entries). State Board of Education and CU Regents have no shared Position in manifests/foundation.yml and adding one in parallel with other workers risks conflicting codes; judicial seats are retention questions with no seat identifiers in the list; RTD is a special district. Pending a decision.

## Counts

- General contests: 100; party primary races: 186
- General candidate entries: 253; primary candidate entries: 235
- Records: 449 Candidacy, 86 District, 86 Election, 273 Office, 4 Party, 268 Person, 273 Race
- General candidates reused unchanged from existing repo files: 39
- New people whose name code was already used elsewhere (minted with --new; no cross-state or same-person link): 14

## Modeling

- Every Person definition has a full code from `tools/seed_contract.py mint` and a matching provisional username. All three manifests carry document-level `scope: state: STATE-USA-CO`, so districts nest under the state.
- Primaries are nominations: each party+contest on the official primary list gets a POSITION-NOMINEE office (nominee_for the general office, nominating_organization the party) and a race in ELECTION-USA-CO-2026_PRIMARY. Contests/parties absent from the official primary list get no primary.
- Party labels are as printed by the official source. No winner, incumbency or vote total is recorded.
- Write-in candidates on the official lists are included with ballot line kind write_in (they are on the official primary or general list but are not party nominees).
- Unaffiliated general candidates use ballot line kind designation; minor parties without a primary (Libertarian, Unity, American Constitution, Approval Voting, Forward, Center) use kind unclassified with the printed label, except Libertarian and Unity, which held some primaries and have Party records.
- Lieutenant Governor has no primary: the gubernatorial nominee designates the running mate after the primary (C.R.S. 1-4-502(3)). Governor and Lt. Governor are separate races paired by party.
- Name splits from context: Lynda Zamora Wilson, Lori Garcia Sander and Chela Garcia Irlando treated as compound (Hispanic double) surnames; Kenny Van Nguyen has middle name Van, surname Nguyen. Other three-part names keep the middle word as a middle name.

## Flags for review

- No websites: the Colorado SoS lists do not publish candidate websites, so candidate_accounts/ has no Colorado file.
- Withdrawals: the official lists give no withdrawal records. Three party primaries have no same-party nominee on the general list (SD 31 R DiManna, HD 28 R Bond, HD 58 D Smith); classified unknown.
- Two Republican general nominees are not on the Republican primary list for their seat (Paul Kohlhoff SD 25, Jennifer Qualteri SD 34): likely vacancy-committee replacements; not confirmed by an official vacancy record.
- Jena Griswold appears as the Democratic Attorney General nominee in the official general list (she was Secretary of State); recorded as printed.
- The existing federal file labels Colorado federal candidates "Democrat"/"Republican" with kind unclassified; the SoS prints "Democratic Party"/"Republican Party". Not edited (reused unchanged).
- Party primaries with no same-party nominee on the general list: 3; general nominees with no matching primary candidacy: 2; names in more than one contest: 0; existing repo candidacies not matched: 0. Details in conflicts.md.

## Files

- `co_2026_review.csv`: one row per candidate entry with person code, mint facts/resolution, candidacy code, withdrawal class and source.
- `district_crosswalk.csv`: legislative district codes to TIGER 2024 GEOIDs.
- `conflicts.md`: automatic and manual flags.
