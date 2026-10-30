# Maryland 2026 general and primary candidacies

Built by Ascent Clerk (overnight worker B) on 2026-10-29 in micharisma-seeds/v1 under the current AGENTS.md / CONTRIBUTING.md / WORKERS.md contract.

## Sources (official first)

- Maryland State Board of Elections, 2026 Gubernatorial Primary candidate list (CSV): https://elections.maryland.gov/elections/2026/primary_candidates/2026_GP_statewide_candidatelist.csv
- Maryland State Board of Elections, 2026 Gubernatorial General candidate list (CSV, last updated 10/16/2026): https://elections.maryland.gov/elections/2026/general_candidates/2026_GG_statewide_candidatelist.csv
- Maryland State Board of Elections, official 2026 primary results (seat counts, ballot presence): https://elections.maryland.gov/elections/2026/primary_results/index.html
- Existing repo records reused: federal_candidates_2026.yml, statewide_races_2026.yml, elections_2026.yml, federal_races_2026.yml.

## Scope

- In: Governor/Lt. Governor, Comptroller, Attorney General, 8 US House seats (no US Senate race in Maryland in 2026), all 47 State Senate seats and all House of Delegates districts/subdistricts, plus the June 23 Democratic and Republican primaries.
- Deferred: non-primary filer (Working Class Party) (1), non-primary filer (Green) (1), non-primary filer (Unaffiliated) (1), non-primary filer (Other Candidates) (1), Judge of the Circuit Court (2), Justice Supreme Court of Maryland (1), Judge Appellate Court of Maryland At Large (1). Circuit judges are local; Supreme Court/Appellate Court entries are retention questions.

## Counts

- General contests: 130; party primary races: 218
- General candidate entries: 325; primary candidate entries: 506
- Records: 812 Candidacy, 118 District, 118 Election, 337 Office, 2 Party, 505 Person, 337 Race
- General candidates reused unchanged from existing repo files: 19
- New people whose name code was already used elsewhere (minted with --new; no cross-state or same-person link): 31

## Modeling

- Every Person definition has a full code from `tools/seed_contract.py mint` and a matching provisional username. All three manifests carry document-level `scope: state: STATE-USA-MD`, so districts nest under the state.
- Primaries are nominations: each party+contest on the official primary list gets a POSITION-NOMINEE office (nominee_for the general office, nominating_organization the party) and a race in ELECTION-USA-MD-2026_PRIMARY. Contests/parties absent from the official primary list get no primary.
- Party labels are as printed by the official source. No winner, incumbency or vote total is recorded.
- House of Delegates: 3-member districts, and 1- or 2-member subdistricts (A/B/C). Each district/subdistrict is one District and one multi-seat Office; the seat count ("Vote for up to N") is in the race description, taken from the official primary results headers. Each party nomination office also sets `nominee_count` to that district or subdistrict's seat count. General offices retain the seat count in the race description.
- Names use the SBE split fields (ballot last name and suffix; first and middle name), so compound surnames come from the official record, not inference.
- Withdrawn/disqualified/declined candidates are not given candidacies unless the official primary results show them on the ballot (then status withdrawn). Each is classified in the review CSV by its official status date: before-primary-ballot: 43, unknown: 6, after-primary: 11.
- Green and Working Class Party nominees are nominated by party designation, not primary; they have general candidacies only (ballot line kind unclassified). Unaffiliated petition candidates use kind designation. "Designated by Central Committee" general nominees filled a vacancy after the primary and are noted in the CSV.
- Websites: 182 verified Channel records (site loaded and named the candidate); 38 omitted (see conflicts.md).

## Flags for review

- Review the Central Committee designations and the general-list withdrawals (classified after-primary by date).
- The existing federal file uses "Democrat" labels with kind unclassified for Maryland federal candidates; reused unchanged.
- Party primaries with no same-party nominee on the general list: 1; general nominees with no matching primary candidacy: 2; names in more than one contest: 8; existing repo candidacies not matched: 0. Details in conflicts.md.

## Files

- `md_2026_review.csv`: one row per candidate entry with person code, mint facts/resolution, candidacy code, withdrawal class and source.
- `district_crosswalk.csv`: legislative district codes to TIGER 2024 GEOIDs.
- `conflicts.md`: automatic and manual flags.
