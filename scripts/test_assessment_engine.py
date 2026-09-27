#!/usr/bin/env python3
"""Golden and edge-case tests for scripts/assessment_engine.py.

Run: python3 -m unittest scripts/test_assessment_engine.py
"""
from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import assessment_engine as eng  # noqa: E402

EXAMPLE = ROOT / "referencia" / "exemplo-saida"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class GoldenExampleTest(unittest.TestCase):
    """The engine must reproduce the published example outputs."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.framework = load(ROOT / "framework.json")
        cls.respostas = load(ROOT / "respostas.json.example")
        cls.scores = eng.compute_scores(cls.framework, cls.respostas)
        precise = eng.compute_scores(
            cls.framework, cls.respostas, precise=True)
        cls.gaps = eng.compute_gaps(precise, cls.respostas)
        cls.recs = eng.compute_recommendations(
            cls.gaps, cls.framework, cls.respostas)

    def test_overall_and_threshold(self) -> None:
        expected = load(EXAMPLE / "scores.json")
        self.assertEqual(self.scores["overall"], expected["overall"])
        self.assertEqual(self.scores["threshold"], expected["threshold"])

    def test_pillars_and_capabilities(self) -> None:
        expected = load(EXAMPLE / "scores.json")
        keys = ("id", "score", "label", "answered", "applicable")
        for got, exp in zip(self.scores["pillars"], expected["pillars"]):
            self.assertEqual({k: got[k] for k in keys},
                             {k: exp[k] for k in keys})
        keys += ("weight", "pillar_id", "strategies")
        for got, exp in zip(self.scores["capabilities"],
                            expected["capabilities"]):
            self.assertEqual({k: got[k] for k in keys},
                             {k: exp[k] for k in keys})

    def test_gaps(self) -> None:
        expected = load(EXAMPLE / "gaps.json")
        self.assertEqual(self.gaps["summary"], expected["summary"])
        for got, exp in zip(self.gaps["gaps"], expected["gaps"]):
            self.assertEqual(got, exp)

    def test_recommendation_ranking(self) -> None:
        expected = load(EXAMPLE / "recomendacoes.json")
        exp_rank = [
            (s["strategy_id"], s["cumulative_priority"])
            for s in expected["ranked_strategies"]
        ]
        got_rank = [
            (s["strategy_id"], s["cumulative_priority"])
            for s in self.recs["ranked_strategies"]
        ]
        self.assertEqual(got_rank, exp_rank)


class EdgeCaseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.framework = load(ROOT / "framework.json")
        self.base = load(ROOT / "respostas.json.example")

    def _with_levels(self, value) -> dict:
        data = copy.deepcopy(self.base)
        for entry in data["responses"].values():
            entry["level"] = value
        return data

    def test_no_answers_is_blocked(self) -> None:
        scores = eng.compute_scores(self.framework, self._with_levels(None))
        self.assertIsNone(scores["overall"]["score"])
        self.assertEqual(scores["threshold"]["status"], "BLOCKED")

    def test_out_of_range_level_rejected(self) -> None:
        with self.assertRaises(eng.InputError):
            eng.compute_scores(self.framework, self._with_levels(5))

    def test_non_numeric_level_rejected(self) -> None:
        with self.assertRaises(eng.InputError):
            eng.compute_scores(self.framework, self._with_levels("3"))

    def test_fractional_levels_accepted(self) -> None:
        scores = eng.compute_scores(self.framework, self._with_levels(2.5))
        self.assertEqual(scores["overall"]["score"], 2.5)
        self.assertEqual(scores["overall"]["label"], "L3 — Gerenciado")

    def test_met_target_has_no_gap(self) -> None:
        data = self._with_levels(4)
        precise = eng.compute_scores(self.framework, data, precise=True)
        gaps = eng.compute_gaps(precise, data)
        self.assertEqual(gaps["gaps"], [])

    def test_deterministic(self) -> None:
        first = eng.compute_scores(self.framework, self.base)
        second = eng.compute_scores(self.framework, self.base)
        first["metadata"].pop("computed_at")
        second["metadata"].pop("computed_at")
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
