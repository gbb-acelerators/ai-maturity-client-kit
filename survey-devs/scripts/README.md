# `survey-devs/scripts/`

🌐 English · [Português (Brasil)](README.pt-br.md) · [Español](README.es.md)

📖 **Navigation:** [🏠 Index](../../README.md) · [« Developer Survey](../README.md)

Scripts that compute developer AI maturity from the anonymous Developer Survey.

## Contents

| File | Purpose |
| --- | --- |
| [rubric.py](rubric.py) | Deterministic rubric across `DS-D2` to `DS-D8`. Maps answers (from Forms in EN, PT-BR or ES, through [../options.json](../options.json)) to scores. The score bands match the v1 survey rubric. |
| [calculate_maturity.py](calculate_maturity.py) | Reads `survey-devs/responses-devs.json` and generates `output/developer-survey-maturity-<date>.json` with `DS-D#` keys. |
| [generate_insights.py](generate_insights.py) | Generates `output/insights-developer-survey-<date>.md`. Section 12 links survey signals to v2 questions. English by default; pass `--lang pt-br` or `--lang es`. Option tables are shown in the report language. |

## Usage

```bash
python3 survey-devs/scripts/calculate_maturity.py
python3 survey-devs/scripts/generate_insights.py
python3 survey-devs/scripts/generate_insights.py --lang pt-br
python3 survey-devs/scripts/generate_insights.py --lang es
```

Survey outputs are context for v2 reports. They never change v2 scores.
