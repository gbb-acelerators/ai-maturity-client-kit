---
name: ai-maturity-reports
description: Orchestrates the AI Maturity Assessment reporting pipeline with v2 as default and v1 archived support. Use for "run assessment pipeline", "AI maturity reports", "pipeline completo".
---

# Skill: AI maturity reports

Run the official scripts in order. Never compute or render by hand.

## Full pipeline

```bash
python3 scripts/assessment_engine.py all
python3 scripts/fill_workbook.py
python3 relatorios/scripts/build_payload_and_render.py
```

## v2 default

The pipeline uses v2 when `respostas.json::metadata.framework_version` starts with `2`.

Expected v2 outputs:

- `saida/scores.json`
- `saida/gaps.json`
- `saida/recomendacoes.json`
- `saida/pontuacao-v2-<date>.xlsx`
- `saida/payload_v2.json`
- `saida/v2_assessment_summary.pdf`
- `saida/v2_roadmap_g1.pdf`
- `saida/v2_roadmap_g2.pdf`
- `saida/v2_roadmap_g3.pdf`

## v1 archive

The same scripts dispatch v1 inputs to the archived 158 question, 3 pillar flow and existing v1 PDF set.

## Companion surveys

Developer Survey and Learning Survey outputs may enrich the narrative, but they do not change v2 scores. When both are discussed, call Developer Survey dimensions `DS-D#`.

## Chat response

Report framework, coverage, generated JSONs, workbook, PDFs, and warnings. If any command fails, show the failing command and the script error.
