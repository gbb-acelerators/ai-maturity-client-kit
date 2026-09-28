# Cómo crear Microsoft Forms para el AI Maturity Assessment (v2)

🌐 [English](INSTRUCOES-FORMS.md) · [Português (Brasil)](INSTRUCOES-FORMS.pt-br.md) · Español

**`ASSESSMENT`** · 📖 [🏠 Índice](../README.es.md) · [« Guía paso a paso](../GUIA-PASSO-A-PASSO.es.md) · Estás aquí · [» Survey-devs](../survey-devs/INSTRUCOES-FORMS-DEVS.es.md)

> [!TIP]
> Framework v2 tiene **5 preguntas de perfil y 61 preguntas puntuadas en 9 dimensiones** (127 elementos de Forms, cerca de 25 a 40 minutos por persona). Las instrucciones v1 (158 preguntas) están archivadas en [v1/INSTRUCOES-FORMS.md](v1/INSTRUCOES-FORMS.md).

## Comparación rápida de los 4 caminos

| Camino | Tiempo de setup | Cuándo usar |
| --- | --- | --- |
| **A. Microsoft Forms completo** | 60 a 90 minutos | Varias personas por rol; quieres resultados por persona y flag de brecha de percepción. |
| **B. Piloto con una dimensión** | 15 minutos | Validar redacción y duración con 3 a 5 personas antes del lanzamiento completo. |
| **C. Template Excel o SharePoint** | 5 minutos | Workshops, o cuando Forms no está disponible: una fila por persona en [template-export-forms.xlsx](template-export-forms.xlsx). |
| **D. Formulario HTML offline** | Ninguno | Una persona por vez, sin Microsoft 365: [formularios/assessment-v2.html](../formularios/assessment-v2.es.html) exporta un `respostas.json` por persona. |

## Camino A: Microsoft Forms completo

1. Abre el banco de preguntas en tu idioma: [perguntas-para-forms.en.md](perguntas-para-forms.en.md) (EN), [perguntas-para-forms.md](perguntas-para-forms.md) (PT-BR) o [perguntas-para-forms.es.md](perguntas-para-forms.es.md) (ES). Los tres son generados desde [framework.v2.json](../framework.v2.json) y tienen las mismas preguntas, opciones, anclas y notas de alcance.
2. Ve a <https://forms.office.com>, crea un formulario en blanco y nómbralo `AI-Assisted SDLC Maturity Assessment v2 - <Organización>`.
3. Pega el [aviso de privacidad](#aviso-de-privacidad-pégalo-en-la-descripción-del-formulario) en la descripción del formulario y llena los corchetes.
4. Agrega **10 secciones**: Sección 0 (perfil) y D1 a D9.
5. Sección 0: agrega `R-Q1` a `R-Q5` como **Opción**. Activa **Múltiples respuestas** solo para `R-Q3`.
6. Para cada pregunta puntuada agrega:
   - una **Opción** (respuesta única) cuyo título comienza con el ID y dos puntos, por ejemplo `D4-Q3: Are well-scoped tasks delegated ...`;
   - las 6 opciones, en orden, manteniendo el prefijo `L0` a `L4` y `NA` al inicio;
   - las líneas **L3 looks like** y **L4 looks like**, y la **Scope note** cuando la pregunta tenga una, en el subtítulo;
   - un **Texto largo** opcional con el título exacto `Evidence (D4-Q3)`.
7. Opcional: en `...` > `Branching`, permite que personas que respondan Executive o Product / program manager en `R-Q1` salten D4 a D7. Las preguntas saltadas cuentan como no respondidas, no como `NA`.
8. `Settings`: restringe a tu organización, o usa `Anyone can respond` si compartes por link.
9. Comparte el link. Busca **al menos 3 personas por rol**: los resúmenes por persona marcan grupos menores como muestra baja, y las flags de brecha de percepción y divergencia entre personas encuestadas necesitan suficientes respuestas para ser útiles.
10. Cuando haya respuestas: `Responses` > `Open in Excel`, descarga el archivo y ejecuta:

    ```bash
    make import XLSX=respostas-forms.xlsx
    make pipeline
    ```

> [!IMPORTANT]
> El importador encuentra cada columna por el ID al inicio del título (`D1-Q1:`, `R-Q1:`) y cada columna de evidencia por `Evidence (<ID>)`. Detecta v2 a partir de esos IDs. No traduzcas el rótulo `Evidence (<ID>)` ni los prefijos de opciones.

## Camino B: Piloto con una dimensión

Crea el formulario con la Sección 0 y una dimensión. D4 es un buen comienzo porque tiene 8 preguntas. Recolecta 3 a 5 respuestas, luego ejecuta:

```bash
python3 scripts/import_forms_excel.py <file> --allow-partial
```

El engine reporta cobertura `BLOCKED` porque hay menos de 25 preguntas respondidas. Usa el piloto solo para revisar redacción y duración.

## Camino C: Template Excel o SharePoint

1. Copia [template-export-forms.xlsx](template-export-forms.xlsx) a SharePoint o OneDrive. Su fila de encabezado tiene el formato exacto del export de Forms: columnas de perfil, columnas de respuesta `D#-Q#` y columnas `Evidence (D#-Q#)`.
2. Cada persona llena una fila. Las respuestas deben empezar con `L0` a `L4` o `NA`. `R-Q3` acepta varias opciones separadas por `;`.
3. Descarga el archivo y ejecuta `make import XLSX=<file>`.

Un ejemplo lleno y sintético es [v2-mock-forms-export.xlsx](v2-mock-forms-export.xlsx) (14 personas ilustrativas; no es un cliente real).

## Camino D: Formulario HTML offline más merge

Usa este camino cuando las personas encuestadas no puedan acceder a Microsoft Forms o cuando necesites un flujo rápido de workshop.

1. Envía [../formularios/assessment-v2.html](../formularios/assessment-v2.es.html) a cada persona, o ábrelo desde el repositorio.
2. El formulario se ejecuta offline, soporta EN, PT-BR y ES, muestra la nota de alcance de cada pregunta y exporta una persona por `respostas.json`.
3. Recolecta los archivos exportados en una carpeta, por ejemplo `exports/`.
4. Une los archivos:

   ```bash
   make merge DIR=exports/
   ```

El script de merge asigna IDs únicos `R01`, `R02` y así sucesivamente. Rechaza archivos v1 y organizaciones mixtas excepto cuando pasas `--org` o `--allow-mixed-org` a `scripts/merge_offline_respostas.py`. Hace backup de un `respostas.json` existente antes de escribir el archivo unido.

Luego ejecuta:

```bash
make pipeline
```

## Aviso de privacidad (pégalo en la descripción del formulario)

```text
Esta evaluación pregunta sobre prácticas de ingeniería, no sobre desempeño individual.
Recolectamos tu rol, el alcance de tus respuestas, las herramientas de IA que usas, tus años de experiencia y tu tiempo hands-on, para que los resultados puedan mostrarse por rol.
Controlador: [organización]. Finalidad: diagnóstico de madurez en IA y roadmap.
Acceso: [nombres o equipo]. Retención: [período], luego eliminación.
Los resultados se reportan de forma agregada; grupos con menos de 3 personas se marcan como muestra baja.
Preguntas o solicitudes de eliminación: [contacto].
```

Alinea estos puntos con tu equipo de privacidad o legal antes del lanzamiento (LGPD / GDPR); esta lista no es asesoría legal:

- **Minimización:** el formulario no necesita nombre ni email. Si Forms los recolecta automáticamente, desactívalo o restringe el acceso al export.
- **Almacenamiento:** mantén `.xlsx`, `respostas.json` y `saida/` en almacenamiento administrado con acceso restringido. `respostas.json` y `saida/` están en `.gitignore`; nunca hagas commit de ellos.
- **Retención y eliminación:** elimina las respuestas de Forms y los archivos exportados cuando termine el período de retención.

## Cómo las respuestas se convierten en scores

El engine ([scripts/assessment_engine.py](../scripts/assessment_engine.py)) sigue la sección 8 de [AI-Maturity-Form-Questions_v2.es.md](AI-Maturity-Form-Questions_v2.es.md): media agrupada por pregunta, media por dimensión, media ponderada de dimensiones, bandas de nivel semiabiertas, y flags de baja confianza, riesgo de amplificación, brecha de percepción, divergencia entre personas encuestadas, alcance, L3/L4 sin verificación y cobertura de evidencia.

Los cross-checks opcionales de evidencia vienen de `make scan-repos` y `make telemetry`. Aparecen en el PDF de resumen y se listan como riesgos en la guía de implementación cuando desafían una respuesta.

## Solución de problemas

| Síntoma | Corrección |
| --- | --- |
| `No column header starts with a question ID` | Los títulos de preguntas no comienzan con `D1-Q1:`. Renómbralos en Forms y exporta de nuevo. |
| `Only N of 61 v2 questions were found` | Algunos títulos perdieron el ID. Usa `--allow-partial` solo para piloto. |
| `unrecognized value at R-Q1` | Se editó el texto de la opción. Usa el texto exacto del banco de preguntas (cualquiera de los 3 idiomas se acepta). |
| Heatmap de persona dice muestra baja | Menos de 3 personas en ese rol. Invita a más personas o lee esa columna con cuidado. |
| `make merge` rechaza un archivo | Verifica si es un export v1 o si la organización difiere de los otros exports. |
