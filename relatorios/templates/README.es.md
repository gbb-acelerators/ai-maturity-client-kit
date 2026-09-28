# `relatorios/templates/`

🌐 [English](README.md) · [Português (Brasil)](README.pt-br.md) · Español

📖 **Navegación:** [🏠 Índice](../../README.es.md) · [« Informes](../README.es.md)

Plantillas Jinja2 para PDFs de informes. Coordina los cambios porque afectan a todos los clientes que usan el kit.

## Contenido

| Archivo | Renderiza |
| --- | --- |
| [`v2_assessment_summary.html.j2`](v2_assessment_summary.html.j2) | `v2_assessment_summary.pdf`: resumen ejecutivo, puntuación, prioridades, verificaciones cruzadas de evidencia y contexto de Developer Survey cuando está disponible. |
| [`v2_roadmap_group.html.j2`](v2_roadmap_group.html.j2) | PDFs de roadmap de grupo G1, G2 y G3. |
| [`v2_implementation_guide.html.j2`](v2_implementation_guide.html.j2) | `v2_implementation_guide.pdf`: gobernanza, responsables de dimensiones, RACI, plan faseado, gestión del cambio, riesgos, métricas, primeros 90 días y referencias. |
| [`v2_round_comparison.html.j2`](v2_round_comparison.html.j2) | `comparacao-rodadas.pdf` desde `scripts/compare_rounds.py --pdf`. |
| [`_v2_components.html.j2`](_v2_components.html.j2) | Macros v2 compartidas. |
| [`_print.css`](_print.css) | CSS de impresión con el tratamiento visual de cuatro cuadrados de Microsoft. |
| Plantillas legacy | Plantillas de informes v1 archivadas usadas solo por el dispatch v1. |

## Cómo personalizar

> [!CAUTION]
> Editar archivos `.html.j2` afecta a todos los clientes que usan el kit. Para personalización por cliente, edita `implementation-guide-inputs.json` o vuelve a ejecutar el wizard, luego renderiza de nuevo.

Si cambias plantillas:

1. Ejecuta `make smoke`.
2. Ejecuta `make validate-docs`.
3. Compara con las salidas en [../../referencia/exemplo-saida/](../../referencia/exemplo-saida/).

## Variables clave consumidas

Cada plantilla espera campos de `payload_v2.json`. La guía de implementación lee campos normalizados del wizard desde `relatorios/scripts/wizard_inputs.py`; los valores vacíos se renderizan como `to fill with the client`.

## i18n

Las cadenas localizables viven en [../i18n/](../i18n/) (`en.json`, `es.json`, `pt-br.json`). Las plantillas las leen mediante `{{ t('key') }}`.
