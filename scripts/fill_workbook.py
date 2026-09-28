#!/usr/bin/env python3
"""Populate the auditable scoring workbook from respostas.json.

Deterministic implementation of the /preencher-planilha skill. Copies
referencia/pontuacao-e-calculo.xlsx to saida/, fills the three teaching
sheets, and adds full sheets (every question, capability, and pillar)
whose formulas follow referencia/pontuacao-e-calculo.md: only answered
questions count, weights come from framework.json, and targets from
respostas.json::target_overrides.

Usage:
    python3 scripts/fill_workbook.py
    python3 scripts/fill_workbook.py --respostas X.json --out DIR
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "referencia" / "pontuacao-e-calculo.xlsx"
DEFAULT_TARGET = 3.0

HEADERS = {
    "en": {
        "answers": "Answers",
        "caps": "Capabilities",
        "summary": "Pillars and Overall",
        "a_cols": ("Question ID", "Pillar", "Capability", "Question",
                   "Level (0-4)", "Weight", "Answered", "Level × Weight",
                   "Label", "Evidence"),
        "c_cols": ("Capability", "Name", "Pillar", "Weight", "Answered",
                   "Σ(Level × Weight)", "Σ(Weight answered)", "Score",
                   "Label", "Target", "Gap", "Priority score", "Priority",
                   "Score × Weight", "Weight if scored"),
        "s_cols": ("Pillar", "Name", "Score", "Label"),
        "overall": "OVERALL",
        "answered": "Questions answered",
        "threshold": "Coverage status",
    },
    "pt-br": {
        "answers": "Respostas",
        "caps": "Capabilities",
        "summary": "Pilares e Overall",
        "a_cols": ("ID Questão", "Pilar", "Capability", "Pergunta",
                   "Nível (0-4)", "Peso", "Respondida", "Nível × Peso",
                   "Rótulo", "Evidência"),
        "c_cols": ("Capability", "Nome", "Pilar", "Peso", "Respondidas",
                   "Σ(Nível × Peso)", "Σ(Peso respondidas)", "Score",
                   "Rótulo", "Target", "Gap", "Priority score",
                   "Prioridade", "Score × Peso", "Peso se pontuada"),
        "s_cols": ("Pilar", "Nome", "Score", "Rótulo"),
        "overall": "OVERALL",
        "answered": "Questões respondidas",
        "threshold": "Status de cobertura",
    },
}


def label_formula(ref: str) -> str:
    return (f'=IF({ref}="","—",IF({ref}<0.5,"L0 — Inicial",'
            f'IF({ref}<1.5,"L1 — Em Desenvolvimento",'
            f'IF({ref}<2.5,"L2 — Definido",'
            f'IF({ref}<3.5,"L3 — Gerenciado","L4 — Otimizando")))))')


def priority_formula(ref: str) -> str:
    return (f'=IF({ref}="","",IF({ref}>=2.4,"P0 — Crítico",'
            f'IF({ref}>=1.6,"P1 — Alto",'
            f'IF({ref}>=0.9,"P2 — Médio","P3 — Baixo"))))')


def locale_of(respostas: dict) -> str:
    raw = str(respostas.get("metadata", {}).get("language") or "en")
    return "pt-br" if raw.lower().startswith("pt") else "en"


def validate(respostas: dict) -> list[str]:
    errors = []
    for qid, entry in (respostas.get("responses") or {}).items():
        level = entry.get("level") if isinstance(entry, dict) else None
        if level is None:
            continue
        if isinstance(level, bool) or not isinstance(level, (int, float)) \
                or not 0 <= level <= 4:
            errors.append(f"{qid}: {level!r}")
    return errors


def fix_text_formulas(wb) -> int:
    """The template stores explanatory text such as '= SUMPRODUCT(níveis
    × pesos) ...' as formulas, which Excel cannot parse. Save it as text."""
    fixed = 0
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                value = cell.value
                if (cell.data_type == "f" and isinstance(value, str)
                        and value.startswith("= ")):
                    cell.value = value
                    cell.data_type = "s"
                    fixed += 1
    return fixed


def fill_teaching_sheets(wb, responses, weights, cap_weights, targets):
    for ws in wb.worksheets:
        rows = [r for r in range(1, ws.max_row + 1)
                if str(ws.cell(r, 1).value or "") in weights]
        if not rows:
            continue
        first, last = rows[0], rows[-1]
        cap_id = "-".join(str(ws.cell(first, 1).value).split("-")[:2])
        for r in rows:
            qid = ws.cell(r, 1).value
            ws.cell(r, 3).value = (responses.get(qid) or {}).get("level")
            ws.cell(r, 5).value = weights[qid]
            ws.cell(r, 4).value = label_formula(f"C{r}")
            ws.cell(r, 6).value = f'=IF(C{r}="",0,C{r}*E{r})'
        rng_c, rng_e = f"C{first}:C{last}", f"E{first}:E{last}"
        cells = {}
        for r in range(last + 1, ws.max_row + 1):
            key = str(ws.cell(r, 1).value or "")
            cells[key] = r
        r_sum, r_w = cells.get("Σ(Nível × Peso)"), cells.get("Σ(Peso)")
        r_score = cells.get("CAPABILITY SCORE")
        if r_sum and r_w and r_score:
            ws.cell(r_sum, 6).value = f"=SUMPRODUCT({rng_c},{rng_e})"
            ws.cell(r_w, 6).value = (
                f"=SUMPRODUCT(ISNUMBER({rng_c})*{rng_e})")
            ws.cell(r_score, 6).value = (
                f'=IF(F{r_w}=0,"",F{r_sum}/F{r_w})')
            if cells.get("Rótulo de maturidade"):
                ws.cell(cells["Rótulo de maturidade"], 6).value = (
                    label_formula(f"F{r_score}"))
        r_target = cells.get("Target level")
        r_gap = cells.get("gap_size = target − current")
        r_cw = cells.get("Peso da capability")
        r_ps = cells.get("priority_score = peso × gap")
        if r_score and r_target and r_gap:
            ws.cell(r_gap, 6).value = (
                f'=IF(F{r_score}="","",MAX(0,F{r_target}-F{r_score}))')
        if r_gap and r_cw and r_ps:
            ws.cell(r_ps, 6).value = (
                f'=IF(F{r_gap}="","",F{r_cw}*F{r_gap})')
            if cells.get("Prioridade"):
                ws.cell(cells["Prioridade"], 6).value = (
                    priority_formula(f"F{r_ps}"))
        if cells.get("Target level"):
            ws.cell(cells["Target level"], 6).value = float(
                targets.get(cap_id, DEFAULT_TARGET))
        if cells.get("Peso da capability"):
            ws.cell(cells["Peso da capability"], 6).value = (
                cap_weights[cap_id])


def fix_summary_sheet(wb, targets: dict) -> None:
    """Make the template summary tolerate unanswered capabilities."""
    for ws in wb.worksheets:
        if not str(ws.title).startswith("📊"):
            continue
        for r in range(1, ws.max_row + 1):
            cap = str(ws.cell(r, 3).value or "")
            if " — " in cap and "-C" in cap.split(" — ")[0]:
                cap_id = cap.split(" — ")[0]
                ws.cell(r, 7).value = float(
                    targets.get(cap_id, DEFAULT_TARGET))
                ws.cell(r, 6).value = f'=IF(D{r}="",0,D{r}*E{r})'
                ws.cell(r, 8).value = f'=IF(D{r}="","",MAX(0,G{r}-D{r}))'
                ws.cell(r, 9).value = (
                    f'=IF(H{r}="","",IF(E{r}*H{r}>=2.4,"P0",'
                    f'IF(E{r}*H{r}>=1.6,"P1",'
                    f'IF(E{r}*H{r}>=0.9,"P2","P3"))))')
            formula = ws.cell(r, 4).value
            if isinstance(formula, str) and formula.startswith("=") and \
                    "IFERROR" not in formula and ws.cell(r, 2).value in (
                        "P1", "P2", "P3", "OVERALL SCORE"):
                ws.cell(r, 4).value = f'=IFERROR({formula[1:]},"")'


def add_full_sheets(wb, framework, respostas, loc: str) -> None:
    h = HEADERS[loc]
    responses = respostas.get("responses") or {}
    targets = respostas.get("target_overrides") or {}
    ans = wb.create_sheet(h["answers"])
    ans.append(h["a_cols"])
    caps = wb.create_sheet(h["caps"])
    caps.append(h["c_cols"])
    summ = wb.create_sheet(h["summary"])
    summ.append(h["s_cols"])
    row = 1
    cap_rows = []
    for pillar in framework["pillars"]:
        for cap in pillar["capabilities"]:
            for q in cap["questions"]:
                row += 1
                entry = responses.get(q["id"]) or {}
                ans.append([
                    q["id"], pillar["id"], cap["id"],
                    entry.get("text_pt_br", ""), entry.get("level"),
                    float(q.get("weight", 1.0)),
                    f'=IF(E{row}="",0,1)', f"=IF(G{row}=1,E{row}*F{row},0)",
                    label_formula(f"E{row}"), entry.get("evidence", ""),
                ])
            cap_rows.append((pillar["id"], cap))
    last_ans = row
    a = f"'{h['answers']}'!"
    for i, (pid, cap) in enumerate(cap_rows, start=2):
        name = cap.get("name_pt_br") if loc == "pt-br" else cap.get("name")
        caps.append([
            cap["id"], name, pid, float(cap.get("weight", 1.0)),
            f"=COUNTIFS({a}$C$2:$C${last_ans},A{i},"
            f"{a}$G$2:$G${last_ans},1)",
            f"=SUMIFS({a}$H$2:$H${last_ans},{a}$C$2:$C${last_ans},A{i})",
            f"=SUMIFS({a}$F$2:$F${last_ans},{a}$C$2:$C${last_ans},A{i},"
            f"{a}$G$2:$G${last_ans},1)",
            f'=IF(G{i}=0,"",F{i}/G{i})',
            label_formula(f"H{i}"),
            float(targets.get(cap["id"], DEFAULT_TARGET)),
            f'=IF(H{i}="","",MAX(0,J{i}-H{i}))',
            f'=IF(K{i}="","",D{i}*K{i})',
            priority_formula(f"L{i}"),
            f'=IF(H{i}="",0,H{i}*D{i})',
            f'=IF(H{i}="",0,D{i})',
        ])
    last_cap = len(cap_rows) + 1
    c = f"'{h['caps']}'!"
    for j, pillar in enumerate(framework["pillars"], start=2):
        name = (pillar.get("name_pt_br") if loc == "pt-br"
                else pillar.get("name"))
        summ.append([
            pillar["id"], name,
            f"=IFERROR(SUMIFS({c}$N$2:$N${last_cap},{c}$C$2:$C${last_cap},"
            f"A{j})/SUMIFS({c}$O$2:$O${last_cap},{c}$C$2:$C${last_cap},"
            f"A{j}),0)",
            label_formula(f"C{j}"),
        ])
    r = len(framework["pillars"]) + 3
    summ.cell(r, 1, h["overall"])
    summ.cell(r, 3, f'=IFERROR(SUM({c}$N$2:$N${last_cap})/'
                    f'SUM({c}$O$2:$O${last_cap}),"")')
    summ.cell(r, 4, label_formula(f"C{r}"))
    summ.cell(r + 1, 1, h["answered"])
    summ.cell(r + 1, 3, f"=SUM({a}$G$2:$G${last_ans})")
    summ.cell(r + 2, 1, h["threshold"])
    summ.cell(r + 2, 3, f'=IF(C{r + 1}>=40,"OK",'
                        f'IF(C{r + 1}>=25,"WARNING","BLOCKED"))')


def run(args) -> int:
    try:
        import openpyxl
    except ImportError:
        print("✗ openpyxl is required: make install-deps", file=sys.stderr)
        return 1
    src = Path(args.respostas)
    if not src.exists():
        print(f"✗ {src} not found. Run `make init` or "
              f"/importar-respostas-excel first.", file=sys.stderr)
        return 1
    respostas = json.loads(src.read_text(encoding="utf-8"))
    version = str(respostas.get("metadata", {}).get("framework_version")
                  or "1")
    if version.split(".")[0] not in ("0", "1"):
        import fill_workbook_v2
        return fill_workbook_v2.run(args)
    errors = validate(respostas)
    if errors:
        print("✗ Invalid levels (must be null or 0-4):\n  "
              + "\n  ".join(errors), file=sys.stderr)
        return 1
    framework = json.loads((ROOT / "framework.json").read_text("utf-8"))
    weights = {q["id"]: float(q.get("weight", 1.0))
               for p in framework["pillars"] for c in p["capabilities"]
               for q in c["questions"]}
    cap_weights = {c["id"]: float(c.get("weight", 1.0))
                   for p in framework["pillars"] for c in p["capabilities"]}
    responses = respostas.get("responses") or {}
    answered = sum(1 for q in weights
                   if (responses.get(q) or {}).get("level") is not None)
    if answered == 0:
        print("⚠️ No answered questions: nothing to fill.")
        return 1
    wb = openpyxl.load_workbook(TEMPLATE)
    fix_text_formulas(wb)
    fill_teaching_sheets(wb, responses, weights, cap_weights,
                         respostas.get("target_overrides") or {})
    fix_summary_sheet(wb, respostas.get("target_overrides") or {})
    add_full_sheets(wb, framework, respostas, locale_of(respostas))
    wb.calculation.fullCalcOnLoad = True
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    date = datetime.date.today().isoformat()
    out = out_dir / f"pontuacao-preenchida-{date}.xlsx"
    wb.save(out)
    status = ("OK" if answered >= 40 else
              "WARNING" if answered >= 25 else "BLOCKED")
    print(f"✓ Workbook: {out}")
    print(f"• Answered: {answered} / {len(weights)} "
          f"({round(100 * answered / len(weights))}%) · {status}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--respostas", default=str(ROOT / "respostas.json"))
    ap.add_argument("--out", default=str(ROOT / "saida"))
    return run(ap.parse_args())


if __name__ == "__main__":
    sys.exit(main())
