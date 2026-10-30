# Iowa 2026 seed research

Official sources (Iowa Secretary of State, saved through a browser):
- Primary candidate list, June 2, 2026: IA_2026_Primary_Candidate_List.pdf. The header says "This is the final candidate list after the withdrawal and objection period."
- General candidate list, November 3, 2026: IA_2026_General_Candidate_List.pdf. It notes that ballot vacancies after the primary may be filled by convention until August 19.

SoS URLs: primary https://sos.iowa.gov/sites/default/files/2026-04/2026%20Primary%20-%20Candidate%20List%20Database%20-%20All%20Elections.pdf ; general https://sos.iowa.gov/sites/default/files/2026-08/2026%20General%20-%20Candidate%20List%20Database%20-%20All%20Elections.pdf (linked from https://sos.iowa.gov/general-election). They return 403 to curl and were saved through a browser. The raw PDFs are not committed because they include candidate addresses, phone numbers and emails. Only the office, party, ballot name and filing date were read.

Scope: U.S. Senate, U.S. House CD 1-4, Governor, Lieutenant Governor, Secretary of State, Auditor, Treasurer, Secretary of Agriculture, Attorney General, State Senate (the 25 districts up in 2026) and State House (100 districts). All are single-member. Rows showing "--" (no candidate) are skipped.

Modeling:
- Parties: Republican, Democratic and Libertarian (general only, with no primary). "No Party" candidates have petition ballot lines.
- Primary nomination offices and races exist for each party contest with at least one candidate, including unopposed ones. Results are not recorded.
- Lieutenant Governor appears only on the general list; Iowa elects the Lieutenant Governor jointly with the Governor.
- New Office OFFICE-USA-IA-GOVERNOR (POSITION-GOVERNOR). Other statewide and federal offices and races are referenced.
- The 14 federal general candidacies and their people are reused from federal_candidates_2026.yml, matched by contest and surname. Federal primary candidates who did not advance (Wahls, Carlin, Pautsch, Terrell and others) were minted new.
- TIGER crosswalk: SLDU/SLDL GEOID = 19 + zero-padded district number.

Counts: 511 Candidacies (280 primary, 231 general, plus 14 reused federal general candidacies), 290 new Persons, 346 Offices / 346 Races (220 primary), 125 Districts / Elections, 3 Parties and 0 websites. There is no website column. Campaign email domains were not used because they are contact information. 21 cross-state name-code collisions were all minted --new; none were Iowa records.
