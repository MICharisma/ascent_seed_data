# New Hampshire 2026 (Ascent Clerk)

Built 2026-10-30 from official New Hampshire Secretary of State files for the Sep 8, 2026 state primary. The files were downloaded through a browser from www.sos.nh.gov, which blocks automated fetches with a 403. Every file is listed by URL in `urls.txt` (110 files) under `https://www.sos.nh.gov/sites/g/files/ehbemt561/files/inline-documents/sonh/`. The results index is https://www.sos.nh.gov/elections/elections/election-results.

Files used:

| Contest | Files |
|---|---|
| Governor and U.S. Senator | `2026-sp-governor-summary-{democratic,republican}.xlsx` and `2026-sp-us-senator-summary-{democratic,republican}.xlsx` (statewide summaries by county) |
| U.S. House | `2026-sp-congressional-district-{1,2}-{democratic,republican}.xlsx` |
| Executive Council | `2026-sp-executive-council-{1..5}-{democratic,republican}.xlsx` |
| State Senate | `2026-sp-state-senate-*-{democratic,republican}.xlsx`, covering districts 1 to 24 |

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
- **Counts:** 96 people and 161 candidacies (102 primary, 59 new general).

## Not included: State House (needs a source)

The State House (multi-member districts; each race should say "vote for N") is out of scope for this PR and needs a source. The browser download folder does contain `2026-sp-house-<county>-{democratic,republican}.xlsx` files (State Representatives primary results by county, with "District No. N (seats)" headers), but they are not used in this PR.

## Websites

None verified, so `candidate_accounts/` is untouched.
