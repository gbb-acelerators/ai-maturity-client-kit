#!/usr/bin/env python3
"""Tests for the companion surveys next to framework v2.

Run: python3 -m unittest scripts/test_surveys.py
"""
from __future__ import annotations

import copy
import json
import re
import subprocess
import sys
import tempfile
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


OPTIONS = json.loads((ROOT / "survey-devs" / "options.json").read_text(
    "utf-8"))
MOCK_DEVS = json.loads((ROOT / "survey-devs" / "respostas-mock-devs.json")
                       .read_text("utf-8"))


def bank_options(suffix: str) -> dict[str, list[str]]:
    text = (ROOT / "survey-devs" / f"perguntas-para-forms-devs{suffix}.md"
            ).read_text("utf-8")
    out = {}
    for block in re.split(r"\n### (?:Question|Pergunta|Pregunta) `",
                          text)[1:]:
        qid = block.split("`", 1)[0]
        m = re.search(r"\n(?:Options|Opções|Opciones):\s*\n(.*?)"
                      r"(?=\n### |\n## |\n---|\Z)", block, re.S)
        if m:
            out[qid] = [ln[2:].strip() for ln in m.group(1).splitlines()
                        if ln.startswith("- ")]
    return out


def translated(data: dict, lang: str) -> dict:
    out = copy.deepcopy(data)
    for person in out["respondents"]:
        for qid, entry in person["responses"].items():
            value = entry.get("value") if isinstance(entry, dict) else None
            if not isinstance(value, str) or qid not in OPTIONS:
                continue
            table = {o["pt"]: o[lang] for o in OPTIONS[qid]}
            entry["value"] = "; ".join(
                table.get(p.strip(), p.strip())
                for p in value.split(";") if p.strip())
    return out


def team_scores(data: dict) -> tuple:
    scores = [rubric.score_respondent(p["responses"], "en")
              for p in data["respondents"]]
    team = rubric.aggregate_team(scores, "en")
    return (team["team_overall_score"],
            {k: v["team_score"] for k, v in team["dimensions"].items()})


class DeveloperSurveyOptionsTest(unittest.TestCase):
    def test_banks_follow_options_file(self) -> None:
        for suffix, lang in (("", "pt"), (".en", "en"), (".es", "es")):
            bank = bank_options(suffix)
            self.assertEqual(sorted(bank), sorted(OPTIONS), suffix)
            for qid, opts in OPTIONS.items():
                self.assertEqual(bank[qid], [o[lang] for o in opts],
                                 f"{suffix} {qid}")

    def test_options_are_safe_for_forms(self) -> None:
        for qid, opts in OPTIONS.items():
            for lang in ("pt", "en", "es"):
                values = [o[lang] for o in opts]
                self.assertEqual(len(set(values)), len(values), qid)
                for value in values:
                    self.assertNotRegex(value, "[;\u2014\u2013]", qid)

    def test_any_language_scores_the_same(self) -> None:
        base = team_scores(MOCK_DEVS)
        for lang in ("en", "es"):
            self.assertEqual(team_scores(translated(MOCK_DEVS, lang)), base)
        old = copy.deepcopy(MOCK_DEVS)
        for person in old["respondents"]:
            entry = person["responses"].get("S7-Q2")
            if entry and entry.get("value") == "Não, cada um se vira":
                entry["value"] = "Não \u2014 cada um se vira"
        self.assertEqual(team_scores(old), base)

    def test_insights_show_options_in_report_language(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "respostas-devs.json"
            src.write_text(json.dumps(translated(MOCK_DEVS, "es"),
                                      ensure_ascii=False), encoding="utf-8")
            subprocess.run(
                [sys.executable, str(ROOT / "survey-devs" / "scripts" /
                                     "gerar_insights.py"),
                 "--input", str(src), "--out", tmp, "--lang", "en"],
                check=True, capture_output=True)
            report = next(Path(tmp).glob("insights-developer-survey-*.md"))
            text = report.read_text("utf-8")
        self.assertIn("Daily (several hours)", text)
        self.assertNotIn("Diariamente (varias horas)", text)


if __name__ == "__main__":
    unittest.main()
