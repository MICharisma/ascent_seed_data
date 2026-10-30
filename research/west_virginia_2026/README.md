# West Virginia 2026 (Ascent Clerk)

Built 2026-10-29 from official West Virginia Secretary of State sources only:

| Source | URL |
|---|---|
| Candidate Listing, election "11/03/2026 - GENERAL 2026", office type Federal/Statewide/State Race: 244 regular candidates + 8 write-in candidates (read through the page's public listing request, `POST /candidate-web-api/candidates`, no token) | https://candidates.wvsos.gov/ |
| May 12, 2026 primary results, SoS results site (Clarity ENR, election 126209, version 375698, `summary.json`) | https://results.enr.clarityelections.com/WV/126209/ |

## Model

- **Partisan primaries** (May 12): one POSITION-NOMINEE office and `-2026_PRIMARY` race per Republican and Democratic contest in the results. No other party had primary contests; Libertarian, Constitution and Mountain general candidates have general candidacies only.
- **Nominee flag:** Y when the candidate is on the SoS general listing for the same office and party; N otherwise. Where no primary candidate for a party is on the listing, the flag is left blank for that contest (4 contests, see conflicts.md).
- **State Senate:** 17 districts (`DISTRICT-USA-WV-SENATE-SD_n`), two senators each on staggered terms. `OFFICE-USA-WV-SENATE-SD_n` is the regular-term seat on the 2026 ballot. Districts 3 and 17 also elect the other seat for an unexpired term (`OFFICE-USA-WV-SENATE-SD_n-UNEXPIRED_TERM`), with seat_code and notes saying so.
- **House of Delegates:** 100 single-member districts (`DISTRICT-USA-WV-HOUSE-HD_n`, `OFFICE-USA-WV-HOUSE-HD_n`, POSITION-STATE_REPRESENTATIVE, title "Member of the House of Delegates").
- **Ballot lines:** Republican, Democratic, Libertarian, Constitution, Mountain are parties (5 new Party records). Independent and No Party Affiliation are designations. The 8 certified write-ins are write-in lines (with the party the SoS lists, where it lists one).
- Same-person merges only within a contest (primary and general rows of the same race; 6 differ only in nickname quotes). No one appears in two contests.
- 369 new people, 591 candidacies (347 primary + 244 general new; 8 existing federal general candidacies and people reused unchanged). 5 new Parties, no new Positions. No statewide state offices are on the 2026 ballot.

## Not included

Judicial contests (nonpartisan; May 12 Supreme Court/ICA/circuit/family court and the Nov unexpired circuit/family court seats), county offices, party executive committees, park district boards, ballot measures.

## Websites

The SoS listing shows self-reported campaign websites, but none were verified, so `candidate_accounts/` is untouched.

## Local integration corrections

Removed invalid party associations from 3 write-in ballot lines. Source labels and `kind: write_in` are preserved; only party-kind lines may carry a party association.
