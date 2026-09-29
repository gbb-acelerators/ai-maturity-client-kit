# `reference/sample-output/v1/es/`

📖 **Navegación:** [🏠 Índice](../../../../README.es.md) · [« Carpeta de ejemplos](../../README.es.md)

Versión en **español** de los 5 PDFs de referencia archivados de framework v1, generados a partir del payload de ejemplo v1 (Cliente Exemplo S.A., locale forzado a `es`).

## Contenido

| Archivo | Descripción |
|---|---|
| `score_justification.pdf` | Justificación de puntuación |
| `roadmap_part_pillar_p1.pdf` | Roadmap parte 1, pilar Productividad del desarrollador |
| `roadmap_part_pillar_p2.pdf` | Roadmap parte 2, pilar Ciclo de vida DevOps |
| `roadmap_part_pillar_p3.pdf` | Roadmap parte 3, pilar Plataforma de aplicaciones |
| `roadmap_part4.pdf` | Guía de implementación consolidada |

## Cuándo usarlo

- Mostrar a un cliente cómo se ven los PDFs v1 en español (`"language": "es"` en `responses.json::metadata`).
- Verificar que las plantillas manejan bien textos más largos.

> [!NOTE]
> Los PDFs v1 en PT-BR están en la carpeta superior, [`../`](../). Los de inglés están en [`../en/`](../en/).

## Cómo regenerarlo

```bash
python3 reports/scripts/render_reports.py \
  --payload reference/sample-output/v1/payload.json \
  --locale es \
  --out reference/sample-output/v1/es
```
