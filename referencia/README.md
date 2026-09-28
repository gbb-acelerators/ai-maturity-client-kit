# `referencia/`: reference material

🌐 English · [Português (Brasil)](README.pt-br.md)

Framework v2 is the default reference model. v1 material remains archived.

| Path | Purpose |
| --- | --- |
| [framework-v2.md](framework-v2.md) | Generated v2 framework guide with scoring rules, scope notes, crosswalk, and references. |
| [dimensoes/](dimensoes/) | Generated per-dimension pages for D1 to D9 in EN, PT-BR, and ES. |
| [calculadora-pontuacao.html](calculadora-pontuacao.html) | Generated trilingual v2 what-if calculator. Load `saida/scores.json`, adjust weights and targets, and inspect level, gap, priority, horizon, amplification risk, and strategies. |
| [v1/calculadora-pontuacao.html](v1/calculadora-pontuacao.html) | Archived v1 calculator. |
| [exemplo-saida/](exemplo-saida/) | Illustrative v2 outputs, including 5 PDFs, comparison PDF, workbook, repo scan, telemetry, surveys, and wizard inputs. |
| [v1/](v1/) | Archived v1 pillar references and examples. |
| [branding/](branding/) | Brand and voice guidance. |

The v2 scoring source of truth is the deterministic engine and [../coleta/AI-Maturity-Form-Questions_v2.md](../coleta/AI-Maturity-Form-Questions_v2.md). Do not use archived v1 pillar pages for new assessments.

Use `make examples-v2` to regenerate the illustrative examples. Use `make validate-docs` to check generated helpers and package docs.
