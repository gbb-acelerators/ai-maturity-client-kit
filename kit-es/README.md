# Kit AI Maturity Assessment

Este paquete en español usa framework v2 por defecto. v1 sigue archivado y soportado para entradas historicas.

## Contenido

- Assessment v2 principal: 5 preguntas de perfil, 61 preguntas puntuadas, 9 dimensiones.
- Formulario offline v2: [../formularios/assessment-v2.html](../formularios/assessment-v2.html).
- Instrucciones Forms: [INSTRUCCIONES-FORMS.md](INSTRUCCIONES-FORMS.md).
- Guia paso a paso: [PASO-A-PASO.md](PASO-A-PASO.md).
- Scripts deterministicos en [../scripts/](../scripts/).

## Ejecutar

```bash
make init
make import XLSX=respostas-forms.xlsx
make scores
make workbook
make pipeline
```

Las salidas v2 incluyen `scores.json`, `gaps.json`, `recomendacoes.json`, `pontuacao-v2-<date>.xlsx`, `payload_v2.json` y 4 PDFs: summary mas roadmaps G1, G2 y G3.

## Archivo v1

Usa `make init-v1` solo para assessments v1 archivados. v1 usa 158 preguntas, 3 pilares y activos en [../coleta/v1/](../coleta/v1/), [../formularios/v1/](../formularios/v1/) y [../referencia/v1/](../referencia/v1/).
