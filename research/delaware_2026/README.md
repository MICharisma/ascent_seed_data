# Delaware 2026 candidacies

Built by Ascent Clerk on 2026-10-29 from the Delaware Department of Elections filed-candidates lists:

- General, Nov 3, 2026: https://elections.delaware.gov/candidates/candidatelist/genl_fcddt_2026.html (page "Last Updated: 2026-10-29 07:56 PM")
- Primary, Sep 15, 2026: https://elections.delaware.gov/candidates/candidatelist/prim_fcddt_2026.html

## Scope

| Contest | General candidacies | Notes |
|---|---|---|
| U.S. Senate | 2 (existing) | Coons and Katz general candidacies reused from `federal_candidates_2026.yml` |
| U.S. House At-Large | 2 (existing) | McBride and Arminio reused |
| Attorney General, State Treasurer, Auditor of Accounts | 7 | existing offices/races from `statewide_races_2026.yml` |
| State Senate | 21 in 11 districts (1, 5, 7, 8, 9, 12, 13, 14, 15, 19, 20) | single-member districts |
| State House | 65 in all 41 districts | single-member districts |

- 97 general candidates, 71 primary candidacies in 29 contested Sep 15 party primaries (23 Democratic, 6 Republican).
- 135 new Person records with minted full codes and provisional usernames; 4 existing federal people reused.
- 52 new districts (`scope: state: STATE-USA-DE` on the foundation document) with their general elections; TIGER 2024 GEOIDs in `district_crosswalk.csv`.
- 3 Party records: Democratic, Republican, Independent Party of Delaware (printed "Ind Pty of DE").
- 49 verified campaign websites in `candidate_accounts/de_2026_websites.yml` (owned by the general Candidacy).

County offices on the same list (New Castle, Kent, Sussex: 37 general and 9 primary rows) are out of scope for this PR.

## Primaries

Delaware holds closed party primaries only for contested nominations; the Department's primary list contains only those contests. Each is a POSITION-NOMINEE office (`nominee_for` the general office, `nominating_organization` the party) with a race in `ELECTION-USA-DE-2026_PRIMARY`. Unopposed nominees have a general candidacy only. Every listed primary candidate, winner or loser, has a primary candidacy. No winners or vote totals are recorded; the general list is the source for who is on the November ballot.

## People

All new people were minted with `tools/seed_contract.py mint`. Ten name codes are shared with existing people in other states or other local races (Frank Burns and Maureen Madden PA House, Mike Miller TX Governor, David C. Graham KS Senate, and six local VA/CT/CA names). All were minted `--new`: none share a state and nothing in-state links them. See the review CSV `mint_resolution` column.

Multi-word names split from context (see conflicts.md): Melanie Ross Levin, Melissa Minor Brown and Valerie Jones Giltner as compound surnames; Kerri Evelyn Harris, Bryan William Shupe, Timothy Dale Dukes, Michael Alexander Smith, Adriana Leela Bohm, Shane Nicole Darby and Ruby Keeler Schaeffer with middle names. Quoted nicknames are dropped from the name fields.

## Withdrawals

| Candidate | Office | Classification | Evidence |
|---|---|---|---|
| Lee Murphy (R) | Representative in Congress | before-primary-ballot | general list: filed 7/13/2026, "WITHDRAWN 7/21/2026"; not on the primary list |
| Nikki Miller (R) | State Representative District 20 | before-primary-ballot | general list: "WITHDRAWN 2/20/2026"; not on the primary list |
| Dan Poliseno (R) | State Representative District 20 | before-primary-ballot | general list: "WITHDRAWN 3/16/2026"; not on the primary list |

They have no candidacies; they are in the review CSV with `in_pr=N`.

## Websites omitted

12 filed websites failed verification on 2026-10-29: Lydia York (403), Austin Cassidy (500), Shawn L. Dottery (thequietcoalition.com loads but does not name him), Kendra Johnson (526), Jeffrey N. Spiegelman (no TLS response), Alonna Berry, Mike Smith, Bryan William Shupe, Valerie Jones Giltner, Maureen Madden, Ryan Stuckey (500), Ed Osienski (403). Several 403/500s look like bot protection; a browser check may confirm them.

## Checks (2026-10-29)

- `.venv/bin/python -m unittest discover -s tools -p 'test_*.py' -v`: 24 tests OK
- `tools/seed_contract.py export-catalog`, then `export-catalog --check`: OK
- `tools/seed_contract.py validate manifests examples`: 0 failed
- `tools/seed_contract.py accounts manifests/contributions/ascent-clerk/candidate_accounts`: 0 failed

CI (`validate-seeds.yml`) is disabled on the repository, so no CI run.
