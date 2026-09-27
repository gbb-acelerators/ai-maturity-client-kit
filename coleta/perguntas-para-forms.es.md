# Banco de preguntas para Microsoft Forms: AI-Assisted SDLC Maturity Assessment v2

> Generado a partir de `framework.v2.json` (versión 2.0.1) por `scripts/generate_v2_collection.py`. No lo edite a mano. Fuente del texto: [AI-Maturity-Form-Questions_v2.md](AI-Maturity-Form-Questions_v2.md). El banco v1 (158 preguntas) está archivado en [v1/](v1/).

## Cómo armar el formulario

1. Vaya a <https://forms.office.com> y cree un formulario en blanco. Título sugerido: `AI-Assisted SDLC Maturity Assessment v2 - <Organización>`.
2. Pegue el aviso de privacidad de [../kit-es/INSTRUCCIONES-FORMS.md](../kit-es/INSTRUCCIONES-FORMS.md) en la descripción del formulario.
3. Agregue **10 secciones**: Sección 0 (perfil) y una por dimensión, D1 a D9.
4. Sección 0: agregue las 5 preguntas de perfil como **Choice**. `R-Q3` permite varias respuestas. No puntúan.
5. Para cada pregunta puntuada agregue 2 elementos: un **Choice** (respuesta única) cuyo título empieza con el ID y dos puntos (por ejemplo `D4-Q3: ...`), con las 6 opciones de abajo en orden; y un **Long Text** opcional con el título `Evidence (<ID>)`.
6. Pegue las líneas **L3 se ve así** y **L4 se ve así** en el subtítulo de la pregunta.
7. Comparta el enlace. Busque al menos 3 personas por rol (`R-Q1`).
8. `Responses` > `Open in Excel`, descargue el archivo y ejecute `make import XLSX=<archivo>`.

Total de elementos: 5 de perfil + 61 puntuadas + 61 campos opcionales de evidencia = 127 elementos.

## Las 6 opciones de toda pregunta puntuada

- **L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad**
- **L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)**
- **L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)**
- **L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)**
- **L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados**
- **NA - No sé / No aplica**

> Mantenga el prefijo `L0` a `L4` y `NA` al inicio de cada opción y el ID al inicio de cada título: el importador depende de ambos. Mantenga también la etiqueta `Evidence (<ID>)` en inglés.

## Cómo responder

- Lea cada pregunta como "¿en qué medida esto es cierto?".
- Responda en el nivel más alto en que **todas** las partes de la pregunta son ciertas.
- Si cobertura, gobernanza y medición indican niveles distintos, elija el menor.
- Elija `L0` cuando la práctica podría aplicar pero todavía no existe; elija `NA` solo cuando no sabe o la actividad no existe en su alcance.

---

## Sección 0: Perfil de la persona que responde (no puntúa)

### R-Q1: Rol principal

**R-Q1: ¿Qué opción describe mejor tu rol principal?**

_Choice, respuesta única_

- Software engineer / developer
- Engineering manager / tech lead
- Arquitecto
- Platform / DevOps / SRE engineer
- Security / AppSec
- QA / test engineer
- Product / program manager
- Executive (CTO, VP, Director)
- Otro

### R-Q2: Alcance de tus respuestas

**R-Q2: ¿En qué alcance se basan tus respuestas?**

_Choice, respuesta única_

- Un solo equipo
- Varios equipos en una unidad de negocio
- Una unidad de negocio
- Toda la organización

### R-Q3: Herramientas principales de AI coding

**R-Q3: ¿Qué herramientas de IA usas al menos semanalmente para trabajo de software? (múltiples respuestas)**

_Choice, varias respuestas_

- GitHub Copilot en el IDE (completions, chat, agent mode)
- GitHub Copilot cloud agent / code review / CLI
- Claude Code o Claude en otros clientes
- Herramientas internas basadas en Microsoft Foundry / Azure OpenAI
- Otras herramientas comerciales de AI coding
- Modelos internos o self-hosted
- Ninguna

### R-Q4: Experiencia profesional

**R-Q4: ¿Cuántos años de experiencia profesional en software tienes?**

_Choice, respuesta única_

- Menos de 2
- 2-5
- 6-10
- Más de 10

### R-Q5: Tiempo hands-on

**R-Q5: En una semana típica, ¿cuánto de tu tiempo es hands-on construyendo (code, configuración, pruebas)?**

_Choice, respuesta única_

- Menos de 20%
- 20-50%
- 51-80%
- Más de 80%

---

## Sección D1: Estrategia, política y gobernanza de IA

_7 preguntas. Por qué importa: DORA identifica una "postura de IA clara y comunicada" como amplificadora de los beneficios de la IA [1]; Microsoft CAF exige que "todo agente debe ser observable, gobernado y seguro" [19]._

### D1-Q1: Estrategia de IA para ingeniería de software

**D1-Q1: ¿Existe una estrategia documentada de IA para ingeniería de software, patrocinada por liderazgo, que declare objetivos explícitos y se comunique a todos los equipos de ingeniería?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Estrategia publicada y revisada al menos anualmente; los objetivos (por ejemplo entrega, calidad, developer experience) tienen responsables; la mayoría de los ingenieros puede decir dónde encontrarla.
- **L4 se ve así:** La estrategia se revisa a partir de resultados medidos (D9) y se vincula a OKRs de negocio; el progreso se informa al liderazgo con una cadencia fija.
- **Ejemplos de evidencia:** Documento de estrategia, comunicación de liderazgo, entradas de OKR.
- **Campo de evidencia:** `Evidence (D1-Q1)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D1-Q2: Política de uso aceptable

**D1-Q2: ¿Está claro para los ingenieros cómo pueden y no pueden usar IA en el trabajo, incluidos qué datos pueden compartirse con herramientas de IA?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** La política escrita de uso aceptable cubre code, datos de clientes, secretos e IP de terceros; es parte del onboarding; las excepciones tienen un responsable.
- **L4 se ve así:** La política se aplica mediante controles técnicos (por ejemplo content exclusion, prevención de pérdida de datos, allowlists) y se audita; las violaciones disparan alertas automatizadas.
- **Ejemplos de evidencia:** Enlace de la política, checklist de onboarding, configuración de controles.
- **Campo de evidencia:** `Evidence (D1-Q2)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D1-Q3: Herramientas y modelos aprobados

**D1-Q3: ¿Existe un catálogo mantenido de herramientas, funciones y modelos de IA aprobados para desarrollo de software, gestionado mediante políticas enterprise o de la organización?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Las políticas enterprise/de la organización habilitan solo funciones y modelos aprobados; el catálogo lista responsable, manejo de datos y fecha de revisión para cada herramienta.
- **L4 se ve así:** Los nuevos modelos y herramientas pasan por una evaluación definida (calidad, costo, seguridad) antes de habilitarse; los retirados se eliminan según cronograma.
- **Ejemplos de evidencia:** Configuraciones de política de Copilot, catálogo de herramientas, registros de evaluación de modelos.
- **Campo de evidencia:** `Evidence (D1-Q3)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D1-Q4: Protección de datos, IP y residencia

**D1-Q4: ¿Los requisitos de residencia, retención, propiedad intelectual y privacidad de datos están definidos y aplicados a las herramientas y agentes de IA usados en el SDLC?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Los requisitos se documentan por herramienta; repositorios o archivos sensibles se excluyen del contexto de IA; la retención de logs y memoria sigue la política.
- **L4 se ve así:** El cumplimiento se evalúa continuamente (por ejemplo con un compliance manager) y se mapea a regulaciones como el EU AI Act cuando aplica.
- **Ejemplos de evidencia:** Registros de procesamiento de datos, configuraciones de exclusión, política de retención.
- **Campo de evidencia:** `Evidence (D1-Q4)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D1-Q5: Niveles de autonomía para trabajo con IA

**D1-Q5: ¿La organización definió qué tareas son lideradas por desarrollador, realizadas por desarrollador con agente, o totalmente lideradas por agente, y los controles requeridos para cada nivel?**

- **Nota de alcance:** Mide la política que define niveles de autonomía. Cómo se escriben las tareas para agentes es D3-Q3; con qué frecuencia se delega el trabajo es D4-Q3.
- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Una matriz publicada mapea tipos de tarea (por ejemplo upgrades de dependencias, generación de pruebas, trabajo de feature, cambios en producción) a niveles de autonomía y aprobaciones requeridas.
- **L4 se ve así:** La matriz se aplica mediante reglas de plataforma (por ejemplo branch protection, revisores requeridos por ruta) y se actualiza a partir de datos de incidentes y calidad.
- **Ejemplos de evidencia:** Matriz de autonomía, rulesets de repositorio, registros de cambios.
- **Campo de evidencia:** `Evidence (D1-Q5)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D1-Q6: IA responsable y framework de riesgo

**D1-Q6: ¿El uso de IA en ingeniería de software está gobernado por un estándar de IA responsable y un framework de riesgo reconocido (por ejemplo Microsoft Responsible AI Standard, NIST AI RMF, ISO/IEC 42001)?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Se adopta un framework nombrado; los riesgos relacionados con IA están en el registro de riesgos con responsables y revisiones.
- **L4 se ve así:** Los controles del framework se auditan interna o externamente; los resultados retroalimentan política y tooling.
- **Ejemplos de evidencia:** Mapeo del framework, entradas del registro de riesgos, informes de auditoría.
- **Campo de evidencia:** `Evidence (D1-Q6)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D1-Q7: Registro e identidad de agentes

**D1-Q7: ¿Todo agente de IA usado en el SDLC (coding agents, review agents, custom agents, pipeline agents) está registrado con un responsable, un propósito, una identidad distinta y un alcance de acceso definido?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Un único inventario lista todos los agentes con responsable, plataforma y permisos; cada agente se ejecuta bajo su propia identidad, no una cuenta humana compartida.
- **L4 se ve así:** Los agentes no registrados ("shadow") se detectan automáticamente; el ciclo de vida de identidad (creación, revisión, eliminación) está automatizado.
- **Ejemplos de evidencia:** Inventario de agentes, configuración de identidad (por ejemplo Microsoft Entra Agent ID), revisiones de acceso.
- **Campo de evidencia:** `Evidence (D1-Q7)` · _Herramienta, % de cobertura, métrica, período, enlace_

---

## Sección D2: Habilitación, habilidades y cultura

_6 preguntas. Por qué importa: Gartner espera que GenAI requiera que 80% de la fuerza laboral de ingeniería se capacite en nuevas habilidades hasta 2027 [30]; DORA pregunta sobre capacitación, aprendizaje entre pares y apoyo para la experimentación [2]._

### D2-Q1: Capacitación estructurada de IA

**D2-Q1: ¿Los ingenieros reciben capacitación estructurada en las herramientas de IA aprobadas y workflows de agentes, más allá del onboarding predeterminado del proveedor?**

- **Unidad de cobertura:** ingenieros
- **L3 se ve así:** Currículo basado en rol (desarrollador, revisor, plataforma, seguridad) con finalización rastreada; la capacitación se exige antes de habilitar funciones de agentes; enseña patrones que preservan el aprendizaje (pedir explicaciones, intentar primero, luego comparar) y no solo delegación total.
- **L4 se ve así:** El currículo se actualiza cada trimestre a partir de datos de uso y patrones de falla; existen rutas avanzadas (orquestación de agentes, evaluación).
- **Ejemplos de evidencia:** Rutas de aprendizaje, tasas de finalización, reglas de bloqueo de habilitación.
- **Campo de evidencia:** `Evidence (D2-Q1)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D2-Q2: Aprendizaje entre pares y champions

**D2-Q2: ¿Existen formatos regulares de aprendizaje entre pares (demos, brown bags, office hours) y una red de champions de IA en los equipos?**

- **Unidad de cobertura:** equipos
- **L3 se ve así:** Existen champions en la mayoría de los equipos; las sesiones se realizan al menos mensualmente; las grabaciones y ejemplos se comparten en un solo lugar.
- **L4 se ve así:** Una comunidad de práctica cura activos reutilizables (instrucciones, archivos de prompt, agentes) y mide su reutilización.
- **Ejemplos de evidencia:** Lista de champions, calendario de sesiones, repositorio compartido de ejemplos.
- **Campo de evidencia:** `Evidence (D2-Q2)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D2-Q3: Apoyo para la experimentación

**D2-Q3: ¿La organización da a los ingenieros tiempo, sandboxes y presupuesto para experimentar con seguridad con nuevas herramientas de IA y patrones de agentes?**

- **Unidad de cobertura:** equipos
- **L3 se ve así:** Existen entornos en sandbox y una ruta liviana de solicitud; los experimentos se registran y sus resultados se comparten.
- **L4 se ve así:** Los experimentos exitosos pasan al catálogo aprobado (D1-Q3) mediante una ruta definida en semanas.
- **Ejemplos de evidencia:** Suscripciones de sandbox, log de experimentos, registros de promoción.
- **Campo de evidencia:** `Evidence (D2-Q3)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D2-Q4: Habilidades de ingeniería de contexto

**D2-Q4: ¿Los ingenieros están capacitados para dar a las herramientas de IA el contexto correcto (alcance claro de la tarea, archivos relevantes, restricciones, ejemplos) y mantener el contexto ajustado?**

- **Unidad de cobertura:** ingenieros
- **L3 se ve así:** La orientación y los ejemplos sobre ingeniería de contexto son parte de la capacitación; los equipos revisan la calidad de sus instrucciones y prompts.
- **L4 se ve así:** Las prácticas de contexto se miden (por ejemplo tasa de éxito o uso de tokens por tarea) y se mejoran con el tiempo.
- **Ejemplos de evidencia:** Páginas de orientación, checklists de review, métricas antes/después.
- **Campo de evidencia:** `Evidence (D2-Q4)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D2-Q5: Roles y trayectorias de carrera

**D2-Q5: ¿Se actualizaron descripciones de puesto, frameworks de carrera y expectativas de desempeño para ingeniería asistida por IA y agentic engineering (por ejemplo dirigir agentes, revisar salida de IA, ingeniería de IA)?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Se publican perfiles de rol actualizados; las evaluaciones de desempeño reconocen el uso efectivo de IA y la calidad del review, no el volumen bruto de salida.
- **L4 se ve así:** Existen roles dedicados (por ejemplo ingeniero de IA, responsable de plataforma de agentes) con una ruta clara de crecimiento.
- **Ejemplos de evidencia:** Framework de carrera, descripciones de rol.
- **Campo de evidencia:** `Evidence (D2-Q5)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D2-Q6: Onboarding asistido por IA

**D2-Q6: ¿Los nuevos ingenieros usan herramientas de IA para entender codebases y volverse productivos, con tiempo de ramp-up medido?**

- **Unidad de cobertura:** ingenieros
- **L3 se ve así:** El onboarding incluye recorridos de codebase guiados por IA e instrucciones de repositorio; se rastrea el tiempo hasta el primer PR mergeado; los nuevos ingenieros son evaluados en lectura de code y debugging, no solo en salida.
- **L4 se ve así:** Las métricas de ramp-up y habilidades se comparan entre cohortes y se usan para mejorar material e instrucciones de onboarding.
- **Ejemplos de evidencia:** Playbook de onboarding, datos de tiempo hasta primer PR, resultados de verificación de habilidades.
- **Campo de evidencia:** `Evidence (D2-Q6)` · _Herramienta, % de cobertura, métrica, período, enlace_

---

## Sección D3: Planificar, especificar y diseñar

_6 preguntas. Por qué importa: en agentic coding, "las personas toman la mayoría de las decisiones de planificación (qué hacer) y Claude toma la mayoría de las decisiones de ejecución (cómo hacerlo)" [24]; la calidad de la definición de la tarea impulsa la calidad de la salida del agente [8], [27]._

### D3-Q1: IA en refinamiento de backlog

**D3-Q1: ¿Se usa IA para redactar y refinar issues o user stories, incluidos criterios de aceptación, con un responsable humano que las aprueba?**

- **Unidad de cobertura:** equipos
- **L3 se ve así:** La mayoría de los equipos usa IA para redactar o mejorar elementos de trabajo; los criterios de aceptación son obligatorios antes de comenzar el trabajo.
- **L4 se ve así:** La calidad de los elementos de trabajo (claridad, capacidad de prueba) se mide y se vincula con retrabajo y cycle time.
- **Ejemplos de evidencia:** Templates de issue, ejemplos de elementos de trabajo, verificaciones de calidad.
- **Campo de evidencia:** `Evidence (D3-Q1)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D3-Q2: Especificación antes de la implementación

**D3-Q2: Para cambios no triviales, ¿se produce y revisa un plan o especificación por escrito antes de que un agente de IA implemente el cambio?**

- **Unidad de cobertura:** equipos
- **L3 se ve así:** Los planes o specs se almacenan en el repositorio o se vinculan a la issue, y un humano los revisa antes de la implementación por el agente.
- **L4 se ve así:** Las specs son el contrato para verificación automatizada (pruebas, checks) y se mantienen sincronizadas con el code.
- **Ejemplos de evidencia:** Archivos de spec, reviews de plan, PRs que referencian specs.
- **Campo de evidencia:** `Evidence (D3-Q2)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D3-Q3: Alcance de tareas para agentes

**D3-Q3: ¿Las tareas dadas a coding agents están bien delimitadas (pequeñas, con criterios de aceptación claros y punteros a code relevante) antes de asignarse?**

- **Nota de alcance:** Mide cómo se delimitan las tareas para agentes. La política de autonomía es D1-Q5; el volumen de delegación es D4-Q3.
- **Unidad de cobertura:** equipos
- **L3 se ve así:** Los equipos siguen orientación escrita para issues listas para agentes; las tareas demasiado grandes se dividen antes de la asignación.
- **L4 se ve así:** El éxito de tareas de agentes y las tasas de retrabajo se rastrean por tipo de tarea y se usan para refinar la orientación.
- **Ejemplos de evidencia:** Directrices de tareas para agentes, ejemplos de issues, datos de tasa de éxito.
- **Campo de evidencia:** `Evidence (D3-Q3)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D3-Q4: Decisiones de arquitectura y diseño

**D3-Q4: ¿Se usa IA para apoyar el trabajo de diseño (análisis de opciones, modos de amenaza y falla, architecture decision records) mientras las decisiones permanecen con humanos responsables?**

- **Unidad de cobertura:** equipos
- **L3 se ve así:** Los ADRs se versionan; se adjunta análisis asistido por IA; un humano nombrado aprueba cada decisión.
- **L4 se ve así:** Los agentes verifican nuevos cambios contra decisiones registradas y señalan conflictos automáticamente.
- **Ejemplos de evidencia:** Repositorio de ADR, registros de design review.
- **Campo de evidencia:** `Evidence (D3-Q4)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D3-Q5: Enfoque centrado en el usuario

**D3-Q5: ¿El trabajo asistido por IA está vinculado a resultados claros para usuarios e informado por feedback de usuarios?**

- **Unidad de cobertura:** equipos
- **L3 se ve así:** Los elementos de trabajo referencian el problema del usuario y la medida de éxito; el feedback se revisa antes de priorizar.
- **L4 se ve así:** Las métricas de resultado del usuario son parte de la definition of done para entrega asistida por IA.
- **Ejemplos de evidencia:** Briefs de producto, registros de loop de feedback, dashboards de resultados.
- **Campo de evidencia:** `Evidence (D3-Q5)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D3-Q6: Modernización asistida por IA

**D3-Q6: ¿Se usan herramientas y agentes de IA para entender, hacer upgrade y migrar code legado (por ejemplo upgrades de framework o runtime, migración a cloud), con resultados verificados por pruebas?**

- **Unidad de cobertura:** equipos
- **L3 se ve así:** Existe un proceso repetible de modernización asistida por IA para tipos comunes de upgrade, con gates de prueba.
- **L4 se ve así:** El backlog de modernización se reduce continuamente mediante agentes bajo review humano, con tasas de éxito rastreadas.
- **Ejemplos de evidencia:** Runbooks de upgrade, PRs de migración, resultados de pruebas.
- **Campo de evidencia:** `Evidence (D3-Q6)` · _Herramienta, % de cobertura, métrica, período, enlace_

---

## Sección D4: Code e ingeniería de contexto

_8 preguntas. Por qué importa: GitHub mide la profundidad de adopción como una progresión de "Code first" a "Agent first" y "Multi-agent" [6]; Anthropic describe el contexto como "un recurso finito con retornos marginales decrecientes" [25]._

### D4-Q1: Profundidad de uso de IA entre superficies

**D4-Q1: ¿Qué tan profundamente usan IA los ingenieros entre superficies: completions y ediciones de agentes en el IDE, superficies de agentes de GitHub (cloud agent, code review, CLI), y varios agentes juntos?**

- **Nota de alcance:** Mide qué tan profundamente se usa IA. Si ese uso se mide es D9-Q1.
- **Unidad de cobertura:** ingenieros
- **L1 a L2 se ven así:** Principalmente completions y chat ("Code first").
- **L3 se ve así:** Muchos ingenieros usan regularmente al menos una superficie de agente de GitHub ("Agent first"), confirmado por métricas de uso.
- **L4 se ve así:** El uso multi-agent es normal ("Multi-agent"), con distribución de cohortes rastreada mensualmente.
- **Ejemplos de evidencia:** Dashboard o API de métricas de uso de Copilot: distribución de cohortes de adopción, usuarios activos diarios/semanales.
- **Campo de evidencia:** `Evidence (D4-Q1)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D4-Q2: Modo agente para trabajo multi-file

**D4-Q2: ¿Los ingenieros usan IDE agent mode (o equivalente) para cambios multi-file, y revisan cada cambio antes de hacer commit?**

- **Unidad de cobertura:** ingenieros
- **L3 se ve así:** Agent mode es el valor predeterminado para refactors y features multi-file en la mayoría de los equipos; los cambios se revisan en el diff antes del commit.
- **L4 se ve así:** Los equipos comparten patrones de agent mode que funcionan y rastrean dónde falla; los permisos de herramientas se ajustan por repositorio.
- **Ejemplos de evidencia:** Uso por feature/mode, directrices del equipo.
- **Campo de evidencia:** `Evidence (D4-Q2)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D4-Q3: Delegación a coding agents

**D4-Q3: ¿Se asignan issues a coding agents (por ejemplo Copilot cloud agent) y estos producen pull requests que se mergean después de review humano?**

- **Nota de alcance:** Mide cuánto trabajo se delega a coding agents. La política de autonomía es D1-Q5; el alcance de tareas es D3-Q3.
- **Unidad de cobertura:** equipos
- **L3 se ve así:** La mayoría de los equipos delega issues adecuadas a un coding agent; se rastrea la proporción de PRs mergeados creados por agentes.
- **L4 se ve así:** La tasa de merge de PRs de agentes, el retrabajo y la tasa de correcciones post-merge se rastrean por tipo de tarea; las reglas de delegación (D1-Q5) se ajustan a partir de estos datos.
- **Ejemplos de evidencia:** Conteos de PRs creados por agentes, tasa de merge, tiempo hasta merge, correcciones de seguimiento.
- **Campo de evidencia:** `Evidence (D4-Q3)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D4-Q4: Instrucciones de repositorio

**D4-Q4: ¿Los repositorios contienen custom instructions versionadas y revisadas para herramientas de IA (por ejemplo `.github/copilot-instructions.md`, `AGENTS.md`) que describen build, test, convenciones y restricciones?**

- **Unidad de cobertura:** repositorios
- **L3 se ve así:** La mayoría de los repositorios activos tiene instrucciones estructuradas (build, test, convenciones, restricciones) con un responsable; los cambios pasan por PR review; los archivos se actualizan cuando el codebase cambia en vez de commitarlos una sola vez.
- **L4 se ve así:** Las instrucciones se generan a partir de una base compartida, se verifican por obsolescencia, y se mide su efecto en la tasa de merge de agentes y calidad de code, ya que los archivos de instrucciones por sí solos no garantizan mejores resultados.
- **Ejemplos de evidencia:** Archivos de instrucciones, cobertura entre repositorios, historial de cambios, métricas antes/después de PRs de agentes.
- **Campo de evidencia:** `Evidence (D4-Q4)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D4-Q5: Prompts, agentes y skills reutilizables

**D4-Q5: ¿Existe una biblioteca compartida y curada de archivos de prompt, custom agents y skills reutilizables, con responsables y versionado?**

- **Unidad de cobertura:** equipos
- **L3 se ve así:** Un repositorio central contiene archivos de prompt y custom agents aprobados; los equipos los reutilizan en vez de copiarlos.
- **L4 se ve así:** Los activos se evalúan antes del release (calidad, costo), el uso se rastrea y los activos no usados se retiran.
- **Ejemplos de evidencia:** Repositorio de biblioteca, perfiles de custom agents, métricas de reutilización.
- **Campo de evidencia:** `Evidence (D4-Q5)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D4-Q6: Gobernanza de MCP servers

**D4-Q6: ¿Los MCP servers y otras herramientas de agentes se gobiernan mediante una allowlist o registry, con herramientas acotadas y responsables nombrados?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Se aplica una allowlist enterprise de MCP o un registry customizado; cada server tiene un responsable, una security review y herramientas limitadas.
- **L4 se ve así:** Las tool calls se registran y revisan; los nuevos servers pasan security checks automatizados antes de agregarse.
- **Ejemplos de evidencia:** Política de allowlist o registry, configuración de MCP, registros de review.
- **Campo de evidencia:** `Evidence (D4-Q6)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D4-Q7: Acceso de IA al conocimiento interno

**D4-Q7: ¿Las herramientas y agentes de IA pueden usar de forma segura fuentes internas (code, documentación, wikis, elementos de trabajo) como contexto, mediante conectores aprobados?**

- **Unidad de cobertura:** equipos
- **L3 se ve así:** Los conectores aprobados dan a las herramientas de IA acceso consciente de permisos a las principales fuentes internas; las respuestas citan material interno.
- **L4 se ve así:** Las fuentes de conocimiento se curan para uso de IA (actualidad, ownership) y se evalúa la calidad de retrieval.
- **Ejemplos de evidencia:** Configuración de conectores, evaluaciones de retrieval.
- **Campo de evidencia:** `Evidence (D4-Q7)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D4-Q8: Selección y enrutamiento de modelos

**D4-Q8: ¿La elección del modelo se ajusta a la complejidad de la tarea (modelos más pequeños para trabajo rutinario, frontier models para trabajo complejo), mediante orientación o enrutamiento automático?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** La orientación escrita mapea tipos de tarea a modelos; los modelos predeterminados se establecen por política.
- **L4 se ve así:** El enrutamiento automático está implementado y se ajusta con datos de costo y calidad.
- **Ejemplos de evidencia:** Orientación de modelos, configuraciones de política, configuración de enrutamiento.
- **Campo de evidencia:** `Evidence (D4-Q8)` · _Herramienta, % de cobertura, métrica, período, enlace_

---

## Sección D5: Review, calidad y pruebas

_7 preguntas. Por qué importa: DORA vincula el volumen de cambios impulsados por IA con la inestabilidad, a menos que existan sistemas de control sólidos [3]; GitHub exige revisión humana antes de que se mergeen PRs de agentes [7]; 46% de los desarrolladores desconfían de la precisión de la salida de IA [37]._

### D5-Q1: AI-assisted code review

**D5-Q1: ¿AI code review (por ejemplo Copilot code review) se aplica a pull requests, con un revisor humano aún responsable de la aprobación?**

- **Unidad de cobertura:** repositorios
- **L3 se ve así:** AI review se ejecuta automáticamente en la mayoría de los PRs; los equipos rastrean sugerencias útiles versus descartadas.
- **L4 se ve así:** Las reglas de review se ajustan por repositorio a partir de los resultados de sugerencias; se rastrean tiempo de review y defectos escapados; los PRs donde solo IA revisó code creado por IA son visibles y gobernados.
- **Ejemplos de evidencia:** Rulesets de repositorio, métricas de adopción de code review, resultados de sugerencias.
- **Campo de evidencia:** `Evidence (D5-Q1)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D5-Q2: Human-in-the-loop para cambios de agentes

**D5-Q2: ¿Los pull requests creados por agentes requieren aprobación humana independiente (no el solicitante), con workflow runs aprobadas antes de ejecutarse?**

- **Unidad de cobertura:** repositorios
- **L3 se ve así:** Se mantienen las protecciones predeterminadas: los PRs de agentes necesitan un aprobador independiente; "Approve and run workflows" no se deshabilita sin una decisión de riesgo documentada.
- **L4 se ve así:** Los requisitos de aprobación escalan con el riesgo (D1-Q5) y se auditan; las excepciones expiran automáticamente.
- **Ejemplos de evidencia:** Rulesets, branch protection, configuraciones de agentes.
- **Campo de evidencia:** `Evidence (D5-Q2)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D5-Q3: Mismos quality gates para code de IA y humano

**D5-Q3: ¿Los cambios generados por IA y creados por agentes pasan los mismos checks requeridos (build, tests, linting, security scans, coverage) que los cambios humanos?**

- **Unidad de cobertura:** repositorios
- **L3 se ve así:** Los checks requeridos se aplican mediante rulesets en los protected branches de la mayoría de los repositorios, sin bypass para identidades de agentes.
- **L4 se ve así:** Los gates son policy as code, aplicados en todos los repositorios (>90%) y revisados después de incidentes.
- **Ejemplos de evidencia:** Rulesets, checks requeridos, listas de bypass.
- **Campo de evidencia:** `Evidence (D5-Q3)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D5-Q4: Lotes pequeños

**D5-Q4: ¿Los cambios se mantienen pequeños (límites de tamaño de PR, un tema por PR), incluidos los cambios producidos por agentes?**

- **Nota de alcance:** Mide el tamaño de cambios asistidos por IA. Con qué frecuencia se commitea code y qué tan rápido se revierte es D8-Q2.
- **Unidad de cobertura:** equipos
- **L3 se ve así:** La orientación de tamaño de PR se aplica o monitorea; los PRs de agentes demasiado grandes se dividen antes del review.
- **L4 se ve así:** El tamaño de lote se rastrea contra change failure rate y tiempo de review, y se usa para ajustar límites.
- **Ejemplos de evidencia:** Distribución de tamaño de PR, configuración de bot o ruleset.
- **Campo de evidencia:** `Evidence (D5-Q4)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D5-Q5: Pruebas asistidas por IA

**D5-Q5: ¿Se usa IA para generar y mantener pruebas, con calidad de pruebas verificada (por ejemplo coverage del code cambiado, mutation testing) en vez de solo conteo de pruebas?**

- **Nota de alcance:** Mide IA usada para escribir y mejorar pruebas. Si las pruebas automatizadas actúan como gate es D8-Q7.
- **Unidad de cobertura:** equipos
- **L3 se ve así:** La mayoría de los equipos usa IA para escribir pruebas; coverage de líneas cambiadas es un check requerido.
- **L4 se ve así:** La efectividad de pruebas (mutation score, defectos escapados) se rastrea; flaky tests se detectan y se ponen en cuarentena automáticamente.
- **Ejemplos de evidencia:** Informes de coverage, resultados de mutation testing, dashboard de flaky tests.
- **Campo de evidencia:** `Evidence (D5-Q5)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D5-Q6: Cultura de verificación y confianza calibrada

**D5-Q6: ¿Los ingenieros verifican sistemáticamente la salida de IA (la ejecutan, la prueban, la leen) y se mide la confianza en la salida de IA con el tiempo?**

- **Nota de alcance:** Mide comportamiento de review y calibración de confianza. Cómo se encuesta developer experience es D9-Q4.
- **Unidad de cobertura:** equipos
- **L3 se ve así:** Las directrices de review explican qué verificar en la salida de IA; la confianza en la salida de IA es parte de la encuesta a desarrolladores.
- **L4 se ve así:** La confianza y la precisión se comparan con datos reales de defectos, y la orientación se actualiza donde divergen.
- **Ejemplos de evidencia:** Directrices de review, resultados de encuesta, análisis de defectos.
- **Campo de evidencia:** `Evidence (D5-Q6)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D5-Q7: Salud del code generado por IA

**D5-Q7: ¿Se monitorea la salud de largo plazo del code generado por IA (duplicación, churn, complejidad, mantenibilidad)?**

- **Unidad de cobertura:** repositorios
- **L3 se ve así:** Se recopilan métricas de code health para la mayoría de los repositorios y se revisan en retrospectivas de equipo; el code generado por IA tiene un responsable humano nombrado.
- **L4 se ve así:** Las tendencias de salud (por ejemplo complejidad cognitiva, advertencias de static analysis) se comparan entre code con alta presencia de IA y otro code, con acciones correctivas rastreadas.
- **Ejemplos de evidencia:** Dashboards de static analysis, informes de churn, archivos de ownership.
- **Campo de evidencia:** `Evidence (D5-Q7)` · _Herramienta, % de cobertura, métrica, período, enlace_

---

## Sección D6: Seguridad y AI Supply Chain

_7 preguntas. Por qué importa: OWASP enumera prompt injection (LLM01), supply chain (LLM03) y agencia excesiva (LLM06) entre los principales riesgos [38], y agent goal hijack (ASI01) en primer lugar para aplicaciones agentic [39]; NIST SP 800-218A agrega prácticas específicas de IA al SSDF [40]._

### D6-Q1: Scanning de base en todo repositorio

**D6-Q1: ¿Code scanning (SAST), secret scanning con push protection y dependency review se aplican a todos los repositorios, incluidas branches de agentes?**

- **Unidad de cobertura:** repositorios
- **L3 se ve así:** Habilitado por defecto para todos los repositorios nuevos y la mayoría de los existentes; push protection se aplica a todo commit, humano o de agente; las alertas tienen responsables y objetivos de nivel de servicio.
- **L4 se ve así:** La cobertura es casi completa y se verifica automáticamente; mean time to remediate se rastrea.
- **Ejemplos de evidencia:** Dashboard de cobertura de seguridad, tiempo de remediación.
- **Campo de evidencia:** `Evidence (D6-Q1)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D6-Q2: Remediación asistida por IA

**D6-Q2: ¿Se usa remediación asistida por IA (por ejemplo autofix para code scanning) para corregir vulnerabilidades, con correcciones revisadas y probadas antes del merge?**

- **Unidad de cobertura:** repositorios
- **L3 se ve así:** Las sugerencias de autofix están habilitadas para la mayoría de los repositorios; se rastrean tasas de aceptación y reapertura.
- **L4 se ve así:** Las campañas de seguridad usan remediación con IA a escala, y el tiempo de remediación se informa al liderazgo.
- **Ejemplos de evidencia:** Configuraciones de autofix, métricas de remediación.
- **Campo de evidencia:** `Evidence (D6-Q2)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D6-Q3: Defensas contra prompt injection para agentes

**D6-Q3: ¿Los agentes están protegidos contra prompt injection y goal hijack (contenido no confiable tratado como datos, instrucciones ocultas filtradas, egress de red restringido)?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Agent firewalls y restricciones de egress se mantienen activados; la orientación indica a los equipos qué fuentes de contenido no son confiables.
- **L4 se ve así:** Los agentes pasan regularmente por red team contra escenarios OWASP LLM01 y ASI01; los hallazgos se rastrean hasta el cierre.
- **Ejemplos de evidencia:** Configuración de firewall, informes de red team.
- **Campo de evidencia:** `Evidence (D6-Q3)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D6-Q4: Least privilege para agentes

**D6-Q4: ¿Los agentes se ejecutan con least privilege (tokens con alcance, sin secretos de producción, branches restringidos, entornos en sandbox)?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Los permisos de agentes se documentan y revisan; los agentes no pueden acceder a credenciales de producción ni hacer push a protected branches.
- **L4 se ve así:** Los permisos son just-in-time y limitados en el tiempo; el acceso se revisa automáticamente.
- **Ejemplos de evidencia:** Configuración de entorno de agentes, alcances de token, revisiones de acceso.
- **Campo de evidencia:** `Evidence (D6-Q4)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D6-Q5: AI supply chain

**D6-Q5: ¿Modelos, MCP servers, extensiones de IDE y herramientas de agentes se evalúan antes del uso, con procedencia y SBOMs para lo que construyen y entregan?**

- **Unidad de cobertura:** repositorios
- **L3 se ve así:** Un proceso de review cubre componentes de IA; SBOMs y procedencia de build se producen para la mayoría de los builds.
- **L4 se ve así:** La procedencia se verifica en el deploy (por ejemplo metas de nivel SLSA); los componentes no evaluados se bloquean automáticamente.
- **Ejemplos de evidencia:** Registros de review de componentes, muestras de SBOM y atestación.
- **Campo de evidencia:** `Evidence (D6-Q5)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D6-Q6: Threat modeling para features y agentes de IA

**D6-Q6: ¿Las features de IA y workflows agentic se someten a threat modeling con riesgos específicos de IA (OWASP LLM and Agentic Top 10, NIST SP 800-218A)?**

- **Unidad de cobertura:** servicios
- **L3 se ve así:** Se requieren threat models para nuevas features de IA y workflows de agentes, y seguridad los revisa.
- **L4 se ve así:** Los threat models se actualizan después de incidentes y ejercicios de red team; los controles se verifican mediante pruebas automatizadas.
- **Ejemplos de evidencia:** Documentos de threat model, registros de security review.
- **Campo de evidencia:** `Evidence (D6-Q6)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D6-Q7: Rastro de auditoría para acciones de agentes

**D6-Q7: ¿Las sesiones y acciones de agentes (prompts, tool calls, commits, aprobaciones) se registran, son atribuibles a una identidad y se retienen según la política?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** La actividad de agentes se registra centralmente y se vincula con el usuario solicitante y la identidad del agente.
- **L4 se ve así:** Los logs alimentan detección de anomalías; las auditorías pueden reconstruir cualquier cambio de agente de punta a punta.
- **Ejemplos de evidencia:** Configuración de audit log, ejemplo de investigación.
- **Campo de evidencia:** `Evidence (D6-Q7)` · _Herramienta, % de cobertura, métrica, período, enlace_

---

## Sección D7: Entregar y operar

_6 preguntas. Por qué importa: más cambios generados por IA necesitan redes de seguridad sólidas en la entrega [3], [5]; Microsoft recomienda observación continua de la actividad de agentes [19] y está extendiendo agentes a operaciones de cloud [22]._

### D7-Q1: IA en pipelines CI/CD

**D7-Q1: ¿Se usa IA para crear, mantener y solucionar problemas en pipelines CI/CD (por ejemplo explicar runs fallidos, proponer correcciones), sobre pipeline-as-code?**

- **Unidad de cobertura:** repositorios
- **L3 se ve así:** Los pipelines son code en la mayoría de los repositorios; el análisis de fallas asistido por IA está disponible para todos los equipos.
- **L4 se ve así:** Los agentes proponen correcciones y optimizaciones de pipeline automáticamente, bajo review, con tiempo de build y tasa de fallas rastreados.
- **Ejemplos de evidencia:** Repositorios de pipeline, uso de análisis de fallas, métricas de build.
- **Campo de evidencia:** `Evidence (D7-Q1)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D7-Q2: Entrega progresiva y rollback

**D7-Q2: ¿Los equipos pueden lanzar cambios asistidos por IA de forma segura mediante entrega progresiva (feature flags, canary o blue/green) y rollback automatizado?**

- **Unidad de cobertura:** servicios
- **L3 se ve así:** La mayoría de los servicios usa feature flags o rollout por etapas; rollback está automatizado para servicios críticos.
- **L4 se ve así:** Las decisiones de rollout se guían automáticamente por señales de salud; change failure rate y tiempo de recuperación se rastrean por servicio.
- **Ejemplos de evidencia:** Plataforma de feature flags, configuración de rollout, registros de rollback.
- **Campo de evidencia:** `Evidence (D7-Q2)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D7-Q3: Respuesta a incidentes asistida por IA

**D7-Q3: ¿Se usa IA en respuesta a incidentes (correlación de alertas, resumen, hipótesis de causa raíz, borradores de revisión post-incidente) con humanos al mando?**

- **Unidad de cobertura:** servicios
- **L3 se ve así:** Los ingenieros de on-call en la mayoría de los equipos usan IA para triage y resúmenes; las revisiones post-incidente registran si la IA ayudó.
- **L4 se ve así:** Los agentes de operaciones ejecutan diagnósticos aprobados automáticamente; el tiempo de restauración se compara antes y después de la adopción.
- **Ejemplos de evidencia:** Configuración de herramientas de incidentes, timelines de incidentes, datos de tiempo de restauración.
- **Campo de evidencia:** `Evidence (D7-Q3)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D7-Q4: Observabilidad de agentes

**D7-Q4: ¿Los agentes de IA en el SDLC son observables (traces de runs y tool calls, latencia, fallas, costo), por ejemplo mediante OpenTelemetry?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Los runs de agentes emiten telemetría al stack central de observabilidad; los dashboards muestran fallas y costo por agente.
- **L4 se ve así:** Las alertas se disparan por drift de agentes, picos de error o anomalías de costo; los hallazgos alimentan gobernanza (D1).
- **Ejemplos de evidencia:** Dashboards de telemetría, reglas de alerta.
- **Campo de evidencia:** `Evidence (D7-Q4)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D7-Q5: Infrastructure as code con guardrails

**D7-Q5: ¿Se usa IA para escribir y revisar infrastructure as code, con guardrails de policy-as-code que bloquean cambios no conformes?**

- **Unidad de cobertura:** servicios
- **L3 se ve así:** La mayor parte de la infraestructura es code; IaC generado por IA pasa los mismos policy checks y plan reviews.
- **L4 se ve así:** Drift se detecta y corrige mediante GitOps; las violaciones de política por IaC generado por IA se rastrean y van a la baja.
- **Ejemplos de evidencia:** Repositorios de IaC, reglas de policy-as-code, informes de drift.
- **Campo de evidencia:** `Evidence (D7-Q5)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D7-Q6: Automatización operacional impulsada por agentes

**D7-Q6: ¿Las tareas operacionales (runbooks, remediación, actualizaciones de dependencias y patches) están automatizadas por agentes bajo reglas de aprobación definidas?**

- **Unidad de cobertura:** servicios
- **L3 se ve así:** Los runbooks comunes y las actualizaciones de dependencias están automatizados; las aprobaciones siguen la matriz de autonomía (D1-Q5).
- **L4 se ve así:** La mayoría de las operaciones rutinarias se ejecuta automáticamente con aprobaciones auditadas; el esfuerzo humano se desplaza a excepciones.
- **Ejemplos de evidencia:** Catálogo de automatización, logs de aprobación.
- **Campo de evidencia:** `Evidence (D7-Q6)` · _Herramienta, % de cobertura, métrica, período, enlace_

---

## Sección D8: Fundamentos de ingeniería (amplificadores de IA)

_7 preguntas. Por qué importa: DORA encuentra que estas capacidades amplifican los beneficios de la adopción de IA, y que una plataforma interna de alta calidad se correlaciona con la capacidad de desbloquear valor de IA [1], [3]._

### D8-Q1: Control de versiones para todo

**D8-Q1: ¿Application code, configuración, automatización de build, configuración de sistema y prompts/instrucciones de IA están todos almacenados en control de versiones?**

- **Unidad de cobertura:** equipos
- **L3 se ve así:** Los cinco tipos de activos están versionados para la mayoría de los servicios.
- **L4 se ve así:** Nada llega a producción sin una fuente versionada; los checks lo confirman automáticamente.
- **Ejemplos de evidencia:** Inventario de repositorios, fuentes de configuración.
- **Campo de evidencia:** `Evidence (D8-Q1)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D8-Q2: Frecuencia de commit y rollback rápido

**D8-Q2: ¿Los ingenieros hacen commit de cambios pequeños con frecuencia y confían en undo/revert rápido al experimentar con salida de IA?**

- **Nota de alcance:** Mide frecuencia de commit y velocidad de rollback. El tamaño de cambios asistidos por IA es D5-Q4.
- **Unidad de cobertura:** equipos
- **L3 se ve así:** La mayoría de los ingenieros hace commit al menos diariamente; revertir un cambio es rutinario y rápido.
- **L4 se ve así:** Trunk-based development con branches de corta duración es la norma; se mide el tiempo de revert.
- **Ejemplos de evidencia:** Datos de frecuencia de commit, edad de branch.
- **Campo de evidencia:** `Evidence (D8-Q2)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D8-Q3: Plataforma interna de calidad

**D8-Q3: ¿Existe una internal developer platform fácil de usar, que abstrae infraestructura y hace que la ruta segura y conforme sea la predeterminada para humanos y agentes?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Un equipo dedicado de plataforma ofrece golden paths de self-service usados por la mayoría de los equipos; el equipo actúa sobre el feedback.
- **L4 se ve así:** Los agentes usan las mismas APIs y guardrails de plataforma que los humanos; la satisfacción con la plataforma se mide y mejora.
- **Ejemplos de evidencia:** Catálogo de plataforma, golden paths, encuesta de satisfacción.
- **Campo de evidencia:** `Evidence (D8-Q3)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D8-Q4: Ecosistema de datos saludable

**D8-Q4: ¿Los ingenieros y herramientas de IA pueden encontrar y usar datos internos confiables (no aislados en silos, de buena calidad, respondibles rápidamente)?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Los datos clave están catalogados con responsables e indicadores de calidad; la mayoría de las preguntas puede responderse en una hora.
- **L4 se ve así:** La calidad de datos se monitorea automáticamente; existen linaje y contratos para datos críticos.
- **Ejemplos de evidencia:** Catálogo de datos, dashboards de calidad.
- **Campo de evidencia:** `Evidence (D8-Q4)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D8-Q5: Entornos reproducibles para humanos y agentes

**D8-Q5: ¿Los entornos de desarrollo son reproducibles (devcontainers, cloud workspaces, toolchains fijadas) para que humanos y agentes hagan build y test de la misma forma?**

- **Unidad de cobertura:** repositorios
- **L3 se ve así:** La mayoría de los repositorios define un entorno reproducible; los agentes usan la misma definición.
- **L4 se ve así:** Los entornos inician en minutos para cualquier repositorio; se detecta drift respecto de la definición.
- **Ejemplos de evidencia:** Archivos devcontainer, tiempos de start-up de entorno.
- **Campo de evidencia:** `Evidence (D8-Q5)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D8-Q6: Documentación como contexto listo para IA

**D8-Q6: ¿La documentación se mantiene como code, actualizada y con ownership, para que pueda servir como contexto confiable para herramientas de IA?**

- **Unidad de cobertura:** repositorios
- **L3 se ve así:** Los docs viven junto al code con responsables; los docs obsoletos se señalan en reviews.
- **L4 se ve así:** La actualidad se verifica automáticamente; los cambios de docs generados por IA se revisan como code.
- **Ejemplos de evidencia:** Repositorios de docs, checks de actualidad.
- **Campo de evidencia:** `Evidence (D8-Q6)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D8-Q7: Pruebas automatizadas como sistema de control

**D8-Q7: ¿Las pruebas automatizadas son suficientemente profundas y rápidas para detectar regresiones de altos volúmenes de cambios generados por IA (unit, integration, end-to-end, contract)?**

- **Nota de alcance:** Mide pruebas automatizadas como sistema de control. IA usada para escribir pruebas es D5-Q5.
- **Unidad de cobertura:** servicios
- **L3 se ve así:** La mayoría de los servicios tiene pruebas automatizadas por capas que se ejecutan en cada PR dentro de time budgets acordados.
- **L4 se ve así:** Las suites de prueba se ajustan a partir de datos de defectos escapados; el tiempo de feedback se rastrea y mejora.
- **Ejemplos de evidencia:** Inventario de suites de prueba, duraciones de pipeline, datos de defectos escapados.
- **Campo de evidencia:** `Evidence (D8-Q7)` · _Herramienta, % de cobertura, métrica, período, enlace_

---

## Sección D9: Medición, valor y AI FinOps

_7 preguntas. Por qué importa: estudios controlados van desde 55.8% más rápido [33] y 26.08% más tareas completadas [34] hasta 19% más lento con una fuerte brecha de percepción [35], por lo que las organizaciones necesitan su propia medición objetiva; Gartner predice que los costos de AI coding superarán el salario promedio de un desarrollador para 2028 [32]._

### D9-Q1: Métricas de profundidad de adopción

**D9-Q1: ¿La adopción de IA se rastrea con telemetría más allá del conteo de seats (usuarios activos, engagement por feature, cohortes de adopción)?**

- **Nota de alcance:** Mide si la adopción se rastrea. Qué tan profundamente se usa IA es D4-Q1.
- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Las métricas de uso (por ejemplo la API o dashboard de métricas de uso de Copilot) se revisan mensualmente por el liderazgo de ingeniería.
- **L4 se ve así:** El movimiento de cohortes es un objetivo gestionado; las acciones de habilitación se evalúan por su efecto en las cohortes.
- **Ejemplos de evidencia:** Dashboards de uso, informes de tendencia de cohortes.
- **Campo de evidencia:** `Evidence (D9-Q1)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D9-Q2: Métricas de resultado de entrega

**D9-Q2: ¿Las métricas de entrega de software (lead time, deployment frequency, change failure rate, time to restore) se rastrean y comparan antes y después de la adopción de IA?**

- **Unidad de cobertura:** servicios
- **L3 se ve así:** Las métricas DORA se recopilan automáticamente para la mayoría de los servicios y se revisan con datos de adopción de IA.
- **L4 se ve así:** Las métricas de entrega son parte de decisiones de inversión en IA; las regresiones disparan acción correctiva.
- **Ejemplos de evidencia:** Dashboards DORA, comparación baseline versus actual.
- **Campo de evidencia:** `Evidence (D9-Q2)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D9-Q3: Métricas de flujo de pull request

**D9-Q3: ¿Se rastrean el throughput de PR, el tiempo hasta merge y la proporción y tasa de merge de PRs creados por IA o agentes?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Las métricas de ciclo de vida de PR se reportan por organización; los PRs creados por agentes se identifican por separado, incluida su tasa de correcciones post-merge.
- **L4 se ve así:** Las métricas de flujo se vinculan con métricas de calidad (D5) para que el flujo más rápido no se compre con inestabilidad.
- **Ejemplos de evidencia:** Métricas de ciclo de vida de PR, informes de PRs de agentes, análisis de correcciones de seguimiento.
- **Campo de evidencia:** `Evidence (D9-Q3)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D9-Q4: Developer experience y fricción

**D9-Q4: ¿Developer experience se mide regularmente (productividad percibida, fricción, confianza en IA, satisfacción), usando un framework reconocido como SPACE o las preguntas de resultado de DORA?**

- **Nota de alcance:** Mide la encuesta de developer experience. Comportamiento de review y calibración de confianza es D5-Q6.
- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Una encuesta se realiza al menos dos veces al año con buena participación; los resultados se comparten y generan acciones.
- **L4 se ve así:** Los resultados de encuestas se combinan con telemetría (D9-Q1 a Q3) para encontrar y eliminar fricción.
- **Ejemplos de evidencia:** Instrumento de encuesta, tasa de participación, log de acciones.
- **Campo de evidencia:** `Evidence (D9-Q4)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D9-Q5: Medición controlada de impacto

**D9-Q5: ¿El impacto de IA se estima con comparaciones controladas o basadas en cohortes (por ejemplo piloto versus control, cohortes de adopción, antes/después con un baseline) en vez de solo estimaciones autorreportadas?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Se ejecutó y documentó al menos una comparación controlada o de cohorte, con sus limitaciones.
- **L4 se ve así:** Las comparaciones se ejecutan continuamente para herramientas y prácticas principales; las decisiones las citan.
- **Ejemplos de evidencia:** Diseño del estudio, resultados, registros de decisión.
- **Campo de evidencia:** `Evidence (D9-Q5)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D9-Q6: Gobernanza de costos de IA (AI FinOps)

**D9-Q6: ¿Los costos de IA (seats, premium requests, tokens, runs de agentes) se presupuestan, monitorean por equipo y caso de uso, con thresholds y revisiones regulares?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Existen presupuestos y thresholds de alerta por organización o equipo; los workflows de alto consumo se revisan en retrospectivas.
- **L4 se ve así:** Se rastrea el costo por resultado (por ejemplo por PR mergeado); las prácticas de enrutamiento y contexto se ajustan para reducir desperdicio.
- **Ejemplos de evidencia:** Dashboards de costo, alertas de presupuesto, notas de retrospectiva.
- **Campo de evidencia:** `Evidence (D9-Q6)` · _Herramienta, % de cobertura, métrica, período, enlace_

### D9-Q7: Vínculo con valor de negocio

**D9-Q7: ¿Los resultados de ingeniería con IA se conectan con valor de negocio (business case, supuestos de ROI, OKRs) y se revisan con stakeholders de finanzas o negocio?**

- **Unidad de cobertura:** práctica de toda la organización (use las columnas de gobernanza y medición)
- **L3 se ve así:** Existe un business case con supuestos explícitos y se revisa al menos anualmente.
- **L4 se ve así:** El valor se informa con una cadencia fija con insumos medidos de D9-Q1 a Q6; la inversión se ajusta a partir de los resultados.
- **Ejemplos de evidencia:** Business case, informes de valor.
- **Campo de evidencia:** `Evidence (D9-Q7)` · _Herramienta, % de cobertura, métrica, período, enlace_
