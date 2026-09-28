# `formularios/`: assessment forms

🌐 English · [Português (Brasil)](README.pt-br.md) · [Español](README.es.md)

Framework v2 is the default for new assessments.

| Asset | Purpose |
| --- | --- |
| [assessment-v2.html](assessment-v2.html) | Generated offline v2 form in PT-BR, EN, and ES. It opens in the browser language, runs without internet, shows each question scope note, and exports one respondent per `respostas.json`. The repository copies `assessment-v2.pt-br.html` and `assessment-v2.es.html` open in Portuguese and Spanish; each language package ships its copy under this name. |
| [v1/](v1/) | Archived v1 visual forms for historical assessments. |

Use the offline flow when Microsoft Forms is unavailable or when a workshop needs local collection:

```bash
# Collect each exported respostas.json under exports/, then:
make merge DIR=exports/
make pipeline
```

The v2 form follows [../coleta/AI-Maturity-Form-Questions_v2.md](../coleta/AI-Maturity-Form-Questions_v2.md): 5 profile questions (`R-Q1` to `R-Q5`) and 61 scored questions (`D#-Q#`) across 9 dimensions.

Archived v1 HTML files live in [v1/](v1/). Each one has a Portuguese (`.pt-br.html`) and a Spanish (`.es.html`) copy in the repository; each language package ships its copy under the base name:

- [v1/P1-produtividade-do-desenvolvedor.html](v1/P1-produtividade-do-desenvolvedor.html)
- [v1/P2-ciclo-de-vida-devops.html](v1/P2-ciclo-de-vida-devops.html)
- [v1/P3-plataforma-de-aplicações.html](v1/P3-plataforma-de-aplicações.html)
