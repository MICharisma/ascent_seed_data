# Idaho 2026 (Ascent Clerk)

Built 2026-10-30 from official Idaho Secretary of State sources only:

| Source | URL |
|---|---|
| Candidate Filing Portal, Search Filed Candidates, "FINAL CANDIDATES LIST", election "November 03, 2026 - 2026 GENERAL" (592 filings; read through the portal's public search, which includes filing status, withdrawal date, write-in flag and SoS voter ID) | https://run.voteidaho.gov/search |
| Same portal, election "May 19, 2026 - 2026 PRIMARY" (2,545 filings), used for primary withdrawals and voter IDs | https://run.voteidaho.gov/search |
| Official primary results (marked official, published 2026-08-24), "Summary and Precinct Results Excel"; statewide/district totals summed from the county summary rows | https://results.voteidaho.gov/results/public/id/elections/may2026 |
| Canvass report (cross-check) | https://archive.voteidaho.gov/results/2026/primary/canvass_report_2026_primary.pdf |

## Model

- **Partisan closed/semi-closed primaries** (May 19): one POSITION-NOMINEE office and `-2026_PRIMARY` race per party contest in the official results (Republican, Democratic, Libertarian). The Constitution Party had no primary contests in the results; its general candidates have general candidacies only.
- **Nominee flag:** Y when the candidate is on the SoS final general list for the same office and party (including those later marked Withdrawn); N otherwise. Every R/D/L general candidate matched a primary entrant.
- **Legislature:** 35 districts as `DISTRICT-USA-ID-LEGISLATIVE-LD_n`, each electing a State Senator (`OFFICE-USA-ID-SENATE-LD_n`, POSITION-STATE_SENATOR) and two State Representatives in separately lettered seats (`OFFICE-USA-ID-HOUSE-LD_n-SEAT_A` / `-SEAT_B`, POSITION-STATE_REPRESENTATIVE), the same pattern as the Washington PR's POS_1/POS_2.
- **Governor:** new office (POSITION-GOVERNOR). Idaho nominates the Governor and the Lt. Governor separately.
- **Ballot lines:** Republican, Democratic, Libertarian, Constitution are parties (new Party records). "Independent" is a designation. The 2 certified write-ins on the general list (Governor) are write-in lines.
- **Same person across contests:** merged only when the SoS voter ID matches (none were needed in this build).
- 303 new people, 514 new candidacies (296 primary, 218 general). 13 existing federal people/candidacies reused unchanged. 4 new Parties, no new Positions.

## Withdrawals (18 rows)

10 before-primary-ballot (withdrawal date on or before the Mar 6 deadline), 7 after-primary, 1 unknown (John H Garrett, whose general-list row has no date; his primary-list row is dated 2026-06-15, after the primary). Dates are from the portal.

## Not included

County offices, magistrate/district judges, Supreme Court seats, community college and highway districts, precinct committeemen, ballot measures.

## Websites

The portal gives no websites; `candidate_accounts/` is untouched.
