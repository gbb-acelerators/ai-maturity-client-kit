---
name: preencher-planilha
description: Populates the auditable scoring workbook from respostas.json by invoking scripts/fill_workbook.py. Supports v2 and archived v1 through the dispatcher. Use for "preencher planilha", "fill spreadsheet", "Excel auditavel", "populate scoring workbook".
argument-hint: optional path different from respostas.json
---

# Skill: Populate auditable workbook

Always run the workbook dispatcher. Do not edit the workbook manually.

## Command

```bash
python3 scripts/fill_workbook.py
```

`make workbook` is equivalent.

## v2 behavior

For v2 inputs, the dispatcher calls `scripts/fill_workbook_v2.py` and writes:

- `saida/pontuacao-v2-<date>.xlsx`

The workbook includes formulas and an engine cross-check column. It uses v2 IDs `D#-Q#`, profile IDs `R-Q1` to `R-Q5`, dimension weights, target overrides, and `NA` handling.

## v1 behavior

For v1 inputs, the dispatcher keeps the archived workbook flow and existing v1 output name.

## Chat response

Report the generated workbook path, detected framework version, answered count, coverage status, and whether the engine cross-check passed if the script prints it.
