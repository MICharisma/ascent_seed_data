# North Carolina 2026 (Ascent Clerk)

Official sources (NC State Board of Elections public bucket):
- Candidate listing: https://s3.amazonaws.com/dl.ncsbe.gov/Elections/2026/Candidate%20Filing/Candidate_Listing_2026.csv (rows with election_dt 03/03/2026 = primary ballot, 11/03/2026 = general ballot; per-county rows deduplicated)
- Mar 3 primary precinct results: https://s3.amazonaws.com/dl.ncsbe.gov/ENRS/2026_03_03/results_pct_20260303.zip (used only to check winners, withdrawals and runoff need; no vote totals recorded)

## Scope
US Senate, US House 1–14 (existing offices/races), Supreme Court Associate Justice Seat 1 (general only, no primary), Court of Appeals Seats 1–3, state Senate (50 districts) and state House (120 districts) – only districts with candidates in the listing. All NC contests are single-seat (vote_for 1 everywhere). No statewide executive offices are on the 2026 ballot. **Not modeled:** Superior Court judges, District Attorneys, clerks of court and county/municipal contests in the same file.

## Model
- Parties: Democratic, Republican, Libertarian, Green. One Unaffiliated general candidate (ballot line kind petition, no party).
- Nomination office + Mar 3 primary race (ELECTION-USA-NC-2026_PRIMARY) only for party contests on the official primary list (82). NC holds no primary when only one candidate files (G.S. 163-110), so those nominees have a general candidacy only.
- No second primary (May 12) occurred: no NCSBE results exist for that date, and no primary leader was at or below 30%.
- Names: legal first/middle/last from the SBE file (case taken from name_on_ballot); suffixes and nicknames are not stored.
- The 42 US Senate/House general candidacies in federal_candidates_2026.yml are reused (all matched; persons reused for their primaries).

## Counts
4 parties, 170 districts + 170 elections, 256 offices / 256 races (174 general offices, 82 nomination offices), 449 new persons, 529 candidacies (205 primary entries, 366 general entries, 42 general reused).

## Withdrawals / substitutions (review CSV, in_pr = N)
- US House 11 REP: Chuck Edwards won the primary, absent from the general list; Jennifer Capps Balkcom named REP nominee 08/11/2026 (G.S. 163-114).
- HD 117 REP: Balkcom (primary winner) moved to US House 11; Chelsea Walsh named 08/14/2026. Balkcom is one person with candidacies in both contests.
- HD 32 DEM: Curtis McRae won the primary, replaced by Bryan K. Cohn 06/22/2026.
- HD 119 REP: Mike Clampitt won the primary, replaced by runner-up Anna Ferguson 04/13/2026.
- HD 73 DEM: Kim DeLaney printed "DECEASED"; the contest shows 0 votes tabulated, so no DEM primary is modeled; Thomas J. Monks is the nominee.
Reasons for the withdrawals are not stated in the official files.

## Collisions
25 name codes shared with people in other states → all minted `--new` (no cross-state links). Internal: Don Davis (US House 1) and Danny E. Davis (HD 118) are distinct people.

## Notes
- Name mismatch handled: "DeDreana Freeman" (filing) = "Dedreana Freeman" (results), SD 22 DEM.
- No websites in the source, so no candidate_accounts file.
- CI ("Validate seed contributions") is disabled on the repo and was not enabled; all local checks pass.
