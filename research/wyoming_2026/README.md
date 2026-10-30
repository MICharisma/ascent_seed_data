# Wyoming 2026 seed research

Sources (official, Wyoming Secretary of State):
- General candidates: https://sos.wyo.gov/Elections/Docs/2026/2026_WY_General_Election_Candidates.csv
- Primary candidates: https://sos.wyo.gov/Elections/Docs/2026/2026_WY_Primary_Election_Candidates.csv
- Withdrawn primary candidates: https://sos.wyo.gov/Elections/Docs/2026/2026_WY_Withdrawn_Primary_Election_Candidates.pdf
- (Withdrawn general PDF returned 404 at build time.)

Scope: federal, statewide, State Senate and State House. County/municipal offices and the 21 judicial retention rows are out of scope.

Counts: 322 Candidacies, 208 Persons, 194 Offices, 194 Races, 79 Districts, 79 Elections, 4 Parties (Republican, Democratic, Constitution, Libertarian; Independent is a petition line), 71 verified website Channels.

Notes:
- All Wyoming House districts are single-member (62 HDs); Senate District 6 is a special election in 2026.
- Primaries are modeled as party nominations (POSITION-NOMINEE) only where the official primary list shows them.
- Federal people/candidacies reused from federal_candidates_2026.yml: Hageman, Byrd, Gray, Kinney, Haggit, Johnson.
- 7 name-code collisions, all minted --new (no in-state evidence of identity).
- See conflicts.md for name, withdrawal and website flags; wy_2026_review.csv for per-row review.
