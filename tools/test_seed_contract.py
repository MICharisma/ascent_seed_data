import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import yaml

import seed_contract as contract


class CandidateAccountsTest(unittest.TestCase):
    def setUp(self):
        self.document = contract.load_document(contract.ROOT / "examples/candidate_accounts.json")
        self.schema = contract.validator("candidate-accounts.schema.json")
        person, campaign = [row["references"]["owner"] for row in self.document["records"]]
        self.index = {
            person: {"code": person, "type": "Person", "attributes": {"first_name": "Avery", "last_name": "Example"},
                     "references": {}, "files": ["people.yml"]},
            campaign: {"code": campaign, "type": "Candidacy", "attributes": {},
                       "references": {"person": person, "race": "RACE-USA-NY-GOVERNOR-2026_GENERAL"}, "files": ["races.yml"]},
        }

    def test_templates_are_equivalent_and_match_both_schemas(self):
        yaml_document = contract.load_document(contract.ROOT / "examples/candidate_accounts.yml")
        self.assertEqual(self.document, yaml_document)
        for name in ("asc.schema.json", "candidate-accounts.schema.json"):
            schema = contract.validator(name)
            schema.validate(self.document)
            schema.validate(yaml_document)
        contract.check_accounts([("example", self.document)], self.index)

    def test_general_example_pairs_are_equivalent_and_match_the_catalog_schema(self):
        schema = contract.validator("asc.schema.json")
        for name in ("minimum_election", "government_branches", "profile_images"):
            with self.subTest(example=name):
                yaml_document = contract.validate_file(contract.ROOT / f"examples/{name}.yml", schema)
                json_document = contract.validate_file(contract.ROOT / f"examples/{name}.json", schema)
                self.assertEqual(yaml_document, json_document)

    def test_county_fips_is_a_string_with_leading_zeros_and_replaces_attribute_code(self):
        document = {"format": "micharisma-seeds/v1", "namespace": "MIC", "catalog": "ASC", "records": [
            {"type": "County", "code": "COUNTY-USA-AL-AUTAUGA", "attributes": {"name": "Autauga County", "fips": "01001"},
             "references": {"state": "STATE-USA-AL"}}
        ]}
        schema = contract.validator("asc.schema.json")
        schema.validate(document)
        attributes = document["records"][0]["attributes"]
        for value in (1001, "1001", "AL001"):
            attributes["fips"] = value
            with self.subTest(value=value):
                self.assertTrue(list(schema.iter_errors(document)))
        attributes.pop("fips")
        attributes["code"] = "01001"
        self.assertTrue(list(schema.iter_errors(document)))

    def test_worker_schema_rejects_incomplete_or_unsupported_records(self):
        for mutation in ("empty", "id", "owner_id", "owner_type", "new_person", "unknown_platform", "missing_source",
                         "missing_owner", "source_date", "source_url", "blank_note", "profile_url", "unofficial",
                         "at_handle", "groups", "alias", "short_owner", "lowercase_code"):
            document = copy.deepcopy(self.document)
            row = document["records"][0]
            if mutation == "empty":
                document["records"] = []
            elif mutation in ("id", "owner_id", "owner_type"):
                row["attributes"][mutation] = 7347
            elif mutation == "new_person":
                row["type"] = "Person"
            elif mutation == "unknown_platform":
                row["attributes"]["platform"] = "mastodon"
            elif mutation == "missing_source":
                del row["source"]
            elif mutation == "missing_owner":
                row["references"] = {}
            elif mutation == "source_date":
                row["source"]["captured_on"] = "2026-02-30"
            elif mutation == "source_url":
                row["source"]["url"] = "javascript:alert(1)"
            elif mutation == "blank_note":
                row["source"]["verification_note"] = "   "
            elif mutation == "profile_url":
                row["attributes"]["url"] = "https://"
            elif mutation == "unofficial":
                row["attributes"]["official"] = False
            elif mutation == "at_handle":
                row["attributes"]["handle"] = "@avery"
            elif mutation == "groups":
                document["groups"] = []
            elif mutation == "alias":
                row["aliases"] = ["CHANNEL-ALIAS"]
            elif mutation == "short_owner":
                row["references"]["owner"] = 7347
            else:
                row["code"] = row["code"].lower()
            with self.subTest(mutation=mutation):
                self.assertTrue(list(self.schema.iter_errors(document)))

    def test_accounts_require_existing_full_owner_codes(self):
        for owner in ("PERSON-EXAMPLE_AV", "PERSON-NOT_IN_CATALOG_7K", "PARTY-USA-NY-EXAMPLE"):
            document = copy.deepcopy(self.document)
            document["records"][0]["references"]["owner"] = owner
            with self.subTest(owner=owner), self.assertRaisesRegex(ValueError, "existing full Person or Candidacy"):
                contract.check_accounts([("example", document)], self.index)

    def test_collisions_and_conflicts_fail_and_identical_replay_passes(self):
        row = self.document["records"][0]
        index = self.index | {row["code"]: copy.deepcopy(row)}
        contract.check_accounts([("example", self.document)], index)
        for mutation in ("other_code", "other_owner", "changed_url", "duplicate_submission"):
            document = copy.deepcopy(self.document)
            if mutation == "other_code":
                document["records"][0]["code"] = "CHANNEL-BSKY-SECOND_CODE"
            elif mutation == "other_owner":
                document["records"][0]["references"]["owner"] = document["records"][1]["references"]["owner"]
            elif mutation == "changed_url":
                document["records"][0]["attributes"]["url"] = "https://example.com/other"
            else:
                document["records"].append(copy.deepcopy(row))
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                contract.check_accounts([("example", document)], index)
        second = copy.deepcopy(row)
        second["code"] = "CHANNEL-BSKY-ANOTHER_CODE"
        with self.assertRaisesRegex(ValueError, "account already uses"):
            contract.check_accounts([("one", self.document), ("two", {"records": [second]})], self.index)

    def test_catalog_finds_nested_owners_and_exports_their_race(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            person, campaign = self.index.values()
            document = {"format": "micharisma-seeds/v1", "namespace": "MIC", "catalog": "ASC",
                        "scope": {"race": campaign["references"]["race"]},
                        "groups": [{"groups": [{"records": [
                            {key: row[key] for key in ("type", "code", "attributes", "references")}
                            for row in (person, campaign)
                        ]}]}]}
            (root / "nested.json").write_text(json.dumps(document))
            index = contract.catalog(root)
            exported = list(contract.owners(index))
            self.assertEqual(len(exported), 2)
            candidacy = next(row for row in exported if row["type"] == "Candidacy")
            self.assertEqual(candidacy["name"], "Avery Example")
            self.assertEqual(candidacy["person"], person["code"])
            self.assertEqual(candidacy["race"], campaign["references"]["race"])
            contract.check_accounts([("example", self.document)], index)

    def test_unsafe_or_ambiguous_documents_fail_before_validation(self):
        cases = [(".yml", text) for text in (
            "catalog: ASC\ncatalog: OTHER\n", "a: &a [1]\nb: *a\n", "a: {<<: {b: 1}}\n",
            "a: !ruby/object:Thing {}\n", "a: !!binary SGVsbG8=\n", "---\na: 1\n---\nb: 2\n",
            "a: .inf\n", "a: <%= 1 %>\n", "1: value\n")]
        cases += [(".json", '{"a":1,"a":2}'), (".json", '{"a":NaN}')]
        with tempfile.TemporaryDirectory() as directory:
            for suffix, text in cases:
                path = Path(directory) / ("bad" + suffix)
                path.write_text(text)
                with self.subTest(text=text), self.assertRaises((ValueError, yaml.YAMLError)):
                    contract.load_document(path)

    def test_catalog_cannot_hide_conflicts_in_already_saved_submissions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            baseline = copy.deepcopy(self.document)
            (root / "existing.json").write_text(json.dumps(baseline))
            for mutation in ("url", "owner", "second_code"):
                incoming = copy.deepcopy(baseline)
                row = incoming["records"][0]
                if mutation == "url":
                    row["attributes"]["url"] = "https://example.com/changed"
                elif mutation == "owner":
                    row["references"]["owner"] = baseline["records"][1]["references"]["owner"]
                else:
                    row["code"] = "CHANNEL-BSKY-SECOND_CODE"
                (root / "submission.json").write_text(json.dumps(incoming))
                with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                    contract.catalog(root)

    def test_cli_validates_both_formats_and_returns_failure_without_writing(self):
        with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            paths = []
            for suffix in (".json", ".yml"):
                path = Path(directory) / ("accounts" + suffix)
                path.write_text(json.dumps(self.document) if suffix == ".json" else yaml.safe_dump(self.document))
                before = path.read_bytes()
                with patch.object(contract, "catalog", return_value=self.index):
                    self.assertEqual(contract.main(["accounts", str(path)]), 0)
                self.assertEqual(path.read_bytes(), before)
                self.assertEqual(contract.main(["validate", str(path)]), 0)
                paths.append(str(path))
            with patch.object(contract, "catalog", return_value=self.index):
                self.assertEqual(contract.main(["accounts", *paths]), 1)
            self.assertEqual(contract.main(["accounts", str(Path(directory) / "missing.yml")]), 1)
            self.assertEqual(contract.main(["validate", str(Path(directory) / "empty")]), 1)
            path.write_text('{}')
            self.assertEqual(contract.main(["accounts", str(path)]), 1)

    def test_general_validation_applies_worker_checks_in_reserved_directory(self):
        with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            folder = Path(directory) / "candidate_accounts"
            folder.mkdir()
            path = folder / "new-york.json"
            path.write_text(json.dumps(self.document))
            with patch.object(contract, "catalog", return_value=self.index):
                self.assertEqual(contract.main(["validate", str(folder)]), 0)
            with patch.object(contract, "catalog", return_value={}):
                self.assertEqual(contract.main(["validate", str(folder)]), 1)
            document = copy.deepcopy(self.document)
            del document["records"][0]["source"]
            path.write_text(json.dumps(document))
            self.assertEqual(contract.main(["validate", str(folder)]), 1)

    def test_person_definitions_require_full_disambiguated_codes_and_reject_duplicates(self):
        schema = contract.validator("asc.schema.json")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bare = {
                "format": "micharisma-seeds/v1", "namespace": "MIC", "catalog": "ASC",
                "records": [{"type": "Person", "code": "PERSON-JAMES_LT", "attributes": {"first_name": "Letitia", "last_name": "James"}}],
            }
            bare_path = root / "bare.json"
            bare_path.write_text(json.dumps(bare))
            with self.assertRaisesRegex(ValueError, "requires a disambiguator; bare name codes are allowed only as references"):
                contract.validate_file(bare_path, schema)
            with self.assertRaisesRegex(ValueError, "requires a disambiguator"):
                contract.catalog(root)

            bad_username = copy.deepcopy(bare)
            bad_username["records"][0] = {
                "type": "Person", "code": "PERSON-JAMES_LT_6J",
                "attributes": {"username": "james_lt_9z", "username_status": "provisional", "first_name": "Letitia", "last_name": "James"},
            }
            bare_path.write_text(json.dumps(bad_username))
            with self.assertRaisesRegex(ValueError, "provisional username 'james_lt_9z' must match 'james_lt_6j'"):
                contract.validate_file(bare_path, schema)

            # A verified username is the person's own choice, so it may differ from the code.
            bad_username["records"][0]["attributes"].update(username="tishjames", username_status="verified")
            bare_path.write_text(json.dumps(bad_username))
            contract.validate_file(bare_path, schema)

            valid = copy.deepcopy(bare)
            valid["records"][0] = {
                "type": "Person", "code": "PERSON-JAMES_LT_6J",
                "attributes": {"username": "james_lt_6j", "first_name": "Letitia", "last_name": "James"},
            }
            first_path = root / "first.json"
            second_path = root / "second.json"
            bare_path.unlink()
            first_path.write_text(json.dumps(valid))
            second_path.write_text(json.dumps(valid))
            with self.assertRaisesRegex(ValueError, "duplicate Person definition PERSON-JAMES_LT_6J"):
                contract.catalog(root)
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(contract.main(["validate", str(first_path), str(second_path)]), 1)

    def test_mint_computes_deterministic_code_and_steps_on_collision(self):
        self.assertEqual(contract.name_code("Kathy Hochul"), "hochul_kt")
        self.assertEqual(contract.name_code("Joe Canino"), "canino_jo")
        self.assertEqual(contract.name_code("James Athans Jr."), "athans_jm")
        result = contract.mint_person_code("NY", "2026-11-03", "Kathy Hochul", "Governor", index={}, taken=set())
        self.assertEqual(result["code"], "PERSON-HOCHUL_KT_9A")
        self.assertEqual(result["username"], "hochul_kt_9a")

        next_slot = contract.mint_person_code("NY", "2026-11-03", "Kathy Hochul", "Governor", index={}, taken={"hochul_kt_9a"})
        self.assertEqual(next_slot["code"], "PERSON-HOCHUL_KT_9B")

    def test_mint_requires_explicit_choice_when_name_code_already_exists(self):
        index = {
            "PERSON-LEVY_MT_2Q": {
                "code": "PERSON-LEVY_MT_2Q", "type": "Person",
                "attributes": {"first_name": "Matt", "last_name": "Levy"},
                "references": {}, "files": ["2026/florida/local.yml"],
            },
            "CANDIDACY-FL-LEVY": {
                "code": "CANDIDACY-FL-LEVY", "type": "Candidacy", "attributes": {},
                "references": {"person": "PERSON-LEVY_MT_2Q", "race": "RACE-USA-FL-PORT-2026_GENERAL"},
                "files": ["2026/florida/local.yml"],
            },
        }
        with self.assertRaisesRegex(ValueError, r"PERSON-LEVY_MT_2Q: Matt Levy \(RACE-USA-FL-PORT-2026_GENERAL\)"):
            contract.mint_person_code("CA", "2026-06-02", "Matthew Chase Levy", "Governor", index=index, taken={"levy_mt_2q"})

        same = contract.mint_person_code(
            "CA", "2026-06-02", "Matthew Chase Levy", "Governor",
            same_as="PERSON-LEVY_MT_2Q", index=index, taken={"levy_mt_2q"}
        )
        self.assertEqual(same["code"], "PERSON-LEVY_MT_2Q")
        self.assertEqual(same["resolution"], "existing")

        minted = contract.mint_person_code(
            "CA", "2026-06-02", "Matthew Chase Levy", "Governor",
            is_new=True, index=index, taken={"levy_mt_2q"}
        )
        self.assertRegex(minted["code"], r"^PERSON-LEVY_MT_[2-9][A-HJ-NP-Z]$")
        self.assertNotEqual(minted["code"], "PERSON-LEVY_MT_2Q")
        self.assertEqual(minted["resolution"], "new")

        stdout = io.StringIO()
        with patch.object(contract, "catalog", return_value=index), patch.object(contract, "taken_usernames", return_value={"levy_mt_2q"}), contextlib.redirect_stdout(stdout):
            self.assertEqual(contract.main([
                "mint", "--state", "CA", "--date", "2026-06-02",
                "--name", "Matthew Chase Levy", "--office", "Governor", "--new"
            ]), 0)
        self.assertEqual(stdout.getvalue().strip(), minted["code"])


if __name__ == "__main__":
    unittest.main()
