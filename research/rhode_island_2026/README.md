# Rhode Island 2026 seed research

Official source: the RI Secretary of State / Board of Elections candidate report, https://vote.sos.ri.gov/Forms/elections/Reports/Candidates.xlsx (3,202 rows, saved 2026-10-30 through a browser because the site sits behind a Cloudflare challenge). The raw file is not committed because it contains candidates' home addresses, phone numbers, emails and voter IDs. Only the name, party, office, district, declaration and ballot-status columns were read. No contact information is in this PR.

Election names in the file: `09/09/2026 - STATEWIDE PRIMARY` (3,041 rows) and `11/03/2026 - STATEWIDE GENERAL ELECTION` (161 rows).

Scope: U.S. Senate, U.S. House CD 1-2, Governor, Lieutenant Governor, Secretary of State, Attorney General, General Treasurer, State Senate (38 districts) and State House (75 districts). All districts are single-member. Local offices, party committees (town, ward, district committees) and nonpartisan local races are out of scope.

Selection rules:
- Primary candidacies are rows on the 9/9 primary with DECLARATION = Valid and ON P.B (On Primary Ballot) = Yes.
- General candidacies are rows with DECLARATION = Valid and ON E.B (On Election Ballot) = Yes.
- The W.P / W.E (won) columns were not used. No winners, vote totals or incumbency are recorded.

Additional official source: the RI Board of Elections certified results for the 9/9/2026 primary, https://elections.ri.gov/sites/g/files/xkgbur756/files/2026-10/Prim26_CSV_ResultsEXPORT.csv (statewide totals, "OFFICIAL RESULTS"), linked from https://elections.ri.gov/elections/results. The summary PDF is https://elections.ri.gov/sites/g/files/xkgbur756/files/2026-09/Prim26_Summary.pdf. The BOE certified the primary after one recount and two re-reads, none of which changed an outcome in scope.

**General election:** the SoS candidate report marks no party nominee as On Election Ballot. So the Democratic and Republican November candidacies (148, one per primary contest) come from the certified primary results: the candidate with the most votes in each contest. Each one was matched to the primary entry in the same contest by surname. All 148 matched exactly. No contest was within 1%, and no write-in led. Independents (14) come from On Election Ballot = Yes. The Won P/E columns were still not used. Substitutions made after the primary (party-committee replacements for vacancies or withdrawals) are not reflected; see conflicts.md.

Modeling:
- Parties: Democrat and Republican (the SoS labels), defined as PARTY-USA-RI-DEMOCRATIC and PARTY-USA-RI-REPUBLICAN.
- Primary nomination offices (nominee_count 1) and races exist for every party primary contest with at least one candidate on the ballot, including unopposed ones. Rhode Island prints unopposed primary candidates.
- There is a new Office, OFFICE-USA-RI-GOVERNOR (POSITION-GOVERNOR), with a new general Race. Lieutenant Governor, Secretary of State, Attorney General, General Treasurer and federal offices and races are referenced from statewide_races_2026.yml and federal_races_2026.yml.
- Federal people are reused from federal_candidates_2026.yml: Reed (listed as John F Reed, federal record "Jack"), McKay, Amo (listed as Gabriel), Keenan, Magaziner and Mellor, plus the existing general candidacies for the independents Bahry (Senate) and DeSouza (CD 1). Burbridge, Munoz and Skoly were minted new.
- TIGER crosswalk: SLDU/SLDL GEOID = 44 + zero-padded district number.

Counts: 338 Candidacies (184 primary, 154 general; the six federal general candidacies are reused), 190 new Persons, 262 Offices / 262 Races, 113 Districts / 113 Elections, 2 Parties and 0 websites (the report has no website column). 5 cross-state name-code collisions (Thompson, Bennett, Smith, Stewart, Felix) were all minted --new; none involved another RI record.
