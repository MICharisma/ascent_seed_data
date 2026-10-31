# Alaska 2026 seed research

Sources (official, Alaska Division of Elections):
- General candidate list (3 pages): https://www.elections.alaska.gov/candidates/?election=26genr (also &frm-page-407=2 and =3)
- Primary candidate list (Aug 18, 2026): https://www.elections.alaska.gov/candidates/?election=26prim

Note: the site has a certificate problem with plain curl, so pages were fetched with certificate checks disabled. These are the official pages, not a mirror.

Scope: U.S. Senate, U.S. House, Governor/Lieutenant Governor, State Senate (lettered districts on the 2026 ballot) and all 40 State House districts. Judicial retention is out of scope.

Model (top-four primary + ranked-choice general):
- Primary: one nomination office per contest, OFFICE-...-NOMINEE_TOP_FOUR (POSITION-NOMINEE, nominating_organization ORGANIZATION-USA-AK-TOP_FOUR_PRIMARY, nominee_count 4), raced in ELECTION-USA-AK-2026_PRIMARY. All certified primary candidates are included because Alaska prints every certified candidate.
- General: ranked-choice; this is noted in each race description.
- Ballot lines are `designation` lines showing the printed voter-registration designation (e.g. "Registered Republican", "Nonpartisan", "Undeclared"). These are not party nominations, and no Party records are created.
- Governor/Lieutenant Governor tickets are split into a Governor candidacy and a Lieutenant Governor candidacy, in both the primary and the general. New Office: OFFICE-USA-AK-GOVERNOR. The existing Lieutenant Governor office is reused.
- Certified write-ins on the general list (DeWitt/Steere, Parkin/Greer, Sid Hill, Heather McElwain, Lady Donna Dutchess, Angela Darbous, Sarah D. Short) get `write_in` ballot lines.

Counts: 330 Candidacies, 191 Persons, 105 Offices, 105 Races (54 top-four primaries), 50 Districts, 50 Elections, 74 verified website Channels.

Federal records reused: Sullivan (Dan S., PERSON-SULLIVAN_DN_9A), Sullivan (Daniel J. Jr., PERSON-SULLIVAN_DN_8B), Peltola, Heikes, Begich, Hafner, Bill Hill and McDermott. 11 cross-state name-code collisions were all minted --new.
