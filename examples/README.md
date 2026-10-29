# Choose a seed example

Every example has a `micharisma-seeds/v1` envelope with `namespace: MIC` and `catalog: ASC`. JSON and YAML use the same fields and entity codes. This folder is outside `manifests/` and is not imported during ordinary seeding.

## Minimum election graph

[minimum_election.yml](minimum_election.yml) and [minimum_election.json](minimum_election.json) contain the same ten records. Together they define a country, state, district, legislative position, office, election, race, person, candidacy, and website account. The contest, person, and account are fictional examples within real U.S./New York geography.

The example keeps the graph small and makes its identity and operating state explicit. It has one candidate in one race. Add more Person and Candidacy records for a contested race.

Use these examples in a disposable development or test database. Before using the structure for a reference-data contribution, replace the fictional contest, person, account, codes, and source evidence with sourced records.

| Requested data | Seed representation | Dependency in this example |
|---|---|---|
| Countries | Country with `code` and `name` | None |
| States | State with `code` and `name` | `references.country` |
| Districts | District with `name` and `kind` | `scope.state` supplies the parent jurisdiction |
| Branches of government | `Position.attributes.branch` | `legislative`, `executive`, or `judicial` |
| Offices | Office with `is_active` | Position and a place's jurisdiction |
| Elections | Election with name, date, kind, status, and mock/historical flags | State jurisdiction and existing Year 2026 |
| Races | Race with `status` | Election and Office |
| People | Person with a full disambiguated code and name | Mint new identities as described in [People](../CONTRIBUTING.md#people); only a surname is required by the model |
| Candidates | Candidacy with status and participation | Person and Race |
| Accounts | Channel with platform, handle, URL, and official flag | Person owner; a campaign account can instead reference a Candidacy |

Jurisdiction records are created by the importer for Country, State, and District. Reference the place's code where a jurisdiction is required. The state's election contains the district office because `scope.state` nests the district beneath the state.

Every U.S. state district definition must supply that matching state scope, either on the record or through its document or group. The offline validator rejects missing or mismatched scope before import.

### Year prerequisite

Years are foundation records loaded from the repository's root `years.yml`. `YEAR-2026` references a Year whose `year` is 2026. Year is not an accepted manifest record type, and the importer does not create a missing year from that reference.

Normal reference seeding already loads the year records. For an otherwise empty disposable app database, load those years before importing this example. From the Ascent app checkout:

```sh
bin/rails runner 'require Rails.root.join("db/seeds/data_paths"); require Rails.root.join("db/seeds/year_seeder"); YearSeeder.seed'
```

A nonzero exit means the prerequisite failed. The command loads the existing foundation year data and reports the number of Year records. Do not run it against an unintended environment. The example import tests preload only Year 2026 and create every other record from the manifest.

### Validate and import one format

From this data repository, after the environment setup in [WORKERS.md](../WORKERS.md#set-up-validation):

```sh
.venv/bin/python tools/seed_contract.py validate examples/minimum_election.yml examples/minimum_election.json examples/government_branches.yml examples/government_branches.json
```

A nonzero exit or a nonzero `failed` count means validation failed. The command checks all four example files and their field types. It does not check the database's Year prerequisite or resolve references.

In that same disposable app database, import only the chosen example file from the Ascent checkout:

```sh
bin/rails runner 'report = Seeds::LibraryImporter.new.call([Rails.root.join("db/seeds/ascent_seed_data/examples/minimum_election.yml").to_s]); puts report.transform_values(&:length).to_json'
```

A nonzero exit means the import failed. On an otherwise empty database with its Year prerequisite, the report has 10 created records and zero conflicts. Substitute `minimum_election.json` to use JSON. Importing both versions describes the same identities; they are alternate representations of one dataset, not two elections. See [import behavior](../CONTRIBUTING.md#import-behavior) for conflicts and replay.

## Government branch values

[government_branches.yml](government_branches.yml) and [government_branches.json](government_branches.json) contain three Position records showing every branch value. This pair has no external dependencies. Importing it with the minimum election graph reuses the same State Representative position.

The app stores a branch as an attribute on Position and GoverningBody. It is not a separate Branch entity. In the minimum graph, `Office#branch` inherits its Position's branch because no GoverningBody is assigned. Governance types such as Legislature, Court, and Board are a separate concept; the minimum graph does not need them.

## Add media to existing candidates

- [candidate_accounts.yml](candidate_accounts.yml) and [candidate_accounts.json](candidate_accounts.json) show verified-account submissions. Replace their placeholder owners with exported existing codes before using the stricter account validator.
- [candidate_social_media.yml](candidate_social_media.yml) adds a fictional person, channels, and a post through the general contract.
- [profile_images.yml](profile_images.yml) and [profile_images.json](profile_images.json) show two images and four shared placements. Replace placeholder subject codes with exported existing codes. Uploads and thumbnails belong to Active Storage in the app; seed files carry source links and metadata.

These examples do not generate images, activate OpenAI portrait generation, or supply API credentials. Keep portrait generation disabled pending legal review.
