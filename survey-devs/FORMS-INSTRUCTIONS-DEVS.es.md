# Cómo crear el Microsoft Forms para el Developer Survey

🌐 [English](FORMS-INSTRUCTIONS-DEVS.md) · [Português (Brasil)](FORMS-INSTRUCTIONS-DEVS.pt-br.md) · Español

**`🅱️ SURVEY-DEVS`** · _anónimo_ · 📖 [🏠 Índice](../README.es.md) · [« Recolección principal](../collection/FORMS-INSTRUCTIONS.es.md) · Estás aquí · [» Learning Survey](../survey-learning/FORMS-INSTRUCTIONS-LEARNING.es.md)

> [!IMPORTANT]
> Encuesta **anónima** de **75 preguntas** en 9 secciones para entender cómo los desarrolladores de tu organización usan GitHub Copilot, modos de Copilot Chat (Ask/Edit/Agent/**Coding Agent**), **Copilot Spaces**, **Microsoft Foundry**, agentes IA + **MCP / A2A**, instruction files, prácticas (TDD/SDD con Spec Kit), **personas Agentic DevOps** (System Designer / Agent Operator), gobernanza y seguridad (incl. **JIT permissions** y **alcance+red-lines de agentes**). Tiempo estimado por persona encuestada: **20-25 min**.

**Versión 2.0 (2026-05-08)**: términos actualizados con la documentación oficial más reciente de Microsoft/GitHub.

**Diferente de la evaluación principal** (Likert L0-L4 organizacional). Esta es **individual y conductual**: cuantas más personas desarrolladoras respondan, más rica será la imagen.

---

## 🎯 Cuándo usar esta encuesta

- ✅ Antes de definir una estrategia de adopción de IA para ingeniería
- ✅ Después de un rollout de GitHub Copilot, para medir la adopción real
- ✅ Como input para `/implementation-wizard` (Implementation Guide de la evaluación principal)
- ✅ Trimestralmente, para seguir la evolución cultural
- ✅ Antes de workshops de Copilot/AI, para identificar brechas

---

## 🔐 Anonimato: CRÍTICO

Esta encuesta es **anónima por diseño**:

- ❌ No pedimos nombre, email ni ID corporativo
- ✅ Solo recopilamos: cargo, años de experiencia, patrones de uso, opiniones
- ✅ Los desarrolladores responden con más honestidad cuando saben que es anónima
- ⚠️ En Microsoft Forms, **MARCA "Anonymous responses"** en Settings (sin eso, Forms captura el email de la cuenta MS365)

---

## 📋 Los 9 temas cubiertos (v2.0)

| # | Sección | Foco | Preguntas |
|---|---|---|---|
| **S1** | Perfil del encuestado | Cargo, experiencia, stack, modelo de trabajo | 7 |
| **S2** | GitHub Copilot: Adopción y Modos | Licencia, frecuencia, **Ask / Edit / Agent / Coding Agent (autónomo)**, features (incl. **Spaces**), ganancia | 9 |
| **S3** | Otras herramientas Microsoft / GitHub AI | **Microsoft Foundry** (antes Azure AI Foundry), **Foundry Agent Service**, **Copilot Spaces**, **Coding Agent**, GHAS, **Spec Kit**, **MCP** | 7 |
| **S4** | Prácticas de Desarrollo con IA | **TDD con IA**, **SDD con Spec Kit**, pair programming, refactoring, debugging, onboarding | 9 |
| **S5** | Conceptos y Estructura de Agentes | Agente vs asistente, modos Copilot, **custom agents/skills/prompts**, **A2A**, handoffs, subagentes, **personas Agentic DevOps** (System Designer / Agent Operator), **TESTEAR agents antes de usarlos** | 11 |
| **S6** | Markdown / Memory / Instructions | `copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`, custom instructions en **Spaces**, **Foundry Memory** | 6 |
| **S7** | Usabilidad y Best Practices | Cómo aprendieron (incl. MS Build / GitHub Universe), Champion, métricas DORA/DX, iteraciones, confianza | 9 |
| **S8** | Seguridad y Gobernanza | Política de IA, datos sensibles, GHAS, CodeQL, SBOM, **Microsoft Defender for DevOps**, DLP, audit, **alcance+red-lines de agents**, **JIT permissions**, entrenamiento | 13 |
| **S9** | Pain Points & Wishlist | Frustraciones, ideas, feature requests | 4 |
| | | **TOTAL** | **75** |

---

## 🛠️ Cómo crear el Forms (paso a paso)

### Paso 1 · Crear el formulario

1. Ve a <https://forms.office.com>
2. Haz clic en **+ New Form**
3. Título sugerido: `Developer Survey: Cómo mi equipo usa GitHub e IA hoy`
4. Subtítulo (pega esto):

```text
Encuesta ANÓNIMA (20-25 min) sobre tus prácticas con GitHub Copilot,
modos de Copilot Chat (Ask/Edit/Agent), agentes IA, instruction files,
mejores prácticas de IA + Dev, y seguridad.

Tus respuestas alimentarán el roadmap de adopción de IA del equipo.
NO pedimos nombre ni email, solo cargo, años de experiencia y patrones.

Tiempo estimado: 20-25 min.
```

### Paso 2 · ⚠️ CONFIGURAR ANONIMATO

**Settings (engranaje ⚙️ en la esquina superior derecha):**

| Setting | Valor |
|---|---|
| **Anonymous responses** | ☑ **MARCADO** (CRÍTICO: sin eso, Forms captura email) |
| **Who can respond** | "Anyone with the link" (si es cross-org) o "Only people in my organization" |
| **One response per person** | ☐ DESMARCADO (queremos múltiples) |
| **Accept responses** | ☑ MARCADO |
| **Email notification** | ☑ MARCADO (opcional: recibes aviso por cada respuesta) |
| **Customize thank you message** | "¡Gracias! Tus respuestas se están agregando con las del resto del equipo." |

> 🔍 **Cómo confirmar el anonimato:** después de crearlo, abre el enlace en una ventana privada. Si "Logged in as [tu email]" NO aparece arriba, es anónimo.

### Paso 3 · Crear 9 secciones

En Forms, botón **+ Add new** → icono de sección (o "Add section"):

```text
Section 1: S1 Perfil del encuestado                       (7 preguntas)
Section 2: S2 GitHub Copilot Adopción y Modos              (9 preguntas)
Section 3: S3 Otras herramientas Microsoft / GitHub AI     (7 preguntas)
Section 4: S4 Prácticas de Desarrollo con IA               (9 preguntas)
Section 5: S5 Conceptos y Estructura de Agentes            (11 preguntas)
Section 6: S6 Markdown / Memory / Instructions             (6 preguntas)
Section 7: S7 Usabilidad y Best Practices                  (9 preguntas)
Section 8: S8 Seguridad y Gobernanza                       (13 preguntas)
Section 9: S9 Pain Points & Wishlist                       (4 preguntas)
```

### Paso 4 · Agregar las 75 preguntas

Usa el banco en el idioma de las personas encuestadas como **fuente para copiar/pegar**: inglés [`question-bank-devs.md`](question-bank-devs.md), portugués [`question-bank-devs.pt-br.md`](question-bank-devs.pt-br.md) o español [`question-bank-devs.es.md`](question-bank-devs.es.md). Las opciones de respuesta están traducidas en cada banco; [`options.json`](options.json) las mapea de vuelta a las mismas opciones canónicas, así que los puntajes no dependen del idioma del formulario. Cada pregunta tiene:

- **Tipo** (`choice`, `multi`, `text`)
- **ID** (`S2-Q1`, `S5-Q3`, etc.)
- **Texto de la pregunta**
- **Opciones** (para choice/multi)

**Para cada pregunta en Forms:**

1. Tipo:
   - `choice` (Single answer) → **Choice** con "Multiple answers" DESMARCADO
   - `multi` (Multiple answers) → **Choice** con "Multiple answers" MARCADO
   - `text` (Long Text) → **Long answer**

2. **El TÍTULO de la pregunta DEBE comenzar con el ID + dos puntos**:

   ```text
   S2-Q1: ¿Tienes una licencia activa de GitHub Copilot?
   ```

   > ⚠️ **CRÍTICO:** el ID es usado por la skill `/import-survey-devs` para mapear de vuelta al schema. No quites ni cambies el formato `SX-QY:`.

3. **Opciones** (para choice/multi): pega las opciones listadas en el MD, **una por línea**, en orden.

4. **Required**: marca como required solo las 7 preguntas de Perfil (S1-Q1 a S1-Q7). Deja las demás opcionales (los desarrolladores pueden saltarlas).

### Paso 5 · Compartir

1. Botón **+ Send / Collect responses** arriba
2. Elige **Link** (no Email, que rompe el anonimato)
3. Copia la URL
4. Comparte vía:
   - **Slack/Teams:** canal #engineering o #copilot-users
   - **Email a todos los desarrolladores:** "Encuesta anónima de 20 min: tu opinión cuenta"
   - **All-hands:** proyecta un código QR de la URL para que los desarrolladores lo escaneen
5. **Deadline sugerido:** 2 semanas. Recuerda una vez por semana.

### Paso 6 · Seguir las respuestas

- La pestaña **Responses** muestra el conteo en tiempo real
- Recomendado: **al menos 5 personas encuestadas**, idealmente **15+** para insights ricos
- Si la participación es baja: 1-on-1s con líderes para incentivarla

### Paso 7 · Exportar cuando tengas suficientes respuestas

1. Pestaña **Responses** → botón **Open in Excel**
2. Guarda el archivo como **`survey-devs-responses.xlsx`**
3. Muévelo a la **raíz del kit** (no dentro de `survey-devs/`)
4. **Anonimato confirmado:** las columnas D (Email) y E (Name) deben estar vacías

### Paso 8 · Analizar con el kit

En Copilot Chat (modo Agent):

```text
/import-survey-devs
```

La skill:

- Detecta `survey-devs-responses.xlsx`
- Interpreta 75 preguntas × N personas encuestadas
- Genera `survey-devs/responses-devs.json`
- Genera `output/import-survey-log-<DATE>.md`

Luego:

```text
/insights-developer-survey
```

Genera un informe agregado en `output/insights-developer-survey-<DATE>.md` (en **inglés por defecto**; los scripts aceptan `--lang pt-br` para portugués (Brasil) y `--lang es` para español) con:

- Distribución por cargo
- Top 5 features de Copilot más usadas
- % de adopción por modo (Ask/Edit/Agent/Workspace)
- Conocimiento de conceptos (agentes, MCP, handoffs)
- Madurez de instruction files
- Brechas de gobernanza y seguridad
- Citas de pain points (anonimizadas)
- Recomendaciones priorizadas para el roadmap

---

## 🅱️ Ruta alternativa: Excel/SharePoint directo (sin Forms)

Más rápida si el equipo es pequeño (3-5 desarrolladores) y técnico.

1. Abre `survey-devs/template-export-forms-devs.xlsx`
2. Borra las 5 filas de personas encuestadas mock (filas 2-6) y conserva la fila 1 (headers)
3. Guarda como `survey-devs-responses.xlsx` y súbelo a SharePoint con un enlace "Anyone can edit"
4. Cada desarrollador completa **una fila** con sus respuestas (texto libre en las celdas de respuesta)
5. Cuando todos terminen: descarga → mueve a la raíz del kit → `/import-survey-devs`

**Trade-off:** menos visual que Forms, pero cero setup. Adecuado para equipos técnicos.

---

## 💡 Best practices de recolección

### Lanza con contexto

No sueltes el enlace en Slack sin contexto. Crea un momento:

> "Equipo, antes de definir la estrategia de IA para ingeniería del próximo trimestre, queremos escuchar cómo usan IA hoy. Encuesta anónima de 20-25 min con 75 preguntas (Copilot, agentes, seguridad y más). Sus respuestas van directo al roadmap. Link: <URL>. Deadline: 2 semanas."

### Garantiza anonimato (de verdad)

- Confirma que Settings → Anonymous esté MARCADO
- No fuerces login MS365 (si lo compartes externamente)
- En el informe agregado, nunca cites personas encuestadas específicas, solo patrones

### Recuerda periódicamente

- D+3: recordatorio amable en el canal
- D+7: recap "X respuestas hasta ahora, quedan Y días"
- D+10: 1-on-1s con líderes para impulsar
- D+14: deadline final + comienza el análisis

### Comparte los insights

Es más probable que los desarrolladores respondan la próxima encuesta si ven que la anterior llevó a acciones. Después de `/insights-developer-survey`:

- Preséntalo en un all-hands
- Genera quick wins (workshop, biblioteca de prompts, etc.)
- Repite trimestralmente para medir evolución

---

## 🆘 Troubleshooting

| Problema | Diagnóstico | Solución |
|---|---|---|
| La skill no detecta el archivo | No está en la raíz | Mueve `survey-devs-responses.xlsx` a la raíz del kit |
| La skill dice "0 respondents" | Email/Name no están vacíos pero las preguntas están vacías | Revisa que las personas encuestadas hayan respondido al menos 1 pregunta |
| Headers no reconocidos | Falta "SX-QY:" al inicio | Edita los headers manualmente para incluir el ID |
| El email aparece en Excel | Anonimato OFF | Reconfigura Forms → Settings → Anonymous Responses ON y vuelve a enviar |
| Baja participación (< 5 respuestas) | Lanzado sin contexto | Relanza con un mensaje del líder, deadline y propósito |

---

## 📚 Referencias

- **Las 75 preguntas formateadas:** [`question-bank-devs.es.md`](question-bank-devs.es.md) (español), [`question-bank-devs.md`](question-bank-devs.md) (inglés), [`question-bank-devs.pt-br.md`](question-bank-devs.pt-br.md) (portugués)
- **Plantilla Excel lista (5 mocks):** [`template-export-forms-devs.xlsx`](template-export-forms-devs.xlsx)
- **JSON estructurado de ejemplo:** [`mock-responses-devs.json`](mock-responses-devs.json)
- **Skill de importación:** [`../.github/skills/import-survey-devs/SKILL.md`](../.github/skills/import-survey-devs/SKILL.md)
- **Skill de insights:** [`../.github/skills/insights-developer-survey/SKILL.md`](../.github/skills/insights-developer-survey/SKILL.md)
- **Relación con la evaluación principal:** esta encuesta COMPLEMENTA la evaluación de madurez. Sus insights ayudan a validar las preguntas v2 listadas en `survey_crosswalk` en [framework.v2.json](../framework.v2.json) (por ejemplo D4-Q1 para la adopción de Copilot, D4-Q4 para las instrucciones y D6-Q1 para la gobernanza). Los resultados de la encuesta nunca cambian los puntajes v2.

---

**Versión:** 1.0 · **Fecha:** 2026-05-08

---

## ¿Trabado en alguno de estos pasos?

<details>
<summary><strong>FAQ: preguntas comunes sobre el Developer Survey (anónimo)</strong></summary>

| Síntoma | Causa probable | Cómo corregir |
|---|---|---|
| El Excel exportado tiene **Email** y **Name** completos | **Anonymous responses** NO estaba marcado en Forms | Forms Settings → ✅ **Anonymous responses** → recopila otra vez |
| Los desarrolladores se quejan de que es muy largo (20-25 min) | Demasiadas preguntas marcadas como required | Marca required **solo en S1** (perfil); deja el resto opcional |
| Tengo menos de 5 personas encuestadas | Los insights no son muy confiables | Mínimo absoluto: 3. Ideal: 5+. Excelente: 15+. Extiende la campaña 1 semana |
| La skill calcula madurez pero el número parece bajo | Rúbrica determinística L0-L4: refleja la realidad | Consulta [`MATURITY-RUBRIC.es.md`](MATURITY-RUBRIC.es.md) para entender la escala |
| Quiero saltarme esta encuesta | Está bien: es opcional | Ve directo al Learning Survey o ejecuta solo la evaluación principal |

</details>

---

## Continuar leyendo

| ← ANTERIOR | SIGUIENTE → |
|:---|---:|
| **[Recolección de la evaluación principal](../collection/FORMS-INSTRUCTIONS.es.md)** | **[Learning & Growth Survey](../survey-learning/FORMS-INSTRUCTIONS-LEARNING.es.md)** |
| 3 rutas para recopilar las 61 preguntas de evaluación (v2) vía Forms / Excel. | 32 preguntas identificadas: plan de capacitación con Champions y workshops. |

↑ [Volver al índice del kit](../README.es.md)
