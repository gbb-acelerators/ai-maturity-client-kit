# `reports/scripts/`

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

📖 **Navegación:** [🏠 Índice](../../README.es.md) · [« Informes](../README.es.md)

Scripts de Python que construyen payloads y renderizan los informes PDF con Jinja2 y WeasyPrint.

## Contenido

| Archivo | Propósito |
| --- | --- |
| [`build_payload_and_render.py`](build_payload_and_render.py) | Dispatcher principal. Detecta v1 o v2 desde `responses.json`, construye `payload_v2.json`, incluye contexto de encuestas, verificaciones cruzadas de evidencia y entradas del wizard, luego renderiza. `--payload` no es necesario para el flujo estándar. |
| [`build_report_v2.py`](build_report_v2.py) | Renderizador v2 para los 5 PDFs: resumen, G1, G2, G3 y guía de implementación. |
| [`wizard_inputs.py`](wizard_inputs.py) | Parser compartido para `implementation-guide-inputs.json`. Acepta los 11 campos v2 y permite que la Parte 4 v1 ignore campos adicionales. Los campos vacíos se renderizan como `to fill with the client`. |
| [`render_reports.py`](render_reports.py) | Renderizador Jinja2 a WeasyPrint de nivel inferior usado por el dispatcher. |
| [`branding.py`](branding.py) | Logo de cuatro cuadrados de Microsoft, colores oficiales, cadena de rol y contacto solo por email para PDFs y helpers HTML. |
| [`render_smoke.py`](render_smoke.py) | Renderizador smoke para una revisión pequeña de PDF. |

## Pipeline visual

```mermaid
flowchart LR
    A[responses.json] --> M[build_payload_and_render.py]
    B[output/scores.json] --> M
    C[output/gaps.json] --> M
    D[output/recommendations.json] --> M
    E[implementation-guide-inputs.json] --> M
    F[output/repo-scan.json optional] --> M
    G[output/telemetry.json optional] --> M
    I[output/dora-metrics.json optional] --> M
    H[output/developer-survey-maturity-*.json optional] --> M
    M --> P[output/payload_v2.json]
    P --> R[build_report_v2.py]
    R --> O[5 v2 PDFs in output/]
```

## Uso

```bash
# Render completo del informe después de la puntuación
python3 reports/scripts/build_payload_and_render.py

# Construir solo el payload
python3 reports/scripts/build_payload_and_render.py --no-render

# Target end-to-end estándar
make pipeline
```

Usa `make compare BEFORE=old.json AFTER=responses.json` para `output/round-comparison.pdf`; usa los estilos de informe v2.

## Dependencias

```bash
pip install jinja2 weasyprint openpyxl
# o
make install-deps
```

> [!NOTE]
> WeasyPrint necesita bibliotecas del sistema (Cairo, Pango). En macOS: `brew install pango`. En Linux/WSL: instala el paquete `libpango-1.0-0`.
