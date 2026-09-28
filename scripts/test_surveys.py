#!/usr/bin/env python3
"""Tests for the companion surveys next to framework v2.

Run: python3 -m unittest scripts/test_surveys.py
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "survey-devs" / "scripts"))
sys.path.insert(0, str(ROOT / "survey-learning" / "scripts"))

import gerar_insights  # noqa: E402
import gerar_plano_capacitacao as plano  # noqa: E402
import rubric  # noqa: E402

FW = json.loads((ROOT / "framework.v2.json").read_text("utf-8"))
QIDS = {q["id"] for d in FW["dimensions"] for q in d["questions"]}


class SurveyIdTest(unittest.TestCase):
    def test_developer_survey_ids_do_not_collide(self) -> None:
        ids = [d[0] for d in rubric.DIMENSIONS]
        self.assertEqual(ids, [f"DS-D{n}" for n in range(2, 9)])
        self.assertEqual(list(plano.DIMENSION_NAMES), ids)
        self.assertFalse(set(ids) & {d["id"] for d in FW["dimensions"]})

    def test_crosswalk_points_to_v2_questions(self) -> None:
        crosswalk = FW["survey_crosswalk"]
        self.assertEqual(sorted(crosswalk),
                         sorted(d[0] for d in rubric.DIMENSIONS))
        for qids in crosswalk.values():
            self.assertTrue(qids)
            self.assertTrue(set(qids) <= QIDS)
        rows = gerar_insights.crosswalk_rows(
            gerar_insights.STRINGS["en"], ROOT)
        self.assertEqual(len(rows), 7)
        self.assertIn("D4-Q4", rows[4])

    def test_learning_priorities_accept_old_and_new_options(self) -> None:
        people = [
            {"responses": {"L3-Q1": {"value":
                "D8 — Security & Governance (GHAS); D2 — Copilot"}}},
            {"responses": {"L3-Q1": {"value":
                "DS-D8 Security & Governance (GHAS)"}}},
        ]
        counts = plano.collect_priorities(people)
        self.assertEqual(counts["DS-D8"], 2)
        self.assertEqual(counts["DS-D2"], 1)


if __name__ == "__main__":
    unittest.main()
