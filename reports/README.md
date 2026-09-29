# `reports/`: report rendering

🌐 English · [Português (Brasil)](README.pt-br.md) · [Español](README.es.md)

The report dispatcher supports v2 by default and v1 for archived inputs.

## Run

```bash
python3 reports/scripts/build_payload_and_render.py
```

The script reads `responses.json::metadata.framework_version` and dispatches automatically. `make pipeline` runs scoring, workbook generation, payload building, and rendering.

## v2 outputs

- `output/payload_v2.json`
- `output/v2_assessment_summary.pdf`
- `output/v2_roadmap_g1.pdf`, D1, D2, D9.
- `output/v2_roadmap_g2.pdf`, D3, D4, D5.
- `output/v2_roadmap_g3.pdf`, D6, D7, D8.
- `output/v2_implementation_guide.pdf`.

The summary includes section 2.2 Evidence cross-checks when `output/repo-scan.json` or `output/telemetry.json` exists, and Developer Survey context when `output/developer-survey-maturity-*.json` exists. The implementation guide uses `implementation-guide-inputs.json`; empty wizard fields render as `to fill with the client`.

## Comparison reports

`make compare BEFORE=old.json AFTER=responses.json` calls `scripts/compare_rounds.py --pdf` and writes `output/round-comparison.pdf`. It supports v2 to v2, v1 to v2 indicative baseline through v1 lineage, and v1 to v1.

## v1 archive

v1 inputs still render the archived 5 PDF set. Do not point new assessment docs to v1 pillar PDFs unless the input is v1.

## Localization

PDF language comes from `responses.json::metadata.language`: `en`, `pt-BR`, or `es`. PT-BR and ES PDFs use comma decimals.
