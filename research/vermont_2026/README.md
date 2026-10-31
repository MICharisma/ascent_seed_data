# Vermont 2026 seed research

Sources (official, Vermont Secretary of State; linked from https://sos.vermont.gov/elections/election-info-resources/candidates):
- General qualified candidates (last updated 9/23/2026): https://outside.vermont.gov/dept/sos/Elections_Division/election_info_resources/candidates/2026_general_election_qualified_candidates.xlsx
- Statewide primary qualified candidates (Aug 11, 2026; last updated 8/7/2026): https://outside.vermont.gov/dept/sos/Elections_Division/election_info_resources/candidates/2026_statewide_primary_qualified_candidates.xlsx

Scope: U.S. House, Governor and statewide officers, State Senate (16 districts) and State House (109 districts). Out of scope: justices of the peace, county offices (assistant judge, probate judge, sheriff, state's attorney, high bailiff), registered primary write-ins.

Counts: 629 Candidacies, 353 Persons, 333 Offices, 333 Races (207 primary nominations: Democratic, Progressive, Republican), 125 Districts, 125 Elections, 7 Parties (Democratic, Republican, Progressive, Peace and Justice, Freedom and Unity, Women's Liberation Vegi-Aryan, Green), 23 verified website Channels.

Multi-member districts (seats from the SoS "Vote for Count"): 75 single-seat, 45 two-seat, 5 three-seat districts (Senate and House combined). Primary nominee_count equals the seat count.

Modeling:
- Fusion nominees (REP/DEM, DEM/REP, DEM/PROG, PROG/DEM) carry one party ballot line per listed party, in SoS order.
- Independent/Unaffiliated are petition lines.
- District codes use the SoS district abbreviations (e.g. HOUSE-HD_ADD_RUT, SENATE-SD_CHI_SE). Senate names on the list end in " 1", which was dropped. No TIGER GEOIDs recorded (Vermont's alphanumeric legislative GEOIDs were not verified); see district_crosswalk.csv.
- New Office: OFFICE-USA-VT-GOVERNOR (POSITION-GOVERNOR); no Governor office existed. No new Position.
- Names are title-cased from the all-caps ballot names; the raw ballot name is kept in the review CSV.
- Federal records reused: Malloy, Balint, Altair, Ortiz, Seymour, Walton. 15 cross-state name-code collisions, all minted --new.
- No withdrawals are marked on either list.
