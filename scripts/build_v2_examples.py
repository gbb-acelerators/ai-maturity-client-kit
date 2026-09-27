#!/usr/bin/env python3
"""Regenerate the v2 reference example in referencia/exemplo-saida/.

Runs the real pipeline (engine, v2 workbook, v2 reports) on the
illustrative mock respostas.v2.json.example, once per language:

- PT-BR PDFs and workbook at the folder root
- EN and ES PDFs in en/ and es/
- scores.json, gaps.json, recomendacoes.json and payload_v2.json (EN)
  at the folder root

The archived v1 example lives in referencia/exemplo-saida/v1/ and is not
touched. Requires jinja2, weasyprint and openpyxl.

Usage:
    python3 scripts/build_v2_examples.py
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "referencia" / "exemplo-saida"
LANGS = {"pt-BR": DEST, "en": DEST / "en", "es": DEST / "es"}
PDFS = ["v2_assessment_summary", "v2_roadmap_g1", "v2_roadmap_g2",
        "v2_roadmap_g3"]


def run(*cmd: str) -> None:
    subprocess.run([sys.executable, *cmd], check=True, cwd=ROOT,
                   stdout=subprocess.DEVNULL)


def main() -> int:
    mock = json.loads((ROOT / "respostas.v2.json.example").read_text(
        encoding="utf-8"))
    for lang, target in LANGS.items():
        with tempfile.TemporaryDirectory() as tmp:
            kit = Path(tmp)
            out = kit / "saida"
            data = json.loads(json.dumps(mock))
            data["metadata"]["language"] = lang
            (kit / "respostas.json").write_text(
                json.dumps(data, ensure_ascii=False, indent=2),
                encoding="utf-8")
            shutil.copy(ROOT / "framework.v2.json", kit)
            run("scripts/assessment_engine.py", "all", "--respostas",
                str(kit / "respostas.json"), "--out", str(out))
            run("scripts/fill_workbook_v2.py", "--respostas",
                str(kit / "respostas.json"), "--out", str(out))
            run("relatorios/scripts/build_report_v2.py", "--kit", str(kit),
                "--out", str(out))
            target.mkdir(parents=True, exist_ok=True)
            for name in PDFS:
                shutil.copy(out / f"{name}.pdf", target / f"{name}.pdf")
            if lang == "pt-BR":
                for old in target.glob("pontuacao-v2-*.xlsx"):
                    old.unlink()
                book = next(out.glob("pontuacao-v2-*.xlsx"))
                shutil.copy(book, target / "pontuacao-v2-EXEMPLO.xlsx")
            if lang == "en":
                for name in ("scores.json", "gaps.json",
                             "recomendacoes.json", "payload_v2.json"):
                    shutil.copy(out / name, DEST / name)
        print(f"✓ {lang}: {target.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
