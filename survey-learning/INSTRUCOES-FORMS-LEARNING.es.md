# Cómo crear el Microsoft Forms para el Learning & Growth Survey

🌐 [English](INSTRUCOES-FORMS-LEARNING.md) · [Português (Brasil)](INSTRUCOES-FORMS-LEARNING.pt-br.md) · Español

**`🅲️ SURVEY-LEARNING`** · _identificado_ · 📖 [🏠 Índice](../README.es.md) · [« Survey-devs](../survey-devs/INSTRUCOES-FORMS-DEVS.es.md) · Estás aquí · [» Wizard](../wizard/README.es.md)

> [!WARNING]
> A diferencia de las otras 2 encuestas, esta es **IDENTIFICADA** (nombre + email requeridos). Tiene 32 preguntas en 7 secciones para construir el **roadmap de capacitación personalizado** del equipo: workshops, cohorts, Champions Network y mentoría. Tiempo estimado por desarrollador: **5-8 min**.

**Diferente de las otras 2 encuestas:**

- Evaluación principal: madurez organizacional (Likert L0-L4 declarada por liderazgo)
- Developer Survey: comportamiento real ANÓNIMO
- **Este Learning Survey: roadmap de capacitación IDENTIFICADO**: necesita nombre+email para invitar a las personas correctas a los workshops correctos

---

## ⚠️ ¿Por qué IDENTIFICADO (no anónimo)?

Para producir valor accionable, esta encuesta **necesita saber quién es quién**:

- Invitar a **las personas correctas** a cada workshop (10 asistentes pre-validados es mejor que "70% mostró interés")
- Construir una **Champions Network** con nombres (no anónima)
- Mapear **pares mentor↔mentee** (necesita nombres de ambos lados)
- Asignar un **owner** a los quick wins identificados

**Trade-off honesto:** algunas preguntas (por ejemplo, "cuál es tu nivel en DS-D8 Security?") pueden responderse con menos honestidad si los desarrolladores se sienten juzgados. Por eso:

- El liderazgo debe **comunicar claramente**: "las respuestas se usan para CONSTRUIR HABILIDADES, no para EVALUAR desempeño"
- No uses respuestas en evaluaciones de desempeño
- Comparte el plan consolidado con todo el equipo (transparencia)

Si tu organización prefiere **anonimato puro**: ejecuta el **Developer Survey** (`survey-devs/`) en paralelo y usa la rúbrica determinística como "termómetro objetivo".

---

## 📋 Los 7 temas cubiertos

| # | Sección | Foco | Q |
|---|---|---|---|
| **L1** | Identificación | Nombre, email, rol, equipo | 4 |
| **L2** | Auto-percepción de madurez | Autoevaluación L0-L4 en las 7 dimensiones D2-D8 | 7 |
| **L3** | Dónde quieres crecer | Top 3 dimensiones prioritarias (próximos 6 meses) + por qué | 2 |
| **L4** | Temas específicos | Copilot, Foundry, prácticas (TDD/SDD), agentes, seguridad (checkbox) | 5 |
| **L5** | Formato y cadencia | Workshop hands-on, cohort, self-paced, horarios, horas/semana | 4 |
| **L6** | Champions y mentoría | ¿Quieres ser Champion? ¿Mentoría? ¿Quién es referencia? | 5 |
| **L7** | Barreras y Wishlist | Qué bloquea + workshops deseados + speakers | 5 |
| | | **TOTAL** | **32** |

---

## 🛠️ Cómo crear el Forms (paso a paso)

### Paso 1 · Crear el formulario

1. Ve a <https://forms.office.com> → **+ New Form**
2. Título: `Learning & Growth IA: Qué quieres aprender en los próximos 6 meses?`
3. Subtítulo (pega):

```text
Encuesta de 5-8 min sobre tu plan de capacitación en IA.

⚠️ IDENTIFICADA: usaremos tu nombre+email para INVITARTE a los
workshops/cohorts correctos. Las respuestas individuales NO se compartirán
públicamente, solo insights agregados + listas de asistentes por workshop.

Resultado: plan de capacitación personalizado + cohorts + Champions Network.
```

### Paso 2 · ⚠️ CONFIGURAR como IDENTIFICADO (no anónimo)

**Settings (⚙️):**

| Setting | Valor |
|---|---|
| **Anonymous responses** | ☐ **DESMARCADO** (queremos identificación) |
| **Who can respond** | "Only people in my organization" (recomendado) |
| **One response per person** | ☑ MARCADO (1 por desarrollador) |
| **Accept responses** | ☑ MARCADO |
| **Customize thank you message** | "Thank you! You will receive workshop invitations based on your answers." |

> 🔍 **Diferente del Developer Survey** (`survey-devs/INSTRUCOES-FORMS-DEVS.es.md`): allí activas Anonymous ON; aquí lo dejas OFF.

### Paso 3 · Crear 7 secciones

```text
Section 1: L1 - Identificación                 (4 preguntas)
Section 2: L2 - Auto-percepción (D2-D8)        (7 preguntas)
Section 3: L3 - Dónde quieres crecer           (2 preguntas)
Section 4: L4 - Temas específicos              (5 preguntas)
Section 5: L5 - Formato y cadencia             (4 preguntas)
Section 6: L6 - Champions y mentoría           (5 preguntas)
Section 7: L7 - Barreras y Wishlist            (5 preguntas)
```

### Paso 4 · Agregar las 32 preguntas

Usa el banco en español [`perguntas-para-forms-learning.es.md`](perguntas-para-forms-learning.es.md) como fuente para copiar y pegar. El banco de preguntas canónico es la versión PT-BR, [`perguntas-para-forms-learning.es.md`](perguntas-para-forms-learning.es.md); úsalo si tus personas encuestadas responden en portugués.

**Para cada pregunta:**

1. Tipo:
   - `choice` (Single answer) → **Choice**
   - `multi` (Multiple answers) → **Choice** con Multiple answers MARCADO
   - `text-short` (Short Text, 1 línea) → **Short answer**
   - `text` (Long Text) → **Long answer**

2. **El TÍTULO SIEMPRE empieza con el ID + dos puntos**:

   ```text
   L4-Q1: Qué temas de GitHub Copilot quieres dominar?
   ```

3. **Required**: marca **L1-Q1 (nombre) + L1-Q2 (email)** como required. Deja el resto opcional (los desarrolladores pueden omitirlas).

### Paso 5 · Personalizar L1-Q4 (lista de squads)

La pregunta L1-Q4 ("Equipo / Squad") tiene un placeholder (`[Customize with the organization's team list]` en el banco en inglés, `[Lista a customizar pela org]` en el banco PT-BR). Reemplázalo por los nombres reales de squads de tu organización. Ejemplo:

```text
- Payments Squad
- Onboarding Squad
- Platform Squad
- SRE Core
- Data Platform
- Other / I do not belong to a fixed squad
```

### Paso 6 · Compartir

1. **+ Send / Collect responses** → **Link**
2. Comparte con **TODOS los desarrolladores**:
   - Email del líder de ingeniería: "Durante las próximas 2 semanas, queremos escuchar qué quieren aprender sobre IA: una encuesta IDENTIFICADA de 5-8 min. Resultado: un plan de capacitación personalizado."
   - Canal Slack/Teams #engineering
   - All-hands (presenta el link)

3. **Deadline:** 2 semanas. Recordatorios en D+7 y D+12.

### Paso 7 · Dar seguimiento a las respuestas

- La pestaña **Responses** muestra el conteo en tiempo real
- Recomendado: **al menos 5 desarrolladores**, idealmente **>50% del equipo**
- Como es identificada, puedes ver "X de Y desarrolladores todavía no respondieron" y hacer seguimiento 1:1

### Paso 8 · Exportar

1. **Responses → Open in Excel**
2. Guarda como **`respostas-survey-learning.xlsx`**
3. Muévelo a la **raíz de `kit-cliente/`**
4. Revisa: las columnas D (Email) y E (Name) deben estar COMPLETAS

### Paso 9 · Analizar con el kit

En Copilot Chat (modo Agent):

```text
/importar-survey-learning
```

Genera `survey-learning/respostas-learning.json` (estructurado).

```text
/plano-capacitacao
```

Genera `saida/plano-capacitacao-<DATE>.md` (en **inglés de forma predeterminada**; el script acepta `--lang pt-br` para portugués (Brasil) y `--lang es` para español) con:

- Top 10 temas solicitados (con lista de asistentes pre-validados)
- Cohorts sugeridos por dimensión D2-D8
- Champions Network identificada (3 tiers)
- Pares mentor ↔ mentee
- Calendario de workshops (próximos 90 días)
- Barreras priorizadas
- 5 acciones priorizadas (impacto × facilidad)
- Conexión con /insights-developer-survey + /calcular-scores

### Paso 10 · ⭐ Auto-fill del wizard (Mode D)

Después de generar el plan, ejecutar `/wizard-implementacao` hace que el Copilot Agent **detecte automáticamente** `saida/plano-capacitacao-*.md` y ofrezca **Mode D: Auto-fill**, que llena **7 de los 11** campos del wizard automáticamente:

| Input del wizard (Parte 4 del PDF) | Viene de |
|---|---|
| `executive_steering_committee` | Champions Network "active" |
| `communication_plan` | Calendario de workshops |
| `training_plan` | Cohorts por dimensión |
| `adkar_notes` | Top 5 workshops (Knowledge stage) |
| `quick_wins_w1_4` / `quick_wins_w5_8` / `quick_wins_w9_12` | Calendario de 90 días |

Completa manualmente: **program office (TPO)**, **RACI**, **responsables de dimensión** y el **registro de riesgos del cliente** (el Learning Survey no los cubre). Los campos vacíos muestran "to fill with the client" en la guía de implementación.

**Ahorro estimado:** 30-45 min de trabajo manual en el wizard. Y los datos vienen de tu equipo.

### Paso 11 · Re-renderizar los PDFs con el plan + auto-fill del wizard

```text
/gerar-relatorio
```

La skill detecta:

- ✅ `implementation-guide-inputs.json` (del auto-fill de wizard Mode D) → completa la Parte 4 con tus Champions y workshops
- ✅ `saida/plano-capacitacao-*.md` (de esta encuesta) → enriquece roadmap_part4.pdf
- ✅ `saida/insights-developer-survey-*.md` (si lo ejecutaste) → cruza referencias en el apéndice
- ✅ `saida/maturidade-developer-survey-*.json` (si lo ejecutaste) → score_justification.pdf incluye "maturity vs declared"

**Salida:** 5 PDFs de calidad de producción con datos REALES de la Learning Survey integrados.

---

## 🅱️ Ruta alternativa: Excel/SharePoint directamente

Para equipos pequeños (3-5 desarrolladores):

```bash
cp survey-learning/template-export-forms-learning.xlsx respostas-survey-learning.xlsx
# Borra las filas mock (filas 2-6)
# Sube a SharePoint con permiso de edición
# Cada desarrollador completa una fila (incluyendo name+email)
# Descarga y mueve a la raíz
/importar-survey-learning + /plano-capacitacao
```

---

## 💡 Buenas prácticas

### Compromiso con el uso ético de los datos

Comunica antes de lanzar:

> "Tus respuestas se usarán para: (1) construir nuestro roadmap de capacitación, (2) invitarte a los workshops específicos que pediste y (3) construir la Champions Network. **NO** se usarán para evaluación de desempeño, comparación entre desarrolladores ni se compartirán con clientes externos."

### Privacidad y protección de datos (LGPD / GDPR)

Esta encuesta procesa datos personales (nombre, email, rol, squad, autoevaluación). Acuerda los puntos siguientes con tu equipo de privacidad o legal antes del lanzamiento; esta checklist no es asesoría legal.

- **Propósito y base legal:** documenta por qué se recopilan los datos (plan de capacitación, invitaciones, Champions Network) y la base legal que elija tu equipo.
- **Aviso de privacidad:** incluye el aviso de `perguntas-para-forms-learning.es.md` (paso 3) en el formulario, con responsable, acceso, retención y contacto completos.
- **Minimización:** recopila solo las preguntas de identificación en L1; no agregues campos como ID de empleado o manager.
- **Almacenamiento y acceso:** mantén `respostas-survey-learning.xlsx`, `survey-learning/respostas-learning.json` y `saida/plano-capacitacao-*.md` en almacenamiento gestionado con acceso restringido. Estas rutas están en `.gitignore`; nunca les hagas commit.
- **Apéndice solo para liderazgo:** el apéndice de personas encuestadas del plan contiene nombres y emails. Compártelo solo con las personas que envían invitaciones.
- **Retención y eliminación:** elimina las respuestas de Forms, el `.xlsx`, el JSON y el apéndice del plan cuando termine el período de retención.
- **Solicitudes individuales:** nombra un owner para solicitudes de acceso, corrección y eliminación.

### Cadencia de relanzamiento

- **Cada 6 meses** o después de eventos importantes (rollout de Copilot, cambio de stack, etc.)
- **Compara evolución**: ¿un desarrollador que estaba en L1 en DS-D5 ahora se autoevalúa en L3? Un Champion natural

### Transparencia del plan

- Presenta `plano-capacitacao-DATE.md` en un all-hands
- Las personas que pidieron el workshop X reciben una invitación: cierra el loop
- Los Champions identificados reciben reconocimiento público (con consentimiento)

---

## 🆘 Troubleshooting

| Problema | Solución |
|---|---|
| La skill no detecta el archivo | Muévelo a la raíz de `kit-cliente/` |
| Email/Name vacío en algunas filas | Configuración de Forms: Anonymous OFF + L1-Q1/Q2 required |
| Headers no reconocidos | Asegúrate de que cada pregunta empiece con `L[1-7]-Q\d+:` |
| Un desarrollador rechazó identificarse | Acepta la respuesta parcial; redirígelo a `survey-devs` (anónimo) |
| Baja participación (< 50% del equipo) | El líder de ingeniería debe RESPALDARLA explícitamente |

---

## 📚 Referencias

- **Las 32 preguntas formateadas (español):** [`perguntas-para-forms-learning.es.md`](perguntas-para-forms-learning.es.md) (banco canónico PT-BR: [`perguntas-para-forms-learning.es.md`](perguntas-para-forms-learning.es.md))
- **Plantilla Excel lista:** [`template-export-forms-learning.xlsx`](template-export-forms-learning.xlsx)
- **JSON estructurado de muestra:** [`respostas-mock-learning.json`](respostas-mock-learning.json)
- **Skill de importación:** [`../.github/skills/importar-survey-learning/SKILL.md`](../.github/skills/importar-survey-learning/SKILL.md)
- **Skill de plan:** [`../.github/skills/plano-capacitacao/SKILL.md`](../.github/skills/plano-capacitacao/SKILL.md)
- **Referencia cruzada con el Developer Survey** (anónimo): [`../survey-devs/`](../survey-devs/)

---

**Versión:** 1.0 · **Fecha:** 2026-05-08

---

## ¿Atascado en uno de estos pasos?

<details>
<summary><strong>FAQ: preguntas comunes sobre el Learning & Growth Survey (identificado)</strong></summary>

| Síntoma | Causa probable | Cómo corregir |
|---|---|---|
| Excel llega sin name/email | **Anonymous responses** está marcado (esta encuesta debe ser identificada) | Forms Settings → ❌ DESMARCA **Anonymous responses** |
| ¿Cómo uso el plan para invitar personas? | El plan lista name+email por workshop | Copia la lista de asistentes desde el Markdown → pégala en una invitación de Outlook/Teams |
| Champions Network está vacía en el plan generado | Nadie respondió "sí" en L6-Q1 | Sin Champions autodeclarados: usa el ranking por dimensión como proxy |
| Cohorts están vacíos en algunas dimensiones | Menos de 3 personas encuestadas por dimensión | Pide más participación o acepta cohorts más pequeños |
| ¿Puedo volver a ejecutar el plan si llegan más respuestas? | Sí, es idempotente | Reexporta Excel → `/importar-survey-learning` → `/plano-capacitacao` |

</details>

---

## Sigue leyendo

| ← ANTERIOR | SIGUIENTE → |
|:---|---:|
| **[Developer Survey (anónimo)](../survey-devs/INSTRUCOES-FORMS-DEVS.es.md)** | **[Wizard: Parte 4](../wizard/README.es.md)** |
| 75 preguntas anónimas: Copilot, agentes, gobernanza. | Personaliza el Steering Committee, RACI, ADKAR y Quick Wins del PDF ejecutivo. |

↑ [Volver al Índice del kit](../README.es.md)
