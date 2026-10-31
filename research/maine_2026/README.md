# Maine 2026 seed research

Official sources (Maine Secretary of State, Bureau of Corporations, Elections & Commissions):
- General candidate list: https://www.maine.gov/sos/sites/maine.gov.sos/files/inline-files/2026%20General%20Candidate%20List%20-%20FINAL.xlsx (linked from https://www.maine.gov/sos/elections-voting/upcoming-elections)
- Primary candidate list (June 9): https://www.maine.gov/sos/sites/maine.gov.sos/files/inline-files/2026%20Primary%20Candidate%20List%20posting%20FINAL%203.16.26.xlsx (linked from https://www.maine.gov/sos/elections-voting/election-results-data)
- Pre-primary withdrawals (as of 5/22/26): .../2026%20PrePrimary%20Withdrawal%20List%205%2022%202026.pdf
- Post-primary withdrawals and replacements (as of 9/22/26): .../2026%20Post%20Primary%20Withdrawals%20%26%20Replacement%20Candidates%20-%20Updated%209.22.26_0.pdf

Fetch note: the pages return 403 to a bare curl user agent but load with a browser user agent.

Scope: U.S. Senate, U.S. House CD 1-2, Governor, State Senate (35 districts) and State House (151 districts). All districts are single-member. County offices (sheriff, DA, judge of probate, register of deeds, county commissioner/treasurer) and the special county election are out of scope.

Ranked-choice voting: Maine uses RCV in party primaries and in general elections for federal offices. General elections for Governor and the Legislature are plurality. This is noted in each race description.

Modeling:
- Parties: Democratic, Republican and Green Independent (G, used in the primary only). Non-party general candidates appear with the designation the SoS lists (Independent, Unenrolled, Undeclared or Unaffiliated) as `petition` ballot lines.
- Primary nomination offices (nominee_count 1) and races exist for every printed party primary contest, including unopposed ones.
- New Office OFFICE-USA-ME-GOVERNOR (POSITION-GOVERNOR).
- Federal people and candidacies are reused from federal_candidates_2026.yml. Troy D. Jackson (Allagash) ran in the Democratic Governor primary as "Troy Dale Jackson" and is now the replacement Democratic U.S. Senate nominee. Both candidacies use PERSON-JACKSON_TR_4Y.
- Within a contest, a primary entry is merged with the general entry when the first name, last name and town match (the general list's name form is used). This covers e.g. Michael Hobart/Michael H. Cunningham II, Nathan Robert Leigh/Nathan Burnett, John J./John Contreni Jr. and Kelly Maureen/Kelly Noonan Murphy.
- TIGER crosswalk: SLDU/SLDL GEOID = 23 + zero-padded district number.

Counts: 728 Candidacies, 418 Persons, 521 Offices / 521 Races (334 primary), 186 Districts / 186 Elections, 3 Parties and 0 websites (the SoS lists publish none). 24 cross-state name-code collisions were all minted --new.
