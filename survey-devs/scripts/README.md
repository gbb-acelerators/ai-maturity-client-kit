# `survey-devs/scripts/`

🌐 English · [Português (Brasil)](README.pt-br.md)

📖 **Navigation:** [🏠 Index](../../README.md) · [« Developer Survey](../README.md)

Scripts that compute developer AI maturity from the anonymous Developer Survey.

## Contents

| File | Purpose |
| --- | --- |
| [rubric.py](rubric.py) | Deterministic rubric across `DS-D2` to `DS-D8`. Maps answers to scores. The score bands match the v1 survey rubric. |
| [calcular_maturidade.py](calcular_maturidade.py) | Reads `survey-devs/respostas-devs.json` and generates `saida/maturidade-developer-survey-<date>.json` with `DS-D#` keys. |
| [gerar_insights.py](gerar_insights.py) | Generates `saida/insights-developer-survey-<date>.md`. Section 12 links survey signals to v2 questions. English by default; pass `--lang pt-br` for PT-BR. |

## Usage

```bash
python3 survey-devs/scripts/calcular_maturidade.py
python3 survey-devs/scripts/gerar_insights.py
python3 survey-devs/scripts/gerar_insights.py --lang pt-br
```

Survey outputs are context for v2 reports. They never change v2 scores.
