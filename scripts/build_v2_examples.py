#!/usr/bin/env python3
"""Regenerate the v2 reference example in referencia/exemplo-saida/.

Runs the real scripts on illustrative inputs, once per language:

- the engine, the v2 workbook and the five v2 PDFs on the mock
  respostas.v2.json.example
- the evidence cross-checks: a repository scan of generated fixture
  repositories and scripts/fixtures/copilot-usage-*.mock.json
- the companion surveys on their mocks (PT-BR and EN only, the
  languages the survey scripts support) and the wizard auto-fill from
  the training plan, so the implementation guide shows the full flow
- the round comparison PDF from the v1 example (respostas.json.example)
  to the v2 mock, an indicative baseline through the v1 lineage

Outputs:

- PT-BR PDFs, workbook and survey examples at the folder root
- EN and ES PDFs in en/ and es/
- scores.json, gaps.json, recomendacoes.json, payload_v2.json,
  repo-scan.json and telemetria.json (EN) at the folder root

The archived v1 example in referencia/exemplo-saida/v1/ is not touched.
Requires jinja2, weasyprint, openpyxl and git.

Usage:
    python3 scripts/build_v2_examples.py
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "referencia" / "exemplo-saida"
LANGS = {"pt-BR": DEST, "en": DEST / "en", "es": DEST / "es"}
SURVEY_LANG = {"pt-BR": "pt-br", "en": "en"}
PDFS = ["v2_assessment_summary", "v2_roadmap_g1", "v2_roadmap_g2",
        "v2_roadmap_g3", "v2_implementation_guide", "comparacao-rodadas"]
TELEMETRY = ROOT / "scripts" / "fixtures" / \
    "copilot-usage-organization-28-day.mock.json"
SEATS = "200"
# Fixture repositories: name -> list of (path, number of commits).
FIXTURE_REPOS = {
    "service-01": [], "service-02": [], "service-03": [],
    "service-04": [(".github/copilot-instructions.md", 1)],
    "service-05": [("AGENTS.md", 2)],
    "service-06": [(".github/instructions/api.instructions.md", 1),
                   (".vscode/mcp.json", 1)],
    "service-07": [("CLAUDE.md", 2)],
    "service-08": [(".github/copilot-instructions.md", 1)],
    "service-09": [(".github/copilot-instructions.md", 3),
                   (".github/prompts/review.prompt.md", 1)],
    "service-10": [("AGENTS.md", 1), (".github/agents/reviewer.agent.md", 1),
                   (".github/skills/release/SKILL.md", 1)],
    "service-11": [(".github/agents/triage.agent.md", 1)],
    "service-12": [("AGENTS.md", 2), (".github/prompts/plan.prompt.md", 1),
                   (".specstory/history/2026-09-01-session.md", 1)],
}


def run(*cmd: str) -> None:
    subprocess.run([sys.executable, *cmd], check=True, cwd=ROOT,
                   stdout=subprocess.DEVNULL)


def git(repo: Path, *args: str) -> None:
    env = {**os.environ, "GIT_AUTHOR_DATE": "2026-09-01T12:00:00Z",
           "GIT_COMMITTER_DATE": "2026-09-01T12:00:00Z"}
    subprocess.run(["git", "-C", str(repo), "-c", "user.name=kit",
                    "-c", "user.email=kit@example.com",
                    "-c", "commit.gpgsign=false", *args],
                   check=True, env=env, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)


def make_fixture_repos(base: Path) -> Path:
    for name, files in FIXTURE_REPOS.items():
        repo = base / name
        repo.mkdir(parents=True)
        git(repo, "init", "-q")
        (repo / "README.md").write_text(f"# {name}\n", encoding="utf-8")
        git(repo, "add", ".")
        git(repo, "commit", "-q", "-m", "init")
        for rel, commits in files:
            path = repo / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            for idx in range(commits):
                with path.open("a", encoding="utf-8") as fh:
                    fh.write(f"Illustrative content, revision {idx + 1}\n")
                git(repo, "add", rel)
                git(repo, "commit", "-q", "-m", f"{rel} r{idx + 1}")
    return base


def run_surveys(kit: Path, out: Path, lang: str) -> None:
    run("survey-devs/scripts/calcular_maturidade.py", "--input",
        "survey-devs/respostas-mock-devs.json", "--out", str(out),
        "--lang", lang)
    run("survey-devs/scripts/gerar_insights.py", "--input",
        "survey-devs/respostas-mock-devs.json", "--out", str(out),
        "--lang", lang)
    run("survey-learning/scripts/gerar_plano_capacitacao.py", "--input",
        "survey-learning/respostas-mock-learning.json", "--out", str(out),
        "--lang", lang)
    plan = next(out.glob("plano-capacitacao-*.md"))
    run("wizard/scripts/auto_fill_from_plano.py", "--plano", str(plan),
        "--out", str(kit / "implementation-guide-inputs.json"),
        "--lang", lang)


def main() -> int:
    mock = json.loads((ROOT / "respostas.v2.json.example").read_text(
        encoding="utf-8"))
    with tempfile.TemporaryDirectory() as fixtures:
        repos = make_fixture_repos(Path(fixtures) / "repos")
        for lang, target in LANGS.items():
            with tempfile.TemporaryDirectory() as tmp:
                kit = Path(tmp)
                out = kit / "saida"
                out.mkdir()
                data = json.loads(json.dumps(mock))
                data["metadata"]["language"] = lang
                respostas = kit / "respostas.json"
                respostas.write_text(
                    json.dumps(data, ensure_ascii=False, indent=2),
                    encoding="utf-8")
                shutil.copy(ROOT / "framework.v2.json", kit)
                run("scripts/scan_repos_ai_config.py", "--path", str(repos),
                    "--out", str(out), "--label",
                    "illustrative fixture repositories")
                run("scripts/import_copilot_metrics.py", str(TELEMETRY),
                    "--seats", SEATS, "--out", str(out))
                if lang in SURVEY_LANG:
                    run_surveys(kit, out, SURVEY_LANG[lang])
                run("scripts/assessment_engine.py", "all", "--respostas",
                    str(respostas), "--out", str(out))
                run("scripts/fill_workbook_v2.py", "--respostas",
                    str(respostas), "--out", str(out))
                run("relatorios/scripts/build_report_v2.py", "--kit",
                    str(kit), "--out", str(out))
                run("scripts/compare_rounds.py", "respostas.json.example",
                    str(respostas), "--out", str(out), "--pdf")
                target.mkdir(parents=True, exist_ok=True)
                for name in PDFS:
                    shutil.copy(out / f"{name}.pdf", target / f"{name}.pdf")
                if lang == "pt-BR":
                    for old in target.glob("pontuacao-v2-*.xlsx"):
                        old.unlink()
                    book = next(out.glob("pontuacao-v2-*.xlsx"))
                    shutil.copy(book, target / "pontuacao-v2-EXEMPLO.xlsx")
                    for pattern, name in (
                        ("maturidade-developer-survey-*.json",
                         "maturidade-developer-survey-EXEMPLO.json"),
                        ("insights-developer-survey-*.md",
                         "insights-developer-survey-EXEMPLO.md"),
                        ("plano-capacitacao-*.md",
                         "plano-capacitacao-EXEMPLO.md"),
                    ):
                        shutil.copy(next(out.glob(pattern)), DEST / name)
                    shutil.copy(kit / "implementation-guide-inputs.json",
                                DEST / "implementation-guide-inputs-"
                                       "EXEMPLO.json")
                if lang == "en":
                    for name in ("scores.json", "gaps.json",
                                 "recomendacoes.json", "payload_v2.json",
                                 "repo-scan.json", "telemetria.json",
                                 "comparacao-rodadas.json"):
                        shutil.copy(out / name, DEST / name)
            print(f"✓ {lang}: {target.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
