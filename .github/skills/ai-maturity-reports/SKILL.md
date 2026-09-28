---
name: ai-maturity-reports
description: Orchestrates the AI Maturity Assessment reporting pipeline with v2 as default and v1 archived support. Use for "run assessment pipeline", "AI maturity reports", "pipeline completo", "informes de madurez", "ejecutar el pipeline completo".
---

# Skill: AI maturity reports

Run the official scripts in order. Never compute or render by hand.

## Full pipeline

```bash
python3 scripts/assessment_engine.py all
python3 scripts/fill_workbook.py
python3 relatorios/scripts/build_payload_and_render.py
```

## Optional inputs

- Offline form exports: merge first with `python3 scripts/merge_offline_respostas.py <dir>`.
- Evidence cross-checks: `make scan-repos REPOS=...` and `make telemetry METRICS=...`.
- Wizard: place `implementation-guide-inputs.json` at the root before the final render.

## v2 default outputs

- `saida/scores.json`
- `saida/gaps.json`
- `saida/recomendacoes.json`
- `saida/pontuacao-v2-<date>.xlsx`
- `saida/payload_v2.json`
- `saida/v2_assessment_summary.pdf`
- `saida/v2_roadmap_g1.pdf`
- `saida/v2_roadmap_g2.pdf`
- `saida/v2_roadmap_g3.pdf`
- `saida/v2_implementation_guide.pdf`

## v1 archive

The same scripts dispatch v1 inputs to the archived 158 question, 3 pillar flow and existing v1 PDF set.

## Companion surveys

Developer Survey and Learning Survey outputs may enrich the narrative, but they do not change v2 scores. Use `DS-D#` for Developer Survey dimensions.

## Chat response

Report framework, coverage, generated JSONs, workbook, PDFs, evidence status, and warnings. If any command fails, show the failing command and the script error.
