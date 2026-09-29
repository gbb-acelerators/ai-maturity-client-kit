# Preguntas para Microsoft Forms: Developer Survey (GitHub + IA)

🌐 [English](question-bank-devs.md) · [Português (Brasil)](question-bank-devs.pt-br.md) · Español

75 preguntas en 9 secciones. Tiempo estimado: **20-25 min**. ANÓNIMO, no pedimos nombre ni email de la persona encuestada.

**Nota de ejecución:** Este banco localizado traduce las instrucciones, los títulos de las preguntas y las opciones de respuesta. `survey-devs/options.json` asigna cada opción en español, inglés y portugués a la misma opción canónica, así que el puntaje funciona con un formulario creado en cualquiera de los tres idiomas (los formularios antiguos en portugués con guiones en las opciones también se leen). Mantén todos los IDs (`Sx-Qy:`) sin cambios en Microsoft Forms.

## Cómo Crear el Form

1. Ve a <https://forms.office.com> -> **+ New Form**.
2. Título sugerido: `Developer Survey: Cómo mi equipo usa GitHub e IA hoy`.
3. Subtítulo sugerido: Survey anónimo (20-25 min) sobre tus prácticas con GitHub Copilot, modos de Copilot Chat (Ask/Edit/Agent), agentes IA, instruction files, mejores prácticas de IA + Dev, y seguridad. Tus respuestas alimentarán el roadmap de adopción de IA del equipo.
4. Configuración: habilita **Anonymous responses**, deshabilita **One response per person**, y deja **Accept responses** habilitado.
5. Agrega 9 secciones: S1 Perfil del encuestado, S2 GitHub Copilot Adopción y Modos, S3 Otras herramientas Microsoft / GitHub AI, S4 Prácticas de Desarrollo con IA, S5 Conceptos y Estructura de Agentes, S6 Markdown / Memory / Instructions, S7 Usabilidad y Best Practices, S8 Seguridad y Gobernanza, S9 Pain Points & Wishlist.
6. Para cada pregunta abajo, agrega el tipo correspondiente en Forms: `choice`, `multi`, o `text`.
7. El **TÍTULO** de cada pregunta debe comenzar con el ID + dos puntos. Ejemplo: `S2-Q1: ¿Tienes una licencia activa de GitHub Copilot?`
8. El ID es usado por `/import-survey-devs` para mapear de vuelta. NO LO REMUEVAS.
9. Comparte vía **+ Send / Collect responses** -> copiar link -> enviar por Slack/Teams/email.
10. Cuando tengas respuestas, **Responses -> Open in Excel** -> renombra a `survey-devs-responses.xlsx` -> mueve a la raíz del kit.

---

## S1: Perfil del encuestado

_Preguntas básicas sobre ti y tu contexto. Anónimo: no pediremos nombre ni email._

_7 preguntas en esta sección._

### Pregunta `S1-Q1`: _Choice (single answer)_

> **S1-Q1: ¿Cuál es tu cargo actual?**

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

### Pregunta `S1-Q2`: _Choice (single answer)_

> **S1-Q2: ¿Tiempo total como desarrollador?**

Opciones:

- < 2 años
- 2-5 años
- 6-10 años
- 11-15 años
- > 15 años

### Pregunta `S1-Q3`: _Choice (single answer)_

> **S1-Q3: ¿Hace cuánto usas IA en desarrollo (Copilot, Cursor, Claude Code, etc.)?**

Opciones:

- Nunca la usé
- < 3 meses
- 3-12 meses
- 1-2 años
- > 2 años

### Pregunta `S1-Q4`: _Choice (multiple answers)_

> **S1-Q4: ¿Lenguajes principales que usas en el día a día?**

Opciones:

- TypeScript / JavaScript
- Python
- C# / .NET
- Java / Kotlin
- Go
- Rust
- C++
- Ruby
- PHP
- Swift
- SQL (enfoque principal)
- Otro

### Pregunta `S1-Q5`: _Choice (single answer)_

> **S1-Q5: ¿Cuántas horas al día pasas codificando en promedio?**

Opciones:

- < 2h
- 2-4h
- 4-6h
- 6-8h
- > 8h

### Pregunta `S1-Q6`: _Choice (single answer)_

> **S1-Q6: ¿Cuál es el tamaño de tu squad/equipo inmediato?**

Opciones:

- Trabajo solo
- 2-4 personas
- 5-9 personas
- 10-15 personas
- > 15 personas

### Pregunta `S1-Q7`: _Choice (single answer)_

> **S1-Q7: ¿Modelo de trabajo?**

Opciones:

- 100% remoto
- Híbrido (1-2 días presencial)
- Híbrido (3-4 días)
- 100% presencial

---

## S2: GitHub Copilot: Adopción y Modos

_Foco en GitHub Copilot. Incluye los modos actuales (Ask, Edit, Agent), Coding Agent autónomo y Spaces para contexto compartido._

_9 preguntas en esta sección._

### Pregunta `S2-Q1`: _Choice (single answer)_

> **S2-Q1: ¿Tienes una licencia activa de GitHub Copilot?**

Opciones:

- Sí, Copilot Enterprise
- Sí, Copilot Business
- Sí, Copilot Pro+ (individual)
- Sí, Copilot Pro (individual)
- Sí, Copilot Free
- Tengo licencia pero no la uso
- No tengo licencia

### Pregunta `S2-Q2`: _Choice (single answer)_

> **S2-Q2: ¿Frecuencia de uso de Copilot?**

Opciones:

- Diariamente (varias horas)
- Diariamente (esporádico)
- Semanal
- Rara vez
- Nunca

### Pregunta `S2-Q3`: _Choice (multiple answers)_

> **S2-Q3: ¿Qué MODOS de Copilot Chat usas? (selecciona todos los que apliquen)**

Opciones:

- Ask (responder preguntas)
- Edit (edición multiarchivo en el IDE)
- Agent (autónomo en el IDE, ejecuta tasks)
- Copilot Coding Agent (autónomo en GitHub.com, asigna issues, abre PRs solo)
- Plan / Vision
- No uso Chat, solo completion inline
- No conozco esos modos

### Pregunta `S2-Q4`: _Choice (single answer)_

> **S2-Q4: ¿Qué MODO usas MÁS en el día a día?**

Opciones:

- Ask
- Edit
- Agent (en el IDE)
- Coding Agent (autónomo en GitHub)
- Plan / Vision
- Solo completion inline
- No sé la diferencia

### Pregunta `S2-Q5`: _Choice (multiple answers)_

> **S2-Q5: ¿Qué features de Copilot usas?**

Opciones:

- Inline code completion
- Chat (preguntas en el IDE)
- Descripciones automáticas de Pull Request
- Pull Request review (Copilot review)
- Generación de tests
- Generación de documentación
- Resolución de issues (Coding Agent asigna issue)
- Slash commands en Chat (/explain, /fix, /tests)
- Copilot Spaces (contexto compartido: repos + docs + custom instructions)
- Copilot Coding Agent (tareas autónomas)
- Copilot CLI (gh copilot)

### Pregunta `S2-Q6`: _Choice (multiple answers)_

> **S2-Q6: ¿Dónde usas Copilot?**

Opciones:

- VS Code
- Visual Studio
- JetBrains (IntelliJ, PyCharm, etc.)
- Neovim
- Xcode
- GitHub.com (web)
- GitHub Mobile
- GitHub Codespaces
- CLI (gh copilot)

### Pregunta `S2-Q7`: _Choice (single answer)_

> **S2-Q7: ¿Ganancia de productividad percibida con Copilot?**

Opciones:

- Negativo (estorba)
- Neutro (sin ganancia)
- +10-20%
- +20-40%
- +40-60%
- +60% o más
- No sé medirlo

### Pregunta `S2-Q8`: _Choice (multiple answers)_

> **S2-Q8: ¿Para QUÉ TAREAS te ayuda más Copilot?**

Opciones:

- Boilerplate / código repetitivo
- Refactoring
- Escribir tests
- Aprender una API/lib nueva
- Debugging
- Explicar código legacy
- Documentación
- SQL / queries complejas
- Regex
- Traducción entre lenguajes
- Onboarding en proyecto nuevo

### Pregunta `S2-Q9`: _Long Text (respuesta libre)_

> **S2-Q9: ¿En qué tareas Copilot NO te ayuda, o te estorba?**

---

## S3: Otras herramientas Microsoft / GitHub AI

_Ecosistema Microsoft Foundry y features avanzadas de GitHub._

_7 preguntas en esta sección._

### Pregunta `S3-Q1`: _Choice (multiple answers)_

> **S3-Q1: ¿Qué otras herramientas Microsoft / GitHub AI usas hoy?**

Opciones:

- Microsoft Foundry (antes Azure AI Foundry)
- Foundry Agent Service (GA, built on OpenAI Responses API)
- Azure OpenAI Service (directo vía API)
- Microsoft 365 Copilot
- GitHub Copilot Spaces
- GitHub Copilot Coding Agent (autónomo)
- GitHub Codespaces
- GitHub Models (playground multi-LLM)
- GitHub Advanced Security (GHAS)
- GitHub Actions con integración de Copilot
- Visual Studio con Copilot avanzado
- Ninguna de las anteriores

### Pregunta `S3-Q2`: _Choice (multiple answers)_

> **S3-Q2: ¿Para QUÉ usas Microsoft Foundry / Azure OpenAI, si lo usas?**

Opciones:

- PoC / experimentación
- Feature de producto en producción
- Embeddings / RAG
- Foundry Agent Service para agentes autónomos
- Multi-agent orchestration vía MCP
- Fine-tuning
- Connectors (Dynamics, SAP, SharePoint, etc.)
- No lo uso

### Pregunta `S3-Q3`: _Choice (single answer)_

> **S3-Q3: ¿Conoces GitHub Copilot Coding Agent, el sucesor autónomo de Workspace que toma issues y abre PRs?**

Opciones:

- Lo uso activamente en producción
- Ya lo probé pero no lo uso de forma recurrente
- Lo conozco pero nunca lo usé
- No lo conozco

### Pregunta `S3-Q4`: _Choice (single answer)_

> **S3-Q4: ¿Conoces Copilot Spaces, la funcionalidad de contexto compartido que reemplazó Knowledge Bases?**

Opciones:

- Uso y creo Spaces para mi equipo
- Uso Spaces creados por otros
- Lo conozco pero no lo uso
- No lo conozco

### Pregunta `S3-Q5`: _Choice (single answer)_

> **S3-Q5: ¿Conoces GitHub Spec Kit (github/spec-kit) para Spec-Driven Development?**

Opciones:

- Lo uso
- Lo conozco pero no lo uso
- No lo conozco

### Pregunta `S3-Q6`: _Choice (single answer)_

> **S3-Q6: ¿Conoces MCP (Model Context Protocol), el estándar para que agentes consuman tools/contexto?**

Opciones:

- Uso servidores MCP en mi workflow
- Configuré algún MCP server custom
- Conozco el concepto
- No lo conozco

### Pregunta `S3-Q7`: _Choice (single answer)_

> **S3-Q7: ¿Has usado GitHub Models para probar diferentes LLMs (gpt-4o, claude, llama, etc.)?**

Opciones:

- Lo uso de forma recurrente
- Ya lo probé
- No lo conozco

---

## S4: Prácticas de Desarrollo con IA

_Cómo incorporas IA en tu flujo: TDD, SDD, pair programming con IA y prácticas relacionadas._

_9 preguntas en esta sección._

### Pregunta `S4-Q1`: _Choice (single answer)_

> **S4-Q1: ¿Practicas TDD con IA, escribiendo tests primero con Copilot?**

Opciones:

- Siempre que sea posible
- Frecuentemente
- A veces
- Rara vez
- Nunca
- No sé qué es TDD

### Pregunta `S4-Q2`: _Choice (single answer)_

> **S4-Q2: ¿Practicas SDD (Spec-Driven Development), escribiendo una spec para que IA genere código?**

Opciones:

- Lo uso activamente (con Spec Kit o similar)
- Ya lo probé en algunos proyectos
- Conozco el concepto pero no lo uso
- Nunca escuché hablar de eso

### Pregunta `S4-Q3`: _Choice (multiple answers)_

> **S4-Q3: ¿En QUÉ momentos consultas IA durante el coding?**

Opciones:

- Antes de empezar (planear arquitectura)
- Durante (autocomplete + preguntas)
- Después de implementar (review/refactor)
- Cuando me trabo (debugging)
- Para escribir tests
- Para escribir docs
- Para code review de mi propio PR

### Pregunta `S4-Q4`: _Choice (single answer)_

> **S4-Q4: ¿Consideras Copilot / un agente IA como pair programmer?**

Opciones:

- Sí, lo trato como par
- A veces (depende de la tarea)
- No, solo una herramienta de autocompletar
- No lo uso de forma estructurada

### Pregunta `S4-Q5`: _Choice (single answer)_

> **S4-Q5: ¿Con qué frecuencia refactorizas código con ayuda de IA?**

Opciones:

- Todas las semanas
- Algunas veces por mes
- Rara vez
- Nunca

### Pregunta `S4-Q6`: _Choice (single answer)_

> **S4-Q6: ¿Quién mantiene la documentación del código en tu equipo?**

Opciones:

- IA la genera y el equipo la revisa
- Los devs la escriben manualmente, IA ayuda a veces
- El equipo la mantiene manualmente, sin IA
- La documentación está abandonada

### Pregunta `S4-Q7`: _Choice (single answer)_

> **S4-Q7: Cuando tienes un bug difícil, ¿cuál es tu primera acción?**

Opciones:

- Le pregunto a Copilot Chat / Claude / otra IA
- Busco en logs / debugger
- Le pregunto a un colega humano
- Stack Overflow / documentación
- Depende del bug

### Pregunta `S4-Q8`: _Choice (single answer)_

> **S4-Q8: Al hacer onboarding en un proyecto nuevo, ¿usas IA (con Copilot Spaces o similar) para entender la base de código?**

Opciones:

- Siempre, es lo primero que hago
- Frecuentemente
- A veces
- No, leo README y código manualmente

### Pregunta `S4-Q9`: _Long Text (respuesta libre)_

> **S4-Q9: Describe una práctica concreta con IA que cambió tu productividad en los últimos 6 meses:**

---

## S5: Conceptos y Estructura de Agentes

_Verifica conocimiento y uso de agentes de IA estructurados, incluyendo personas Agentic DevOps de Microsoft y prácticas de prueba/gobernanza de agentes._

_11 preguntas en esta sección._

### Pregunta `S5-Q1`: _Choice (single answer)_

> **S5-Q1: ¿Sabes qué es un AI agent, autónomo versus asistente reactivo?**

Opciones:

- Sí, lo explico claramente
- Sí, vagamente
- No sé la diferencia
- No conozco el término

### Pregunta `S5-Q2`: _Choice (single answer)_

> **S5-Q2: ¿Sabes la diferencia entre Ask, Edit, Agent y Coding Agent (modos de Copilot)?**

Opciones:

- Sí, los uso conscientemente
- Más o menos
- No sé la diferencia

### Pregunta `S5-Q3`: _Choice (single answer)_

> **S5-Q3: ¿Ya creaste o usaste un custom agent (.github/agents/*.agent.md o equivalente Claude/Cursor)?**

Opciones:

- Ya creé uno
- Ya usé uno pero no creé ninguno
- Sé que existen pero nunca usé uno
- No sabía que era posible

### Pregunta `S5-Q4`: _Choice (single answer)_

> **S5-Q4: ¿Conoces el concepto de skill (SKILL.md o equivalente, bloque reutilizable de instrucciones)?**

Opciones:

- Lo conozco y lo uso
- Lo conozco pero no lo uso
- No lo conozco

### Pregunta `S5-Q5`: _Choice (single answer)_

> **S5-Q5: ¿Ya creaste prompt files (.prompt.md en .github/prompts/)?**

Opciones:

- Sí, varias
- Sí, una o dos
- No, pero planeo hacerlo
- No lo conozco

### Pregunta `S5-Q6`: _Choice (single answer)_

> **S5-Q6: ¿Conoces A2A (Agent-to-Agent protocol), agentes comunicándose entre sí?**

Opciones:

- Lo uso (p. ej., Foundry A2A Tool)
- Conozco el concepto
- No lo conozco

### Pregunta `S5-Q7`: _Choice (single answer)_

> **S5-Q7: ¿Conoces handoffs entre agentes, cuando el agente A pasa contexto al agente B?**

Opciones:

- Lo uso
- Conozco el concepto
- No lo conozco

### Pregunta `S5-Q8`: _Choice (single answer)_

> **S5-Q8: ¿Conoces subagentes, cuando un agente principal delega tareas a subagentes especializados?**

Opciones:

- Lo uso
- Conozco el concepto
- No lo conozco

### Pregunta `S5-Q9`: _Choice (single answer)_

> **S5-Q9: ¿Conoces las personas Microsoft Agentic DevOps: System Designer y Agent Operator?**

Opciones:

- Sí, las adopto explícitamente
- Conozco el concepto
- No lo conozco

### Pregunta `S5-Q10`: _Choice (single answer)_

> **S5-Q10: ¿TESTEAS tus custom agents/prompts/skills antes de usarlos en código real?**

Opciones:

- Siempre, tengo test suite para mis agents
- Frecuentemente, manual pero sistemático
- A veces, solo sanity check
- Rara vez / nunca
- No creo agents/prompts/skills

### Pregunta `S5-Q11`: _Choice (multiple answers)_

> **S5-Q11: ¿Qué primitivos YA CREASTE para uso personal/equipo?**

Opciones:

- Custom prompts (.prompt.md)
- Custom skills (SKILL.md)
- Custom agents (.agent.md)
- Custom MCP server
- Archivos de instrucciones (copilot-instructions.md / AGENTS.md / CLAUDE.md)
- Spaces compartidos
- Ninguno de los anteriores

---

## S6: Markdown / Memory / Instructions

_Sobre archivos de configuración que enseñan al agente sobre tu proyecto._

_6 preguntas en esta sección._

### Pregunta `S6-Q1`: _Choice (multiple answers)_

> **S6-Q1: ¿Qué archivos de instrucciones usas hoy?**

Opciones:

- .github/copilot-instructions.md
- .github/instructions/*.instructions.md
- AGENTS.md
- CLAUDE.md (raíz del proyecto)
- .cursorrules
- Custom instructions en Copilot Spaces
- Ninguno

### Pregunta `S6-Q2`: _Choice (single answer)_

> **S6-Q2: ¿Quién mantiene los archivos de instrucciones en tu proyecto?**

Opciones:

- Todo el equipo contribuye
- 1-2 personas dedicadas
- Los mantengo solo
- Nadie los mantiene, están desactualizados
- No tenemos

### Pregunta `S6-Q3`: _Choice (single answer)_

> **S6-Q3: ¿Frecuencia de actualización de esos archivos?**

Opciones:

- Todas las semanas
- Mensualmente
- Trimestralmente
- Cuando algo se rompe
- Nunca los actualizo

### Pregunta `S6-Q4`: _Choice (multiple answers)_

> **S6-Q4: ¿QUÉ incluyes en los archivos de instrucciones?**

Opciones:

- Code style / convenciones del proyecto
- Domain knowledge (reglas de negocio)
- Stack / herramientas
- Forbidden patterns (qué NO hacer)
- Examples (good vs bad code)
- Estructura de carpetas / arquitectura
- Comandos comunes (test, build, deploy)
- No tengo instrucciones

### Pregunta `S6-Q5`: _Choice (single answer)_

> **S6-Q5: ¿Tienes una prompt library compartida con tu equipo (repo o Copilot Space dedicado)?**

Opciones:

- Sí, Copilot Space compartido
- Sí, repo dedicado
- Sí, wiki/Confluence
- Cada quien mantiene el suyo
- No compartimos prompts

### Pregunta `S6-Q6`: _Choice (single answer)_

> **S6-Q6: ¿Usas memoria persistente del agente (Foundry Memory, Claude memory, Copilot memory)?**

Opciones:

- Lo uso activamente
- Ya lo probé
- No lo conozco

---

## S7: Usabilidad y Best Practices

_Cómo tú y tu equipo aprenden y mejoran el uso de IA._

_9 preguntas en esta sección._

### Pregunta `S7-Q1`: _Choice (multiple answers)_

> **S7-Q1: ¿Cómo APRENDISTE a usar Copilot/IA en desarrollo?**

Opciones:

- Autoaprendizaje (prueba y error)
- Workshop interno de la empresa
- Documentación oficial
- Videos de YouTube
- Curso online (Coursera, Udemy, MS Learn)
- Champion en el equipo
- Eventos / conferencias (Microsoft Build, GitHub Universe)
- Comunidades / Discord / Slack

### Pregunta `S7-Q2`: _Choice (single answer)_

> **S7-Q2: ¿Existe un AI/Copilot Champion en tu equipo/empresa que ayuda a otros?**

Opciones:

- Sí, soy yo
- Sí, otra persona
- No, pero debería haber
- No, cada quien se las arregla

### Pregunta `S7-Q3`: _Choice (single answer)_

> **S7-Q3: ¿Hay un canal/comunidad interna para discutir uso de IA en ingeniería?**

Opciones:

- Sí, activo (>5 mensajes/semana)
- Sí, poco activo
- No tenemos canal dedicado
- No sé

### Pregunta `S7-Q4`: _Choice (multiple answers)_

> **S7-Q4: ¿Tu organización MIDE productividad del dev de forma estructurada?**

Opciones:

- DORA metrics (lead time, deployment freq, MTTR, change failure)
- DX index (developer experience)
- SPACE framework
- Métricas de adopción de Copilot (active users)
- Self-report periódico (survey)
- No medimos formalmente

### Pregunta `S7-Q5`: _Choice (single answer)_

> **S7-Q5: ¿Cuántas iteraciones típicas de prompt necesitas antes de tener un buen resultado?**

Opciones:

- Acierta en el 1er intento
- 2-3 iteraciones
- 4-6 iteraciones
- 7+ iteraciones (frecuente)

### Pregunta `S7-Q6`: _Choice (single answer)_

> **S7-Q6: ¿Confías en el código generado por IA lo suficiente para mergearlo SIN revisar línea por línea?**

Opciones:

- Nunca, siempre reviso
- Para cambios triviales (sí)
- Frecuentemente (confío)
- Casi siempre

### Pregunta `S7-Q7`: _Choice (single answer)_

> **S7-Q7: ¿Con qué frecuencia detectas hallucinations, cuando la IA inventa APIs/métodos inexistentes?**

Opciones:

- Diariamente
- Semanalmente
- Rara vez
- Casi nunca

### Pregunta `S7-Q8`: _Choice (single answer)_

> **S7-Q8: Desde que adoptaste IA, ¿sientes que aprendes más o menos sobre ingeniería?**

Opciones:

- Aprendiendo MUCHO MÁS (IA acelera)
- Un poco más
- Más o menos igual
- Aprendiendo MENOS (dependencia)
- No sé evaluarlo

### Pregunta `S7-Q9`: _Choice (single answer)_

> **S7-Q9: ¿Compartes buenos prompts/ejemplos de uso con colegas en Spaces, Slack o Confluence?**

Opciones:

- Frecuentemente, en un canal compartido
- A veces, en persona
- Rara vez
- Nunca

---

## S8: Seguridad y Gobernanza

_Prácticas de seguridad en el uso de IA y gobernanza de agentes (alcance, red-lines, permisos JIT, auditoría)._

_13 preguntas en esta sección._

### Pregunta `S8-Q1`: _Choice (single answer)_

> **S8-Q1: ¿Tu organización tiene una POLÍTICA DOCUMENTADA de uso de IA en ingeniería?**

Opciones:

- Sí, política formal y clara
- Sí, pero poco clara
- Política informal (sin documento)
- No tenemos política
- No sé

### Pregunta `S8-Q2`: _Choice (single answer)_

> **S8-Q2: ¿Sabes QUÉ DATOS pueden ir a LLMs externas (Copilot, ChatGPT)?**

Opciones:

- Sé claramente qué se puede y qué NO se puede
- Tengo una idea general
- Vagamente
- No sé

### Pregunta `S8-Q3`: _Choice (multiple answers)_

> **S8-Q3: ¿Qué tipos de datos JAMÁS colocas en prompts de IA externa?**

Opciones:

- PII / datos personales de clientes
- Secrets / API keys / tokens
- Código de IP estratégico
- Datos financieros
- Datos de salud
- Ninguna restricción (no tenemos política)

### Pregunta `S8-Q4`: _Choice (multiple answers)_

> **S8-Q4: ¿Qué herramientas de SEGURIDAD están activas en tu repo?**

Opciones:

- GitHub Advanced Security (GHAS)
- CodeQL scanning
- Secret scanning
- Dependabot / dependency review
- SBOM (Software Bill of Materials)
- Microsoft Defender for DevOps
- Microsoft Defender for Cloud
- Snyk / SonarQube / otro SAST
- Ninguna

### Pregunta `S8-Q5`: _Choice (single answer)_

> **S8-Q5: ¿Code Scanning corre sobre código GENERADO por IA en el PR o IDE?**

Opciones:

- Sí, gate obligatorio en el PR
- Sí, opcional
- Corre pero no bloquea
- No corre

### Pregunta `S8-Q6`: _Choice (single answer)_

> **S8-Q6: ¿Tu organización genera SBOM de servicios críticos?**

Opciones:

- Sí, automatizado
- Sí, manual cuando se solicita
- No generamos
- No sé

### Pregunta `S8-Q7`: _Choice (single answer)_

> **S8-Q7: ¿Existe un proceso formal de REVIEW para código generado por IA antes del merge?**

Opciones:

- Sí, review obligatorio por otro humano + scanner
- Review humano obligatorio (sin scanner extra)
- Review opcional
- No tenemos proceso

### Pregunta `S8-Q8`: _Choice (single answer)_

> **S8-Q8: Cuando creas/usas un custom agent, ¿defines ALCANCE y RED-LINES explícitos?**

Opciones:

- Siempre, alcance + red-lines documentados
- Frecuentemente
- A veces
- Rara vez / nunca
- No creo/uso custom agents

### Pregunta `S8-Q9`: _Choice (single answer)_

> **S8-Q9: ¿Tu organización usa permisos JIT (Just-In-Time) para agentes versus permisos persistentes?**

Opciones:

- Sí, JIT obligatorio para agents
- Sí, opcional
- No tenemos JIT
- No sé

### Pregunta `S8-Q10`: _Choice (single answer)_

> **S8-Q10: ¿Tu organización tiene DLP configurado para evitar datos sensibles en prompts?**

Opciones:

- Sí, bloquea activamente
- Sí, alerta pero no bloquea
- No tenemos
- No sé

### Pregunta `S8-Q11`: _Choice (single answer)_

> **S8-Q11: ¿Tu organización tiene AUDIT LOGS de uso de Copilot/agentes IA, incluyendo decisiones autónomas de agents?**

Opciones:

- Sí, logs activos y revisados
- Logs activos pero no revisados
- No tenemos
- No sé

### Pregunta `S8-Q12`: _Choice (single answer)_

> **S8-Q12: ¿Ya recibiste entrenamiento formal de seguridad en el uso de IA?**

Opciones:

- Sí, entrenamiento obligatorio anual
- Sí, una vez (en el onboarding)
- No recibí entrenamiento
- No sé

### Pregunta `S8-Q13`: _Choice (single answer)_

> **S8-Q13: ¿Con qué frecuencia viste a Copilot/IA sugerir código con vulnerabilidad obvia?**

Opciones:

- Diariamente
- Semanalmente
- Mensualmente
- Casi nunca

---

## S9: Pain Points & Wishlist

_Tus ideas y frustraciones. Texto libre: responde con libertad._

_4 preguntas en esta sección._

### Pregunta `S9-Q1`: _Long Text (respuesta libre)_

> **S9-Q1: ¿QUÉ MÁS te frustra hoy en el uso de IA en tu día a día de ingeniería?**

### Pregunta `S9-Q2`: _Long Text (respuesta libre)_

> **S9-Q2: ¿Qué CAMBIO en herramienta/proceso duplicaría tu productividad?**

### Pregunta `S9-Q3`: _Long Text (respuesta libre)_

> **S9-Q3: ¿Qué feature/herramienta Microsoft/GitHub te gustaría que existiera o conocer mejor?**

### Pregunta `S9-Q4`: _Choice (single answer)_

> **S9-Q4: ¿Te gustaría recibir la versión consolidada de este survey (insights agregados de todo el equipo)?**

Opciones:

- Sí, quiero verla
- No, gracias

---

## Resumen final

- **9 secciones** (1 por tema)
- **75 preguntas** (55 choice + 15 multi + 5 long text)
- **Tiempo estimado:** 20-25 min (una pasada rápida toma unos 10 min)
- **Respuestas esperadas:** cuantos más desarrolladores, mejor: mínimo 5, ideal 15+

## Próximos pasos

1. Después de recopilar respuestas, ve a **Responses → Open in Excel** en Microsoft Forms
2. Renombra el Excel a `survey-devs-responses.xlsx`
3. Muévelo a la raíz del kit
4. En Copilot Chat (modo Agent): `/import-survey-devs`
5. Después ejecuta `/insights-developer-survey` para generar el informe consolidado
