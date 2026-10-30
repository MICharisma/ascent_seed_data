# Kentucky 2026 general and primary candidacies

Built by Ascent Clerk (overnight worker B) on 2026-10-29 in micharisma-seeds/v1 under the current AGENTS.md / CONTRIBUTING.md / WORKERS.md contract.

## Sources (official first)

- Kentucky SOS candidate filings, 2026 General Election (official list of general-election candidates incl. nominees, independents, minor parties and write-ins): https://web.sos.ky.gov/CandidateFilings/default.aspx (Kentucky Secretary of State candidate filings, election "2026 General Election", Excel export). Pulled 2026-10-29. Contact columns are not used or committed.
- Certified 2026 primary results (May 19): https://elect.ky.gov/Documents/2026%20Primary%20Certification%20of%20Vote%20Totals%20Final.pdf (text extracted with pdftotext -raw).
- Existing repo records reused: federal_candidates_2026.yml, statewide_races_2026.yml, elections_2026.yml, federal_races_2026.yml.

## Scope

- In: US Senate, 6 US House seats, the 19 even-numbered State Senate seats, all 100 State House seats, and every contested May 19 party primary for those offices. No statewide constitutional offices are elected in 2026 (next in 2027).
- Deferred: District Judge (127), Circuit Judge Family Court (5), Circuit Judge (4), Judge of the Court of Appeals (3), Commonwealth's Attorney (3), Justice of the Supreme Court (1).

## Counts

- General contests: 126; party primary races: 50
- General candidate entries: 206; primary candidate entries: 144
- Records: 329 Candidacy, 119 District, 119 Election, 169 Office, 2 Party, 279 Person, 169 Race
- General candidates reused unchanged from existing repo files: 21
- New people whose name code was already used elsewhere (minted with --new; no cross-state or same-person link): 17

## Modeling

- Every Person definition has a full code from `tools/seed_contract.py mint` and a matching provisional username. All three manifests carry document-level `scope: state: STATE-USA-KY`, so districts nest under the state.
- Primaries are nominations: each party+contest on the official primary list gets a POSITION-NOMINEE office (nominee_for the general office, nominating_organization the party) and a race in ELECTION-USA-KY-2026_PRIMARY. Contests/parties absent from the official primary list get no primary.
- Party labels are as printed by the official source. No winner, incumbency or vote total is recorded.
- General nominees come straight from the official general-election filing list; nothing inferred from vote counts.
- Primary candidates come from the certification PDF. Its candidate names are printed as rotated column headers, so the extracted text splits some surnames (e.g. "CA TLETT"). The parser rejoins short fragments, and every parsed name count was checked against the vote columns. Where the candidate is also on the general list, the official general-list name fields are used; otherwise the given name is split from ballot order (first token = first name).
- Kentucky Party, Libertarian and Independent candidates use kind designation (a Party record is only made for D/R); write-ins are kind write_in.
- Withdrawals/disqualifications from the filing list (no dates given): after-primary: 1, unknown: 2.

## Flags for review

- Primary parse checks: all name counts matched vote columns
- Review primary-only surnames rejoined from fragments.
- Hal Rogers (CD 5, official list) linked to the existing repo candidacy for Harold Rogers in the same district and race (in-state, same office, incumbent).
- Party primaries with no same-party nominee on the general list: 0; general nominees with no matching primary candidacy: 0; names in more than one contest: 0; existing repo candidacies not matched: 0. Details in conflicts.md.

## Files

- `ky_2026_review.csv`: one row per candidate entry with person code, mint facts/resolution, candidacy code, withdrawal class and source.
- `district_crosswalk.csv`: legislative district codes to TIGER 2024 GEOIDs.
- `conflicts.md`: automatic and manual flags.
