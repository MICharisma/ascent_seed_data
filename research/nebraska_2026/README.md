# Nebraska 2026 (Ascent Clerk)

Built 2026-10-29 from official Nebraska Secretary of State files only:

| File | URL |
|---|---|
| Final Statewide General Candidate List, Nov 3, 2026 (dated 9/11/2026) | https://sos.nebraska.gov/sites/default/files/doc/elections/2026/Final_Statewide_General_Candidate_Filing_List_9.11.26.pdf |
| Board of State Canvassers Official Report, Primary Election May 12, 2026 | https://sos.nebraska.gov/sites/default/files/doc/elections/2026/2026_Primary_Canvass_Book.pdf |

## Model

- **Nonpartisan top-two (CA model, PR #11):** the Legislature and State Board of Education primaries are nonpartisan; all voters vote the same contest and the top two advance (Neb. Rev. Stat. 32-811). Each contest gets a `-NOMINEE_TOP_TWO` POSITION-NOMINEE office (nominee_count 1 by default, the contest's Vote For number) nominated by the new `ORGANIZATION-USA-NE-TOP_TWO_PRIMARY` (kind nonpartisan_primary, like ORGANIZATION-USA-CA-TOP_TWO_PRIMARY), and a `-2026_PRIMARY` race. Ballot lines are `Nonpartisan` (designation).
- **Partisan offices** (U.S. Senate, U.S. House, Governor, SoS, Treasurer, AG, Auditor, PSC 2): one party nomination office and primary race per party in the canvass (Republican, Democratic, Libertarian, Legal Marijuana NOW).
- **Nominee flag** = the canvass checkmark (official "advanced"); votes = canvass "Total" row.
- **Governor / Lt. Governor:** Governor is nominated alone; the nominee names the LG afterward. The general ballot prints a joint ticket; split into paired Governor (new office, POSITION-GOVERNOR) and existing LG general candidacies.
- **Legislature:** 25 contests (even districts + LD 41, a 2-year unexpired term). Members mapped to POSITION-STATE_SENATOR (unicameral; members are titled senators).
- **New parties:** Republican, Democratic, Libertarian, Legal Marijuana NOW, Nebraska Working People, America First (all print as parties on the official list). "By Petition" is a petition ballot line (Dan Osborn, Mark Cohen).
- 112 new people, 189 new candidacies (116 primary + 73 general); 17 federal people/candidacies reused unchanged. 1 new Organization, no new Positions.

## Not included

University of Nebraska Board of Regents (no Position exists for a university regent; flagged for a decision), community college, NRD and other local boards, judicial retention.

## Websites

The SoS list gives phone and email, not websites; `candidate_accounts/` is untouched.
