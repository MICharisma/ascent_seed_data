# Oklahoma 2026 general and primary candidacies

Built by Ascent Clerk (overnight worker B) on 2026-10-29 in micharisma-seeds/v1 under the current AGENTS.md / CONTRIBUTING.md / WORKERS.md contract.

## Sources (official first)

- Oklahoma State Election Board candidate filings, April 1-3, 2026: https://filings.okelections.gov/ViewCandidates/2026040120260403/99/all
- Extract of that list: https://filings.okelections.gov/Home/GetExtractWithOffice/ECC/all (state-filed candidates extract). Pulled 2026-10-29. The extract includes candidate birth dates and contact details, so it is not committed; only derived fields are used.
- Official certified results: June 16 primary https://results.okelections.gov/OKER/?elecDate=20260616; Aug 25 runoff primary https://results.okelections.gov/OKER/?elecDate=20260825 (data from the site's public results API, enrapi/getelec and enrapi/GetResults, isOfficial=true).
- Official withdrawals list: https://oklahoma.gov/elections/candidates/2026-candidate-filing-information/2026-candidate-withdrawals.html
- Existing repo records reused: federal_candidates_2026.yml, statewide_races_2026.yml, elections_2026.yml, federal_races_2026.yml.

## Scope

- In: US Senate, 5 US House seats, Governor, Lt. Governor, Attorney General, Treasurer, Auditor and Inspector, Superintendent, Labor, Insurance and Corporation Commissioners, State Senate and State House seats up in 2026, and the June 16 party primaries (runoffs folded in).
- Deferred: District Judge (87), Associate District Judge (86), District Attorney (31), SEN DISTRICT 17 (Unexpired) (unexpired-term special) (5), REP DISTRICT 92 (Unexpired) (unexpired-term special) (2). Unexpired-term specials (SD 17, HD 92) need a separate special-election race and were not modeled.

## Counts

- General contests: 140; party primary races: 83
- General candidate entries: 237; primary candidate entries: 240
- Records: 458 Candidacy, 125 District, 125 Election, 209 Office, 3 Party, 375 Person, 209 Race
- General candidates reused unchanged from existing repo files: 19
- New people whose name code was already used elsewhere (minted with --new; no cross-state or same-person link): 25

## Modeling

- Every Person definition has a full code from `tools/seed_contract.py mint` and a matching provisional username. All three manifests carry document-level `scope: state: STATE-USA-OK`, so districts nest under the state.
- Primaries are nominations: each party+contest on the official primary list gets a POSITION-NOMINEE office (nominee_for the general office, nominating_organization the party) and a race in ELECTION-USA-OK-2026_PRIMARY. Contests/parties absent from the official primary list get no primary.
- Party labels are as printed by the official source. No winner, incumbency or vote total is recorded.
- Oklahoma has closed party primaries; a lone party filer is nominated without a primary, so no primary race is built for them.
- General nominees are taken from official certified results: a majority winner on June 16, or the Aug 25 runoff winner. No inference beyond those official counts, except where flagged (CD 1 Republican: runoff not held after a withdrawal).
- Independent filers use kind designation; no write-ins are allowed in Oklahoma.
- Names use the official first/middle/last/suffix fields from the filing extract.
- Withdrawals classified from the official withdrawal list and the extract removal fields: after-primary: 2, before-primary-ballot: 5.
- No websites: the state-filed extract has no website values.

## Flags for review

- Flags: ('CD', 1) Republican: nominee MARK TEDFORD by runoff withdrawal of Jackson Lahmeyer (no runoff race in official Aug 25 results)
- Party primaries with no same-party nominee on the general list: 0; general nominees with no matching primary candidacy: 0; names in more than one contest: 0; existing repo candidacies not matched: 0. Details in conflicts.md.

## Files

- `ok_2026_review.csv`: one row per candidate entry with person code, mint facts/resolution, candidacy code, withdrawal class and source.
- `district_crosswalk.csv`: legislative district codes to TIGER 2024 GEOIDs.
- `conflicts.md`: automatic and manual flags.
