# Municipalities (Ascent Clerk)

Sources (official Census):
- Places and county subdivisions: 2024 Gazetteer files (https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.html).
- Place-to-county: 2020 national place-by-county file (https://www2.census.gov/geo/docs/reference/codes2020/national_place_by_county2020.txt). CT places were matched to their 2024 town (planning-region) instead.
- Population cutoff: Vintage 2024 city/town estimates, July 1, 2024 (https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/cities/totals/sub-est2024.csv).

Rules:
- Included places are incorporated places with FUNCSTAT A or B, plus the 8 consolidated-government "(balance)" places (FUNCSTAT F) and Washington, DC.
- Included county subdivisions are those with FUNCSTAT A (an active government): New England towns, plus towns and townships in the NJ, PA, NY and Midwest states. Coextensive (FUNCSTAT C) and statistical subdivisions are excluded.
- New York City's five boroughs (county subdivisions with FUNCSTAT G) are included in `ny_municipalities.yml` and counted with its towns. Each references `parent_municipality: MUNICIPALITY-USA-NY-NEW_YORK`, so it nests inside the city, and the county it shares its borders with.
- **CDPs are excluded**: they are statistical areas, not governments. This includes Urban Honolulu. Hawaii has no incorporated places, so there is no `hi_municipalities.yml`.
- A county reference is given only when unambiguous. 1Places spanning several counties have no county.
- Codes follow `MUNICIPALITY-USA-{ST}-{NAME}`. On a name collision within a state, the legal type is appended (`_CITY`, `_TOWN`, `_VILLAGE`, `_TOWNSHIP`...), then the county.
- Independent cities (VA, plus Baltimore, St. Louis and Carson City) also exist as County records in PR #1; see ASC-36.
- `cities_over_100k.yml` lists 341 incorporated places with population ≥ 100,000. It reuses the same codes as the state files. 43 active towns and townships are over 100k but are not "cities", so they are not in that file.

Total 35638 records.

| State | Places | Towns/townships | Total |
|---|---|---|---|
| AK | 149 | 0 | 149 |
| AL | 463 | 0 | 463 |
| AR | 500 | 0 | 500 |
| AZ | 91 | 0 | 91 |
| CA | 482 | 0 | 482 |
| CO | 271 | 0 | 271 |
| CT | 30 | 149 | 179 |
| DC | 1 | 0 | 1 |
| DE | 57 | 0 | 57 |
| FL | 411 | 0 | 411 |
| GA | 537 | 0 | 537 |
| IA | 940 | 0 | 940 |
| ID | 198 | 0 | 198 |
| IL | 1294 | 1411 | 2705 |
| IN | 566 | 1005 | 1571 |
| KS | 625 | 1262 | 1887 |
| KY | 418 | 0 | 418 |
| LA | 303 | 0 | 303 |
| MA | 58 | 293 | 351 |
| MD | 157 | 0 | 157 |
| ME | 23 | 459 | 482 |
| MI | 533 | 1240 | 1773 |
| MN | 855 | 1776 | 2631 |
| MO | 938 | 282 | 1220 |
| MS | 299 | 0 | 299 |
| MT | 127 | 0 | 127 |
| NC | 549 | 0 | 549 |
| ND | 355 | 1306 | 1661 |
| NE | 528 | 320 | 848 |
| NH | 13 | 221 | 234 |
| NJ | 323 | 241 | 564 |
| NM | 105 | 0 | 105 |
| NV | 19 | 0 | 19 |
| NY | 595 | 933 | 1528 |
| OH | 923 | 1308 | 2231 |
| OK | 591 | 0 | 591 |
| OR | 240 | 0 | 240 |
| PA | 1013 | 1546 | 2559 |
| RI | 8 | 31 | 39 |
| SC | 271 | 0 | 271 |
| SD | 310 | 899 | 1209 |
| TN | 345 | 0 | 345 |
| TX | 1224 | 0 | 1224 |
| UT | 255 | 0 | 255 |
| VA | 227 | 0 | 227 |
| VT | 39 | 237 | 276 |
| WA | 281 | 0 | 281 |
| WI | 607 | 1243 | 1850 |
| WV | 230 | 0 | 230 |
| WY | 99 | 0 | 99 |
