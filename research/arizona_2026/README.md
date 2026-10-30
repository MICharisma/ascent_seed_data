# Arizona 2026 (Ascent Clerk)

Built offline from four official Arizona Secretary of State files, saved by hand because azsos.gov, apps.azsos.gov, apps.arizona.vote and results.arizona.vote all return Cloudflare 403 to scripted fetches. Index: https://azsos.gov/elections/election-information/2026-election-info

| File | Use |
|---|---|
| 2026 Candidate Nominations and Petitions Filed (3/30/2026; "Official list of candidates who qualified for the July 21, 2026, Primary Ballot pending any court-ordered removal ARS § 16-351") | name split (filed as "Last, First"), party labels |
| 2026 Primary Write-In and Withdrawn Candidate List (rev. 6/2/2026) | primary write-in labels; withdrawn: "none" |
| 2026 General Write-In and Withdrawn Candidate List (rev. 9/9/2026) | 15 general write-ins; withdrawn: "none" |
| Official Canvass, 2026 Primary Election (issued 8/6/2026) | every primary candidate and the nominees (*) |

The canvass PDF is a scanned image with no text layer, and no OCR tool was available on the build box. Its 269 candidate lines were transcribed by eye from rotated crops. Every non-write-in name matches the filing list token for token. Vote totals were not transcribed or recorded.

## What is modeled

- **Parties (5):** Republican, Democratic, Libertarian, Green, and Arizona Independent Party. The last is printed as "NOL"/"No Labels" in the canvass; see conflicts.md.
- **Districts:** 30 legislative districts, `DISTRICT-USA-AZ-LEGISLATIVE-LD_n`, with one general election each. Each LD elects 1 senator and 2 representatives (Ariz. Const. art. IV pt. 2 §1), so one district serves both chambers. Crosswalk: `district_crosswalk.csv` (TIGER sldu 04001–04030).
- **New offices and general races:** Governor, Corporation Commissioner, State Senate LD 1–30 and State House LD 1–30.
- **Multi-seat contests:** Arizona House (2 seats per LD) and Corporation Commission (2 seats in 2026) are each one office whose race description says "Vote for: 2". Their party nomination offices use `nominee_count: 2`. The contract has no seat-count field on Race/Office, so this lives in descriptions and office notes (Rails item).
- **Existing records reused:** US House CD 1–9, SoS, AG, Treasurer, Superintendent of Public Instruction, Mine Inspector and Lieutenant Governor offices and races. The six statewide race descriptions were updated from "Green Papers…pending" to the official sources.
- **Primary races:** one nomination office and one primary race per contest and party on the canvass, in `ELECTION-USA-AZ-2026_PRIMARY` (July 21). Every canvass candidate gets a candidacy, losers and write-ins included (write-ins use ballot line kind `write_in`).
- **General candidacies:**
  - Canvass nominees (*) for every contest, including 9 write-in nominees: Redkey CD3, Swing CD6, Loughrige SD8, Karp SD19, Carver HD2, Skirbst HD3, Trachsel HD6, Grayson HD7, Cease CC.
  - The 15 certified general write-ins.
  - The 24 US House nominees are the existing `federal_candidates_2026.yml` candidacies (all 24 match the canvass). Those persons are reused for their CD primary candidacies.
- **Not recorded:** incumbency and vote totals. Winners appear only as nominee status taken from the official canvass asterisk.

## Counts

- 5 parties, 30 districts, 30 elections.
- 225 offices: 62 general (Gov, CC, 30 SD, 30 HD) plus 163 nomination offices. 225 races.
- 260 new persons and 461 candidacies:
  - 269 primary candidacies.
  - 192 new general candidacies (216 general entries, 24 of them existing federal).
- Canvass entries by contest: HD 132, SD 66, CD 37, Gov 11, CC 6, SoS 5, SPI 4, AG 3, Treasurer 3, Mine Inspector 2.

## General ballot additions (Election/69)

The official general listing at https://apps.arizona.vote/electioninfo/Election/69 was saved by a browser as PDF and text (federal, state, legislative and judicial tabs). All additions are in `az_2026_general_ballot.yml`.

- **Reconciliation:** every general candidacy already in the PR, and every existing federal one, appears on the listing in the same contest. Every listed candidate already had a general candidacy, with five exceptions:
  - the 4 Lieutenant Governor running mates;
  - Nick Fierro (SD10).
  
  The 15 listing entries marked "Write-In Candidate" are the same 15 people as the 9/9 write-in list, and are already modeled.
- **Lieutenant Governor running mates (4),** in the existing LG general race, which is a joint ticket per the listing:

  | Running mate | Ballot line | Governor nominee |
  | --- | --- | --- |
  | Sine Kerr | Republican | Andy Biggs |
  | John Giles | label "PND", kind `unclassified`, no party | Katie Hobbs |
  | Lisa Castillo | Green | Risa Lombardo |
  | Angela Harrolle Mohan | label "PND", kind `unclassified`, no party | Teri Ann Hourihan |

  The listing does not expand "PND", and no party was inferred. The LG race description now cites the listing.
- **Independents and minor parties:** Nick Fierro, SD10, is printed "(INDEPENDENT)", so he gets an `Independent` line of kind `petition`. No other non-write-in independent or minor-party candidate was missing. The Libertarian, Green and NOL nominees were already in the PR or the federal file.
- **Judicial retention (15),** following the existing Florida retention pattern (`manifests/2026/florida/judicial.yml`). Each retained judge gets an office named `...-RETENTION_OF_<NAME>` with a `seat_code`, a race in the general, and a candidacy with no ballot line.
  - **Supreme Court (statewide, `POSITION-JUSTICE`):** John Lopez IV.
  - **Court of Appeals Division I** (new `DISTRICT-USA-AZ-APPEAL-DIV_1` and its general election; `POSITION-APPELLATE_JUDGE`): Andrew Jacobs, Anni Hill Foster, Daniel Kiley, David Weinzweig, James Morse Jr., Jennifer Perkins, Michael Catlett and Randall Howe.
  - **Court of Appeals Division II** (`DISTRICT-USA-AZ-APPEAL-DIV_2`): Jeffrey Sklar, Michael Kelly, Sean Brearcliffe, Christopher O'Neil, Karl Eppich and Lacey Stover Gard.
- **Not covered:** Superior Court retention. The judicial tab lists only the appellate courts. County-level retention lists were not captured.

### Flags (need review)
- **Court of Appeals electorate:** Arizona retains Court of Appeals judges by county-based districts within each division. The listing gives only the division, so each race is attached to the whole division. A finer district needs a source.
- **Compound names:** for "Anni Hill Foster" and "Lacey Stover Gard", the source gives no surname split, so Hill and Stover are stored as middle names. Suffixes IV and Jr. are dropped from the name parts (they are kept in the office slug, as in Florida).
- **"PND" label** for Giles and Harrolle Mohan is shown as printed.
- **Shared name code:** John Lopez IV shares a name code with Johanna Lopez (FL), so he was minted `--new` with no link.
- **Counts added:**

  | Record | Count |
  | --- | --- |
  | Districts | 2 |
  | Elections | 2 |
  | Offices | 15 |
  | Races | 15 |
  | Persons | 20 |
  | Candidacies | 20 |

## Withdrawals and removals (in az_2026_review.csv, `in_pr = N`)

Both official withdrawn lists read "none". Eighteen filers on the 3/30 list are absent from the canvass:

- **`before-primary-ballot` (17):** they were never on the July 21 ballot; the reason (court challenge under ARS 16-351 or withdrawal) is not in the files.
  - CD1: Ajluni (AIP), Weintraub (D), Gordon (D), Redkey (Green; he ran instead as the CD3 Green write-in)
  - CD2 Descheenie (D), CD4 Davison (R), CD5 Bracht (D), CD6 Bah (AIP), CD8 Martines (AIP)
  - Treasurer Zepeda (AIP), SPI Butts (D), CC Marshall Sr. (R)
  - SD19 Slawson (D), HD2 Skranak (R) and DeSanti (R), HD23 Holmes (R), HD25 Lara (D)
- **Fierro (SD10, Independent)**, formerly `unknown`: he is on the general listing, so he was not withdrawn. He now has a general candidacy.
- **9/9 general list:** the withdrawn section reads "none". No general withdrawals are classified, and no modeled general candidate is missing from the Election/69 listing.

## Names and persons

- Surnames come from the filing's "Last, First" form, e.g. Stahl Hamilton, Garcia Snyder, De Los Santos. "Julia Romero Gusse", "Teresa Leyba Ruiz" and "Jackie O'Donnell Anderson" are filed with a single surname, so the second word is a middle name.
- Write-ins have no filing; their names were split from context (see conflicts.md). Quoted nicknames are not stored; suffixes are dropped (the contract has no field for them).
- Name-code collisions with other states (Marsh, Walsh, Maloney, Cook, Martin, Rose, Carter, Collier, Hill) were all minted `--new`; there are no cross-state links.
- Within Arizona, Flores (Alex CD2 / Alberto HD24) and Gerard Davis (SD24 primary write-in / SPI general write-in) were also kept as separate persons.
- **More flexible name handling is still needed** for nicknames, suffixes and compound names.

## Other notes

- No candidate_accounts file: the source files carry no websites.
- CI ("Validate seed contributions") is disabled on the repo (`disabled_manually`) and was not enabled. Checks were run locally: unittest, `validate manifests examples`, `accounts …/candidate_accounts`, `export-catalog` and `export-catalog --check` all pass.
