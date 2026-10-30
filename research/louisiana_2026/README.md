# Louisiana 2026 candidacies (closed party primaries, Nov 3 general / open primary)

Built by Ascent Clerk (overnight worker B) on 2026-10-29 in micharisma-seeds/v1 under the current AGENTS.md / CONTRIBUTING.md / WORKERS.md contract.

## Sources (official first)

- Secretary of State Candidate Inquiry (official qualifying lists) for Nov 3, 2026: https://voterportal.sos.la.gov/CandidateInquiry?electionDate=20261103 ; May 16 closed party primary: https://voterportal.sos.la.gov/CandidateInquiry?electionDate=20260516 ; June 27 second party primary: https://voterportal.sos.la.gov/CandidateInquiry?electionDate=20260627. Per-office pages use https://voterportal.sos.la.gov/CandidateInquiry/StatewideCandidate/CandidateList?electionId=<electionId>&officeIds=<officeId> (election ids 344, 342, 343). The pages also show candidate addresses, phones and emails; those raw pages are not committed, only names, party and status.
- SOS release on Act 7 of 2026 (U.S. House primaries cancelled, moved to Nov 3 open primary / Dec 12 general): https://www.sos.la.gov/media/dcvl5ojl/051426-fall-house-races.pdf
- Governor's Executive Order JML 26-038 suspending the House party primaries: https://gov.louisiana.gov/assets/2026-Executive-Orders/JML-Exective-Order-26-038.pdf
- SOS Nov 3 quick facts: https://www.sos.la.gov/media/x2jfrc1e/louisiana-election-quick-facts.pdf
- Existing repo records reused: federal_candidates_2026.yml, federal_races_2026.yml, elections_2026.yml.

## Scope

- In: U.S. Senate and Public Service Commission districts 1 and 5 (closed party primaries and Nov 3 general).
- U.S. House (not re-emitted here): the Nov 3 open primary is already modeled in federal_races_2026.yml / federal_candidates_2026.yml as RACE-USA-LA-CONGRESS-CD_n-2026_PRIMARY. All 39 candidates on the official Nov 3 lists (CD1-6) match a candidacy there by district and surname; none missing, none extra.
- Deferred: May 16 closed-party U.S. House filings cancelled by Act 7 (listed "Other/Disq"; not modeled) (31), BESE District 1 (8), State Representative 92nd Representative District (Nov 3 open primary, unexpired-term special) (3), State Representative 39th Representative District (1); Supreme Court, appellate and district judges; local offices. The legislature, governor and other statewide executives are not elected in 2026 (they are elected in 2027).

## Counts

- General contests: 3; party primary races: 5
- General candidate entries: 7; primary candidate entries: 16
- Records: 21 Candidacy, 7 Office, 2 Party, 16 Person, 7 Race
- General candidates reused unchanged from existing repo files: 2
- New people whose name code was already used elsewhere (minted with --new; no cross-state or same-person link): 3

## Modeling

- Every Person definition has a full code from `tools/seed_contract.py mint` and a matching provisional username. All three manifests carry document-level `scope: state: STATE-USA-LA`, so districts nest under the state.
- Primaries are nominations: each party+contest on the official primary list gets a POSITION-NOMINEE office (nominee_for the general office, nominating_organization the party) and a race in ELECTION-USA-LA-2026_PRIMARY. Contests/parties absent from the official primary list get no primary.
- Party labels are as printed by the official source. No winner, incumbency or vote total is recorded.
- Louisiana now uses two systems. Closed party primaries (Act 1 of 2024) apply in 2026 to U.S. Senate, PSC, BESE and Supreme Court: the May 16 party primary needs a majority, with a June 27 second party primary for the top two; the nominees meet independents in the Nov 3 general. These are modeled as POSITION-NOMINEE offices in ELECTION-USA-LA-2026_PRIMARY, with the June 27 round folded into the same race. Nominations where one candidate qualified ("Unopposed") have no primary race.
- U.S. House uses the traditional open (jungle) primary this year: Act 7 cancelled the May/June House party primaries after Louisiana v. Callais and voided their votes. All House candidates, of every party, share one Nov 3 ballot; a majority wins outright, otherwise the top two (any party) meet in the Dec 12 open general. The existing federal files already model the Nov 3 contest as CD_n-2026_PRIMARY (no party-nominee offices), so this PR does not duplicate it. The Dec 12 runoff/general races must be added after the Nov 19 promulgation, only for districts with no majority winner.
- No winner, party or incumbency is inferred; parties are as printed on the qualifying lists. "No Party" is kind designation.
- Withdrawals: James "Jim" Long (unknown). The cancelled May House filings (status "Other/Disq") are not withdrawals and are not modeled.
- No websites: the qualifying lists have email addresses only, which are not recorded.

## Flags for review

- Flags: none
- Add Dec 12 open general (runoff) races for any House district without a Nov 3 majority winner.
- Party primaries with no same-party nominee on the general list: 0; general nominees with no matching primary candidacy: 0; names in more than one contest: 0; existing repo candidacies not matched: 0. Details in conflicts.md.

## Files

- `la_2026_review.csv`: one row per candidate entry with person code, mint facts/resolution, candidacy code, withdrawal class and source.
- `district_crosswalk.csv`: legislative district codes to TIGER 2024 GEOIDs.
- `conflicts.md`: automatic and manual flags.
