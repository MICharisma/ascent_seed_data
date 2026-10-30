# Idaho 2026: conflicts and flags

1. **Source mechanics:** the general list comes from the portal's public search, exported in full through the same request the page makes (`api-run.voteidaho.gov/api/FiledCandidates/SearchCandidates`). There is no static file, so a reviewer can re-check it at https://run.voteidaho.gov/search. The site still links a 2024 CSV only (https://voteidaho.gov/election-results/candidate-list/).
2. **Nominee = presence on the general list** (no "winner" mark in the results). This is an official source, but it isn't a canvass certificate of nomination.
3. **Name forms:**
   - "Pro-Life" (Constitution, Governor) is the ballot name as printed; it is stored as last_name only.
   - "Nickolas 007 Bonds" is stored with middle_name "007".
   - "Lisa Marie" is stored with last name Marie.
   - Possible compound surnames are left in the default split: Enrique Salas Viernes and Becky Sundin Mitchell.
   - "Den Hartog" is set as a compound surname.
   - Confirm all of these.
4. **After-primary withdrawals (7):**
   - David Roth (D, U.S. Senate, 9/1)
   - C. Sierra (Constitution, CD2, 8/17)
   - Brenda H. Quick (D, SD21, 8/5)
   - Anna Germana Scholes (Ind., SD24, 8/14)
   - Emily Fisher (D, HD23A, 8/26)
   - Enrique Salas Viernes (D, HD24B, 9/3)
   - John H Garrett (D, SD8, 6/15 per the primary list)
   - None of them has a general candidacy. Their primary candidacies keep nominee=Y.
5. **--new mints (12):** Brad Little, Kevin A Jones, Steve Johnson, Kirsten Faith Richardson, Mark Harris (SD35; not the NC congressman), Bryan Hopkins, Kevin Marsh, Brad Moore, Richard Marsh, Maureen Anderson, John H Garrett, Steve Miller.
6. Provisional usernames may collide with parallel state PRs.
