#!/usr/bin/env python3
"""One-command demo: the v2 reports from the illustrative mock.

Copies respostas.v2.json.example to a temporary kit, runs the engine,
the auditable workbook and the five v2 PDFs, and writes everything to
saida/demo/. Your respostas.json and saida/ results are not touched.

Usage:
    python3 scripts/run_demo.py [--lang en|pt-BR|es] [--out saida/demo]
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*cmd: str) -> None:
    subprocess.run([sys.executable, *cmd], check=True, cwd=ROOT,
                   stdout=subprocess.DEVNULL)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--lang", default="en", choices=("en", "pt-BR", "es"))
    ap.add_argument("--out", default=str(ROOT / "saida" / "demo"))
    args = ap.parse_args()
    out = Path(args.out)
    with tempfile.TemporaryDirectory() as tmp:
        kit = Path(tmp)
        work = kit / "saida"
        data = json.loads((ROOT / "respostas.v2.json.example").read_text(
            encoding="utf-8"))
        data["metadata"]["language"] = args.lang
        respostas = kit / "respostas.json"
        respostas.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                             encoding="utf-8")
        shutil.copy(ROOT / "framework.v2.json", kit)
        try:
            run("scripts/assessment_engine.py", "all", "--respostas",
                str(respostas), "--out", str(work))
            run("scripts/fill_workbook_v2.py", "--respostas",
                str(respostas), "--out", str(work))
            run("relatorios/scripts/build_report_v2.py", "--kit", str(kit),
                "--out", str(work))
        except subprocess.CalledProcessError as exc:
            print(f"✗ {' '.join(exc.cmd[1:2])} failed. Run make "
                  f"install-deps (jinja2, weasyprint, openpyxl).",
                  file=sys.stderr)
            return 1
        out.mkdir(parents=True, exist_ok=True)
        keep = sorted(work.glob("*.pdf")) + sorted(work.glob("*.xlsx")) + \
            [work / n for n in ("scores.json", "gaps.json",
                                "recomendacoes.json")]
        for path in keep:
            shutil.copy(path, out / path.name)
    print(f"✓ Demo ({args.lang}) in {out}:")
    for path in sorted(out.glob("*.pdf")):
        print(f"  {path.name}")
    print("  Illustrative mock data (Contoso Engineering), not a client.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
