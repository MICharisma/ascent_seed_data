# South Dakota 2026 seed research

Sources (official, South Dakota Secretary of State, CSV export of the candidate grids):
- General: https://vip.sdsos.gov/candidatelist.aspx?eid=774
- Primary (June 2, 2026): https://vip.sdsos.gov/candidatelist.aspx?eid=773

Scope: federal, statewide, State Senate (35 single-member) and State House (35 districts; 33 elect two members, District 26 and 28 are split into single-member subdistricts 26A/26B/28A/28B). County, municipal, water/conservation district and precinct offices are out of scope.

Counts: 325 Candidacies, 246 Persons, 129 Offices, 129 Races (55 primary nominations), 72 Districts, 72 Elections, 3 Parties (Republican, Democratic, Libertarian; Independent = petition line). No website Channels: the SoS lists publish no web addresses and none were guessed.

Modeling:
- Governor and Lieutenant Governor run on a joint general ticket; the ticket is split into Governor and Lieutenant Governor candidacies. Only Governor has a primary (LG nominated at convention).
- Statewide row offices other than Governor are nominated at party conventions; only general candidacies are recorded.
- New Offices: OFFICE-USA-SD-GOVERNOR (POSITION-GOVERNOR) and OFFICE-USA-SD-PUBLIC_UTILITIES_COMMISSIONER, mapped to existing POSITION-PUBLIC_SERVICE_COMMISSIONER (same role as ND's PSC). No new Position added.
- Primary races exist only where active filers exceeded seats (vote for 2 in two-member House districts). 63 uncontested party/district filings were not printed on the primary ballot and get no primary race.
- Federal records reused: Rounds, Bengs, Jackley, Gronli.
- Name-code collisions with other states: 7, all minted --new.
- TIGER GEOIDs omitted for subdistricts 26A/26B/28A/28B (lettered codes not verified).
