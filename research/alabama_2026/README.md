# Alabama 2026 general and primary candidacies

Built by Ascent Clerk (overnight worker B) on 2026-10-29 in micharisma-seeds/v1 under the current AGENTS.md / CONTRIBUTING.md / WORKERS.md contract.

## Sources (official first)

- Secretary of State certification of Republican general candidates (Aug 26, 2026; scanned): https://www.sos.alabama.gov/sites/default/files/election-2026/2026GeneralElectionStateCertificationofRepublicanCandidates.pdf
- ALGOP amended certification of nominees (Sept 2, 2026; adds Will Barfoot SD 25), accepted by the SOS: https://www.sos.alabama.gov/sites/default/files/election-2026/ALGOPAmendedCertification-SD25.pdf
- Secretary of State certification of Democratic general candidates incl. the ADP amended certification of Aug 24 (scanned, rotated tables): https://www.sos.alabama.gov/sites/default/files/election-2026/2026GeneralElectionStateCertificationofDemocraticCandidates.pdf
- Independent candidates (SOS, Aug 26): https://www.sos.alabama.gov/sites/default/files/election-2026/2026GeneralElection-StateCertificationofIndependentCandidate.pdf
- Party primary results workbooks posted by the SOS: https://www.sos.alabama.gov/sites/default/files/05-29-2026/GOP%20Results.xlsx ; https://www.sos.alabama.gov/sites/default/files/election-2026/2026%20Democratic%20Primary%20Election%20Results.xlsx
- Aug 11 special congressional primary qualifiers: https://www.sos.alabama.gov/sites/default/files/election-2026/StateCertificationofRepublicanCandidatesCongressionalDistricts.pdf ; https://www.sos.alabama.gov/sites/default/files/election-2026/StateCertificationofDemocraticCandidatesCongressionalDistricts.pdf; calendar https://www.sos.alabama.gov/sites/default/files/election-2026/Amended2026SpecialPrimaryElectionCalendar_05.27.2026.pdf
- SD 25/26 special primary qualifiers: https://www.sos.alabama.gov/sites/default/files/election-2026/StateCertificationofRepublicanCandidates-SD25and26.pdf ; https://www.sos.alabama.gov/sites/default/files/election-2026/StateCertificationofDemocraticCandidates-SD25and26.pdf
- Existing repo records reused: federal_candidates_2026.yml, statewide_races_2026.yml, federal_races_2026.yml, elections_2026.yml.

## Scope

- In: US Senate, 7 US House seats, Governor, Lt. Governor, Attorney General, Secretary of State, Treasurer, Auditor, Agriculture Commissioner, PSC Places 1 and 2, all 35 Senate and 105 House seats (where a party or independent is certified), and the party primaries.
- Deferred: judicial offices, State Board of Education, and party executive committee seats (other: 9, Associate Justice of the Alabama Supreme Court: 2, Alabama Court of Civil Appeals: 2, Alabama Court of Criminal Appeals: 2, State Board of Education District 2: 1, State Board of Education District 6: 1, State Board of Education District 8: 1, Circuit Judge: 13, District Judge: 27, R primary: Member, State Board of Education: 1, R primary: Member State Board of Education: 1, D primary: District Court Judge: 7).

## Counts

- General contests: 157; party primary races: 67
- General candidate entries: 227; primary candidate entries: 181
- Records: 392 Candidacy, 140 District, 140 Election, 210 Office, 2 Party, 325 Person, 210 Race
- General candidates reused unchanged from existing repo files: 16
- New people whose name code was already used elsewhere (minted with --new; no cross-state or same-person link): 17

## Modeling

- Every Person definition has a full code from `tools/seed_contract.py mint` and a matching provisional username. All three manifests carry document-level `scope: state: STATE-USA-AL`, so districts nest under the state.
- Primaries are nominations: each party+contest on the official primary list gets a POSITION-NOMINEE office (nominee_for the general office, nominating_organization the party) and a race in ELECTION-USA-AL-2026_PRIMARY. Contests/parties absent from the official primary list get no primary.
- Party labels are as printed by the official source. No winner, incumbency or vote total is recorded.
- Most certifications are scanned images. They were OCR-ed (rapidocr); the Democratic list is a rotated table whose district column OCR dropped, so it was rotated and every row read by hand against the page image. The ALGOP Sept 2 amendment has a text layer; its OCR digit errors (S/5, O/0, J/3) were corrected and the list was cross-checked against the Aug 26 SOS OCR.
- Primary candidate lists come from the official results workbooks (candidate names only; no outcome is inferred from votes). Nominees come only from party certifications to the SOS.
- Court-ordered remedial congressional map: CD 1, 2, 6 and 7 held a special primary on Aug 11, 2026; that ballot replaces the May contests for those districts and is modeled as the primary. SD 25 and 26 were also re-run in an Aug 11 special primary; each party had one qualifier, so no primary race is built.
- Independents are kind designation. Withdrawals: the ADP amended certification says it reflects "candidate withdrawals" but does not name them; none can be classified, so none are recorded (status unknown).

## Flags for review

- Flags: R ('SD', 25) Will Barfoot: not on the Aug 26 SOS general certification (added by the Sept 2 ALGOP amendment, accepted without ballot reprint under Ala. Code 17-6-21(b)); R ('HD', 51) Allen Treadaway: not on the Aug 26 SOS general certification (added by the Sept 2 ALGOP amendment, accepted without ballot reprint under Ala. Code 17-6-21(b)); D May primary SD 25 entry Phadra Carson Foster: superseded by the court-ordered Aug 11 special primary for SD 25/26 (not modeled); D May primary SD 25 entry Kirk Hatcher: superseded by the court-ordered Aug 11 special primary for SD 25/26 (not modeled); D May primary SD 25 entry KK Middleton: superseded by the court-ordered Aug 11 special primary for SD 25/26 (not modeled); May 19 Republican CD 1 and CD 6 contests were superseded by the court-ordered Aug 11 special primary for CD 1, 2, 6 and 7; only the Aug 11 candidates are modeled; name variant ('GOV', 0) Republican: primary 'Thomas Tuberville' vs certified nominee 'Tommy Tuberville' (treated as same person); name variant ('AGRI', 0) Republican: primary 'Cory Hill' vs certified nominee 'Corey Hill' (treated as same person); name variant ('HD', 13) Republican: primary 'Mike Elliot' vs certified nominee 'Mike Elliott' (treated as same person)
- Party primaries with no same-party nominee on the general list: 0; general nominees with no matching primary candidacy: 0; names in more than one contest: 0; existing repo candidacies not matched: 0. Details in conflicts.md.

## Files

- `al_2026_review.csv`: one row per candidate entry with person code, mint facts/resolution, candidacy code, withdrawal class and source.
- `district_crosswalk.csv`: legislative district codes to TIGER 2024 GEOIDs.
- `conflicts.md`: automatic and manual flags.
