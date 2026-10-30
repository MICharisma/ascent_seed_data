# New Mexico 2026 (Ascent Clerk)

Built 2026-10-29 from official New Mexico Secretary of State files only (Candidate Portal, saved in full):

| File | URL |
|---|---|
| 2026 General Election Contest/Candidate List (524 rows) | https://candidateportal.servis.sos.state.nm.us/CandidateList.aspx |
| 2026 Primary Election Contest/Candidate List (676 rows) | https://candidateportal.servis.sos.state.nm.us/CandidateList.aspx?eid=2911 |

Each row has the contest, district, party, the SoS first/middle/last name fields, the filing date and a status (Qualified, Withdrawn or Disqualified).

## What is in the PR

- **Statewide:** Governor (new office, POSITION-GOVERNOR; no NM Governor office existed), plus the existing Lieutenant Governor, Secretary of State, Attorney General, State Auditor, State Treasurer and Commissioner of Public Lands races, which are referenced unchanged.
- **Federal:** the U.S. Senate and CD 1-3 general races exist in `federal_candidates_2026.yml` and 8 federal people are reused unchanged. This PR adds the primary nomination races plus general candidacies that were missing (write-ins).
- **Governor/Lt. Governor ticket:** nominated separately on June 2 and elected jointly in November. The SoS general list prints "Governor and Lieutenant Governor" as one line (Haaland and Garcia Richard, D; Hull and Gallegos, R). This PR models them as separate Governor and LG general candidacies paired by party, with the ticket noted (as for PA).
- **State House:** all 70 districts. Districts, offices and general races are new (`DISTRICT-USA-NM-HOUSE-HD_n`).
- **State Senate District 33 only:** the NM Senate is elected in presidential years (2024, 2028). SD 33 is the only Senate contest on both 2026 lists, and the lists don't say why (presumably an unexpired term). Check this.
- **Public Education Commission:** the districts on the 2026 lists, mapped to POSITION-SCHOOL_BOARD_MEMBER as the TX SBOE was.
- **Court of Appeals Position 1:** partisan (Kris Houghton, D, unopposed). New office, POSITION-APPELLATE_JUDGE.
- **Primaries (June 2, certified June 23):** one POSITION-NOMINEE office and one primary race for each contest and party with a Qualified primary candidate. Every Qualified primary candidate gets a candidacy, including unopposed ones, because NM prints unopposed candidates on the primary ballot. **No vote totals:** the SoS results site now shows the general. The nominee flag in the review CSV comes from the official general list (same office, party and name).
- 163 new people, 292 new candidacies (165 primary + 127 general), 3 parties, 76 districts, 2 new offices with existing Positions. No new Positions.

## Not included

- Supreme Court and Court of Appeals **retention** questions (yes/no, not candidacies). District, metropolitan, magistrate, municipal and probate judges, and all county offices, are out of scope.
- **Websites:** the SoS lists give no candidate websites, so `candidate_accounts/` is untouched.

## Withdrawals and disqualifications

See conflicts.md and the `withdrawal` column. 6 are after-primary, 2 unknown, and 22 were disqualified (never on a ballot, so no candidacy).

## Names

Names are converted from the SoS all-caps text to title case. The surname comes from the SoS last-name field, which settles compound surnames such as Garcia Richard, Toulouse Oliver, Vanden Heuvel and De La Cruz. Nicknames in quotes or parentheses ("Patty", "Bill", "Manny", "Day") are stored as the nickname. The title-casing is mechanical, so check for lost internal capitals (for example "Oconnell", who was disqualified and is not in the PR). "(WRITE-IN)" is stripped and the line is written as a write_in ballot line.

## Codes

All new people were minted with `tools/seed_contract.py mint`. 14 share a name code with people in other states and were minted `--new` because there's no in-state evidence. Names are listed in conflicts.md.

## Local import correction

Write-in ballot lines retain their source party labels and `kind: write_in`. They omit the `party` reference because Ascent allows that association only on `kind: party` lines. Party nomination offices still identify the nominating organization.
