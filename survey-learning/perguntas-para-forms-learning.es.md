# Preguntas para Microsoft Forms — Learning & Growth Survey

> **Encuesta IDENTIFICADA** (nombre + email) con 32 preguntas en 7 secciones. Tiempo estimado: **5-8 min**. Se enfoca en lo que los desarrolladores quieren APRENDER, formato preferido, barreras y Champions.

**Diferente de las otras encuestas:**

- Assessment principal: madurez organizacional (Likert L0-L4)

- Developer Survey: baseline comportamental anónimo

- **Este Learning Survey: roadmap de capacitación IDENTIFICADO** (nombre + email requeridos para invitar a las personas a los workshops correctos)

## Cómo crear el Forms

1. Ve a <https://forms.office.com> -> **+ New Form**
2. Título: `Learning & Growth IA — Qué quieres aprender en los próximos 6 meses?`
3. Subtítulo:

   > Encuesta de 5-8 min sobre tu plan de capacitación en IA. IDENTIFICADA (necesitamos nombre + email para invitarte a los workshops correctos). Resultado: plan de capacitación personalizado + cohorts + Champions Network.

   Agrega este aviso de privacidad debajo del subtítulo (completa los corchetes angulares con tu equipo de privacidad o legal):

   > **Aviso de privacidad.** Esta encuesta recopila tu nombre, email, rol y squad para planificar la capacitación, invitarte a workshops y armar la Champions Network. Las respuestas no se usan en evaluaciones de desempeño. Responsable y contacto: `<equipo / email>`. Acceso: `<quién ve las respuestas individuales>`. Retención: `<plazo>`, luego se eliminan. Puedes pedir acceso, corrección o eliminación de tus respuestas en `<contacto>`. Al enviar, aceptas este uso.

4. **Settings**:
   - ☐ **Anonymous responses** (OFF, esta encuesta es identificada)
   - ☑ **Only people in my organization** (recomendado)
   - ☑ **One response per person**
   - ☑ **Accept responses**
   - ☑ Email notification of each response
5. Agrega 7 secciones (una por L1..L7):
   - **L1 — Identificación** (4 preguntas)
   - **L2 — Auto-percepción de madurez IA** (7 preguntas)
   - **L3 — Dónde quieres crecer** (2 preguntas)
   - **L4 — Temas específicos que quieres aprender** (5 preguntas)
   - **L5 — Formato y cadencia preferidos** (4 preguntas)
   - **L6 — Champions y mentoría** (5 preguntas)
   - **L7 — Barreras y wishlist** (5 preguntas)

6. Para cada pregunta abajo:
   - **`choice`** -> Choice (Single answer)
   - **`multi`** -> Choice (Multiple answers)
   - **`text`** -> Long Text
   - **`text-short`** -> Short Text (una línea)

7. El **TÍTULO** debe empezar siempre con el ID + dos puntos. Ejemplo: `L4-Q1: Qué temas de GitHub Copilot quieres dominar?`

8. **Required**: marca L1-Q1 (nombre) y L1-Q2 (email) como obligatorias. Las demás son opcionales.
9. Comparte vía **Send -> Link** con todos los desarrolladores en alcance.
10. Cuando las respuestas estén listas: **Responses -> Open in Excel** -> renombra a `respostas-survey-learning.xlsx` -> mueve a la raíz del kit.

---

## L1 — Identificación

_Encuesta IDENTIFICADA. Usamos tu nombre/email para invitarte a los workshops y cohorts correctos. Las respuestas individuales no se comparten públicamente._

_4 preguntas en esta sección._

### Pregunta `L1-Q1` — _Short Text (una línea)_

> **L1-Q1: Tu nombre completo:**

### Pregunta `L1-Q2` — _Short Text (una línea)_

> **L1-Q2: Email corporativo (para invitaciones a workshops):**

### Pregunta `L1-Q3` — _Choice (single answer)_

> **L1-Q3: Rol:**

Opciones:

- Desarrollador Backend

- Desarrollador Frontend

- Full-Stack

- SRE / Platform Engineer

- Data Engineer / ML Engineer

- Architect

- Tech Lead

- Engineering Manager

- QA / SDET

- DevOps / DevEx

- Otro

### Pregunta `L1-Q4` — _Choice (single answer)_

> **L1-Q4: Equipo / Squad:**

Opciones:

- [Personalizar con la lista de equipos de la organización]

- Otro / no pertenezco a un squad fijo

---

## L2 — Auto-percepción de Madurez IA

_Evalúa tu confianza HOY en cada una de las 7 dimensiones de la rúbrica de madurez. Las respuestas honestas mejoran el plan._

_7 preguntas en esta sección._

### Pregunta `L2-Q1` — _Choice (single answer)_

> **L2-Q1: DS-D2 Copilot Adoption (modos Ask/Edit/Agent/Coding Agent, features, ganancias medidas): cuál es tu nivel?**

Opciones:

- L0 — Nunca lo usé o no lo conozco

- L1 — Conozco lo básico (inline completion)

- L2 — Uso Ask/Edit en el día a día

- L3 — Uso Agent + Spaces y mido ganancias

- L4 — Domino Coding Agent autónomo y la biblioteca de prompts del equipo

### Pregunta `L2-Q2` — _Choice (single answer)_

> **L2-Q2: DS-D3 Microsoft/GitHub Tooling (Foundry, Spaces, Coding Agent, MCP, Spec Kit, GHAS): cuál es tu nivel?**

Opciones:

- L0 — No conozco el ecosistema

- L1 — Solo conozco los nombres

- L2 — Uso 2-3 herramientas básicas

- L3 — Uso 4+ herramientas avanzadas

- L4 — Domino el ecosistema completo, incluyendo Foundry/MCP

### Pregunta `L2-Q3` — _Choice (single answer)_

> **L2-Q3: DS-D4 AI Dev Practices (TDD con IA, SDD, pair programming, debugging con IA): cuál es tu nivel?**

Opciones:

- L0 — Sin prácticas estructuradas

- L1 — Uso IA ocasionalmente

- L2 — Uso TDD o SDD ocasionalmente

- L3 — Trato IA como par en varias fases

- L4 — Mindset completo de pair programmer + SDD con Spec Kit

### Pregunta `L2-Q4` — _Choice (single answer)_

> **L2-Q4: DS-D5 Agent Concepts (custom agents, skills, prompts, MCP, A2A, handoffs, subagentes, personas Agentic DevOps): cuál es tu nivel?**

Opciones:

- L0 — No sé qué es un agente

- L1 — Conozco solo lo básico

- L2 — Conozco los modos de Copilot

- L3 — Ya creé custom agents/skills/prompts

- L4 — Domino MCP, A2A, subagentes y pruebas de agents

### Pregunta `L2-Q5` — _Choice (single answer)_

> **L2-Q5: DS-D6 Instructions / Memory (copilot-instructions.md, AGENTS.md, CLAUDE.md, Spaces, biblioteca de prompts): cuál es tu nivel?**

Opciones:

- L0 — No uso archivos de instrucciones

- L1 — Tengo 1 archivo básico

- L2 — Los uso y actualizo ocasionalmente

- L3 — El equipo los mantiene activamente

- L4 — Biblioteca de prompts compartida + Spaces colaborativos

### Pregunta `L2-Q6` — _Choice (single answer)_

> **L2-Q6: DS-D7 Best Practices (Champion, métricas DORA/DX, comunidad, compartir prompts): cuál es tu nivel?**

Opciones:

- L0 — No tengo cultura de IA estructurada

- L1 — Auto-aprendizaje aislado

- L2 — Tengo Champion en el equipo

- L3 — Mido DORA/DX y comparto con pares

- L4 — Comunidad activa + revisión regular de adopción

### Pregunta `L2-Q7` — _Choice (single answer)_

> **L2-Q7: DS-D8 Security & Governance (política IA, GHAS, SBOM, JIT permissions, red-lines de agents, audit): cuál es tu nivel?**

Opciones:

- L0 — Sin política, sin herramientas

- L1 — Política informal

- L2 — GHAS activo + política básica

- L3 — Scanners obligatorios + SBOM + entrenamiento

- L4 — JIT permissions + red-lines docs + auditoría revisada

---

## L3 — Dónde Quieres Crecer

_Pensando en los próximos 6 meses, en qué dimensiones quieres crecer MÁS?_

_2 preguntas en esta sección._

### Pregunta `L3-Q1` — _Choice (multiple answers)_

> **L3-Q1: Selecciona las 3 dimensiones PRIORITARIAS para tu crecimiento en los próximos 6 meses (elige exactamente 3):**

Opciones:

- DS-D2 Copilot Adoption (modos avanzados, Coding Agent)

- DS-D3 MS/GH Tooling (Foundry, Spaces, Spec Kit, MCP)

- DS-D4 AI Dev Practices (TDD con IA, SDD)

- DS-D5 Agent Concepts (custom agents, MCP, A2A)

- DS-D6 Instructions / Memory (archivos de instrucciones, biblioteca de prompts)

- DS-D7 Best Practices (DORA, comunidad, mentoría)

- DS-D8 Security & Governance (GHAS, SBOM, red-lines)

### Pregunta `L3-Q2` — _Long Text (respuesta libre)_

> **L3-Q2: Por qué elegiste estas 3 dimensiones? (1-2 frases, opcional pero muy útil)**

---

## L4 — Temas Específicos que Quieres Aprender

_Selecciona TODOS los temas que te gustaría aprender o profundizar._

_5 preguntas en esta sección._

### Pregunta `L4-Q1` — _Choice (multiple answers)_

> **L4-Q1: Qué temas de GitHub Copilot quieres dominar?**

Opciones:

- Modo Ask (preguntas efectivas)

- Modo Edit (edición multi-archivo)

- Modo Agent (autónomo en el IDE)

- Coding Agent (autónomo en GitHub.com, asigna issues, abre PRs)

- Copilot Spaces (contexto compartido)

- PR review con Copilot

- Test generation

- Slash commands (/explain, /fix, /tests)

- Copilot CLI

- Ya domino todo esto

### Pregunta `L4-Q2` — _Choice (multiple answers)_

> **L4-Q2: Qué temas de Microsoft Foundry / Azure AI quieres aprender?**

Opciones:

- Microsoft Foundry overview

- Foundry Agent Service (crear agentes)

- Azure OpenAI Service (API directa)

- Embeddings + RAG

- MCP (Model Context Protocol) + Foundry MCP server

- A2A (Agent-to-Agent) protocol

- Multi-agent orchestration

- Connectors (Dynamics, SAP, SharePoint)

- Foundry Memory (contexto de largo plazo)

- No tengo interés en Foundry ahora

### Pregunta `L4-Q3` — _Choice (multiple answers)_

> **L4-Q3: Qué temas de prácticas con IA quieres aprender?**

Opciones:

- TDD con IA (test-first con Copilot)

- SDD con Spec Kit (Spec-Driven Development)

- Prompt engineering (técnicas avanzadas)

- Pair programming con IA (mindset + prácticas)

- Refactoring con IA

- Code review con IA antes del PR

- Debugging asistido por IA

- Onboarding en proyecto nuevo con IA + Spaces

- Documentación automática

### Pregunta `L4-Q4` — _Choice (multiple answers)_

> **L4-Q4: Qué temas de agentes y primitives quieres aprender?**

Opciones:

- Crear custom agents (.agent.md)

- Crear custom skills (SKILL.md)

- Crear prompt files (.prompt.md)

- Configurar custom MCP server

- Subagentes (delegación)

- Handoffs entre agentes

- Personas Agentic DevOps (System Designer, Agent Operator)

- Testar agents (test suites para prompts/skills)

- Guardrails / red-lines de agents

### Pregunta `L4-Q5` — _Choice (multiple answers)_

> **L4-Q5: Qué temas de seguridad y gobernanza quieres aprender?**

Opciones:

- GitHub Advanced Security (CodeQL, secret scanning)

- SBOM (Software Bill of Materials)

- Microsoft Defender for DevOps / Cloud

- DLP para prompts de IA

- JIT permissions para agentes

- Audit logs de IA + análisis

- Política de uso de IA (templates)

- Vulnerabilidades comunes en código generado por IA

- Compliance / LGPD / GDPR + IA

---

## L5 — Formato y Cadencia Preferidos

_Cómo aprendes mejor?_

_4 preguntas en esta sección._

### Pregunta `L5-Q1` — _Choice (multiple answers)_

> **L5-Q1: Qué formatos de aprendizaje funcionan mejor para ti?**

Opciones:

- Workshop hands-on presencial/remoto (3-4h)

- Workshop corto (1h, sandwich seminar)

- Curso online self-paced (Coursera, Pluralsight, MS Learn)

- Pair programming con Champion

- Office hours semanales (Q&A abierto)

- Videos cortos (YouTube, Microsoft Learn)

- Podcast

- Book club / paper club

- Hackathon interno

- Show & tell de pares

- Documentación escrita + ensayo y error

### Pregunta `L5-Q2` — _Choice (single answer)_

> **L5-Q2: Cuánto tiempo por SEMANA dedicarías a aprender IA/Copilot?**

Opciones:

- < 1h/semana

- 1-2h/semana

- 2-4h/semana

- 4-6h/semana

- Más de 6h/semana

### Pregunta `L5-Q3` — _Choice (multiple answers)_

> **L5-Q3: Qué horario/día funciona mejor para workshops síncronos?**

Opciones:

- Miércoles/jueves por la mañana

- Miércoles/jueves por la tarde

- Viernes por la tarde (low-stress)

- Almuerzo (lunch & learn)

- Después del horario laboral (con horas extra)

- No puedo asistir a sesiones síncronas, solo self-paced

### Pregunta `L5-Q4` — _Choice (single answer)_

> **L5-Q4: Prefieres cohorts (grupo fijo aprendiendo junto) o self-paced?**

Opciones:

- Cohort (grupo fijo, más accountability)

- Self-paced (mi ritmo, más flexibilidad)

- Híbrido (módulos self-paced + sesiones síncronas)

- Sin preferencia

---

## L6 — Champions y Mentoría

_Sobre comunidad interna y mentoría._

_5 preguntas en esta sección._

### Pregunta `L6-Q1` — _Choice (single answer)_

> **L6-Q1: Te candidatearías como Champion de IA en tu equipo/empresa (ayudar a otros, organizar workshops)?**

Opciones:

- Sí — quiero ser Champion activo

- Sí — pero solo con soporte/entrenamiento dedicado

- Tal vez — necesito pensarlo

- No tengo interés ahora

### Pregunta `L6-Q2` — _Long Text (respuesta libre)_

> **L6-Q2: A quién en tu equipo/empresa consideras referencia en IA hoy? (nombre opcional, ayuda a mapear champions naturales)**

### Pregunta `L6-Q3` — _Choice (single answer)_

> **L6-Q3: Te gustaría mentoría 1:1 con alguien más experimentado en IA?**

Opciones:

- Sí — mentor senior en IA

- Sí — peer mentoring (mismo nivel, intercambio mutuo)

- No — prefiero auto-aprendizaje

- Otro (especificar en texto libre)

### Pregunta `L6-Q4` — _Choice (single answer)_

> **L6-Q4: Te ofrecerías para mentorear/enseñar a OTRAS personas en algún tema?**

Opciones:

- Sí — en varios temas

- Sí — en 1 tema específico

- Tal vez — depende del tema

- No me siento listo

### Pregunta `L6-Q5` — _Long Text (respuesta libre)_

> **L6-Q5: Si respondiste sí a la pregunta anterior, en qué tema(s) te sentirías cómodo mentoreando?**

---

## L7 — Barreras y Wishlist

_Qué te impide aprender más? Qué workshop te gustaría organizar o asistir?_

_5 preguntas en esta sección._

### Pregunta `L7-Q1` — _Choice (multiple answers)_

> **L7-Q1: Qué BARRERAS te impiden aprender más sobre IA hoy?**

Opciones:

- Falta de tiempo (sprint pressure)

- Falta de licencia Copilot

- Falta de licencia Foundry / Azure AI

- Falta de espacio para experimentar (sandbox / repo de prueba)

- Falta de entrenamiento estructurado

- Falta de Champion en el equipo

- Política de seguridad bloquea experimentos

- No sé por dónde empezar

- No veo prioridad clara del liderazgo

- Falta de presupuesto para cursos pagos

- Todo bien, sin barreras significativas

### Pregunta `L7-Q2` — _Long Text (respuesta libre)_

> **L7-Q2: Qué workshop interno te gustaría que existiera (aunque sea ambicioso)?**

### Pregunta `L7-Q3` — _Long Text (respuesta libre)_

> **L7-Q3: Qué speaker externo (interno/partner/comunidad) te gustaría traer?**

### Pregunta `L7-Q4` — _Long Text (respuesta libre)_

> **L7-Q4: Algo más que quieras compartir sobre tus objetivos de aprendizaje en IA?**

### Pregunta `L7-Q5` — _Choice (single answer)_

> **L7-Q5: Quieres recibir el plan de capacitación consolidado (resultado de esta encuesta) por email?**

Opciones:

- Sí — quiero ver el plan y los workshops sugeridos

- No, gracias

---

## Resumen

- **7 secciones**

- **32 preguntas** (15 choice + 9 multi + 8 text)

- **Tiempo:** 5-8 min

- **Identificada** (requiere nombre + email)

## Próximos pasos

1. Colectar respuestas (1-2 semanas, enviar un recordatorio por semana)
2. Exportar Excel -> renombrar `respostas-survey-learning.xlsx` -> mover a la raíz del kit
3. En Copilot Chat (modo Agent):

   ```text

   /importar-survey-learning
   /plano-capacitacao

   ```text

4. Recibir el plan de capacitación priorizado en `saida/plano-capacitacao-DATA.md`
