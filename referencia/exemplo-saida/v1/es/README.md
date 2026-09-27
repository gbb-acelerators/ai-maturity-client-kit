# Ejemplo de salida — Español

Versión en **Español** de los 5 PDFs de referencia generados a partir de `respostas.json.example` (Cliente Exemplo S.A., locale forzado a `es`).

## PDFs incluidos

- `score_justification.pdf`: Justificación de Puntuación
- `roadmap_part_pillar_p1.pdf`: Roadmap Parte 1, Productividad del Desarrollador
- `roadmap_part_pillar_p2.pdf`: Roadmap Parte 2, Ciclo de Vida DevOps
- `roadmap_part_pillar_p3.pdf`: Roadmap Parte 3, Plataforma de Aplicaciones
- `roadmap_part4.pdf`: Guía de Implementación

## Cómo regenerar

```bash
python3 relatorios/scripts/render_reports.py \
  --payload referencia/exemplo-saida/payload.json \
  --locale es \
  --out referencia/exemplo-saida/es
```

Para generar informes reales en Español, define `metadata.language` como `"es"` en `respostas.json` y ejecuta `/gerar-relatorio`.
