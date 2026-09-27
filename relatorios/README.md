# `relatorios/`: report rendering

The report dispatcher supports v2 by default and v1 for archived inputs.

## Run

```bash
python3 relatorios/scripts/build_payload_and_render.py
```

The script reads `respostas.json::metadata.framework_version` and dispatches automatically.

## v2 outputs

- `saida/payload_v2.json`
- `saida/v2_assessment_summary.pdf`
- `saida/v2_roadmap_g1.pdf`, D1, D2, D9.
- `saida/v2_roadmap_g2.pdf`, D3, D4, D5.
- `saida/v2_roadmap_g3.pdf`, D6, D7, D8.

## v1 archive

v1 inputs still render the archived 5 PDF set. Do not point new assessment docs to v1 pillar PDFs unless the input is v1.

## Localization

PDF language comes from `respostas.json::metadata.language`: `en`, `pt-BR`, or `es`.
