# Arizona 2026: conflicts and judgment calls

1. **Party name: No Labels / Arizona Independent Party.** The 3/30 filing list and the primary write-in list use "Arizona Independent Party" (and "No Labels" for write-in John Skirbst, HD3). The canvass prints "NOL". The existing PR #7 federal candidacies (Aversa CD3, Benoit CD4) carry the label "No Labels Party". The party record is `PARTY-USA-AZ-ARIZONA_INDEPENDENT` ("Arizona Independent Party"), with labels kept as printed per source. The federal labels were not edited.
2. **Federal labels.** The PR #7 AZ House candidacies use "Democrat" with kind `unclassified`; the SoS uses "Democratic". They were left unchanged (existing records); a Rails-side normalization is suggested.
3. **Write-in name splits (no filing):**
   - "Robert "Robbie" Hernandez McDonald Jr." was read as a compound surname, Hernandez McDonald.
   - "G. Seville Hatch" was split as first G., middle Seville.
   - "William "Rex" Josué Pounds IV", "Royce "Rj" Mark Jenkins", "Gage Dylan Thunder", "Athena Maria Eastwood", "Jon Robert Ralston" and "Nicholas N Glenn" were split as first / middle / last.
4. **"Gertritrude Gonzalez"** (GOV general write-in, REP) is kept exactly as printed. It may be a misspelling of Gertrude.
5. **Gerard Davis** was a Green primary write-in for SD24 and is a GRN general write-in for Superintendent. He is likely the same person, but nothing in the sources links the two, so two persons were minted. Merge if confirmed.
6. **David Redkey** filed by petition as the Green candidate for CD1, is absent from the CD1 canvass, and is the certified Green write-in nominee in CD3. He is linked to the existing PERSON-REDKEY_DV_3B (PR #7, CD3 Green).
7. **The canvass was transcribed by eye** from a scanned image because no OCR was available. A spot re-check against a text copy or Election/69 is recommended.
8. **18 filers are missing from the canvass** while the withdrawn list says "none". They are classified `before-primary-ballot` on the strength of the canvass and the "pending court-ordered removal" caveat; the cause is unknown.
