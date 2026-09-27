# AI Maturity Assessment kit

This English package uses framework v2 by default. v1 remains archived and supported for historical inputs.

## Contents

- Main v2 assessment: 5 profile questions, 61 scored questions, 9 dimensions.
- Offline v2 form: [../formularios/assessment-v2.html](../formularios/assessment-v2.html).
- Forms instructions: [FORMS-INSTRUCTIONS.md](FORMS-INSTRUCTIONS.md).
- Step by step guide: [STEP-BY-STEP.md](STEP-BY-STEP.md).
- Deterministic scripts under [../scripts/](../scripts/).

## Run

```bash
make init
make import XLSX=respostas-forms.xlsx
make scores
make workbook
make pipeline
```

v2 outputs include `scores.json`, `gaps.json`, `recomendacoes.json`, `pontuacao-v2-<date>.xlsx`, `payload_v2.json`, and 4 PDFs: summary plus G1, G2, G3 roadmaps.

## v1 archive

Use `make init-v1` only for archived v1 assessments. v1 uses 158 questions, 3 pillars, and assets under [../coleta/v1/](../coleta/v1/), [../formularios/v1/](../formularios/v1/), and [../referencia/v1/](../referencia/v1/).
