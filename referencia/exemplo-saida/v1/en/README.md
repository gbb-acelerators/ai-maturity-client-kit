# `referencia/exemplo-saida/v1/en/`

📖 **Navigation:** [🏠 Index](../../../../README.md) · [« Example folder](../../README.md)

**English** version of the 5 archived framework v1 reference PDFs, generated from the v1 example payload (Cliente Exemplo S.A., locale forced to `en`).

## Contents

| File | Description |
|---|---|
| `score_justification.pdf` | Score justification |
| `roadmap_part_pillar_p1.pdf` | Roadmap part 1, Developer Productivity pillar |
| `roadmap_part_pillar_p2.pdf` | Roadmap part 2, DevOps Lifecycle pillar |
| `roadmap_part_pillar_p3.pdf` | Roadmap part 3, Application Platform pillar |
| `roadmap_part4.pdf` | Consolidated implementation guide |

## When to use

- Show a client how the v1 PDFs look in English (`"language": "en"` in `respostas.json::metadata`).
- Check that the templates handle longer strings (English text tends to be longer than PT-BR).

> [!NOTE]
> The PT-BR v1 PDFs are in the parent folder, [`../`](../). The Spanish ones are in [`../es/`](../es/).

## How to regenerate

```bash
python3 relatorios/scripts/render_reports.py \
  --payload referencia/exemplo-saida/v1/payload.json \
  --locale en \
  --out referencia/exemplo-saida/v1/en
```
