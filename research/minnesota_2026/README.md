# Minnesota 2026 (Ascent Clerk)

Minnesota's Aug 11, 2026 state primary and the Nov 3, 2026 general election, built from the Minnesota Secretary of State election-results media files.

## Sources
- Primary candidates: https://electionresultsfiles.sos.mn.gov/20260811/cand.txt (197 entries; Governor & Lt Governor tickets counted as two).
- General candidates: https://electionresultsfiles.sos.mn.gov/20261103/cand.txt and CandTbl.txt (website column), PartyTbl.txt (party names). The 20261103 vote files hold pre-election test counts; only the candidate lists were used.
- Index: https://electionresults.sos.mn.gov/Select/MediaFiles/Index?ersElectionId=200
- Minn. Stat. 204D.03, 204D.07, 204B.12, 204B.13 (revisor.mn.gov); Legislative Reference Library retirements list (https://www.lrl.mn.gov/legdb/retirements); FEC cn26 (Hassan context only). Ballotpedia used only as a lead.
- The candidate filing site (candidates.sos.mn.gov) sits behind a captcha and was not read.

## Files
- `manifests/contributions/ascent-clerk/mn_2026_foundation.yml` (scope `state: STATE-USA-MN`): 2 parties (Democratic-Farmer-Labor, Republican), 201 districts (67 SD, 134 HD), 201 district general elections.
- `mn_2026_races.yml`: 298 offices and 298 races: new Governor, 2 Supreme Court and 3 Court of Appeals seats, 67 Senate and 134 House offices with general races, and 89 nomination offices (POSITION-NOMINEE) with primary races in ELECTION-USA-MN-2026_PRIMARY.
- `mn_2026_candidates.yml`: 516 people, 606 candidacies (197 primary, 409 general; the 21 US Senate/House general candidacies already in `federal_candidates_2026.yml` are reused).
- `candidate_accounts/mn_2026_sos_websites.yml`: 325 website channels.
- `mn_2026_review.csv` (629 rows), `district_crosswalk.csv` (TIGER sldu 27nnn / sldl 27nnA), `conflicts.md`.
- `statewide_races_2026.yml`: the four existing MN statewide race descriptions now cite the SoS file instead of "Green Papers…pending".

## Modeling
1. **Nominations.** A nomination office and primary race exist for each (contest, major party) that appears in the SoS primary file, including unopposed candidates that file lists. Every primary candidate, winner or loser, has a candidacy. No winner is recorded.
2. **Omitted primaries.** Under Minn. Stat. 204D.03 subd. 3 a lone major-party filer is declared the nominee when filing closes, and the office is left off the primary ballot if all of its candidates were declared. That's why only some legislative districts appear in the primary file. These 320 nominees have a general candidacy only, and the race description and CSV note say so.
3. **Courts.** Supreme Court and Court of Appeals seats are nonpartisan. Under 204D.07 subd. 3 there's no primary unless more than twice as many candidates as seats filed, and none of the seats qualified. Ballot line: `Nonpartisan`, kind `designation`.
4. **Governor / Lt Governor.** Candidates file and appear as joint tickets in both the primary and the general. The ticket is split into separate GOV and LG races and candidacies, and the ticket string is kept in the CSV notes.
5. **Ballot lines.** Labels are the SoS PartyTbl names as printed. DFL and Republican use kind `party` with a party ref. Minor parties (Green, Libertarian, Independent, Forward Independence, United New Independence) use kind `petition`, because they reach the general by nominating petition (204D.07 subd. 2) and don't appear in the primary.
6. **Names.** Quoted nicknames and parentheticals (e.g. "Ahmad R. (Raafat) Hassan", "Marion (O'Neill) Rarick") are dropped from the name fields but kept in the CSV ballot name. Multi-word names were decided from context:
   - Compound surnames: Maye Quade, Johnson Stewart, Oumou Verbeten (official Senate members API `preferred_last_name`), Márquez Simula, Trautmann Cordova, McCabe Ningen (hyphen-free two-part surnames used as the surname in legislative and campaign usage), Van Dover, Van Binsbergen (particle).
   - Double given names: Bobby Joe Champion (Senate API surname "Champion"), Mary Frances Clardy (House directory and email mary.frances.clardy@house.mn.gov).
   - Julie Trang Le: given name Julie, middle name Trang, surname Le (full printed name "Julie Trang Le").
   - Other three-token names (e.g. Ngone Saliou Niang, Lynette Lungay Dumalag) are first / middle / last.
   - Suffixes are not stored because the contract has no field for them.
   - **Ascent will eventually need more flexible name handling** (compound surnames, double given names, name order, suffixes, nicknames). The first/middle/last split here is a best fit.
7. **Person codes.** Full codes come from `seed_contract.mint_person_code` with provisional usernames, using these facts: state MN | 2026-08-11 if the person ran in the primary, else 2026-11-03 | printed name | SoS office title.

## Collisions
Standing rule: a candidate is never linked to a person in another state when both run in the same year. All 11 shared name codes were minted `--new`:
- Ahmad R. (Raafat) Hassan (US Senate DFL primary) gets PERSON-HASSAN_AH_5T, his own MN person. It is not linked to TX PERSON-HASSAN_AH_3N even though FEC records suggest a shared committee, because it is a common name and the two ran in different states in the same year.
- Kurt Michael Anderson (US Senate), Steven E Jacob (SD 20), Cherie Johnson (SD 26), Chris Ford (SD 32), Angela Nelson (SD 35), Keith Allen and Martha Brown (HD 19A), Andy Smith (HD 25B), Jessica L. Johnson (HD 33B), Jess Lewis (HD 43B).
- No one was omitted.

## Withdrawals
- No primary leader differs from the general nominee, so no after-primary withdrawal (204B.13 vacancy) was found.
- Elliott Engen (HD 36A, R): **before-primary-ballot.** The LRL says he filed and later withdrew, he's absent from both SoS files, and 204B.12 allows withdrawal only until 2 days after filing closes.
- Rich Tru (HD 3B, DFL): **unknown.** Only TransparencyUSA (non-official) shows "Withdrew", and the official filing site was unreadable (captcha). He's absent from both SoS files.
- Neither has a record in the manifests, only a CSV row (in_pr N).

## Websites
Each URL comes from the CandTbl website column and was fetched on 2026-10-29. A channel was added only if the site returned 200 and the page contains the candidate's surname. The owner is the general candidacy, and Governor ticket sites go on the Governor candidacy. LG candidates were skipped. Omitted:

| Candidate | Filed URL | Reason |
|---|---|---|
| Tyler Bass | http://bassforcongress.com | HTTP 500 |
| Nathan Wesenberg | wesenbergforsenate.com | no response (TLS/connection error) |
| Colton Kratky | kratky4mn.com | no response (TLS/connection error) |
| Huldah Momanyi-Hiltsley | huldahforhouse.com | 200, name not found on page |
| Natalie Barnes | www.nursenatalieformn.com | no response (TLS/connection error) |
| Tad Jude | tadjude.com | HTTP 202 |
| Marisa Simonetti | marisasimonetti.com | 200, name not found on page |
| Jordan Rasmusson | www.jordanrasmusson.com | HTTP 202 |
| John Howie | howieforsenate.com | HTTP 404 |
| Karen Attia | attiaforsenate.org | HTTP 202 |
| Heather Gustafson | voteheathergustafson.com | HTTP 500 |
| Ngone Saliou Niang | https://niangforsenate.nationbuilder.com | HTTP 500 |
| Mary K Kunesh | marykunesh@gmail.com | 200, name not found on page |
| Brian Stalboerger | www.brianformn.com | HTTP 403 |
| Dustin R. DuFault | www.DuFaultForMN.com | HTTP 202 |
| Juline Birgersson | https://juline4senate.com | HTTP 202 |
| Todd Podgorski | ToddPodgorski.com | no response (TLS/connection error) |
| Zach Duckworth | voteduckworth.com | no response (TLS/connection error) |
| Foung Hawj | www.founghawj.com | no response (TLS/connection error) |
| Leanna Sandahl | sandahlformn.com | no response (TLS/connection error) |
| Natalie Zeleznikar | natalieforhouse.com | HTTP 202 |
| Aaron Schweiger | www.AARONFORMN.com | 200, name not found on page |
| Cal Warwas | www.calwarwas.com | no response (TLS/connection error) |
| Jack L'Heureux | www.jackformnhouse.com | 200, name not found on page |
| Ben Wieman | www.benformnhouse.com | no response (TLS/connection error) |
| Zack Meyman | MEYMANFORMN.COM | no response (TLS/connection error) |
| Marj J Fogelman | marjformnhouse.com | 200, name not found on page |
| Peggy Scott | peggy4house.com | HTTP 500 |
| Nolan West | nolanwest.com | HTTP 202 |
| Jessica L. Johnson | www.JessicaforMNHouse.com | HTTP 202 |
| Ruth Bittner | www.RuthBittnerMN.com | HTTP 202 |
| Kristin Bahner | www.bahnerforhouse.com | HTTP 500 |
| Karl Olson | MNKarlOlson.org | no response (TLS/connection error) |
| Carlie Kotyza-Witthuhn | www.carlieforhouse.com | 200, name not found on page |
| Steven E. Cherney | cherneyformn.com | HTTP 403 |
| Emma Greenman | emmagreenman.com | no response (TLS/connection error) |
| Mary O'Neal | https://onealforhouse66b.com | HTTP 403 |
| Jennifer McPherson | votejennifermcpherson67a.com | 200, name not found on page |
| Seth Kuhl-Stennes | seth4mnsos.org | no response (TLS/connection error) |

## Rails import
- New parties PARTY-USA-MN-DEMOCRATIC_FARMER_LABOR and PARTY-USA-MN-REPUBLICAN; label "Democratic-Farmer-Labor" as printed.
- No cross-state person links. MN Hassan is PERSON-HASSAN_AH_5T.
- Existing federal MN candidacies (PR #7) use kind `unclassified` and were not edited. Their labels match the SoS general file.
- No incumbency, results or winners were recorded, and Tina Smith appears in neither file (open seat).
