# Instrucciones Microsoft Forms · Edición Español

> Cómo publicar las 3 encuestas como Microsoft Forms y agregar las respuestas de vuelta al kit.

🏠 [README](README.md) · 📘 [Paso a paso](PASO-A-PASO.md) · 🇧🇷 [PT-BR](../coleta/INSTRUCOES-FORMS.md)

---

## ¿Por qué Microsoft Forms?

Las 3 encuestas HTML en `formularios/` son convenientes para llenado individual, pero generalmente quieres **múltiples respondentes** (3-5 del liderazgo, 5+ devs anónimos, 3+ devs identificados para learning). Microsoft Forms lo facilita:

- ✅ Recolección multi-respondente nativa
- ✅ Exportación a Excel con todas las respuestas en un archivo
- ✅ Modo anónimo (para el Developer Survey)
- ✅ Validación de campos obligatorios
- ✅ Mobile-friendly

## Forma A · AI Maturity Assessment (158 preguntas)

### Crea el form

1. Ve a <https://forms.office.com> y crea un nuevo form.
2. Usa el banco de preguntas en `coleta/perguntas-para-forms.es.md` (Español, runtime-safe). El banco canónico PT-BR también está disponible en `coleta/perguntas-para-forms.md`.
3. Para cada pregunta:
   - Tipo **Elección** con 5 opciones: `L0 (Inicial)`, `L1 (En Desarrollo)`, `L2 (Definido)`, `L3 (Gestionado)`, `L4 (Optimizando)`.
   - Agrega un **Texto largo** opcional para evidencia/comentarios.
4. Usa **Secciones** para agrupar por pilar (P1, P2, P3).
5. Tiempo recomendado de llenado: 60-90 minutos para la encuesta completa, o distribuir entre líderes por pilar.

### Recolecta respuestas

1. Comparte el link con **3 a 5 miembros del liderazgo**.
2. Espera hasta que cierre la ventana de respuestas.
3. Haz clic en **Abrir en Excel** → guarda como `respostas-forms.xlsx` en la raíz del workspace.

### Agrega al kit

```text
/importar-respostas-excel
```

La skill calcula el **promedio simple por pregunta** entre todos los respondentes (mismo comportamiento que la plataforma de producción) y escribe `respostas.json` listo para `/pipeline-completo`.

## Forma B · Developer Survey (75 preguntas, anónimo)

1. Crea el form usando preguntas de `survey-devs/perguntas-para-forms-devs.es.md` (Español, runtime-safe). El banco canónico PT-BR también está disponible en `survey-devs/perguntas-para-forms-devs.md`.
2. En **Configuración**: habilita **respuestas anónimas** (NO requieras email ni login).
3. Comparte con todos los desarrolladores en alcance (5+ mínimo recomendado).
4. Exporta como `respostas-survey-devs.xlsx` a la raíz del workspace.
5. Ejecuta:

```text
/importar-survey-devs
/insights-developer-survey
```

Output: `saida/insights-developer-survey-<FECHA>.md` con métricas de adopción, gaps de gobernanza, quotes anonimizadas y recomendaciones vinculadas a las capabilities de madurez.

## Forma C · Learning & Growth Survey (32 preguntas, identificado)

> [!IMPORTANT]
> Esta encuesta requiere **nombre + email** porque el output incluye listas de inscritos, asignación a cohorts y pares mentor↔mentee. Asegúrate de que los participantes consientan esto previamente.

1. Crea el form usando preguntas de `survey-learning/perguntas-para-forms-learning.es.md` (Español). El banco canónico PT-BR también está disponible en `survey-learning/perguntas-para-forms-learning.md`.
2. En **Configuración**: requiere **nombre y email** como campos obligatorios. Deshabilita el modo anónimo.
3. Comparte con todos los desarrolladores que recibirán capacitación (3+ mínimo recomendado).
4. Exporta como `respostas-survey-learning.xlsx` a la raíz del workspace.
5. Ejecuta:

```text
/importar-survey-learning
/plano-capacitacao
```

Output: `saida/plano-capacitacao-<FECHA>.md` con top 10 temas demandados, cohorts por dimensión D2-D8 con nombres de inscritos, candidatos a Champions Network, pares mentor↔mentee y calendario 90 días de talleres.

## Workflow recomendado

Para engagements de consultoría seria, ejecuta las 3 en este orden:

```text
1. Encuesta B (devs anónimos)       → baseline comportamental
2. Encuesta C (devs identificados)  → roadmap de capacitación con inscritos
3. Encuesta A (liderazgo)           → assessment organizacional informado
4. /wizard-implementacao             → cruza validación y auto-llena el Implementation Guide
5. /pipeline-completo                → genera los 5 PDFs finales
```

Esta secuencia hace que el assessment del liderazgo sea **informado por datos** en vez de aspiracional, y produce un plan de capacitación con nombres concretos.

## Traducir las preguntas

Las 3 encuestas ya tienen bancos runtime-safe en Inglés y Español:

- `coleta/perguntas-para-forms.en.md`
- `coleta/perguntas-para-forms.es.md`

- `survey-devs/perguntas-para-forms-devs.en.md`
- `survey-devs/perguntas-para-forms-devs.es.md`
- `survey-learning/perguntas-para-forms-learning.en.md`
- `survey-learning/perguntas-para-forms-learning.es.md`

Puedes:

- **Traducir para los respondentes** en Microsoft Forms manteniendo los IDs en los títulos — el Excel exportado se parsea correctamente.
- **Mantener los IDs sin cambios** en los títulos de Microsoft Forms y en el JSON de salida — los PDFs se renderizan en Español vía `relatorios/i18n/es.json`.

Si quieres un banco de preguntas totalmente traducido, contacta a Paula Silva en [LinkedIn](https://linkedin.com/in/paulanunes).

## ¿Atascado en algún paso?

| Problema | Solución |
| --- | --- |
| Las columnas del Excel no coinciden con los IDs | Verifica que no reordenaste preguntas en Forms — los IDs son posicionales |
| `/importar-respostas-excel` falla | Asegúrate que el archivo está en la raíz y se llama exactamente `respostas-forms.xlsx` |
| Faltan respuestas anónimas para encuesta C | La encuesta C requiere nombre+email — re-publica sin modo anónimo |
| Respuestas vacías rompen la agregación | La skill salta celdas vacías; déjalas en blanco en vez de poner "N/A" |

## Continuar leyendo

| ⬅ Anterior | Siguiente ➡ |
| :--- | ---: |
| [📘 Paso a paso](PASO-A-PASO.md) | [🌐 Sitio](https://paulasilvatech.github.io/ai-maturity-client-kit/es/) |

---

**Paula Silva** — Global Developer Solutions Advisor | [LinkedIn](https://linkedin.com/in/paulanunes)
