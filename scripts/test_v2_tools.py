"""Tests for the v2 workbook, round comparison and report payload."""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "relatorios" / "scripts"))

import assessment_engine as engine  # noqa: E402
import compare_rounds  # noqa: E402

MOCK = ROOT / "respostas.v2.json.example"


class V2ToolsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        self.kit = self.tmp / "kit"
        self.out = self.kit / "saida"
        self.out.mkdir(parents=True)
        shutil.copy(ROOT / "framework.v2.json", self.kit)
        shutil.copy(MOCK, self.kit / "respostas.json")
        self.assertEqual(
            engine.run("all", self.kit / "respostas.json", self.out), 0)
        self.scores = json.loads((self.out / "scores.json").read_text())

    def test_workbook_carries_engine_values(self) -> None:
        import openpyxl

        import fill_workbook_v2
        args = SimpleNamespace(respostas=str(self.kit / "respostas.json"),
                               out=str(self.out))
        self.assertEqual(fill_workbook_v2.run(args), 0)
        path = next(self.out.glob("pontuacao-v2-*.xlsx"))
        wb = openpyxl.load_workbook(path)
        self.assertEqual(
            wb.sheetnames,
            ["README", "Answers", "Questions", "Dimensions", "Overall"])
        dims = wb["Dimensions"]
        self.assertEqual(dims.max_row, 10)
        self.assertTrue(str(dims["D2"].value).startswith("=AVERAGE(")
                        or str(dims["D2"].value).startswith("=IF("))
        engine_d = {d["id"]: d["score"] for d in self.scores["dimensions"]}
        for row in dims.iter_rows(min_row=2, values_only=True):
            self.assertEqual(row[9], engine_d[row[0]])
        self.assertEqual(wb["Overall"]["C2"].value,
                         self.scores["overall"]["score"])

    def test_compare_same_round_has_zero_deltas(self) -> None:
        data = json.loads(MOCK.read_text())
        result = compare_rounds.compare_v2_v2(data, data)
        self.assertEqual(result["overall"]["delta"], 0.0)
        self.assertTrue(all(u["delta"] in (0.0, None)
                            for u in result["units"]))

    def test_compare_v1_to_v2_uses_lineage(self) -> None:
        before = json.loads((ROOT / "respostas.json.example").read_text())
        after = json.loads(MOCK.read_text())
        result = compare_rounds.compare_v1_v2(before, after)
        self.assertIsNone(result["overall"]["delta"])
        self.assertTrue(result["caveats"])
        fw = json.loads((ROOT / "framework.v2.json").read_text())
        with_lineage = sum(1 for d in fw["dimensions"]
                           for q in d["questions"] if q["v1_lineage"])
        self.assertEqual(len(result["questions"]), with_lineage)

    def test_report_payload_uses_engine_outputs(self) -> None:
        import build_report_v2
        payload = build_report_v2.build_payload(self.kit, self.out)
        self.assertEqual(payload["overall"], self.scores["overall"])
        self.assertEqual([g["id"] for g in payload["groups"]],
                         ["G1", "G2", "G3"])
        self.assertEqual(sum(len(g["dimensions"])
                             for g in payload["groups"]), 9)
        cited = {n for b in payload["backlog"] for n in b["basis"]}
        self.assertTrue(cited <= {r["n"] for r in payload["references"]})
        for d in payload["dimensions"]:
            for q in d["lowest"]:
                self.assertTrue(q["l3"])


if __name__ == "__main__":
    unittest.main()
