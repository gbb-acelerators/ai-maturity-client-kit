# How to create the Microsoft Forms for the AI Maturity Assessment (v2)

🌐 English · [Português (Brasil)](FORMS-INSTRUCTIONS.pt-br.md) · [Español](FORMS-INSTRUCTIONS.es.md)

**`ASSESSMENT`** · 📖 [🏠 Index](../README.md) · [« Step-by-step guide](../STEP-BY-STEP.md) · You are here · [» Survey-devs](../survey-devs/FORMS-INSTRUCTIONS-DEVS.md)

> [!TIP]
> Framework v2 has **5 profile questions and 61 scored questions in 9 dimensions** (127 Forms elements, about 25 to 40 minutes per respondent). The v1 instructions (158 questions) are archived in [v1/FORMS-INSTRUCTIONS.md](v1/FORMS-INSTRUCTIONS.md).

## Quick comparison of the 4 paths

| Path | Setup time | When to use |
| --- | --- | --- |
| **A. Full Microsoft Forms** | 60 to 90 minutes | Several respondents per role; you want persona results and the perception-gap flag. |
| **B. Pilot with one dimension** | 15 minutes | Validate wording and timing with 3 to 5 people before the full launch. |
| **C. Excel or SharePoint template** | 5 minutes | Workshops, or when Forms is not available: one row per respondent in [template-export-forms.xlsx](template-export-forms.xlsx). |
| **D. Offline HTML form** | None | One respondent at a time, no Microsoft 365 needed: [forms/assessment-v2.html](../forms/assessment-v2.html) exports one `responses.json` per respondent. |

## Path A: Full Microsoft Forms

1. Open the question bank in your language: [question-bank.md](question-bank.md) (EN), [question-bank.pt-br.md](question-bank.pt-br.md) (PT-BR), or [question-bank.es.md](question-bank.es.md) (ES). All three are generated from [framework.v2.json](../framework.v2.json) and have the same questions, options, anchors, and scope notes.
2. Go to <https://forms.office.com>, create a blank form, and name it `AI-Assisted SDLC Maturity Assessment v2 - <Organization>`.
3. Paste the [privacy notice](#privacy-notice-paste-into-the-form-description) into the form description and fill in the brackets.
4. Add **10 sections**: Section 0 (profile) and D1 to D9.
5. Section 0: add `R-Q1` to `R-Q5` as **Choice**. Turn on **Multiple answers** for `R-Q3` only.
6. For each scored question add:
   - a **Choice** (single answer) whose title starts with the ID and a colon, for example `D4-Q3: Are well-scoped tasks delegated ...`;
   - the 6 options, in order, with the `L0` to `L4` and `NA` prefix kept at the start;
   - the **L3 looks like** and **L4 looks like** lines, and the **Scope note** when the question has one, in the subtitle;
   - an optional **Long Text** titled exactly `Evidence (D4-Q3)`.
7. Optional: in `...` > `Branching`, let people who answer Executive or Product / program manager in `R-Q1` skip D4 to D7. Skipped questions count as not answered, not as `NA`.
8. `Settings`: restrict to your organization, or `Anyone can respond` if you share by link.
9. Share the link. Aim for **at least 3 respondents per role**: persona summaries mark smaller groups as low sample, and the perception-gap and respondent-divergence flags need enough respondents to be meaningful.
10. When responses are in: `Responses` > `Open in Excel`, download the file, and run:

    ```bash
    make import XLSX=forms-responses.xlsx
    make pipeline
    ```

> [!IMPORTANT]
> The importer finds each column by the ID at the start of the title (`D1-Q1:`, `R-Q1:`) and each evidence column by `Evidence (<ID>)`. It detects v2 from those IDs. Do not translate the `Evidence (<ID>)` label or the option prefixes.

## Path B: Pilot with one dimension

Create the form with Section 0 and one dimension. D4 is a good start, it has 8 questions. Collect 3 to 5 answers, then run:

```bash
python3 scripts/import_forms_excel.py <file> --allow-partial
```

The engine reports coverage `BLOCKED` because fewer than 25 questions are answered. Use the pilot only to check wording and timing.

## Path C: Excel or SharePoint template

1. Copy [template-export-forms.xlsx](template-export-forms.xlsx) to SharePoint or OneDrive. Its header row has the exact Forms export shape: profile columns, `D#-Q#` answer columns, and `Evidence (D#-Q#)` columns.
2. Each respondent fills one row. Answers must start with `L0` to `L4` or `NA`. `R-Q3` accepts several options separated by `;`.
3. Download the file and run `make import XLSX=<file>`.

A filled, synthetic example is [v2-mock-forms-export.xlsx](v2-mock-forms-export.xlsx) (14 illustrative respondents; not a real client).

## Path D: Offline HTML form plus merge

Use this path when respondents cannot access Microsoft Forms or when you need a fast workshop flow.

1. Send [../forms/assessment-v2.html](../forms/assessment-v2.html) to each respondent, or open it from the repository.
2. The form runs offline, supports EN, PT-BR, and ES, shows each question scope note, and exports one respondent per `responses.json`.
3. Collect the exported files in a folder, for example `exports/`.
4. Merge them:

   ```bash
   make merge DIR=exports/
   ```

The merge script assigns unique IDs `R01`, `R02`, and so on. It refuses v1 files and refuses mixed organizations unless you pass `--org` or `--allow-mixed-org` to `scripts/merge_offline_responses.py`. It backs up an existing `responses.json` before writing the merged file.

Then run:

```bash
make pipeline
```

## Privacy notice (paste into the form description)

```text
This assessment asks about engineering practices, not about individual performance.
We collect your role, the scope of your answers, the AI tools you use, your years of experience, and your hands-on time, so results can be shown per role.
Controller: [organization]. Purpose: AI maturity diagnosis and roadmap.
Access: [names or team]. Retention: [period], then deleted.
Results are reported in aggregate; groups with fewer than 3 people are marked as low sample.
Questions or deletion requests: [contact].
```

Agree on these points with your privacy or legal team before launch (LGPD / GDPR); this checklist is not legal advice:

- **Minimization:** the form does not need name or email. If Forms collects them automatically, disable it or restrict access to the export.
- **Storage:** keep the `.xlsx`, `responses.json`, and `output/` on managed storage with restricted access. `responses.json` and `output/` are in `.gitignore`; never commit them.
- **Retention and deletion:** delete the Forms responses and the exported files when the retention period ends.

## How answers become scores

The engine ([scripts/assessment_engine.py](../scripts/assessment_engine.py)) follows section 8 of [AI-Maturity-Form-Questions_v2.md](AI-Maturity-Form-Questions_v2.md): pooled mean per question, mean per dimension, weighted mean of dimensions, half-open level bands, and the low-confidence, amplification-risk, perception-gap, respondent-divergence, scope, unverified L3/L4, and evidence coverage flags.

Optional evidence cross-checks come from `make scan-repos`, `make telemetry` and `make dora`. They are shown in the summary PDF and listed as risks in the implementation guide when they challenge an answer.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `No column header starts with a question ID` | The question titles do not start with `D1-Q1:`. Rename them in Forms and export again. |
| `Only N of 61 v2 questions were found` | Some titles lost the ID. Use `--allow-partial` for a pilot only. |
| `unrecognized value at R-Q1` | The option text was edited. Use the exact option text from the question bank (any of the 3 languages is accepted). |
| Persona heatmap says low sample | Fewer than 3 respondents for that role. Invite more people or read that column with care. |
| `make merge` refuses a file | Check whether it is a v1 export or whether the organization differs from the other exports. |
