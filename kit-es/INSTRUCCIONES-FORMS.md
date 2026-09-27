# Instrucciones para Microsoft Forms

Este archivo documenta la seccion principal del assessment con framework v2. Los surveys complementarios no cambiaron.

## Forma A: AI Maturity Assessment v2

Usa los activos v2:

- Especificacion: [../coleta/AI-Maturity-Form-Questions_v2.md](../coleta/AI-Maturity-Form-Questions_v2.md).
- Banco generado: [../coleta/perguntas-para-forms.es.md](../coleta/perguntas-para-forms.es.md).
- Formulario offline: [../formularios/assessment-v2.html](../formularios/assessment-v2.html).
- Plantilla de importacion: [../coleta/template-export-forms.xlsx](../coleta/template-export-forms.xlsx).

Crea preguntas de perfil `R-Q1` a `R-Q5`, luego las 61 preguntas puntuadas `D#-Q#`. Mantenga cada titulo empezando con su ID, por ejemplo `D4-Q3: ...`. El importador usa esos IDs.

Opciones para cada pregunta puntuada:

- `L0 - No iniciado: ...`
- `L1 - Explorando: ...`
- `L2 - Adoptando: ...`
- `L3 - Escalando: ...`
- `L4 - Nativo en IA: ...`
- `NA`

Despues de exportar desde Forms, ejecuta:

```bash
python3 scripts/import_forms_excel.py respostas-forms.xlsx
python3 scripts/assessment_engine.py all
```

## Archivo v1

No crees nuevos formularios v1 salvo para comparacion historica. Los activos v1 estan en [../coleta/v1/](../coleta/v1/) y [../formularios/v1/](../formularios/v1/).
