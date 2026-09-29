#!/usr/bin/env python3
"""Tests for scripts/import_forms_excel.py (needs openpyxl).

Run: python3 -m unittest scripts/test_import_forms_excel.py
"""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import import_forms_excel as imp  # noqa: E402

try:
    import openpyxl
except ImportError:  # pragma: no cover
    openpyxl = None


def _args(xlsx: Path, out: Path, **extra) -> argparse.Namespace:
    values = {"xlsx": str(xlsx), "respostas": str(out / "responses.json"),
              "log_dir": str(out), "organization": "Contoso",
              "lang": None, "allow_partial": False}
    values.update(extra)
    return argparse.Namespace(**values)


@unittest.skipIf(openpyxl is None, "openpyxl not installed")
class ImportFormsExcelTest(unittest.TestCase):

    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        framework = json.loads((ROOT / "framework.json").read_text("utf-8"))
        self.qids = imp.framework_qids(framework)

    def _workbook(self, rows: list[dict], header_style: str = ":") -> Path:
        wb = openpyxl.Workbook()
        ws = wb.active
        header = ["ID", "Start time", "Completion time", "Email", "Name"]
        for qid in self.qids:
            header += [f"{qid}{header_style} question text",
                       f"Evidence ({qid})"]
        ws.append(header)
        for i, row in enumerate(rows, start=1):
            values = [i, "", "", row.get("email", ""), row.get("name", "")]
            for qid in self.qids:
                values += [row.get(qid), row.get(f"ev:{qid}")]
            ws.append(values)
        path = self.tmp / "forms.xlsx"
        wb.save(path)
        return path

    def _data(self) -> dict:
        return json.loads((self.tmp / "responses.json").read_text("utf-8"))

    def test_mean_without_rounding_and_prefixed_evidence(self) -> None:
        q = self.qids[0]
        path = self._workbook([
            {"name": "Ana", q: "L2 — Defined — x", f"ev:{q}": "doc A"},
            {"name": "Bo", q: "L3 — Managed — y", f"ev:{q}": "doc B"},
        ])
        self.assertEqual(imp.run(_args(path, self.tmp)), 0)
        entry = self._data()["responses"][q]
        self.assertEqual(entry["level"], 2.5)
        self.assertEqual(entry["n_respondents"], 2)
        self.assertEqual(entry["evidence"], "[Ana]: doc A\n[Bo]: doc B")

    def test_na_and_unknown_values_are_null(self) -> None:
        q1, q2 = self.qids[0], self.qids[1]
        path = self._workbook([{"name": "Ana", q1: "NA — I do not know",
                                q2: "maybe"}])
        imp.run(_args(path, self.tmp))
        data = self._data()["responses"]
        self.assertIsNone(data[q1]["level"])
        self.assertIsNone(data[q2]["level"])
        log = next(self.tmp.glob("import-log-*.md")).read_text("utf-8")
        self.assertIn(f"unrecognized value at {q2}", log)

    def test_single_respondent_keeps_plain_evidence(self) -> None:
        q = self.qids[0]
        path = self._workbook([{"name": "Ana", q: "L4 — x",
                                f"ev:{q}": "dashboard"}])
        imp.run(_args(path, self.tmp))
        entry = self._data()["responses"][q]
        self.assertEqual((entry["level"], entry["evidence"]),
                         (4.0, "dashboard"))

    def test_header_variants(self) -> None:
        q = self.qids[0]
        path = self._workbook([{"name": "Ana", q: "L1 — x"}],
                              header_style=" -")
        imp.run(_args(path, self.tmp))
        self.assertEqual(self._data()["responses"][q]["level"], 1.0)

    def test_backup_and_preserved_targets(self) -> None:
        target = self.tmp / "responses.json"
        previous = json.loads(
            (ROOT / "responses.json.example").read_text("utf-8"))
        target.write_text(json.dumps(previous), encoding="utf-8")
        path = self._workbook([{"name": "Ana", self.qids[0]: "L2"}])
        imp.run(_args(path, self.tmp))
        self.assertTrue(list(self.tmp.glob("responses.json.backup-*")))
        data = self._data()
        self.assertEqual(data["target_overrides"],
                         previous["target_overrides"])
        self.assertEqual(data["metadata"]["language"],
                         previous["metadata"]["language"])

    def test_rejects_file_without_question_columns(self) -> None:
        wb = openpyxl.Workbook()
        wb.active.append(["ID", "Name", "Something"])
        path = self.tmp / "other.xlsx"
        wb.save(path)
        with self.assertRaises(imp.FormsImportError):
            imp.run(_args(path, self.tmp))

    def test_template_export_matches_engine_expectations(self) -> None:
        path = ROOT / "collection" / "v1" / "template-export-forms.xlsx"
        self.assertEqual(imp.run(_args(path, self.tmp)), 0)
        data = self._data()
        self.assertEqual(len(data["metadata"]["respondents"]), 3)
        answered = [r for r in data["responses"].values()
                    if r.get("level") is not None]
        self.assertEqual(len(answered), 46)


if __name__ == "__main__":
    unittest.main()
