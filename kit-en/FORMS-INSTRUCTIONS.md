# Microsoft Forms instructions

This file documents the main assessment section for framework v2. Companion surveys are unchanged.

## Form A: AI Maturity Assessment v2

Use the v2 source assets:

- Question spec: [../coleta/AI-Maturity-Form-Questions_v2.md](../coleta/AI-Maturity-Form-Questions_v2.md).
- Generated question bank: [../coleta/perguntas-para-forms.en.md](../coleta/perguntas-para-forms.en.md).
- Offline form: [../formularios/assessment-v2.html](../formularios/assessment-v2.html).
- Import template: [../coleta/template-export-forms.xlsx](../coleta/template-export-forms.xlsx).

Create profile questions `R-Q1` to `R-Q5`, then the 61 scored questions `D#-Q#`. Keep each question title starting with its ID, for example `D4-Q3: ...`. The importer uses those IDs.

Use these options for every scored question:

- `L0 - Not started: ...`
- `L1 - Exploring: ...`
- `L2 - Adopting: ...`
- `L3 - Scaling: ...`
- `L4 - AI-native: ...`
- `NA`

After exporting from Forms, run:

```bash
python3 scripts/import_forms_excel.py respostas-forms.xlsx
python3 scripts/assessment_engine.py all
```

## v1 archive

Do not build new v1 forms unless you are supporting a historical comparison. v1 assets live under [../coleta/v1/](../coleta/v1/) and [../formularios/v1/](../formularios/v1/).
