#!/usr/bin/env python3
"""Tests for framework v2: data file, engine rules and importer.

Run: python3 -m unittest scripts/test_engine_v2.py
"""
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import engine_v2 as v2  # noqa: E402
import validate_framework_v2 as val  # noqa: E402

FW = json.loads((ROOT / "framework.v2.json").read_text("utf-8"))
MOCK = json.loads((ROOT / "respostas.v2.json.example").read_text("utf-8"))
QIDS = [q["id"] for d in FW["dimensions"] for q in d["questions"]]


def person(pid: str, level, role: str = "Architect",
           hands_on: str = "51-80%", scope: str = "One business unit",
           evidence: str = "") -> dict:
    return {"id": pid,
            "profile": {"R-Q1": role, "R-Q2": scope, "R-Q5": hands_on},
            "answers": {q: {"level": level, "evidence": evidence}
                        for q in QIDS}}


def file_with(people: list[dict]) -> dict:
    return {"metadata": {"framework_version": FW["version"]},
            "respondents": people}


class FrameworkDataTest(unittest.TestCase):
    def test_framework_passes_all_checks(self) -> None:
        errors, cons, ret = val.check(FW)
        self.assertEqual(errors, [])
        self.assertEqual((cons, ret), (99, 59))
        self.assertEqual(val.schema_check(FW)[:2] in ("ok", "sk"), True)

    def test_counts(self) -> None:
        self.assertEqual(len(QIDS), 61)
        self.assertEqual(len(FW["profile_questions"]), 5)


class BandTest(unittest.TestCase):
    def test_half_open_bands_have_no_gaps(self) -> None:
        cases = {0.0: "L0", 0.79: "L0", 0.795: "L0", 0.8: "L1",
                 1.599: "L1", 1.6: "L2", 2.4: "L3", 3.19: "L3",
                 3.2: "L4", 4.0: "L4"}
        for score, level in cases.items():
            self.assertEqual(v2.level_code(FW, score), level, score)


class ScoringTest(unittest.TestCase):
    def test_na_and_skipped_are_excluded(self) -> None:
        a = person("a", 4)
        b = person("b", None)
        del b["answers"]["D1-Q1"]
        s = v2.compute_scores(FW, file_with([a, b]), "en")
        self.assertEqual(s["overall"]["score"], 4.0)
        q = next(x for x in s["questions"] if x["id"] == "D1-Q2")
        self.assertEqual((q["n"], q["na"]), (1, 1))

    def test_empty_dimension_is_excluded_and_low_confidence(self) -> None:
        a = person("a", 2)
        for q in QIDS:
            if q.startswith("D6-"):
                a["answers"][q]["level"] = None
        s = v2.compute_scores(FW, file_with([a]), "en")
        d6 = next(d for d in s["dimensions"] if d["id"] == "D6")
        self.assertIsNone(d6["score"])
        self.assertIn("D6", s["flags"]["low_confidence"])
        self.assertEqual(s["overall"]["score"], 2.0)

    def test_dimension_weights(self) -> None:
        a = person("a", 1)
        for q in QIDS:
            if q.startswith("D1-"):
                a["answers"][q]["level"] = 4
        data = file_with([a])
        data["dimension_weights"] = {"D1": 2.0}
        s = v2.compute_scores(FW, data, "en")
        self.assertAlmostEqual(s["overall"]["score"], (8 + 8) / 10, 3)
        data["dimension_weights"] = {"D1": 3.0}
        with self.assertRaises(v2.InputErrorV2):
            v2.compute_scores(FW, data, "en")

    def test_amplification_risk(self) -> None:
        a = person("a", 3)
        for q in QIDS:
            if q.startswith("D8-"):
                a["answers"][q]["level"] = 1
        s = v2.compute_scores(FW, file_with([a]), "en")
        ids = [x["dimension_id"] for x in s["flags"]["amplification_risk"]]
        self.assertEqual(ids, ["D8"])

    def test_perception_gap_needs_minimum_sample(self) -> None:
        execs = [person(f"e{i}", 4, role="Executive (CTO, VP, Director)",
                        hands_on="Less than 20%") for i in range(2)]
        eng = [person(f"h{i}", 1) for i in range(3)]
        s = v2.compute_scores(FW, file_with(execs + eng), "en")
        self.assertEqual(s["flags"]["perception_gap"]["status"],
                         "insufficient_sample")
        execs.append(person("e3", 4, role="Executive (CTO, VP, Director)",
                            hands_on="Less than 20%"))
        s = v2.compute_scores(FW, file_with(execs + eng), "en")
        gap = s["flags"]["perception_gap"]
        self.assertEqual(gap["status"], "evaluated")
        self.assertEqual(len(gap["dimensions"]), 9)

    def test_scope_caveat_and_evidence(self) -> None:
        people = [person(f"p{i}", 3, scope="A single team")
                  for i in range(3)]
        people[0]["answers"]["D1-Q1"]["evidence"] = "link"
        s = v2.compute_scores(FW, file_with(people), "en")
        self.assertTrue(s["flags"]["scope_caveat"]["flagged"])
        self.assertIn("D1-Q1", s["evidence"]["unverified_questions"])
        self.assertEqual(s["evidence"]["with_evidence"], 1)

    def test_single_respondent_responses_shape(self) -> None:
        data = {"metadata": {"framework_version": "2.0.1"},
                "responses": {q: {"level": 2} for q in QIDS}}
        s = v2.compute_scores(FW, data, "pt-br")
        self.assertEqual(s["overall"]["label"], "L2 Adotando")

    def test_invalid_level(self) -> None:
        a = person("a", 5)
        with self.assertRaises(v2.InputErrorV2):
            v2.compute_scores(FW, file_with([a]), "en")


class GapsAndRecommendationsTest(unittest.TestCase):
    def test_priorities_and_references(self) -> None:
        gaps = v2.compute_gaps(FW, MOCK, "en")
        for g in gaps["gaps"]:
            self.assertAlmostEqual(g["priority_score"],
                                   g["weight"] * g["gap_size"], 2)
        recs = v2.compute_recommendations(FW, gaps, MOCK, "en")
        for r in recs["ranked_strategies"]:
            self.assertGreaterEqual(r["cumulative_priority"], 0.9)
            self.assertTrue(r["references"])
            self.assertIn("L3 anchor", r["first_action"])

    def test_target_override(self) -> None:
        data = copy.deepcopy(MOCK)
        data["target_overrides"] = {"D1": 0.5}
        gaps = v2.compute_gaps(FW, data, "en")
        self.assertNotIn("D1", [g["dimension_id"] for g in gaps["gaps"]])


class ImporterRoundTripTest(unittest.TestCase):
    def test_forms_export_round_trip(self) -> None:
        try:
            import openpyxl  # noqa: F401
        except ImportError:
            self.skipTest("openpyxl not installed")
        import import_forms_excel as imp

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "respostas.json"
            args = SimpleNamespace(
                xlsx=str(ROOT / "coleta" / "v2-mock-forms-export.xlsx"),
                respostas=str(out), log_dir=tmp, organization="X",
                lang=None, allow_partial=False)
            self.assertEqual(imp.run(args), 0)
            data = json.loads(out.read_text("utf-8"))
        self.assertEqual(data["metadata"]["framework_version"],
                         FW["version"])
        self.assertEqual(data["respondents"][0]["profile"]["R-Q3"],
                         MOCK["respondents"][0]["profile"]["R-Q3"])
        a = v2.compute_scores(FW, MOCK, "en")
        b = v2.compute_scores(FW, data, "en")
        for key in ("overall", "dimensions", "questions", "flags"):
            self.assertEqual(a[key], b[key], key)


if __name__ == "__main__":
    unittest.main()
