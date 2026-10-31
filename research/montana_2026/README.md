# Montana 2026 seed research

Official sources (Montana Secretary of State candidate filing system). Both were exported as CSV with the grid's Export-to-CSV postback; raw/ex.py:
- General (Nov 3): https://candidatefiling.mt.gov/candidatefiling/CandidateList.aspx?e=450002987 (272 rows)
- Primary (June 2): https://candidatefiling.mt.gov/candidatefiling/CandidateList.aspx?e=450002928 (380 rows)

Blocked: https://sosmt.gov/elections/ returns 403 to the box. The filing system itself is reachable.

Scope: U.S. Senate, U.S. House CD 1-2, Public Service Commission districts 1 and 5, and the State Senate and State House districts on the 2026 ballot. All districts are single-member. Out of scope: Supreme Court Justice #4 and the district court judge races (nonpartisan judicial).

Modeling:
- Parties: Democratic, Republican, Libertarian. IND general candidates get `petition` lines labeled Independent.
- The general list's NON rows for partisan offices (Jami Dee Woodman for U.S. Senate, and Nate White, Elijah Tidswell and Cari Lynn Olson for state Senate) list "WRITE IN" in the web field and filed in August. They are modeled as `write_in` ballot lines.
- Primary: party rows with status NOMINATED or FILED become primary candidacies (all active). The NOMINATED status is not used to record a winner. Withdrawn and REMOVED rows are left out. IND/NON rows on the primary list (petition filers) are not primary candidates.
- The list's leading asterisk (incumbent marker) is stripped and ignored.
- PSC: new Districts DISTRICT-USA-MT-PSC-PSC_1/_5 and Offices using POSITION-PUBLIC_SERVICE_COMMISSIONER.
- Federal people and candidacies (12) are reused from federal_candidates_2026.yml.
- TIGER crosswalk: SLDU/SLDL = 30 + zero-padded district number.

Counts: 574 Candidacies, 328 Persons, 376 Offices / 376 Races (249 primary), 127 Districts / 127 Elections, 3 Parties and 103 verified website Channels. 6 cross-state name-code collisions were minted --new.

## Local integration corrections

Re-minted Terry Nelson as `PERSON-NELSON_TR_3U` with provisional username `nelson_tr_3u`. `PERSON-NELSON_TR_3T` remains with Colorado Travis Star Nelson; no alias links these different people.
