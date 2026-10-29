import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import reference_catalog
import seed_contract


class ReferenceCatalogTest(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        manifests = self.root / "manifests"
        manifests.mkdir()
        document = {"format": "micharisma-seeds/v1", "namespace": "MIC", "catalog": "ASC", "records": [
            {"type": "State", "code": "STATE-USA-NY", "attributes": {"name": "New York", "code": "NY"}},
            {"type": "Position", "code": "POSITION-MAYOR", "attributes": {"title": "Mayor"}},
        ], "groups": [{"scope": {"state": "STATE-USA-NY"}, "records": [
            {"type": "County", "code": "COUNTY-USA-NY-ALBANY", "aliases": ["COUNTY-ALBANY"],
             "attributes": {"name": "Albany County", "fips": "36001"}},
            {"type": "County", "code": "COUNTY-EXAMPLE-LEADING_ZERO", "attributes": {"name": "Example County", "fips": "01001"}},
            {"type": "Municipality", "code": "MUNICIPALITY-USA-NY-ALBANY", "attributes": {"name": "Albany"},
             "references": {"county": "COUNTY-ALBANY"}},
            {"type": "Person", "code": "PERSON-VEGA_MS_2A", "attributes": {"first_name": "Marisol", "last_name": "Vega"}},
        ]}, {"records": [
            {"type": "Office", "code": "OFFICE-ALBANY-MAYOR", "references": {
                "position": "POSITION-MAYOR", "jurisdiction": {"code": "MUNICIPALITY-USA-NY-ALBANY"}}},
            {"type": "Election", "code": "ELECTION-ALBANY-2026", "attributes": {"name": "Albany 2026 Election"},
             "references": {"jurisdiction": "MUNICIPALITY-USA-NY-ALBANY", "year": "YEAR-2026"}},
            {"type": "Race", "code": "RACE-ALBANY-MAYOR-2026", "references": {
                "office": "OFFICE-ALBANY-MAYOR", "election": "ELECTION-ALBANY-2026"}},
            {"type": "Candidacy", "code": "CANDIDACY-VEGA-2026", "references": {
                "person": "PERSON-VEGA_MS_2A", "race": "RACE-ALBANY-MAYOR-2026"}},
        ]}]}
        (manifests / "example.json").write_text(json.dumps(document))
        self.index = seed_contract.catalog(manifests)
        self.output = self.root / "catalog"

    def test_exports_scope_relationships_names_aliases_and_sources_without_database(self):
        self.assertEqual(reference_catalog.export(self.index, self.output), 10)
        rows = reference_catalog.lookup(self.output, "Albany", "County", "ny")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["code"], "COUNTY-USA-NY-ALBANY")
        self.assertEqual(rows[0]["fips"], "36001")
        self.assertEqual(rows[0]["aliases"], ["COUNTY-ALBANY"])
        self.assertEqual(rows[0]["references"], {"state": "STATE-USA-NY"})
        self.assertEqual(rows[0]["files"], ["manifests/example.json"])
        self.assertEqual(reference_catalog.lookup(self.output, "COUNTY-ALBANY")[0], rows[0])
        self.assertEqual(reference_catalog.lookup(self.output, "01001")[0]["fips"], "01001")
        campaign = reference_catalog.lookup(self.output, "", "Candidacy", "STATE-USA-NY")[0]
        self.assertIn("Marisol Vega", campaign["name"])
        self.assertIn("Mayor · Albany", campaign["name"])
        self.assertEqual(reference_catalog.lookup(self.output, "", "Position")[0]["states"], [])
        readme = (self.output / "README.md").read_text()
        self.assertIn("(../manifests/example.json)", readme)

    def test_generation_is_deterministic_and_check_rejects_stale_missing_or_extra_files(self):
        reference_catalog.export(self.index, self.output)
        before = {str(path): path.read_bytes() for path in self.output.rglob("*") if path.is_file()}
        reference_catalog.export(self.index, self.output, check=True)
        reference_catalog.export(self.index, self.output)
        self.assertEqual(before, {str(path): path.read_bytes() for path in self.output.rglob("*") if path.is_file()})
        target = self.output / "County/STATE-USA-NY.csv"
        target.write_text("stale")
        with self.assertRaisesRegex(ValueError, "Stale catalog files"):
            reference_catalog.export(self.index, self.output, check=True)
        target.unlink()
        with self.assertRaises(ValueError):
            reference_catalog.export(self.index, self.output, check=True)
        reference_catalog.export(self.index, self.output)
        extra = self.output / "extra.csv"
        extra.write_text("old")
        with self.assertRaises(ValueError):
            reference_catalog.export(self.index, self.output, check=True)
        reference_catalog.export(self.index, self.output)
        self.assertFalse(extra.exists())

    def test_rejects_unknown_filters_and_empty_catalogs(self):
        with self.assertRaisesRegex(ValueError, "empty catalog"):
            reference_catalog.export({}, self.output)
        with self.assertRaisesRegex(ValueError, "missing or empty"):
            reference_catalog.lookup(self.output)
        reference_catalog.export(self.index, self.output)
        self.assertEqual(reference_catalog.lookup(self.output, "No such county"), [])
        for filters in ({"entity_type": "Countyy"}, {"state": "ZZ"}):
            with self.assertRaises(ValueError):
                reference_catalog.lookup(self.output, **filters)

    def test_alias_collisions_and_contradictory_definitions_are_not_hidden(self):
        self.index["STATE-USA-NY"]["aliases"] = ["COUNTY-ALBANY"]
        with self.assertRaisesRegex(ValueError, "Alias COUNTY-ALBANY identifies both"):
            reference_catalog.entries(self.index)
        document = {"format": "micharisma-seeds/v1", "namespace": "MIC", "catalog": "ASC", "records": [
            {"type": "State", "code": "STATE-USA-NY", "attributes": {"name": "Different New York"}}
        ]}
        (self.root / "manifests/conflicting.json").write_text(json.dumps(document))
        with self.assertRaisesRegex(ValueError, "contradictory STATE-USA-NY attribute name"):
            seed_contract.catalog(self.root / "manifests")

    def test_cli_lookup_and_export_use_generated_csvs_and_json_output(self):
        with patch.object(seed_contract, "ROOT", self.root):
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(seed_contract.main(["export-catalog"]), 0)
                self.assertIn("Exported 10", output.getvalue())
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(seed_contract.main(["lookup", "Albany", "--type", "County", "--format", "json"]), 0)
                self.assertEqual(json.loads(output.getvalue())[0]["fips"], "36001")
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(seed_contract.main(["lookup", "Albany", "--type", "County"]), 0)
                self.assertIn("Entity code\tName", output.getvalue())
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(seed_contract.main(["lookup", "Not a place"]), 1)


if __name__ == "__main__":
    unittest.main()
