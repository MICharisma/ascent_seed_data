# Utah 2026 general and primary candidacies

Built by Ascent Clerk (overnight worker B) on 2026-10-29 in micharisma-seeds/v1 under the current AGENTS.md / CONTRIBUTING.md / WORKERS.md contract.

## Sources (official first)

- Lieutenant Governor amended 2026 General Election Certification (Sept 21, 2026): https://vote.utah.gov/wp-content/uploads/2026/09/2026-General-Election-Certification-Amended-09-21.pdf
- 2026 Write-In Candidate Certification: https://vote.utah.gov/wp-content/uploads/2026/09/2026-Write-In-Certification.pdf
- 2026 Official Primary Election Certification (Apr 29, 2026; candidates on the June 23 primary ballot): https://vote.utah.gov/wp-content/uploads/2026/04/2026-Official-Primary-Election-Certification.pdf
- June 23 primary statewide canvass (multi-county contests only), used as a cross-check: https://vote.utah.gov/wp-content/uploads/2026/07/2026-Primary-Election-Certification.pdf
- Existing repo records reused: federal_candidates_2026.yml, elections_2026.yml, federal_races_2026.yml.

## Scope

- In: 4 US House seats, the 15 Utah Senate seats up in 2026, all 75 Utah House seats, certified write-ins, and the June 23 Democratic and Republican primaries for those offices. No US Senate or statewide executive offices are elected in 2026.
- Deferred: State Board of Education (partisan; no shared Position yet) (8); judicial retention questions and constitutional amendments.

## Counts

- General contests: 94; party primary races: 25
- General candidate entries: 212; primary candidate entries: 54
- Records: 247 Candidacy, 90 District, 90 Election, 115 Office, 2 Party, 222 Person, 115 Race
- General candidates reused unchanged from existing repo files: 19
- New people whose name code was already used elsewhere (minted with --new; no cross-state or same-person link): 9

## Modeling

- Every Person definition has a full code from `tools/seed_contract.py mint` and a matching provisional username. All three manifests carry document-level `scope: state: STATE-USA-UT`, so districts nest under the state.
- Primaries are nominations: each party+contest on the official primary list gets a POSITION-NOMINEE office (nominee_for the general office, nominating_organization the party) and a race in ELECTION-USA-UT-2026_PRIMARY. Contests/parties absent from the official primary list get no primary.
- Party labels are as printed by the official source. No winner, incumbency or vote total is recorded.
- Both certifications are scanned documents. General names come from the PDF text layer; every name was checked against an independent OCR pass (rapidocr), and 6 OCR errors were corrected (e.g. "KARL! BLACK" to Karli Black, "CHRJS REID" to Chris Reid). The primary certification has no text layer: it was transcribed from OCR, with run-together names (e.g. "ANDREW UZ") re-read at 400 dpi.
- General nominees are taken only from the general certification; nothing is inferred from vote counts.
- Ballot names are in capitals on the certification; display names are title-cased, and Mc-prefixed surnames are capitalized as Mc+Name. Name parts are split by position (first token = first name, last token = surname) and need review for compound surnames.
- Forward, Constitution, Libertarian, Independent American and Green are registered Utah parties but have no Party record in the repo, so their ballot lines are kind unclassified. Unaffiliated candidates are kind designation, and write-ins are kind write_in.
- Withdrawals: Utah publishes no separate withdrawal list. The general certification was amended on Sept 21, but the original was not compared. No withdrawals are recorded; the withdrawal status of primary losers not on the general list is unknown.

## Flags for review

- Re-check the amended certification against the original (pre-amendment) one for replacements or withdrawals.
- Party primaries with no same-party nominee on the general list: 0; general nominees with no matching primary candidacy: 0; names in more than one contest: 0; existing repo candidacies not matched: 0. Details in conflicts.md.

## Files

- `ut_2026_review.csv`: one row per candidate entry with person code, mint facts/resolution, candidacy code, withdrawal class and source.
- `district_crosswalk.csv`: legislative district codes to TIGER 2024 GEOIDs.
- `conflicts.md`: automatic and manual flags.
