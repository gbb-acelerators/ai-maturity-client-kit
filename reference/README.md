# `reference/`: reference material

🌐 English · [Português (Brasil)](README.pt-br.md) · [Español](README.es.md)

Framework v2 is the default reference model. v1 material remains archived.

| Path | Purpose |
| --- | --- |
| [framework-v2.md](framework-v2.md) | Generated v2 framework guide with scoring rules, scope notes, crosswalk, and references. |
| [dimensions/](dimensions/) | Generated per-dimension pages for D1 to D9 in EN, PT-BR, and ES. |
| [scoring-calculator.html](scoring-calculator.html) | Generated trilingual v2 what-if calculator. It opens in the browser language; the repository copies `scoring-calculator.pt-br.html` and `scoring-calculator.es.html` open in Portuguese and Spanish, and each language package ships its copy under this name. Load `output/scores.json`, adjust weights and targets, and inspect level, gap, priority, horizon, amplification risk, and strategies. |
| [v1/scoring-calculator.html](v1/scoring-calculator.html) | Archived v1 calculator. |
| [sample-output/](sample-output/) | Illustrative v2 outputs, including 5 PDFs, comparison PDF, workbook, repo scan, telemetry, surveys, and wizard inputs. |
| [v1/](v1/) | Archived v1 pillar references and examples. |
| [branding/](branding/) | Brand and voice guidance. |

The v2 scoring source of truth is the deterministic engine and [../collection/AI-Maturity-Form-Questions_v2.md](../collection/AI-Maturity-Form-Questions_v2.md). Do not use archived v1 pillar pages for new assessments.

Use `make examples-v2` to regenerate the illustrative examples. Use `make validate-docs` to check generated helpers and package docs.
