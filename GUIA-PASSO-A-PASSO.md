# Step by step: AI Maturity Assessment

English | [Português (Brasil)](GUIA-PASSO-A-PASSO.pt-br.md)

This guide runs the framework v2 assessment from collection to reports. v1 remains available for archived inputs.

## 1. Choose the flow

Use v2 for new assessments. Use v1 only for historical comparison or existing `respostas.json` files without `metadata.framework_version`.

- v2 spec: [coleta/AI-Maturity-Form-Questions_v2.md](coleta/AI-Maturity-Form-Questions_v2.md).
- v2 form: [formularios/assessment-v2.html](formularios/assessment-v2.html).
- v2 Forms instructions: [coleta/INSTRUCOES-FORMS.md](coleta/INSTRUCOES-FORMS.md).
- v1 archive: [coleta/v1/](coleta/v1/), [formularios/v1/](formularios/v1/), [referencia/v1/](referencia/v1/).

## 2. Prepare inputs

```bash
make init
```

This copies `respostas.v2.json.example` to `respostas.json` if the file does not already exist.

You can also import a Microsoft Forms export:

```bash
make import XLSX=respostas-forms.xlsx
```

The importer detects v2 by headers such as `R-Q1:` and `D4-Q3:`. It detects v1 by the archived v1 IDs.

## 3. Understand v2 structure

- 5 profile questions: `R-Q1` to `R-Q5`.
- 61 scored questions: `D#-Q#`.
- 9 dimensions: D1 AI Strategy, Policy and Governance; D2 Enablement, Skills and Culture; D3 Plan, Specify and Design; D4 Code and Context Engineering; D5 Review, Quality and Testing; D6 Security and AI Supply Chain; D7 Deliver and Operate; D8 Engineering Foundations; D9 Measurement, Value and AI FinOps.
- Levels: L0 Not started, L1 Exploring, L2 Adopting, L3 Scaling, L4 AI-native, plus `NA`.

## 4. Run deterministic scoring

```bash
make scores
```

or:

```bash
python3 scripts/assessment_engine.py all
```

Do not compute scores by hand. The engine writes:

- `saida/scores.json`
- `saida/gaps.json`
- `saida/recomendacoes.json`

Coverage is OK at 37 or more answered questions, WARNING at 25 to 36, and BLOCKED below 25.

## 5. Create the workbook

```bash
make workbook
```

For v2, the dispatcher writes `saida/pontuacao-v2-<date>.xlsx`. It includes formulas and an engine cross-check column. For v1, the dispatcher preserves the archived workbook flow.

## 6. Render reports

```bash
make pipeline
```

or, after scores already exist:

```bash
python3 relatorios/scripts/build_payload_and_render.py
```

v2 report files:

- `saida/v2_assessment_summary.pdf`
- `saida/v2_roadmap_g1.pdf`, D1, D2, D9.
- `saida/v2_roadmap_g2.pdf`, D3, D4, D5.
- `saida/v2_roadmap_g3.pdf`, D6, D7, D8.
- `saida/payload_v2.json`.

v1 inputs still produce the archived 5 PDF set.

## 7. Compare rounds

```bash
make compare BEFORE=old-respostas.json AFTER=respostas.json
```

The comparison script supports v2 to v2, v1 to v1, and indicative v1 to v2 comparison through `v1_lineage`.

## 8. Use companion surveys

The Developer Survey and Learning and Growth Survey are unchanged. They provide context for v2 D2, D5, and D9. If you mention Developer Survey dimensions near assessment dimensions, call them `DS-D#`.

## 9. Validate repository sources

```bash
make validate-v2
make validate-docs
make test
```

See [CHANGELOG.md](CHANGELOG.md) for release history.
