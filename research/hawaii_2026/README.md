# Hawaii 2026 (Ascent Clerk)

Built 2026-10-30 from official State of Hawaii Office of Elections sources only:

| Source | URL |
|---|---|
| 2026 Candidate Report (CSV export, 415 rows), with each candidate's status: In Primary, In General, Elected After Primary, Withdrawn, Void, Filed, Issued | https://olvr.hawaii.gov/Controls/CandidateFiling.aspx?elid=94 |
| Aug 8, 2026 primary, final summary report (all precincts counted) | https://elections.hawaii.gov/wp-content/results/2026%20Primary/summary.txt |
| Same, statewide PDF (cross-check) | https://elections.hawaii.gov/wp-content/results/2026%20Primary/histatewide.pdf |

## Model

- **Open partisan primary** (Aug 8): one POSITION-NOMINEE office and `-2026_PRIMARY` race per Democratic, Republican, Libertarian and Green contest in the results. Nonpartisan candidates run in a separate nonpartisan primary and advance under HRS 12-41. Those contests are `-NOMINEE_NONPARTISAN` with the placeholder nominating organization `ORGANIZATION-USA-HI-NONPARTISAN_PRIMARY`, and their ballot line is the designation "Nonpartisan".
- **Nominee flag:** taken from the Candidate Report status, not inferred. Y means "In General" or "Elected After Primary"; N means "In Primary".
- **Elected After Primary:** 29 legislative candidates were elected at the primary. They have a primary candidacy (nominee Y) and no general candidacy. Where no general contest remains for the seat, the seat gets an Office and a primary race but no general Race or district Election.
- **Legislature:** single-member districts. 18 Senate and 48 House districts with a 2026 contest are included (`DISTRICT-USA-HI-SENATE-SD_n`, `-HOUSE-HD_n`).
- **Vacancy contests:** SD18 and SD19 are vacancy elections for the remainder of a term. They use the district's single office, and the race description says it is a vacancy. SD18 has no primary because its candidates filed after the primary.
- **Governor:** new office (POSITION-GOVERNOR). The Lieutenant Governor office and race already existed and are referenced. The two are nominated separately and run as tickets in the general.
- 4 new Parties (Democratic, Republican, Libertarian, Green), one nonpartisan-primary placeholder Organization, no new Positions.
- 186 people and 269 candidacies (189 primary, 80 new general). 6 existing federal people and general candidacies are reused unchanged.

## Not included

OHA trustees, county mayors and councils (nonpartisan special), ballot measures.

## Websites

The Candidate Report lists self-reported websites, but none were verified, so `candidate_accounts/` is untouched.

## Local integration corrections

Added `ORGANIZATION-USA-HI-NONPARTISAN_PRIMARY` as a placeholder Organization with `kind: nonpartisan_primary` and linked all 7 nonpartisan nomination offices to it. This models the nomination process without assigning a political party or changing the source ballot labels.
