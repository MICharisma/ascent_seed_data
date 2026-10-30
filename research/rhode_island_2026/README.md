# Rhode Island 2026 seed research

Official source: the RI Secretary of State / Board of Elections candidate report, https://vote.sos.ri.gov/Forms/elections/Reports/Candidates.xlsx (3,202 rows, saved 2026-10-30 through a browser because the site sits behind a Cloudflare challenge). The raw file is not committed because it contains candidates' home addresses, phone numbers, emails and voter IDs. Only the name, party, office, district, declaration and ballot-status columns were read. No contact information is in this PR.

Election names in the file: `09/09/2026 - STATEWIDE PRIMARY` (3,041 rows) and `11/03/2026 - STATEWIDE GENERAL ELECTION` (161 rows).

Scope: U.S. Senate, U.S. House CD 1-2, Governor, Lieutenant Governor, Secretary of State, Attorney General, General Treasurer, State Senate (38 districts) and State House (75 districts). All districts are single-member. Local offices, party committees (town, ward, district committees) and nonpartisan local races are out of scope.

Selection rules:
- Primary candidacies are rows on the 9/9 primary with DECLARATION = Valid and ON P.B (On Primary Ballot) = Yes.
- General candidacies are rows with DECLARATION = Valid and ON E.B (On Election Ballot) = Yes.
- The W.P / W.E (won) columns were not used. No winners, vote totals or incumbency are recorded.

**General election flag:** the report is incomplete for the general. Every primary row still has ON E.B = No, so the Democratic and Republican nominees are not yet marked as on the general ballot. The only rows with ON E.B = Yes are 14 independent / Independent-Socialist candidates who filed directly for the general. These are seeded as general candidacies (petition ballot lines). Party nominees are not added, because doing that would require the forbidden Won-Primary column. The general race descriptions say this.

Modeling:
- Parties: Democrat and Republican (the SoS labels), defined as PARTY-USA-RI-DEMOCRATIC and PARTY-USA-RI-REPUBLICAN.
- Primary nomination offices (nominee_count 1) and races exist for every party primary contest with at least one candidate on the ballot, including unopposed ones. Rhode Island prints unopposed primary candidates.
- There is a new Office, OFFICE-USA-RI-GOVERNOR (POSITION-GOVERNOR), with a new general Race. Lieutenant Governor, Secretary of State, Attorney General, General Treasurer and federal offices and races are referenced from statewide_races_2026.yml and federal_races_2026.yml.
- Federal people are reused from federal_candidates_2026.yml: Reed (listed as John F Reed, federal record "Jack"), McKay, Amo (listed as Gabriel), Keenan, Magaziner and Mellor, plus the existing general candidacies for the independents Bahry (Senate) and DeSouza (CD 1). Burbridge, Munoz and Skoly were minted new.
- TIGER crosswalk: SLDU/SLDL GEOID = 44 + zero-padded district number.

Counts: 196 Candidacies, 190 new Persons, 262 Offices / 262 Races, 113 Districts / 113 Elections, 2 Parties and 0 websites (the report has no website column). 5 cross-state name-code collisions (Thompson, Bennett, Smith, Stewart, Felix) were all minted --new; none involved another RI record.
