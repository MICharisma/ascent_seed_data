# Kansas 2026 (Ascent Clerk)

Built 2026-10-29 from official Kansas Secretary of State files only:

| File | URL |
|---|---|
| Candidate Lists, election "2026 General" (362 rows) | https://sos.ks.gov/elections/elections_upcoming_candidate.aspx (ASP.NET form, ddlElections=36) |
| Candidate Lists, election "2026 Primary" (378 rows) | same page, ddlElections=35 |
| 2026 Primary Election Official Vote Totals | https://sos.ks.gov/elections/26elec/2026-Primary-Election-Official-Vote-Totals.pdf |

## What is in the PR

- **Statewide:** Governor (new office, POSITION-GOVERNOR) and the existing Lt. Governor, Secretary of State, Attorney General, Treasurer and Commissioner of Insurance races, referenced unchanged.
- **Gov/LG ticket:** Kansas runs the Governor and Lt. Governor as one ticket in both the primary and the general. Each ticket is split into a Governor candidacy and an LG candidacy in matching races, with the running mate noted (as for PA).
- **Federal:** the Senate and CD 1-4 general races and 15 people from `federal_candidates_2026.yml` are reused unchanged. This PR adds the primary nomination races and candidacies.
- **Kansas House:** all 125 districts. **Kansas Senate:** only SD 24 and SD 25 appear on the 2026 lists. The Senate is elected in presidential years, so these are presumably unexpired terms (the SoS doesn't say). **State Board of Education:** districts 1, 3, 5, 7 and 9, mapped to POSITION-SCHOOL_BOARD_MEMBER (as the TX SBOE was).
- **Primaries (Aug 4):** one POSITION-NOMINEE office and race per contest and party (Democratic and Republican only), with official vote totals. The nominee flag comes from the General list.
- **Libertarian and United Kansas** nominate by convention, and independents qualify by petition, so they have general candidacies only.
- **Websites:** 90 `Channel` records in `candidate_accounts/ks_2026_sos_candidate_websites.yml`. They come from the "Web Address" field on the SoS lists and are kept only if the site loaded on 2026-10-29 and showed the candidate's first and last name. 209 URLs were checked and the rest were dropped (no DNS, 403/404/500, or name not found). No social handles.
- **Counts:** 337 new people, 580 new candidacies (337 primary, 243 general), 4 parties, 132 districts. No new Positions.

## Not included

Supreme Court and Court of Appeals retention, district and magistrate judges, and county offices.

## Names

First, middle, last and suffix come from the SoS name fields. Compound surnames are taken from the last-name field, and nicknames in parentheses or quotes are stored as nicknames.

## Same person across contests

Ken Rahjes was Scott Schwab's running mate in the R primary (running-mate ballot city Agra) and is the HD 110 R general nominee (home and ballot city Agra). He's treated as one person, based on that in-state evidence.
