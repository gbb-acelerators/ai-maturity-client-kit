# Step by step: AI Maturity Assessment

🌐 English · [Português (Brasil)](GUIA-PASSO-A-PASSO.pt-br.md)

This guide runs the framework v2 assessment from collection to reports. v1 remains available for archived inputs.

## Quickstart

Fastest path to a first PDF:

```bash
make install-deps
make demo
open saida/demo/*.pdf
```

Real client flow:

```bash
# Collect responses with Microsoft Forms, or with offline HTML exports.
make merge DIR=exports/
# If using Microsoft Forms instead of offline exports:
make import XLSX=respostas-forms.xlsx
make pipeline
# Optional evidence cross-checks.
make scan-repos REPOS=~/src
make telemetry METRICS=copilot-usage.json SEATS=200
# Fill implementation-guide-inputs.json with the wizard, then render again.
make pipeline
```

## 1. Choose the flow

Use v2 for new assessments. Use v1 only for historical comparison or existing `respostas.json` files without `metadata.framework_version`.

- v2 spec: [coleta/AI-Maturity-Form-Questions_v2.md](coleta/AI-Maturity-Form-Questions_v2.md).
- v2 form: [formularios/assessment-v2.html](formularios/assessment-v2.html).
- v2 Forms instructions: [coleta/INSTRUCOES-FORMS.md](coleta/INSTRUCOES-FORMS.md).
- v2 dimension pages: [referencia/dimensoes/](referencia/dimensoes/).
- v1 archive: [coleta/v1/](coleta/v1/), [formularios/v1/](formularios/v1/), [referencia/v1/](referencia/v1/).

## 2. Prepare inputs

```bash
make init
```

This copies `respostas.v2.json.example` to `respostas.json` if the file does not already exist.

You can import a Microsoft Forms export:

```bash
make import XLSX=respostas-forms.xlsx
```

You can also use the offline form. Each respondent opens [formularios/assessment-v2.html](formularios/assessment-v2.html), exports one `respostas.json`, and sends it to the facilitator. Put the exports in one folder and run:

```bash
make merge DIR=exports/
```

The merge assigns unique respondent IDs, refuses v1 files, refuses mixed organizations unless `--org` or `--allow-mixed-org` is used, and backs up an existing `respostas.json` before writing the merged file.

## 3. Understand v2 structure

- 5 profile questions: `R-Q1` to `R-Q5`.
- 61 scored questions: `D#-Q#`.
- 9 dimensions: D1 AI Strategy, Policy and Governance; D2 Enablement, Skills and Culture; D3 Plan, Specify and Design; D4 Code and Context Engineering; D5 Review, Quality and Testing; D6 Security and AI Supply Chain; D7 Deliver and Operate; D8 Engineering Foundations; D9 Measurement, Value and AI FinOps.
- Levels: L0 Not started, L1 Exploring, L2 Adopting, L3 Scaling, L4 AI-native, plus `NA`.
- Reference pages for D1 to D9 include scope notes, anchors, evidence examples, basis, Developer Survey context, and cited references.

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

Coverage is OK at 37 or more answered questions, WARNING at 25 to 36, and BLOCKED below 25. Respondent divergence is flagged when a dimension has at least 3 respondent scores and a standard deviation of 1.0 or more.

## 5. Create the workbook

```bash
make workbook
```

For v2, the dispatcher writes `saida/pontuacao-v2-<date>.xlsx`. It includes formulas and an engine cross-check column. The formulas round comparisons to 9 decimal places so priority boundaries ignore floating-point noise.

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
- `saida/v2_implementation_guide.pdf`.
- `saida/payload_v2.json`.

v1 inputs still produce the archived 5 PDF set.

## 7. Add evidence cross-checks

Run either or both before the final `make pipeline`:

```bash
make scan-repos REPOS=~/src
make telemetry METRICS=copilot-usage.json SEATS=200
```

Repository scan output is `saida/repo-scan.json`. Copilot metrics output is `saida/telemetria.json`. The summary report shows an Evidence cross-checks section and flags answers above what the evidence supports. The implementation guide lists those flags as risks. Without the files, the PDF explains how to produce them.

## 8. Fill the implementation guide wizard

Open the generated trilingual wizard:

```bash
open wizard/implementation-guide-wizard.html
```

It saves 11 fields to `implementation-guide-inputs.json`: `executive_steering_committee`, `tpo`, `dimension_owners`, `raci_matrix`, `communication_plan`, `training_plan`, `adkar_notes`, `risk_register`, `quick_wins_w1_4`, `quick_wins_w5_8`, and `quick_wins_w9_12`. Empty fields render as `to fill with the client`, not sample content.

Mode D can prefill 7 fields from the Learning Survey plan:

```bash
python3 wizard/scripts/auto_fill_from_plano.py --lang en
```

After the wizard, run `make pipeline` again.

## 9. Compare rounds

```bash
make compare BEFORE=old-respostas.json AFTER=respostas.json
```

The comparison script supports v2 to v2 comparable deltas, v1 to v2 indicative baseline through `v1_lineage`, and v1 to v1. It writes `saida/comparacao-rodadas.pdf` when PDF rendering is available.

## 10. Use companion surveys

Developer Survey and Learning and Growth Survey provide context. They do not change v2 scores.

- Developer Survey dimensions are `DS-D2` to `DS-D8` in outputs.
- The v2 summary PDF shows Developer Survey context when `saida/maturidade-developer-survey-*.json` exists.
- Learning Survey output can feed the implementation guide wizard Mode D.
- Survey scripts write EN or PT-BR only.

## 11. Validate repository sources

```bash
python3 scripts/build_kit_docs.py
python3 scripts/build_kit_docs.py --check
make validate-v2
make validate-docs
make test
```

See [CHANGELOG.md](CHANGELOG.md) for release history.
