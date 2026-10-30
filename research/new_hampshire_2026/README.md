# New Hampshire 2026 (Ascent Clerk)

Built 2026-10-30 from official New Hampshire Secretary of State files for the Sep 8, 2026 state primary. The files were downloaded through a browser from www.sos.nh.gov, which blocks automated fetches with a 403. Every file is listed by URL in `urls.txt` (110 files) under `https://www.sos.nh.gov/sites/g/files/ehbemt561/files/inline-documents/sonh/`. The results index is https://www.sos.nh.gov/elections/elections/election-results.

Files used:

| Contest | Files |
|---|---|
| Governor and U.S. Senator | `2026-sp-governor-summary-{democratic,republican}.xlsx` and `2026-sp-us-senator-summary-{democratic,republican}.xlsx` (statewide summaries by county) |
| U.S. House | `2026-sp-congressional-district-{1,2}-{democratic,republican}.xlsx` |
| Executive Council | `2026-sp-executive-council-{1..5}-{democratic,republican}.xlsx` |
| State Senate | `2026-sp-state-senate-*-{democratic,republican}.xlsx`, covering districts 1 to 24 |
| State House | `2026-sp-house-<county>-{democratic,republican}.xlsx` (10 counties x 2 parties) |

Each file's Totals row was checked against the sum of its town rows, and all of them match.

The county files for Governor and U.S. Senator, plus the ballots-cast and names-on-checklist files, were saved but are only used as sources. The county files duplicate the summaries.

## Model

- **Primaries:** one POSITION-NOMINEE office and one `-2026_PRIMARY` race for each Republican and Democratic primary in the results.
  - The results include write-in votes for the other party's candidates (for example "Kelly Ayotte, r" in the Democratic primary). These are not modeled as candidacies.
  - The "Write-Ins" totals are not modeled either.
- **November nominees:** taken from the official primary results. The nominee is the plurality leader among the party's own candidates, but only where that lead is larger than all write-in and cross-party votes combined. That condition held in every contest that had a candidate.
  - Each nominee gets a general candidacy whose note says "Party nominee per the SoS official Sep 8, 2026 primary results".
  - The SoS general-election candidate list could not be fetched (403), so independents and minor-party general candidates are not included. Existing federal ones are left unchanged.
- **SD10, Republican:** no Republican filed. The results show 147 scattered write-ins and 12 write-in votes for Donovan Fenton (D). No Republican nominee is recorded or inferred.
- **New offices:**
  - Governor (POSITION-GOVERNOR).
  - Executive Council EC_1 to EC_5 (existing POSITION-GOVERNORS_COUNCILLOR, district kind "executive council district").
  - State Senate SD_1 to SD_24 (POSITION-STATE_SENATOR).
  - Each has its district and Nov 3, 2026 district election.
- **Other new records:** 2 Parties (Republican and Democratic). No new Positions.
- **Reused unchanged:** the existing U.S. Senate and CD1/CD2 offices and races, and 6 federal general candidacies (Pappas, Sununu, Shaheen, DiLorenzo, Goodlander, Williams). The existing federal candidacies for Laplante (Senate) and Mahrou (CD2) are untouched.
- **State House:** 203 districts, built from the 20 county files `2026-sp-house-<county>-{democratic,republican}.xlsx`.
  - **Codes:** `DISTRICT-USA-NH-HOUSE-<COUNTY>_<n>`, `OFFICE-USA-NH-HOUSE-<COUNTY>_<n>`, seat `<COUNTY>_<n>`.
  - **Seats:** the seat count comes from the SoS header "District No. n (N)". Each office note and general race description says "Vote for: N". 103 districts elect more than one member, up to 10.
  - **Floterial districts:** 39 are marked "F" by the SoS. They overlap underlying districts, so their towns vote in both. The district name has "(floterial)" and the office and race notes say so.
  - **Primaries:** every listed own-party candidate, plus named write-in candidates in that party's primary (ballot line kind write_in), in 375 House party primaries. Votes for the other party's candidates and the "Write-Ins" totals count as write-ins only.
  - **Recounts:** in the 4 districts with SoS recount columns (Hillsborough 33 D, Hillsborough 40 D, Rockingham 16 R, Strafford 6 D), the recount figures are used.
  - **Continuations:** candidate lists that continue onto extra header rows are parsed.
  - **Nominees:** the top N of the party's own candidates, recorded only where the Nth place beats the (N+1)th place plus all write-ins combined. Where a party has fewer than N candidates, all of them must beat the write-ins. The general candidacies say "Party nominee per the SoS official Sep 8, 2026 primary results".
  - **Blank nominees:** 44 House party primaries, listed in conflicts.md: 31 had no candidate of their own and 13 failed the test.
  - **TIGER GEOIDs:** NH SLDL GEOIDs are left blank in the crosswalk. They need a lookup.
- **Counts:** 866 people and 1,594 candidacies. Of these, 770 primary and 662 nominee candidacies are State House. 6 federal general candidacies are reused.

## Websites

None verified, so `candidate_accounts/` is untouched.
