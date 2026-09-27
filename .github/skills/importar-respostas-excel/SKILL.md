---
name: importar-respostas-excel
description: Imports Microsoft Forms Excel exports into respostas.json by invoking scripts/import_forms_excel.py. Detects v2 exports by header IDs and preserves archived v1 import. Use for "importar Forms", "import Excel", "respostas-forms.xlsx".
argument-hint: path to Microsoft Forms .xlsx export
---

# Skill: Import Microsoft Forms responses

Use the deterministic importer. Do not parse the spreadsheet manually.

## Command

```bash
python3 scripts/import_forms_excel.py respostas-forms.xlsx
```

or:

```bash
make import XLSX=respostas-forms.xlsx
```

## v2 detection

The importer detects v2 exports by question header IDs such as `D4-Q3:` and profile IDs `R-Q1` to `R-Q5`. It writes the v2 `respondents` format:

```json
{
  "metadata": {"framework_version": "2.0.1"},
  "respondents": [
    {"id": "r1", "profile": {"R-Q1": "..."}, "answers": {"D1-Q1": {"level": 2, "evidence": "..."}}}
  ]
}
```

`level: null` means `NA`. A missing answer key means not answered.

## v1 behavior

Exports with v1 headers continue through the archived v1 import format.

## After import

Run:

```bash
python3 scripts/assessment_engine.py all
python3 scripts/fill_workbook.py
python3 relatorios/scripts/build_payload_and_render.py
```

## Chat response

Report the detected framework, respondent count, output path, warnings, and next command. Stop if the importer reports unknown headers or invalid levels.
