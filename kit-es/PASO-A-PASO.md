# Paso a paso

[English](../kit-en/STEP-BY-STEP.md) | Español

Este guia ejecuta el assessment v2 desde la recoleccion hasta los reportes. v1 sigue disponible para entradas archivadas.

## 1. Elige el flujo

Usa v2 para nuevos assessments. Usa v1 solo para comparacion historica o archivos `respostas.json` sin `metadata.framework_version`.

- Especificacion v2: [../coleta/AI-Maturity-Form-Questions_v2.md](../coleta/AI-Maturity-Form-Questions_v2.md).
- Formulario v2: [../formularios/assessment-v2.html](../formularios/assessment-v2.html).
- Instrucciones Forms v2: [../coleta/INSTRUCOES-FORMS.md](../coleta/INSTRUCOES-FORMS.md).
- Archivo v1: [../coleta/v1/](../coleta/v1/), [../formularios/v1/](../formularios/v1/), [../referencia/v1/](../referencia/v1/).

## 2. Prepara entradas

```bash
make init
```

Esto copia `respostas.v2.json.example` a `respostas.json` si el archivo no existe.

Tambien puedes importar una exportacion de Microsoft Forms:

```bash
make import XLSX=respostas-forms.xlsx
```

El importador detecta v2 por encabezados como `R-Q1:` y `D4-Q3:`. Detecta v1 por los IDs archivados.

## 3. Entiende v2

- 5 preguntas de perfil: `R-Q1` a `R-Q5`.
- 61 preguntas puntuadas: `D#-Q#`.
- 9 dimensiones: D1 Estrategia, Politica y Gobernanza de IA; D2 Habilitacion, Habilidades y Cultura; D3 Planificar, Especificar y Disenar; D4 Codigo e Ingenieria de Contexto; D5 Revision, Calidad y Pruebas; D6 Seguridad y Cadena de Suministro de IA; D7 Entregar y Operar; D8 Fundamentos de Ingenieria; D9 Medicion, Valor y AI FinOps.
- Niveles: L0 No iniciado, L1 Explorando, L2 Adoptando, L3 Escalando, L4 Nativo en IA, mas `NA`.

## 4. Ejecuta scoring deterministico

```bash
make scores
```

No calcules scores a mano. El motor escribe `saida/scores.json`, `saida/gaps.json` y `saida/recomendacoes.json`.

## 5. Crea la planilla

```bash
make workbook
```

Para v2 se genera `saida/pontuacao-v2-<date>.xlsx`, con formulas y columna de verificacion del motor.

## 6. Genera reportes

```bash
make pipeline
```

Archivos v2: `v2_assessment_summary.pdf`, `v2_roadmap_g1.pdf`, `v2_roadmap_g2.pdf`, `v2_roadmap_g3.pdf` y `payload_v2.json`.

## 7. Compara rondas

```bash
make compare BEFORE=old-respostas.json AFTER=respostas.json
```

Soporta v2 a v2, v1 a v1 y comparacion indicativa v1 a v2 via `v1_lineage`.

## 8. Surveys complementarios

Developer Survey y Learning and Growth Survey no cambiaron. Contextualizan v2 D2, D5 y D9. Si mencionas dimensiones del Developer Survey junto a las del assessment, usa `DS-D#`.

Consulta [../CHANGELOG.md](../CHANGELOG.md) para el historial.
