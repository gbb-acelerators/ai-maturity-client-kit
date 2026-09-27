---
name: preencher-planilha
description: Reads respostas.json and populates the auditable Excel workbook (pontuacao-e-calculo.xlsx) into saida/. Use when the user asks to "preencher a planilha", "transferir respostas para o Excel", "popular o xlsx", "fill the spreadsheet", "fill responses into Excel", "populate scoring workbook", "exportar para planilha", "Excel auditável" or similar.
argument-hint: optional path different from respostas.json
---

# Skill: Populate auditable spreadsheet

## When to use
- Client finished filling `respostas.json` and wants to see numbers in a "touchable" spreadsheet.
- Need to audit cell-by-cell before generating the executive report.

## Inputs
- `respostas.json` (workspace root) — source of truth
- `framework.json` — question/capability weights
- `referencia/pontuacao-e-calculo.xlsx` — template (NEVER modify; always copy)

## Expected output
- `saida/pontuacao-preenchida-<YYYY-MM-DD>.xlsx`
- Brief chat message (English by default, or the user's language): how many questions answered, threshold status, relative link to generated file.

## Implementation: invoke the official script

```bash
python3 scripts/fill_workbook.py
```

**DO NOT edit the workbook in chat.** The script copies the template, fills the three teaching sheets with framework weights and client targets, and adds full sheets for every question, capability, and pillar. Its formulas follow the official algorithm (only answered questions count), so the workbook matches `saida/scores.json`. Fractional levels from multi-respondent imports (for example 2.5) are valid.

## Procedure (follow in order)

1. **Validate inputs**:
   - `respostas.json` exists and parses as JSON.
   - For each `responses[qid]`, validate that `level` is `null` or a number in `[0, 4]` (decimals allowed). If invalid, stop and list problematic qids.

2. **Compute coverage**:
   - `total_answered` = count of questions with `level != null`.
   - `total_applicable` = total questions in `framework.json` (158).
   - Determine `threshold_status`: ≥40 OK, 25–39 WARNING, <25 BLOCKED.

3. **Populate spreadsheet**:
   - Copy `referencia/pontuacao-e-calculo.xlsx` to `saida/pontuacao-preenchida-<DATE>.xlsx`.
   - Open the xlsx with `openpyxl` (preserving formulas).
   - For each "Exemplo P1/P2/P3" sheet, replace input cell values (column C — Nível) with values from `respostas.json` for the corresponding qids (P1-C1-Q1..Q5 / P2-C1-Q1..Q6 / P3-C5-Q1..Q6). Keep weights as-is unless user requests custom.
   - **DO NOT manually recalculate** — the SUMPRODUCT formulas in the xlsx do this when client opens in Excel.

4. **(Optional) Append raw responses**:
   - Add a "Raw responses" sheet with the full table: `qid | level | label | evidence`.

5. **Report in chat (English by default, or the user's language)**:
   ```
   ✓ Spreadsheet populated: saida/pontuacao-preenchida-2026-05-08.xlsx
   • Answered: 45 / 158 (28%)
   • Threshold: WARNING (25-39, preliminary result)
   • Suggested next step: run /calcular-scores to generate scores.json
   ```

## Error handling
- If `respostas.json` doesn't exist → instruct client to copy from `respostas.json.example` if available, or start from scratch.
- If 0 responses → don't generate file, just warn.
- If invalid level (e.g., 5) → list problematic qids and stop.

## Constraints
- NEVER modify `referencia/`, `framework.json`, `respostas.json`.
- Output ALWAYS in `saida/` with descriptive name + ISO date.
