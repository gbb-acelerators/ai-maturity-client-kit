# `coleta/`: collection assets

🌐 English · [Português (Brasil)](README.pt-br.md)

Framework v2 is the default collection flow.

| Asset | Purpose |
| --- | --- |
| [AI-Maturity-Form-Questions_v2.md](AI-Maturity-Form-Questions_v2.md) | Approved v2.0.1 source spec. |
| [INSTRUCOES-FORMS.md](INSTRUCOES-FORMS.md) | English Microsoft Forms, Excel, and offline merge setup for v2. |
| [INSTRUCOES-FORMS.pt-br.md](INSTRUCOES-FORMS.pt-br.md) | PT-BR Microsoft Forms, Excel, and offline merge setup for v2. |
| [perguntas-para-forms.md](perguntas-para-forms.md) | Generated PT-BR v2 question bank. |
| [perguntas-para-forms.en.md](perguntas-para-forms.en.md) | Generated English v2 question bank. |
| [perguntas-para-forms.es.md](perguntas-para-forms.es.md) | Generated Spanish v2 question bank. |
| [template-export-forms.xlsx](template-export-forms.xlsx) | v2 Microsoft Forms import template. |
| [v1/](v1/) | Archived v1 banks, instructions, and template. |

The offline form exports one respondent per `respostas.json`. Collect exports in a folder and run `make merge DIR=exports/` before `make pipeline`.

Regenerate v2 collection assets with:

```bash
make generate-v2
```

Validate without changing files with:

```bash
make validate-v2
```
