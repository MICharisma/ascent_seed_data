# Wisconsin 2026 seed data

Sources (Wisconsin Elections Commission, official):
- General: "All Contests and Candidates, November 3, 2026" xlsx (state-level rows, Jurisdiction = STATE OF WISCONSIN). The ballot name is used for display.
- Primary: the August 11, 2026 Partisan Primary canvass. The signed canvass statements PDF is a scanned image with no text layer, so the candidate list was read from the WEC canvass summary results report (generated 8/27/2026): https://elections.wi.gov/sites/default/files/documents/August%202026%20Partisan%20Primary_Summary%20Results.pdf
- The candidates-on-ballot PDF and the registered write-in list (as of 10/19) were reviewed. Registered write-ins are not seeded.

Model: the primaries are POSITION-NOMINEE offices raced in ELECTION-USA-WI-2026_PRIMARY (D, R, Wisconsin Green). Independents are petition ballot lines. No vote totals, winners or incumbency are recorded.
Governor/Lt. Governor: separate primary contests; in the general they run as a joint ticket, split into a Governor candidacy and a Lieutenant Governor candidacy (noted on each).
Federal House candidacies are reused from federal_candidates_2026.yml (21 matched). There is no 2026 U.S. Senate race in Wisconsin.
Counts: 549 new candidacies (308 primary, 241 general) + 21 reused federal, 305 people, 361 offices/races, 116 districts, 3 parties.
Websites: none added (none verified in this pass).
No candidate contact information is committed; raw files stay outside the repo.
