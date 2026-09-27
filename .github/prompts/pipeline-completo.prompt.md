---
mode: agent
---

# Pipeline completo: AI Maturity Assessment

Run the complete assessment pipeline. Framework v2 is the default. v1 remains supported when `respostas.json` has no `metadata.framework_version` or has a `1.x` version.

## Rules

- Do not compute scores, gaps, recommendations, workbooks, or reports by hand.
- Do not edit framework files, generated question banks, templates, scripts, or `Makefile`.
- Use the deterministic dispatchers. They select v2 or v1 from `respostas.json::metadata.framework_version`.

## Steps

1. Confirm required input:
   - `respostas.json` exists.
   - Optional Microsoft Forms import: run `python3 scripts/import_forms_excel.py <xlsx>` first.
2. Run the deterministic engine:
   ```bash
   python3 scripts/assessment_engine.py all
   ```
3. Populate the auditable workbook:
   ```bash
   python3 scripts/fill_workbook.py
   ```
4. Render reports:
   ```bash
   python3 relatorios/scripts/build_payload_and_render.py
   ```
5. Report outputs.

## v2 expected outputs

- `saida/scores.json`
- `saida/gaps.json`
- `saida/recomendacoes.json`
- `saida/pontuacao-v2-<date>.xlsx`
- `saida/payload_v2.json`
- `saida/v2_assessment_summary.pdf`
- `saida/v2_roadmap_g1.pdf`
- `saida/v2_roadmap_g2.pdf`
- `saida/v2_roadmap_g3.pdf`

## v1 expected outputs

v1 inputs still use the archived 158 question, 3 pillar flow and produce the existing v1 outputs, including the 5 PDF report set.

## Final chat template

```text
Pipeline complete.
Framework: v2.0.1 or v1 archived flow
Coverage: <status> (<answered>/<applicable>)
JSON outputs: scores.json, gaps.json, recomendacoes.json
Workbook: <file>
Reports: <files>
Notes: <flags or blockers from script output>
```
