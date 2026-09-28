# `relatorios/`: renderización de informes

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

El dispatcher de informes admite v2 por defecto y v1 para entradas archivadas.

## Ejecutar

```bash
python3 relatorios/scripts/build_payload_and_render.py
```

El script lee `respostas.json::metadata.framework_version` y despacha automáticamente. `make pipeline` ejecuta puntuación, generación de workbook, construcción de payload y renderización.

## Salidas v2

- `saida/payload_v2.json`
- `saida/v2_assessment_summary.pdf`
- `saida/v2_roadmap_g1.pdf`, D1, D2, D9.
- `saida/v2_roadmap_g2.pdf`, D3, D4, D5.
- `saida/v2_roadmap_g3.pdf`, D6, D7, D8.
- `saida/v2_implementation_guide.pdf`.

El resumen incluye la sección 2.2 Verificaciones cruzadas de evidencia cuando existe `saida/repo-scan.json` o `saida/telemetria.json`, y contexto de Developer Survey cuando existe `saida/maturidade-developer-survey-*.json`. La guía de implementación usa `implementation-guide-inputs.json`; los campos vacíos del wizard se renderizan como `to fill with the client`.

## Informes de comparación

`make compare BEFORE=old.json AFTER=respostas.json` llama a `scripts/compare_rounds.py --pdf` y escribe `saida/comparacao-rodadas.pdf`. Soporta v2 a v2, baseline indicativo v1 a v2 mediante linaje v1, y v1 a v1.

## Archivo v1

Las entradas v1 todavía renderizan el conjunto archivado de 5 PDFs. No apuntes docs de evaluaciones nuevas a PDFs de pilares v1 a menos que la entrada sea v1.

## Localización

El idioma del PDF viene de `respostas.json::metadata.language`: `en`, `pt-BR` o `es`. Los PDFs PT-BR y ES usan decimales con coma.
