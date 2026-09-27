---
name: gerar-relatorio
description: Renders v2 executive PDFs, or archived v1 PDFs, by invoking relatorios/scripts/build_payload_and_render.py. Use for "gerar relatorio", "generate report PDFs", "executive report", "PDF final".
---

# Skill: Generate reports

Always invoke the report dispatcher. Do not assemble payloads or PDFs by hand.

## Command

```bash
python3 relatorios/scripts/build_payload_and_render.py
```

`make pipeline` runs scores plus this renderer.

## Required inputs

- `respostas.json`
- `saida/scores.json`
- `saida/gaps.json`
- `saida/recomendacoes.json`

Run `python3 scripts/assessment_engine.py all` first if any are missing.

## v2 outputs

- `saida/payload_v2.json`
- `saida/v2_assessment_summary.pdf`
- `saida/v2_roadmap_g1.pdf`: D1, D2, D9.
- `saida/v2_roadmap_g2.pdf`: D3, D4, D5.
- `saida/v2_roadmap_g3.pdf`: D6, D7, D8.

## v2 report content to preserve

Surface coverage, bands, weighted dimension priorities, S1 to S7 recommendations, low confidence, amplification risk, perception gap, scope caveat, unverified L3/L4, persona summaries, and backlog top 5 questions when present.

## v1 behavior

v1 inputs still render the existing 5 PDF report set through the archived flow.

## Chat response

List generated files, framework detected, locale from `metadata.language`, and any warnings printed by the script. If rendering dependencies are missing, install only the existing dependencies documented by the repo.
