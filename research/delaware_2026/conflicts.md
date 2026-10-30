# Delaware 2026: conflicts and judgment calls

1. **Federal party labels.** `federal_candidates_2026.yml` (PR #7) labels Coons and McBride "Democrat" with `kind: unclassified`; the Department prints "Democratic". The federal records are reused unchanged.
2. **Federal names.** The existing federal people are "Christopher A. Coons", "Michael Katz", "Joseph Arminio"; the ballot prints "Chris Coons", 'Michael "Dr. Mike" Katz', 'Joseph "Dr. Joe" Arminio'. Same people (same office, same state, FEC-sourced); reused.
3. **Ballot names needing review.**
   - "E. No-Trump Hansen" (U.S. Senate Democratic primary): recorded as first name "E.", middle "No-Trump", last "Hansen", exactly as printed. Maintainer may prefer a different split.
   - "Wm Shannon Morris" (HD 30): first "Wm", middle "Shannon".
   - "Watara T.F. Heath" (HD 8 R primary): middle "T.F.".
   - Compound surnames from context (campaign sites and legislature): Melanie Ross Levin (MelanieRossLevin.com), Melissa Minor Brown (legislature styles her Minor-Brown), Valerie Jones Giltner (Jones-Giltner). The minting tool forms the name code from the last surname word.
   - Kyra L Hoffner / Kyra L. Hoffner: same person on both lists (punctuation only).
4. **Late general filings.** David C. Graham (AG, R, filed 8/24), April Callaway (Auditor, R, 8/26) and several Republican legislative nominees filed after the July 14 filing deadline, presumably as party-designated nominees for vacancies on the ticket. The list shows them as Qualified; no primary candidacy is created because they were not on the primary list.
5. **State Senate seats.** The general list has 11 Senate districts (1, 5, 7, 8, 9, 12, 13, 14, 15, 19, 20). Taken as printed.
6. **Name-code collisions** with people in other states (PA House: Frank Burns, Maureen Madden; TX: Mike Miller; KS: David C. Graham) minted `--new` per the same-year cross-state rule.
