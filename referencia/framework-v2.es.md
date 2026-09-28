🌐 [English](framework-v2.md) · [Português (Brasil)](framework-v2.pt-br.md) · Español

# Framework AI Maturity v2: guía de referencia

Generado desde `framework.v2.json` (framework 2.0.1) por `scripts/generate_v2_reference.py`. La fuente de verdad es [la especificación v2](../coleta/AI-Maturity-Form-Questions_v2.md). No edite este archivo a mano.

## Método de puntuación

- Valor de la respuesta: L0 a L4 = 0 a 4. Las respuestas NA y en blanco se excluyen.
- Puntaje de la pregunta: media de los valores de las personas.
- Puntaje de la dimensión: media de los puntajes de sus preguntas. Una dimensión sin preguntas respondidas no tiene puntaje.
- General: media ponderada de las dimensiones con puntaje (pesos 1,0 por defecto, permitido de 0,50 a 2,00).
- Cobertura: OK desde 37 preguntas con puntaje, WARNING desde 25, BLOCKED por debajo.
- Brecha = objetivo (por defecto 3,00) menos puntaje. Prioridad = peso × brecha: P0 desde 2,40, P1 desde 1,60, P2 desde 0,90, si no P3.
- Alertas: baja confianza (más del 30% NA), riesgo de amplificación (D5, D6 o D8 un rango por debajo del general), brecha de percepción (ejecutivos vs hands-on, al menos 3 de cada uno), salvedad de alcance, L3/L4 no verificado (menos del 50% de respuestas con evidencia), divergencia entre personas encuestadas (desviación estándar de los puntajes de dimensión por persona de 1,00 o más, con al menos 3 personas).
- Verificaciones cruzadas, cuando existen los archivos: el escaneo de repositorios (niveles RAMP [47]) limita D4-Q4 por la fracción de repositorios con configuración de IA versionada, y las métricas de uso de Copilot [6] limitan D4-Q1 por las fases de adopción. El informe señala respuestas por encima de lo que sostiene la evidencia.

### Rangos de nivel

| Nivel | Puntaje |
| --- | --- |
| L0 No iniciado | [0,00; 0,80) |
| L1 Explorando | [0,80; 1,60) |
| L2 Adoptando | [1,60; 2,40) |
| L3 Escalando | [2,40; 3,20) |
| L4 Nativo en IA | [3,20; 4,00] |

### Ejemplo resuelto: D8 en el mock ilustrativo

El mock (`respostas.v2.json.example`, 14 personas ilustrativas) da estos valores, calculados por `scripts/engine_v2.py`.

| Pregunta | Puntaje | Respuestas | NA |
| --- | ---: | ---: | ---: |
| D8-Q1 Control de versiones para todo | 1,07 | 14 | 0 |
| D8-Q2 Frecuencia de commit y rollback rápido | 1,23 | 13 | 1 |
| D8-Q3 Plataforma interna de calidad | 1,29 | 14 | 0 |
| D8-Q4 Ecosistema de datos saludable | 0,92 | 13 | 1 |
| D8-Q5 Entornos reproducibles para humanos y agentes | 1,00 | 14 | 0 |
| D8-Q6 Documentación como contexto listo para IA | 1,36 | 14 | 0 |
| D8-Q7 Pruebas automatizadas como sistema de control | 0,75 | 12 | 2 |

Puntaje de D8 = media de los 7 puntajes de las preguntas = **1,09** (L1 Explorando). Brecha hasta 3,00 = 1,91; prioridad = 1,00 × 1,91 = 1,91 → **P1 Alto**.

General = media de los 9 puntajes de dimensión = **2,04** (L2 Adoptando).

## Dimensiones y preguntas

### D1: Estrategia, política y gobernanza de IA

**Por qué importa:** DORA identifica una "postura de IA clara y comunicada" como amplificadora de los beneficios de la IA [1], [2]; Microsoft CAF afirma que "todo agente debe ser observable, gobernado y seguro" [19].

**Página de la dimensión:** [dimensoes/D1.es.md](dimensoes/D1.es.md)

**Estrategias:** S7, S5, S6 · **Grupo del informe:** G1 (Dirección, personas y valor)

#### D1-Q1: Estrategia de IA para ingeniería de software

¿Existe una estrategia documentada de IA para ingeniería de software, patrocinada por liderazgo, que declare objetivos explícitos y se comunique a todos los equipos de ingeniería?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Estrategia publicada y revisada al menos anualmente; los objetivos (por ejemplo entrega, calidad, developer experience) tienen responsables; la mayoría de los ingenieros puede decir dónde encontrarla.
- L4: La estrategia se revisa a partir de resultados medidos (D9) y se vincula a OKRs de negocio; el progreso se informa al liderazgo con una cadencia fija.

**Ejemplos de evidencia:** Documento de estrategia, comunicación de liderazgo, entradas de OKR.  
**Base:** [1] [2] [18]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** organization · **Audiencia:** engineering-leader, architect, security

#### D1-Q2: Política de uso aceptable

¿Está claro para los ingenieros cómo pueden y no pueden usar IA en el trabajo, incluidos qué datos pueden compartirse con herramientas de IA?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La política escrita de uso aceptable cubre code, datos de clientes, secretos e IP de terceros; es parte del onboarding; las excepciones tienen un responsable.
- L4: La política se aplica mediante controles técnicos (por ejemplo content exclusion, prevención de pérdida de datos, allowlists) y se audita; las violaciones disparan alertas automatizadas.

**Ejemplos de evidencia:** Enlace de la política, checklist de onboarding, configuración de controles.  
**Base:** [1] [2] [20] [21]  
**Origen en v1:** P1-C1-Q5 (parcial)  
**Unidad:** organization · **Audiencia:** engineering-leader, architect, security

#### D1-Q3: Herramientas y modelos aprobados

¿Existe un catálogo mantenido de herramientas, funciones y modelos de IA aprobados para desarrollo de software, gestionado mediante políticas enterprise o de la organización?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Las políticas enterprise/de la organización habilitan solo funciones y modelos aprobados; el catálogo lista responsable, manejo de datos y fecha de revisión para cada herramienta.
- L4: Los nuevos modelos y herramientas pasan por una evaluación definida (calidad, costo, seguridad) antes de habilitarse; los retirados se eliminan según cronograma.

**Ejemplos de evidencia:** Configuraciones de política de Copilot, catálogo de herramientas, registros de evaluación de modelos.  
**Base:** [2] [15] [32] [49]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** organization · **Audiencia:** engineering-leader, architect, security

#### D1-Q4: Protección de datos, IP y residencia

¿Los requisitos de residencia, retención, propiedad intelectual y privacidad de datos están definidos y aplicados a las herramientas y agentes de IA usados en el SDLC?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los requisitos se documentan por herramienta; repositorios o archivos sensibles se excluyen del contexto de IA; la retención de logs y memoria sigue la política.
- L4: El cumplimiento se evalúa continuamente (por ejemplo con un compliance manager) y se mapea a regulaciones como el EU AI Act cuando aplica.

**Ejemplos de evidencia:** Registros de procesamiento de datos, configuraciones de exclusión, política de retención.  
**Base:** [19] [20]  
**Origen en v1:** P1-C1-Q5 (parcial)  
**Unidad:** organization · **Audiencia:** engineering-leader, architect, security

#### D1-Q5: Niveles de autonomía para trabajo con IA

¿La organización definió qué tareas son lideradas por desarrollador, realizadas por desarrollador con agente, o totalmente lideradas por agente, y los controles requeridos para cada nivel?

_Nota de alcance: Mide la política que define niveles de autonomía. Cómo se escriben las tareas para agentes es D3-Q3; con qué frecuencia se delega el trabajo es D4-Q3._

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Una matriz publicada mapea tipos de tarea (por ejemplo upgrades de dependencias, generación de pruebas, trabajo de feature, cambios en producción) a niveles de autonomía y aprobaciones requeridas.
- L4: La matriz se aplica mediante reglas de plataforma (por ejemplo branch protection, revisores requeridos por ruta) y se actualiza a partir de datos de incidentes y calidad.

**Ejemplos de evidencia:** Matriz de autonomía, rulesets de repositorio, registros de cambios.  
**Base:** [7] [26] [32] [49] [56]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** organization · **Audiencia:** engineering-leader, architect, security

#### D1-Q6: IA responsable y framework de riesgo

¿El uso de IA en ingeniería de software está gobernado por un estándar de IA responsable y un framework de riesgo reconocido (por ejemplo Microsoft Responsible AI Standard, NIST AI RMF, ISO/IEC 42001)?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Se adopta un framework nombrado; los riesgos relacionados con IA están en el registro de riesgos con responsables y revisiones.
- L4: Los controles del framework se auditan interna o externamente; los resultados retroalimentan política y tooling.

**Ejemplos de evidencia:** Mapeo del framework, entradas del registro de riesgos, informes de auditoría.  
**Base:** [20] [21] [41] [42]  
**Origen en v1:** P3-C3-Q5 (parcial)  
**Unidad:** organization · **Audiencia:** engineering-leader, architect, security

#### D1-Q7: Registro e identidad de agentes

¿Todo agente de IA usado en el SDLC (coding agents, review agents, custom agents, pipeline agents) está registrado con un responsable, un propósito, una identidad distinta y un alcance de acceso definido?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Un único inventario lista todos los agentes con responsable, plataforma y permisos; cada agente se ejecuta bajo su propia identidad, no una cuenta humana compartida.
- L4: Los agentes no registrados ("shadow") se detectan automáticamente; el ciclo de vida de identidad (creación, revisión, eliminación) está automatizado.

**Ejemplos de evidencia:** Inventario de agentes, configuración de identidad (por ejemplo Microsoft Entra Agent ID), revisiones de acceso.  
**Base:** [19] [39]  
**Origen en v1:** P3-C5-Q4 (parcial)  
**Unidad:** organization · **Audiencia:** engineering-leader, architect, security

### D2: Habilitación, habilidades y cultura

**Por qué importa:** Gartner espera que GenAI requiera que 80% de la fuerza laboral de ingeniería se capacite en nuevas habilidades hasta 2027 [30]; DORA pregunta sobre capacitación, aprendizaje entre pares y apoyo para la experimentación [2].

**Página de la dimensión:** [dimensoes/D2.es.md](dimensoes/D2.es.md)

**Estrategias:** S5 · **Grupo del informe:** G1 (Dirección, personas y valor)

#### D2-Q1: Capacitación estructurada de IA

¿Los ingenieros reciben capacitación estructurada en las herramientas de IA aprobadas y workflows de agentes, más allá del onboarding predeterminado del proveedor?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Currículo basado en rol (desarrollador, revisor, plataforma, seguridad) con finalización rastreada; la capacitación se exige antes de habilitar funciones de agentes; enseña patrones que preservan el aprendizaje (pedir explicaciones, intentar primero, luego comparar) y no solo delegación total.
- L4: El currículo se actualiza cada trimestre a partir de datos de uso y patrones de falla; existen rutas avanzadas (orquestación de agentes, evaluación).

**Ejemplos de evidencia:** Rutas de aprendizaje, tasas de finalización, reglas de bloqueo de habilitación.  
**Base:** [2] [30] [48]  
**Origen en v1:** P1-C5-Q4, P1-C3-Q6 (parcial)  
**Unidad:** engineers · **Audiencia:** engineering-leader, developer

#### D2-Q2: Aprendizaje entre pares y champions

¿Existen formatos regulares de aprendizaje entre pares (demos, brown bags, office hours) y una red de champions de IA en los equipos?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Existen champions en la mayoría de los equipos; las sesiones se realizan al menos mensualmente; las grabaciones y ejemplos se comparten en un solo lugar.
- L4: Una comunidad de práctica cura activos reutilizables (instrucciones, archivos de prompt, agentes) y mide su reutilización.

**Ejemplos de evidencia:** Lista de champions, calendario de sesiones, repositorio compartido de ejemplos.  
**Base:** [2]  
**Origen en v1:** P1-C6-Q6  
**Unidad:** teams · **Audiencia:** engineering-leader, developer

#### D2-Q3: Apoyo para la experimentación

¿La organización da a los ingenieros tiempo, sandboxes y presupuesto para experimentar con seguridad con nuevas herramientas de IA y patrones de agentes?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Existen entornos en sandbox y una ruta liviana de solicitud; los experimentos se registran y sus resultados se comparten.
- L4: Los experimentos exitosos pasan al catálogo aprobado (D1-Q3) mediante una ruta definida en semanas.

**Ejemplos de evidencia:** Suscripciones de sandbox, log de experimentos, registros de promoción.  
**Base:** [2]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** teams · **Audiencia:** engineering-leader, developer

#### D2-Q4: Habilidades de ingeniería de contexto

¿Los ingenieros están capacitados para dar a las herramientas de IA el contexto correcto (alcance claro de la tarea, archivos relevantes, restricciones, ejemplos) y mantener el contexto ajustado?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La orientación y los ejemplos sobre ingeniería de contexto son parte de la capacitación; los equipos revisan la calidad de sus instrucciones y prompts.
- L4: Las prácticas de contexto se miden (por ejemplo tasa de éxito o uso de tokens por tarea) y se mejoran con el tiempo.

**Ejemplos de evidencia:** Páginas de orientación, checklists de review, métricas antes/después.  
**Base:** [25] [30] [32]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** engineers · **Audiencia:** engineering-leader, developer

#### D2-Q5: Roles y trayectorias de carrera

¿Se actualizaron descripciones de puesto, frameworks de carrera y expectativas de desempeño para ingeniería asistida por IA y agentic engineering (por ejemplo dirigir agentes, revisar salida de IA, ingeniería de IA)?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Se publican perfiles de rol actualizados; las evaluaciones de desempeño reconocen el uso efectivo de IA y la calidad del review, no el volumen bruto de salida.
- L4: Existen roles dedicados (por ejemplo ingeniero de IA, responsable de plataforma de agentes) con una ruta clara de crecimiento.

**Ejemplos de evidencia:** Framework de carrera, descripciones de rol.  
**Base:** [30]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** organization · **Audiencia:** engineering-leader, developer

#### D2-Q6: Onboarding asistido por IA

¿Los nuevos ingenieros usan herramientas de IA para entender codebases y volverse productivos, con tiempo de ramp-up medido?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: El onboarding incluye recorridos de codebase guiados por IA e instrucciones de repositorio; se rastrea el tiempo hasta el primer PR mergeado; los nuevos ingenieros son evaluados en lectura de code y debugging, no solo en salida.
- L4: Las métricas de ramp-up y habilidades se comparan entre cohortes y se usan para mejorar material e instrucciones de onboarding.

**Ejemplos de evidencia:** Playbook de onboarding, datos de tiempo hasta primer PR, resultados de verificación de habilidades.  
**Base:** [27] [48]  
**Origen en v1:** P1-C5-Q2, P1-C5-Q6, P1-C5-Q7  
**Unidad:** engineers · **Audiencia:** engineering-leader, developer

### D3: Planificar, especificar y diseñar

**Por qué importa:** en agentic coding, "las personas toman la mayoría de las decisiones de planificación (qué hacer) y Claude toma la mayoría de las decisiones de ejecución (cómo hacerlo)" [24]; la calidad de la definición de la tarea impulsa la calidad de la salida del agente [8], [27].

**Página de la dimensión:** [dimensoes/D3.es.md](dimensoes/D3.es.md)

**Estrategias:** S5, S3 · **Grupo del informe:** G2 (Planificar, construir y revisar)

#### D3-Q1: IA en refinamiento de backlog

¿Se usa IA para redactar y refinar issues o user stories, incluidos criterios de aceptación, con un responsable humano que las aprueba?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La mayoría de los equipos usa IA para redactar o mejorar elementos de trabajo; los criterios de aceptación son obligatorios antes de comenzar el trabajo.
- L4: La calidad de los elementos de trabajo (claridad, capacidad de prueba) se mide y se vincula con retrabajo y cycle time.

**Ejemplos de evidencia:** Templates de issue, ejemplos de elementos de trabajo, verificaciones de calidad.  
**Base:** [16] [17]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** teams · **Audiencia:** product-owner, architect, developer

#### D3-Q2: Especificación antes de la implementación

Para cambios no triviales, ¿se produce y revisa un plan o especificación por escrito antes de que un agente de IA implemente el cambio?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los planes o specs se almacenan en el repositorio o se vinculan a la issue, y un humano los revisa antes de la implementación por el agente.
- L4: Las specs son el contrato para verificación automatizada (pruebas, checks) y se mantienen sincronizadas con el code.

**Ejemplos de evidencia:** Archivos de spec, reviews de plan, PRs que referencian specs.  
**Base:** [23] [24] [27] [58]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** teams · **Audiencia:** product-owner, architect, developer

#### D3-Q3: Alcance de tareas para agentes

¿Las tareas dadas a coding agents están bien delimitadas (pequeñas, con criterios de aceptación claros y punteros a code relevante) antes de asignarse?

_Nota de alcance: Mide cómo se delimitan las tareas para agentes. La política de autonomía es D1-Q5; el volumen de delegación es D4-Q3._

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los equipos siguen orientación escrita para issues listas para agentes; las tareas demasiado grandes se dividen antes de la asignación.
- L4: El éxito de tareas de agentes y las tasas de retrabajo se rastrean por tipo de tarea y se usan para refinar la orientación.

**Ejemplos de evidencia:** Directrices de tareas para agentes, ejemplos de issues, datos de tasa de éxito.  
**Base:** [1] [8] [24] [49]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** teams · **Audiencia:** product-owner, architect, developer

#### D3-Q4: Decisiones de arquitectura y diseño

¿Se usa IA para apoyar el trabajo de diseño (análisis de opciones, modos de amenaza y falla, architecture decision records) mientras las decisiones permanecen con humanos responsables?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los ADRs se versionan; se adjunta análisis asistido por IA; un humano nombrado aprueba cada decisión.
- L4: Los agentes verifican nuevos cambios contra decisiones registradas y señalan conflictos automáticamente.

**Ejemplos de evidencia:** Repositorio de ADR, registros de design review.  
**Base:** [8] [24] [26]  
**Origen en v1:** P1-C3-Q5, P1-C6-Q5  
**Unidad:** teams · **Audiencia:** product-owner, architect, developer

#### D3-Q5: Enfoque centrado en el usuario

¿El trabajo asistido por IA está vinculado a resultados claros para usuarios e informado por feedback de usuarios?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los elementos de trabajo referencian el problema del usuario y la medida de éxito; el feedback se revisa antes de priorizar.
- L4: Las métricas de resultado del usuario son parte de la definition of done para entrega asistida por IA.

**Ejemplos de evidencia:** Briefs de producto, registros de loop de feedback, dashboards de resultados.  
**Base:** [1] [2] [3]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** teams · **Audiencia:** product-owner, architect, developer

#### D3-Q6: Modernización asistida por IA

¿Se usan herramientas y agentes de IA para entender, hacer upgrade y migrar code legado (por ejemplo upgrades de framework o runtime, migración a cloud), con resultados verificados por pruebas?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Existe un proceso repetible de modernización asistida por IA para tipos comunes de upgrade, con gates de prueba.
- L4: El backlog de modernización se reduce continuamente mediante agentes bajo review humano, con tasas de éxito rastreadas.

**Ejemplos de evidencia:** Runbooks de upgrade, PRs de migración, resultados de pruebas.  
**Base:** [16] [17]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** teams · **Audiencia:** product-owner, architect, developer

### D4: Código e ingeniería de contexto

**Por qué importa:** GitHub mide la profundidad de adopción como una progresión de "Code first" a "Agent first" y "Multi-agent" [6]; Anthropic describe el contexto como "un recurso finito con retornos marginales decrecientes" [25].

**Página de la dimensión:** [dimensoes/D4.es.md](dimensoes/D4.es.md)

**Estrategias:** S5, S6, S4 · **Grupo del informe:** G2 (Planificar, construir y revisar)

#### D4-Q1: Profundidad de uso de IA entre superficies

¿Qué tan profundamente usan IA los ingenieros entre superficies: completions y ediciones de agentes en el IDE, superficies de agentes de GitHub (cloud agent, code review, CLI), y varios agentes juntos?

_Nota de alcance: Mide qué tan profundamente se usa IA. Si ese uso se mide es D9-Q1._

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L1-L2: Principalmente completions y ediciones de agente en el IDE ("Code first"); el uso solo de chat cuenta como Passive en las cohortes de GitHub.
- L3: Muchos ingenieros usan regularmente al menos una superficie de agente de GitHub ("Agent first"), confirmado por métricas de uso.
- L4: El uso multi-agent es normal ("Multi-agent"), con distribución de cohortes rastreada mensualmente.

**Ejemplos de evidencia:** Dashboard o API de métricas de uso de Copilot: distribución de cohortes de adopción, usuarios activos diarios/semanales.  
**Base:** [6]  
**Origen en v1:** P1-C1-Q1  
**Unidad:** engineers · **Audiencia:** developer, platform-engineer

#### D4-Q2: Modo agente para trabajo multi-file

¿Los ingenieros usan IDE agent mode (o equivalente) para cambios multi-file, y revisan cada cambio antes de hacer commit?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Agent mode es el valor predeterminado para refactors y features multi-file en la mayoría de los equipos; los cambios se revisan en el diff antes del commit.
- L4: Los equipos comparten patrones de agent mode que funcionan y rastrean dónde falla; los permisos de herramientas se ajustan por repositorio.

**Ejemplos de evidencia:** Uso por feature/mode, directrices del equipo.  
**Base:** [6] [27]  
**Origen en v1:** P1-C1-Q1 (parcial)  
**Unidad:** engineers · **Audiencia:** developer, platform-engineer

#### D4-Q3: Delegación a coding agents

¿Se asignan issues a coding agents (por ejemplo Copilot cloud agent) y estos producen pull requests que se mergean después de review humano?

_Nota de alcance: Mide cuánto trabajo se delega a coding agents. La política de autonomía es D1-Q5; el alcance de tareas es D3-Q3._

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La mayoría de los equipos delega issues adecuadas a un coding agent; se rastrea la proporción de PRs mergeados creados por agentes.
- L4: La tasa de merge de PRs de agentes, el retrabajo y la tasa de correcciones post-merge se rastrean por tipo de tarea; las reglas de delegación (D1-Q5) se ajustan a partir de estos datos.

**Ejemplos de evidencia:** Conteos de PRs creados por agentes, tasa de merge, tiempo hasta merge, correcciones de seguimiento.  
**Base:** [6] [7] [14] [49] [50]  
**Origen en v1:** P3-C5-Q1 (parcial)  
**Unidad:** teams · **Audiencia:** developer, platform-engineer

#### D4-Q4: Instrucciones de repositorio

¿Los repositorios contienen custom instructions versionadas y revisadas para herramientas de IA (por ejemplo `.github/copilot-instructions.md`, `AGENTS.md`) que describen build, test, convenciones y restricciones?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La mayoría de los repositorios activos tiene instrucciones estructuradas (build, test, convenciones, restricciones) con un responsable; los cambios pasan por PR review; los archivos se actualizan cuando el codebase cambia en vez de commitarlos una sola vez.
- L4: Las instrucciones se generan a partir de una base compartida, se verifican por obsolescencia, y se mide su efecto en la tasa de merge de agentes y calidad de code, ya que los archivos de instrucciones por sí solos no garantizan mejores resultados.

**Ejemplos de evidencia:** Archivos de instrucciones, cobertura entre repositorios, historial de cambios, métricas antes/después de PRs de agentes.  
**Base:** [2] [8] [25] [27] [46] [47] [55]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** repositories · **Audiencia:** developer, platform-engineer

#### D4-Q5: Prompts, agentes y skills reutilizables

¿Existe una biblioteca compartida y curada de archivos de prompt, custom agents y skills reutilizables, con responsables y versionado?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Un repositorio central contiene archivos de prompt y custom agents aprobados; los equipos los reutilizan en vez de copiarlos.
- L4: Los activos se evalúan antes del release (calidad, costo), el uso se rastrea y los activos no usados se retiran.

**Ejemplos de evidencia:** Repositorio de biblioteca, perfiles de custom agents, métricas de reutilización.  
**Base:** [11] [25] [47]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** teams · **Audiencia:** developer, platform-engineer

#### D4-Q6: Gobernanza de MCP servers

¿Los MCP servers y otras herramientas de agentes se gobiernan mediante una allowlist o registry, con herramientas acotadas y responsables nombrados?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Se aplica una allowlist enterprise de MCP o un registry customizado; cada server tiene un responsable, una security review y herramientas limitadas.
- L4: Las tool calls se registran y revisan; los nuevos servers pasan security checks automatizados antes de agregarse.

**Ejemplos de evidencia:** Política de allowlist o registry, configuración de MCP, registros de review.  
**Base:** [9] [10] [38]  
**Origen en v1:** P3-C5-Q4  
**Unidad:** organization · **Audiencia:** developer, platform-engineer · **Preparación de platform engineering:** sí

#### D4-Q7: Acceso de IA al conocimiento interno

¿Las herramientas y agentes de IA pueden usar de forma segura fuentes internas (code, documentación, wikis, elementos de trabajo) como contexto, mediante conectores aprobados?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los conectores aprobados dan a las herramientas de IA acceso consciente de permisos a las principales fuentes internas; las respuestas citan material interno.
- L4: Las fuentes de conocimiento se curan para uso de IA (actualidad, ownership) y se evalúa la calidad de retrieval.

**Ejemplos de evidencia:** Configuración de conectores, evaluaciones de retrieval.  
**Base:** [1] [2] [19]  
**Origen en v1:** P1-C3-Q2, P1-C3-Q3  
**Unidad:** teams · **Audiencia:** developer, platform-engineer · **Preparación de platform engineering:** sí

#### D4-Q8: Selección y enrutamiento de modelos

¿La elección del modelo se ajusta a la complejidad de la tarea (modelos más pequeños para trabajo rutinario, frontier models para trabajo complejo), mediante orientación o enrutamiento automático?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La orientación escrita mapea tipos de tarea a modelos; los modelos predeterminados se establecen por política.
- L4: El enrutamiento automático está implementado y se ajusta con datos de costo y calidad.

**Ejemplos de evidencia:** Orientación de modelos, configuraciones de política, configuración de enrutamiento.  
**Base:** [26] [32]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** organization · **Audiencia:** developer, platform-engineer

### D5: Revisión, calidad y pruebas

**Por qué importa:** DORA vincula el volumen de cambios impulsados por IA con la inestabilidad, a menos que existan sistemas de control sólidos [3]; GitHub exige revisión humana antes de que se mergeen PRs de agentes [7]; 46% de los desarrolladores desconfían de la precisión de la salida de IA [37].

**Página de la dimensión:** [dimensoes/D5.es.md](dimensoes/D5.es.md)

**Estrategias:** S5, S7 · **Grupo del informe:** G2 (Planificar, construir y revisar)

#### D5-Q1: AI-assisted code review

¿AI code review (por ejemplo Copilot code review) se aplica a pull requests, con un revisor humano aún responsable de la aprobación?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: AI review se ejecuta automáticamente en la mayoría de los PRs; los equipos rastrean sugerencias útiles versus descartadas.
- L4: Las reglas de review se ajustan por repositorio a partir de los resultados de sugerencias; se rastrean tiempo de review y defectos escapados; los PRs donde solo IA revisó code creado por IA son visibles y gobernados.

**Ejemplos de evidencia:** Rulesets de repositorio, métricas de adopción de code review, resultados de sugerencias.  
**Base:** [6] [12] [14] [54] [55]  
**Origen en v1:** P1-C1-Q2, P1-C4-Q1  
**Unidad:** repositories · **Audiencia:** developer, qa-test

#### D5-Q2: Human-in-the-loop para cambios de agentes

¿Los pull requests creados por agentes requieren aprobación humana independiente (no el solicitante), con workflow runs aprobadas antes de ejecutarse?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Se mantienen las protecciones por defecto: los PRs de agentes necesitan una aprobación humana independiente (las aprobaciones de Copilot, si están habilitadas, no cuentan); "Approve and run workflows" no se desactiva sin una decisión de riesgo documentada.
- L4: Los requisitos de aprobación escalan con el riesgo (D1-Q5) y se auditan; las excepciones expiran automáticamente.

**Ejemplos de evidencia:** Rulesets, branch protection, configuraciones de agentes.  
**Base:** [7] [12] [14] [38] [53] [55] [56]  
**Origen en v1:** P3-C5-Q5, P2-C9-Q3  
**Unidad:** repositories · **Audiencia:** developer, qa-test

#### D5-Q3: Mismos quality gates para code de IA y humano

¿Los cambios generados por IA y creados por agentes pasan los mismos checks requeridos (build, tests, linting, security scans, coverage) que los cambios humanos?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los checks requeridos se aplican mediante rulesets en los protected branches de la mayoría de los repositorios, sin bypass para identidades de agentes.
- L4: Los gates son policy as code, aplicados en todos los repositorios (>90%) y revisados después de incidentes.

**Ejemplos de evidencia:** Rulesets, checks requeridos, listas de bypass.  
**Base:** [3] [7] [31] [50] [55]  
**Origen en v1:** P1-C4-Q2, P1-C4-Q4  
**Unidad:** repositories · **Audiencia:** developer, qa-test

#### D5-Q4: Lotes pequeños

¿Los cambios se mantienen pequeños (límites de tamaño de PR, un tema por PR), incluidos los cambios producidos por agentes?

_Nota de alcance: Mide el tamaño de cambios asistidos por IA. Con qué frecuencia se commitea code y qué tan rápido se revierte es D8-Q2._

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La orientación de tamaño de PR se aplica o monitorea; los PRs de agentes demasiado grandes se dividen antes del review.
- L4: El tamaño de lote se rastrea contra change failure rate y tiempo de review, y se usa para ajustar límites.

**Ejemplos de evidencia:** Distribución de tamaño de PR, configuración de bot o ruleset.  
**Base:** [1] [2] [5] [53] [57]  
**Origen en v1:** P1-C4-Q6  
**Unidad:** teams · **Audiencia:** developer, qa-test

#### D5-Q5: Pruebas asistidas por IA

¿Se usa IA para generar y mantener pruebas, con calidad de pruebas verificada (por ejemplo coverage del code cambiado, mutation testing) en vez de solo conteo de pruebas?

_Nota de alcance: Mide IA usada para escribir y mejorar pruebas. Si las pruebas automatizadas actúan como gate es D8-Q7._

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La mayoría de los equipos usa IA para escribir pruebas; coverage de líneas cambiadas es un check requerido.
- L4: La efectividad de pruebas (mutation score, defectos escapados) se rastrea; flaky tests se detectan y se ponen en cuarentena automáticamente.

**Ejemplos de evidencia:** Informes de coverage, resultados de mutation testing, dashboard de flaky tests.  
**Base:** [3] [8] [17]  
**Origen en v1:** P1-C1-Q4, P2-C6-Q1, P2-C6-Q5, P2-C6-Q6, P2-C6-Q7  
**Unidad:** teams · **Audiencia:** developer, qa-test

#### D5-Q6: Cultura de verificación y confianza calibrada

¿Los ingenieros verifican sistemáticamente la salida de IA (la ejecutan, la prueban, la leen) y se mide la confianza en la salida de IA con el tiempo?

_Nota de alcance: Mide comportamiento de review y calibración de confianza. Cómo se encuesta developer experience es D9-Q4._

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Las directrices de review explican qué verificar en la salida de IA; la confianza en la salida de IA es parte de la encuesta a desarrolladores.
- L4: La confianza y la precisión se comparan con datos reales de defectos, y la orientación se actualiza donde divergen.

**Ejemplos de evidencia:** Directrices de review, resultados de encuesta, análisis de defectos.  
**Base:** [3] [23] [35] [37] [48] [52]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** teams · **Audiencia:** developer, qa-test

#### D5-Q7: Salud del code generado por IA

¿Se monitorea la salud de largo plazo del code generado por IA (duplicación, churn, complejidad, mantenibilidad)?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Se recopilan métricas de code health para la mayoría de los repositorios y se revisan en retrospectivas de equipo; el code generado por IA tiene un responsable humano nombrado.
- L4: Las tendencias de salud (por ejemplo complejidad cognitiva, advertencias de static analysis) se comparan entre code con alta presencia de IA y otro code, con acciones correctivas rastreadas.

**Ejemplos de evidencia:** Dashboards de static analysis, informes de churn, archivos de ownership.  
**Base:** [2] [5] [47] [51]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** repositories · **Audiencia:** developer, qa-test

### D6: Seguridad y cadena de suministro de IA

**Por qué importa:** OWASP enumera prompt injection (LLM01:2025), supply chain (LLM03:2025) y agencia excesiva (LLM06:2025) entre los principales riesgos [38], y agent goal hijack (ASI01) en primer lugar para aplicaciones agentic [39]; NIST SP 800-218A agrega al SSDF prácticas para el desarrollo de modelos de IA [40].

**Página de la dimensión:** [dimensoes/D6.es.md](dimensoes/D6.es.md)

**Estrategias:** S7, S6 · **Grupo del informe:** G3 (Proteger, entregar y fundamentos)

#### D6-Q1: Scanning de base en todo repositorio

¿Code scanning (SAST), secret scanning con push protection y dependency review se aplican a todos los repositorios, incluidas branches de agentes?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Habilitado por defecto para todos los repositorios nuevos y la mayoría de los existentes; push protection se aplica a todo commit, humano o de agente; las alertas tienen responsables y objetivos de nivel de servicio.
- L4: La cobertura es casi completa y se verifica automáticamente; mean time to remediate se rastrea.

**Ejemplos de evidencia:** Dashboard de cobertura de seguridad, tiempo de remediación.  
**Base:** [7] [13] [40] [52]  
**Origen en v1:** P1-C4-Q3, P2-C4-Q1, P2-C4-Q2, P2-C4-Q3, P2-C4-Q4, P2-C10-Q1  
**Unidad:** repositories · **Audiencia:** security, platform-engineer

#### D6-Q2: Remediación asistida por IA

¿Se usa remediación asistida por IA (por ejemplo autofix para code scanning) para corregir vulnerabilidades, con correcciones revisadas y probadas antes del merge?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Las sugerencias de autofix están habilitadas para la mayoría de los repositorios; se rastrean tasas de aceptación y reapertura.
- L4: Las campañas de seguridad usan remediación con IA a escala, y el tiempo de remediación se informa al liderazgo.

**Ejemplos de evidencia:** Configuraciones de autofix, métricas de remediación.  
**Base:** [13] [57]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** repositories · **Audiencia:** security, platform-engineer

#### D6-Q3: Defensas contra prompt injection para agentes

¿Los agentes están protegidos contra prompt injection y goal hijack (contenido no confiable tratado como datos, instrucciones ocultas filtradas, egress de red restringido)?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Agent firewalls y restricciones de egress se mantienen activados; la orientación indica a los equipos qué fuentes de contenido no son confiables.
- L4: Los agentes pasan regularmente por red team contra escenarios OWASP LLM01:2025 y ASI01; los hallazgos se rastrean hasta el cierre.

**Ejemplos de evidencia:** Configuración de firewall, informes de red team.  
**Base:** [7] [38] [39]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** organization · **Audiencia:** security, platform-engineer

#### D6-Q4: Least privilege para agentes

¿Los agentes se ejecutan con least privilege (tokens con alcance, sin secretos de producción, branches restringidos, entornos en sandbox)?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los permisos de agentes se documentan y revisan; los agentes no pueden acceder a credenciales de producción ni hacer push a protected branches.
- L4: Los permisos son just-in-time y limitados en el tiempo; el acceso se revisa automáticamente.

**Ejemplos de evidencia:** Configuración de entorno de agentes, alcances de token, revisiones de acceso.  
**Base:** [7] [19] [38] [39]  
**Origen en v1:** P3-C6-Q2, P3-C6-Q3 (parcial)  
**Unidad:** organization · **Audiencia:** security, platform-engineer

#### D6-Q5: AI supply chain

¿Modelos, MCP servers, extensiones de IDE y herramientas de agentes se evalúan antes del uso, con procedencia y SBOMs para lo que construyen y entregan?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Un proceso de review cubre componentes de IA; SBOMs y procedencia de build se producen para la mayoría de los builds.
- L4: La procedencia se verifica en el deploy (por ejemplo metas de nivel SLSA); los componentes no evaluados se bloquean automáticamente.

**Ejemplos de evidencia:** Registros de review de componentes, muestras de SBOM y atestación.  
**Base:** [38] [40] [43] [52]  
**Origen en v1:** P2-C8-Q2, P2-C8-Q3, P2-C10-Q2, P2-C10-Q3, P2-C10-Q5  
**Unidad:** repositories · **Audiencia:** security, platform-engineer

#### D6-Q6: Threat modeling para features y agentes de IA

¿Las features de IA y workflows agentic se someten a threat modeling con riesgos específicos de IA (OWASP LLM and Agentic Top 10, NIST SP 800-218A)?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Se requieren threat models para nuevas features de IA y workflows de agentes, y seguridad los revisa.
- L4: Los threat models se actualizan después de incidentes y ejercicios de red team; los controles se verifican mediante pruebas automatizadas.

**Ejemplos de evidencia:** Documentos de threat model, registros de security review.  
**Base:** [38] [39] [40]  
**Origen en v1:** P2-C4-Q6 (parcial), P3-C3-Q5, P3-C5-Q3  
**Unidad:** services · **Audiencia:** security, platform-engineer

#### D6-Q7: Rastro de auditoría para acciones de agentes

¿Las sesiones y acciones de agentes (prompts, tool calls, commits, aprobaciones) se registran, son atribuibles a una identidad y se retienen según la política?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La actividad de agentes se registra centralmente y se vincula con el usuario solicitante y la identidad del agente.
- L4: Los logs alimentan detección de anomalías; las auditorías pueden reconstruir cualquier cambio de agente de punta a punta.

**Ejemplos de evidencia:** Configuración de audit log, ejemplo de investigación.  
**Base:** [7] [19]  
**Origen en v1:** P3-C6-Q5 (parcial)  
**Unidad:** organization · **Audiencia:** security, platform-engineer

### D7: Entregar y operar

**Por qué importa:** más cambios generados por IA necesitan redes de seguridad sólidas en la entrega [3], [5]; Microsoft recomienda observación continua de la actividad de agentes [19] y está extendiendo agentes a operaciones de cloud [22].

**Página de la dimensión:** [dimensoes/D7.es.md](dimensoes/D7.es.md)

**Estrategias:** S2, S6 · **Grupo del informe:** G3 (Proteger, entregar y fundamentos)

#### D7-Q1: IA en pipelines CI/CD

¿Se usa IA para crear, mantener y solucionar problemas en pipelines CI/CD (por ejemplo explicar runs fallidos, proponer correcciones), sobre pipeline-as-code?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los pipelines son code en la mayoría de los repositorios; el análisis de fallas asistido por IA está disponible para todos los equipos.
- L4: Los agentes proponen correcciones y optimizaciones de pipeline automáticamente, bajo review, con tiempo de build y tasa de fallas rastreados.

**Ejemplos de evidencia:** Repositorios de pipeline, uso de análisis de fallas, métricas de build.  
**Base:** [16] [17]  
**Origen en v1:** P2-C1-Q1, P2-C1-Q2, P2-C1-Q3  
**Unidad:** repositories · **Audiencia:** devops, platform-engineer · **Preparación de platform engineering:** sí

#### D7-Q2: Entrega progresiva y rollback

¿Los equipos pueden lanzar cambios asistidos por IA de forma segura mediante entrega progresiva (feature flags, canary o blue/green) y rollback automatizado?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La mayoría de los servicios usa feature flags o rollout por etapas; rollback está automatizado para servicios críticos.
- L4: Las decisiones de rollout se guían automáticamente por señales de salud; change failure rate y tiempo de recuperación se rastrean por servicio.

**Ejemplos de evidencia:** Plataforma de feature flags, configuración de rollout, registros de rollback.  
**Base:** [3] [5]  
**Origen en v1:** P2-C1-Q6, P2-C5-Q1, P2-C5-Q2, P2-C5-Q3, P2-C5-Q5  
**Unidad:** services · **Audiencia:** devops, platform-engineer

#### D7-Q3: Respuesta a incidentes asistida por IA

¿Se usa IA en respuesta a incidentes (correlación de alertas, resumen, hipótesis de causa raíz, borradores de revisión post-incidente) con humanos al mando?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los ingenieros de on-call en la mayoría de los equipos usan IA para triage y resúmenes; las revisiones post-incidente registran si la IA ayudó.
- L4: Los agentes de operaciones ejecutan diagnósticos aprobados automáticamente; el tiempo de restauración se compara antes y después de la adopción.

**Ejemplos de evidencia:** Configuración de herramientas de incidentes, timelines de incidentes, datos de tiempo de restauración.  
**Base:** [16] [17] [22]  
**Origen en v1:** P2-C3-Q6, P2-C7-Q2, P2-C7-Q5  
**Unidad:** services · **Audiencia:** devops, platform-engineer

#### D7-Q4: Observabilidad de agentes

¿Los agentes de IA en el SDLC son observables (traces de runs y tool calls, latencia, fallas, costo), por ejemplo mediante OpenTelemetry?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los runs de agentes emiten telemetría al stack central de observabilidad; los dashboards muestran fallas y costo por agente.
- L4: Las alertas se disparan por drift de agentes, picos de error o anomalías de costo; los hallazgos alimentan gobernanza (D1).

**Ejemplos de evidencia:** Dashboards de telemetría, reglas de alerta.  
**Base:** [19] [32] [45]  
**Origen en v1:** P2-C3-Q3, P3-C5-Q6  
**Unidad:** organization · **Audiencia:** devops, platform-engineer

#### D7-Q5: Infrastructure as code con guardrails

¿Se usa IA para escribir y revisar infrastructure as code, con guardrails de policy-as-code que bloquean cambios no conformes?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La mayor parte de la infraestructura es code; IaC generado por IA pasa los mismos policy checks y plan reviews.
- L4: Drift se detecta y corrige mediante GitOps; las violaciones de política por IaC generado por IA se rastrean y van a la baja.

**Ejemplos de evidencia:** Repositorios de IaC, reglas de policy-as-code, informes de drift.  
**Base:** [3] [19]  
**Origen en v1:** P2-C2-Q1, P2-C2-Q2, P2-C2-Q4, P2-C2-Q5, P2-C9-Q1  
**Unidad:** services · **Audiencia:** devops, platform-engineer · **Preparación de platform engineering:** sí

#### D7-Q6: Automatización operacional impulsada por agentes

¿Las tareas operacionales (runbooks, remediación, actualizaciones de dependencias y patches) están automatizadas por agentes bajo reglas de aprobación definidas?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los runbooks comunes y las actualizaciones de dependencias están automatizados; las aprobaciones siguen la matriz de autonomía (D1-Q5).
- L4: La mayoría de las operaciones rutinarias se ejecuta automáticamente con aprobaciones auditadas; el esfuerzo humano se desplaza a excepciones.

**Ejemplos de evidencia:** Catálogo de automatización, logs de aprobación.  
**Base:** [19] [22]  
**Origen en v1:** P2-C7-Q7, P2-C10-Q4  
**Unidad:** services · **Audiencia:** devops, platform-engineer · **Preparación de platform engineering:** sí

### D8: Fundamentos de ingeniería (amplificadores de IA)

**Por qué importa:** DORA encuentra que estas capacidades amplifican los beneficios de la adopción de IA, y que una plataforma interna de alta calidad se correlaciona con la capacidad de desbloquear valor de IA [1], [3].

**Página de la dimensión:** [dimensoes/D8.es.md](dimensoes/D8.es.md)

**Estrategias:** S1, S2, S3 · **Grupo del informe:** G3 (Proteger, entregar y fundamentos)

#### D8-Q1: Control de versiones para todo

¿Application code, configuración, automatización de build, configuración de sistema y prompts/instrucciones de IA están todos almacenados en control de versiones?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los cinco tipos de activos están versionados para la mayoría de los servicios.
- L4: Nada llega a producción sin una fuente versionada; los checks lo confirman automáticamente.

**Ejemplos de evidencia:** Inventario de repositorios, fuentes de configuración.  
**Base:** [1] [2]  
**Origen en v1:** P1-C7-Q1 (parcial)  
**Unidad:** teams · **Audiencia:** platform-engineer, devops, developer

#### D8-Q2: Frecuencia de commit y rollback rápido

¿Los ingenieros hacen commit de cambios pequeños con frecuencia y confían en undo/revert rápido al experimentar con salida de IA?

_Nota de alcance: Mide frecuencia de commit y velocidad de rollback. El tamaño de cambios asistidos por IA es D5-Q4._

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La mayoría de los ingenieros hace commit al menos diariamente; revertir un cambio es rutinario y rápido.
- L4: Trunk-based development con branches de corta duración es la norma; se mide el tiempo de revert.

**Ejemplos de evidencia:** Datos de frecuencia de commit, edad de branch.  
**Base:** [2]  
**Origen en v1:** P2-C1-Q4  
**Unidad:** teams · **Audiencia:** platform-engineer, devops, developer

#### D8-Q3: Plataforma interna de calidad

¿Existe una internal developer platform fácil de usar, que abstrae infraestructura y hace que la ruta segura y conforme sea la predeterminada para humanos y agentes?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Un equipo dedicado de plataforma ofrece golden paths de self-service usados por la mayoría de los equipos; el equipo actúa sobre el feedback.
- L4: Los agentes usan las mismas APIs y guardrails de plataforma que los humanos; la satisfacción con la plataforma se mide y mejora.

**Ejemplos de evidencia:** Catálogo de plataforma, golden paths, encuesta de satisfacción.  
**Base:** [1] [2] [3] [31]  
**Origen en v1:** P1-C2-Q1, P1-C2-Q3, P1-C2-Q4, P1-C2-Q5, P1-C2-Q6  
**Unidad:** organization · **Audiencia:** platform-engineer, devops, developer · **Preparación de platform engineering:** sí

#### D8-Q4: Ecosistema de datos saludable

¿Los ingenieros y herramientas de IA pueden encontrar y usar datos internos confiables (no aislados en silos, de buena calidad, respondibles rápidamente)?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los datos clave están catalogados con responsables e indicadores de calidad; la mayoría de las preguntas puede responderse en una hora.
- L4: La calidad de datos se monitorea automáticamente; existen linaje y contratos para datos críticos.

**Ejemplos de evidencia:** Catálogo de datos, dashboards de calidad.  
**Base:** [1] [2]  
**Origen en v1:** P3-C4-Q1, P3-C4-Q2, P3-C4-Q3  
**Unidad:** organization · **Audiencia:** platform-engineer, devops, developer

#### D8-Q5: Entornos reproducibles para humanos y agentes

¿Los entornos de desarrollo son reproducibles (devcontainers, cloud workspaces, toolchains fijadas) para que humanos y agentes hagan build y test de la misma forma?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La mayoría de los repositorios define un entorno reproducible; los agentes usan la misma definición.
- L4: Los entornos inician en minutos para cualquier repositorio; se detecta drift respecto de la definición.

**Ejemplos de evidencia:** Archivos devcontainer, tiempos de start-up de entorno.  
**Base:** [8]  
**Origen en v1:** P1-C2-Q2, P1-C5-Q1, P1-C9-Q1, P1-C9-Q2, P1-C9-Q3  
**Unidad:** repositories · **Audiencia:** platform-engineer, devops, developer · **Preparación de platform engineering:** sí

#### D8-Q6: Documentación como contexto listo para IA

¿La documentación se mantiene como code, actualizada y con ownership, para que pueda servir como contexto confiable para herramientas de IA?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Los docs viven junto al code con responsables; los docs obsoletos se señalan en reviews.
- L4: La actualidad se verifica automáticamente; los cambios de docs generados por IA se revisan como code.

**Ejemplos de evidencia:** Repositorios de docs, checks de actualidad.  
**Base:** [2] [25]  
**Origen en v1:** P1-C3-Q1, P1-C3-Q4, P1-C7-Q1, P1-C7-Q2, P1-C7-Q3, P1-C7-Q4  
**Unidad:** repositories · **Audiencia:** platform-engineer, devops, developer

#### D8-Q7: Pruebas automatizadas como sistema de control

¿Las pruebas automatizadas son suficientemente profundas y rápidas para detectar regresiones de altos volúmenes de cambios generados por IA (unit, integration, end-to-end, contract)?

_Nota de alcance: Mide pruebas automatizadas como sistema de control. IA usada para escribir pruebas es D5-Q5._

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: La mayoría de los servicios tiene pruebas automatizadas por capas que se ejecutan en cada PR dentro de time budgets acordados.
- L4: Las suites de prueba se ajustan a partir de datos de defectos escapados; el tiempo de feedback se rastrea y mejora.

**Ejemplos de evidencia:** Inventario de suites de prueba, duraciones de pipeline, datos de defectos escapados.  
**Base:** [3]  
**Origen en v1:** P2-C6-Q2, P2-C6-Q3, P2-C6-Q4, P1-C8-Q3  
**Unidad:** services · **Audiencia:** platform-engineer, devops, developer

### D9: Medición, valor y AI FinOps

**Por qué importa:** estudios controlados van desde 55.8% más rápido [33] y 26.08% más tareas completadas [34] hasta 19% más lento con una fuerte brecha de percepción [35], por lo que las organizaciones necesitan su propia medición objetiva; Gartner predice que los costos de AI coding superarán el salario promedio de un desarrollador para 2028 [32].

**Página de la dimensión:** [dimensoes/D9.es.md](dimensoes/D9.es.md)

**Estrategias:** S5, S2 · **Grupo del informe:** G1 (Dirección, personas y valor)

#### D9-Q1: Métricas de profundidad de adopción

¿La adopción de IA se rastrea con telemetría más allá del conteo de seats (usuarios activos, engagement por feature, cohortes de adopción)?

_Nota de alcance: Mide si la adopción se rastrea. Qué tan profundamente se usa IA es D4-Q1._

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Las métricas de uso (por ejemplo la API o dashboard de métricas de uso de Copilot) se revisan mensualmente por el liderazgo de ingeniería.
- L4: El movimiento de cohortes es un objetivo gestionado; las acciones de habilitación se evalúan por su efecto en las cohortes.

**Ejemplos de evidencia:** Dashboards de uso, informes de tendencia de cohortes.  
**Base:** [6]  
**Origen en v1:** P1-C1-Q3  
**Unidad:** organization · **Audiencia:** engineering-leader, product-owner

#### D9-Q2: Métricas de resultado de entrega

¿Las métricas de entrega de software (lead time, deployment frequency, change failure rate, time to restore) se rastrean y comparan antes y después de la adopción de IA?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Las métricas DORA se recopilan automáticamente para la mayoría de los servicios y se revisan con datos de adopción de IA.
- L4: Las métricas de entrega son parte de decisiones de inversión en IA; las regresiones disparan acción correctiva.

**Ejemplos de evidencia:** Dashboards DORA, comparación baseline versus actual.  
**Base:** [2] [3] [5]  
**Origen en v1:** P1-C8-Q1, P2-C1-Q5, P2-C5-Q6, P2-C3-Q1  
**Unidad:** services · **Audiencia:** engineering-leader, product-owner

#### D9-Q3: Métricas de flujo de pull request

¿Se rastrean el throughput de PR, el tiempo hasta merge y la proporción y tasa de merge de PRs creados por IA o agentes?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Las métricas de ciclo de vida de PR se reportan por organización; los PRs creados por agentes se identifican por separado, incluida su tasa de correcciones post-merge.
- L4: Las métricas de flujo se vinculan con métricas de calidad (D5) para que el flujo más rápido no se compre con inestabilidad.

**Ejemplos de evidencia:** Métricas de ciclo de vida de PR, informes de PRs de agentes, análisis de correcciones de seguimiento.  
**Base:** [6] [34] [50]  
**Origen en v1:** P1-C4-Q5, P1-C8-Q5  
**Unidad:** organization · **Audiencia:** engineering-leader, product-owner

#### D9-Q4: Developer experience y fricción

¿Developer experience se mide regularmente (productividad percibida, fricción, confianza en IA, satisfacción), usando un framework reconocido como SPACE o las preguntas de resultado de DORA?

_Nota de alcance: Mide la encuesta de developer experience. Comportamiento de review y calibración de confianza es D5-Q6._

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Una encuesta se realiza al menos dos veces al año con buena participación; los resultados se comparten y generan acciones.
- L4: Los resultados de encuestas se combinan con telemetría (D9-Q1 a Q3) para encontrar y eliminar fricción.

**Ejemplos de evidencia:** Instrumento de encuesta, tasa de participación, log de acciones.  
**Base:** [2] [44]  
**Origen en v1:** P1-C8-Q2, P1-C8-Q4  
**Unidad:** organization · **Audiencia:** engineering-leader, product-owner

#### D9-Q5: Medición controlada de impacto

¿El impacto de IA se estima con comparaciones controladas o basadas en cohortes (por ejemplo piloto versus control, cohortes de adopción, antes/después con un baseline) en vez de solo estimaciones autorreportadas?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Se ejecutó y documentó al menos una comparación controlada o de cohorte, con sus limitaciones.
- L4: Las comparaciones se ejecutan continuamente para herramientas y prácticas principales; las decisiones las citan.

**Ejemplos de evidencia:** Diseño del estudio, resultados, registros de decisión.  
**Base:** [6] [34] [35]  
**Origen en v1:** Ninguno (nueva en v2)  
**Unidad:** organization · **Audiencia:** engineering-leader, product-owner

#### D9-Q6: Gobernanza de costos de IA (AI FinOps)

¿Los costos de IA (seats, premium requests, tokens, runs de agentes) se presupuestan, monitorean por equipo y caso de uso, con thresholds y revisiones regulares?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Existen presupuestos y thresholds de alerta por organización o equipo; los workflows de alto consumo se revisan en retrospectivas.
- L4: Se rastrea el costo por resultado (por ejemplo por PR mergeado); las prácticas de enrutamiento y contexto se ajustan para reducir desperdicio.

**Ejemplos de evidencia:** Dashboards de costo, alertas de presupuesto, notas de retrospectiva.  
**Base:** [19] [32] [38] [45]  
**Origen en v1:** P3-C9-Q1 (parcial)  
**Unidad:** organization · **Audiencia:** engineering-leader, product-owner

#### D9-Q7: Vínculo con valor de negocio

¿Los resultados de ingeniería con IA se conectan con valor de negocio (business case, supuestos de ROI, OKRs) y se revisan con stakeholders de finanzas o negocio?

- L0 - No iniciado: Aún no hay práctica, o IA no está permitida para esta actividad
- L1 - Explorando: Uso individual o ad hoc, sin orientación acordada (más de 0% y hasta 25% de los equipos)
- L2 - Adoptando: Práctica a nivel de equipo con orientación escrita (26-50% de los equipos)
- L3 - Escalando: Estándar de la organización, gobernado y medido (51-90% de los equipos)
- L4 - Nativo en IA: Universal (>90%), evaluado y mejorado continuamente, vinculado a resultados
- L3: Existe un business case con supuestos explícitos y se revisa al menos anualmente.
- L4: El valor se informa con una cadencia fija con insumos medidos de D9-Q1 a Q6; la inversión se ajusta a partir de los resultados.

**Ejemplos de evidencia:** Business case, informes de valor.  
**Base:** [18] [28] [32]  
**Origen en v1:** P1-C8-Q6, P3-C9-Q5  
**Unidad:** organization · **Audiencia:** engineering-leader, product-owner

## Referencias

1. DORA. _DORA AI Capabilities Model_. Google Cloud, 2025. <https://dora.dev/ai/capabilities-model/report/>
2. DORA. _DORA AI Capabilities Model: Survey Questions_. Google Cloud, 2025. <https://dora.dev/ai/capabilities-model/questions/>
3. Google Cloud. _Announcing the 2025 DORA Report: State of AI-Assisted Software Development_. 2025. <https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report>
4. DORA. _State of AI-assisted Software Development 2025_. <https://dora.dev/research/2025/dora-report/>
5. Google Cloud. _Announcing the 2024 DORA report_. 2024-10-22. <https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report>
6. GitHub Docs. _GitHub Copilot usage metrics_. <https://docs.github.com/en/copilot/concepts/billing-and-usage/copilot-usage-metrics/copilot-metrics>
7. GitHub Docs. _Risks and mitigations for GitHub Copilot cloud agent_. <https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations>
8. GitHub Docs. _Best practices for using GitHub Copilot to work on tasks_. <https://docs.github.com/enterprise-cloud@latest/copilot/tutorials/cloud-agent/get-the-best-results>
9. GitHub Docs. _Configuring an MCP server allowlist for your enterprise_. <https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-enterprise-allowlist>
10. GitHub Docs. _Restrict MCP server access to a custom registry_. <https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/restrict-based-on-registry>
11. GitHub Docs. _Custom agents configuration_. <https://docs.github.com/en/copilot/reference/custom-agents-configuration>
12. GitHub Docs. _About GitHub Copilot code review_. <https://docs.github.com/copilot/concepts/agents/code-review>
13. GitHub Docs. _About autofix for code scanning_. <https://docs.github.com/en/code-security/concepts/code-scanning/autofix-for-code-scanning>
14. GitHub Docs. _Application card: GitHub Copilot Agents_. <https://docs.github.com/en/copilot/responsible-use/agents>
15. GitHub Docs. _Managing policies and features for GitHub Copilot in your organization_. <https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies>
16. Microsoft Azure Blog. _Agentic DevOps: Evolving software development with GitHub Copilot and Microsoft Azure_. 2025. <https://azure.microsoft.com/en-us/blog/agentic-devops-evolving-software-development-with-github-copilot-and-microsoft-azure/>
17. Microsoft for Developers. _Agentic DevOps in action: Reimagining every phase of the developer lifecycle_. 2025. <https://developer.microsoft.com/blog/reimagining-every-phase-of-the-developer-lifecycle/>
18. Microsoft Learn. _AI strategy: Cloud Adoption Framework_. <https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/strategy>
19. Microsoft Learn. _Govern and secure AI agents: Cloud Adoption Framework_. <https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization>
20. Microsoft Learn. _Responsible AI policies: Cloud Adoption Framework_. <https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/responsible-ai-policies>
21. Microsoft. _Responsible AI Principles and Approach_. <https://www.microsoft.com/en-us/ai/principles-and-approach>
22. Microsoft Azure Blog. _Announcing Azure Copilot agents and AI infrastructure innovations_. 2025. <https://azure.microsoft.com/en-us/blog/announcing-azure-copilot-agents-and-ai-infrastructure-innovations/>
23. Anthropic. _Anthropic Economic Index: AI's impact on software development_. 2025-04-28. <https://www.anthropic.com/research/impact-software-development>
24. Anthropic. _How Claude Code is used in practice_. 2026-06-16. <https://www.anthropic.com/research/claude-code-expertise>
25. Anthropic. _Effective context engineering for AI agents_. 2025-09-29. <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
26. Anthropic. _Building effective agents_. 2024-12-19. <https://www.anthropic.com/engineering/building-effective-agents>
27. Anthropic. _Best practices for Claude Code_. Claude Code Docs. <https://code.claude.com/docs/en/best-practices>
28. Gartner. _Gartner Says 75% of Enterprise Software Engineers Will Use AI Code Assistants by 2028_. 2024-04-11. <https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028>
29. Gartner. _Gartner Identifies the Top Strategic Trends in Software Engineering for 2025 and Beyond_. 2025-07-01. <https://www.gartner.com/en/newsroom/press-releases/2025-07-01-gartner-identifies-the-top-strategic-trends-in-software-engineering-for-2025-and-beyond>
30. Gartner. _Gartner Says Generative AI will Require 80% of Engineering Workforce to Upskill Through 2027_. 2024-10-03. <https://www.gartner.com/en/newsroom/press-releases/2024-10-03-gartner-says-generative-ai-will-require-80-percent-of-engineering-workforce-to-upskill-through-2027>
31. Gartner. _Gartner Says the Market for Enterprise AI Coding Agents Is Entering a New Phase of Expansion and Competitive Realignment_. 2026-05-20. <https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-says-the-market-for-enterprise-ai-coding-agents-is-entering-a-new-phase-of-expansion-and-competitive-realignment>
32. Gartner. _Gartner Predicts AI Coding Costs Will Surpass Average Developer's Salary by 2028 as Token Consumption Surges_. 2026-06-24. <https://www.gartner.com/en/newsroom/press-releases/2026-06-24-gartner-predicts-ai-coding-costs-will-surpass-average-developer-salary-by-2028-as-token-consumption-surges>
33. Peng, S., Kalliamvakou, E., Cihon, P., Demirer, M. _The Impact of AI on Developer Productivity: Evidence from GitHub Copilot_. arXiv:2302.06590, 2023. <https://arxiv.org/abs/2302.06590>
34. Cui, Z. K., Demirer, M., Jaffe, S., Musolff, L., Peng, S., Salz, T. _The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers_. Management Science, published online 2026-02-27. <https://doi.org/10.1287/mnsc.2025.00535> (pre-print: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566>)
35. METR. _Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity_. 2025-07-10. <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/> (paper: <https://arxiv.org/abs/2507.09089>)
36. METR. _We are Changing our Developer Productivity Experiment Design_. 2026-02-24. <https://metr.org/blog/2026-02-24-uplift-update/>
37. Stack Overflow. _2025 Developer Survey: AI_. <https://survey.stackoverflow.co/2025/ai>
38. OWASP GenAI Security Project. _OWASP Top 10 for LLM Applications 2025_. <https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/>
39. OWASP GenAI Security Project. _OWASP Top 10 for Agentic Applications for 2026_. 2025-12-09. <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>
40. NIST. _SP 800-218A: Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile_. 2024-07. <https://csrc.nist.gov/pubs/sp/800/218/a/final>
41. NIST. _AI Risk Management Framework_. <https://www.nist.gov/itl/ai-risk-management-framework>
42. ISO. _ISO/IEC 42001:2023: AI management systems_. <https://www.iso.org/standard/42001>
43. OpenSSF. _SLSA: Supply-chain Levels for Software Artifacts_. <https://slsa.dev/>
44. Forsgren, N., Storey, M.-A., Maddila, C., Zimmermann, T., Houck, B., Butler, J. _The SPACE of Developer Productivity_. ACM Queue 19(1), 2021-03-06. <https://queue.acm.org/detail.cfm?id=3454124> (DOI: <https://doi.org/10.1145/3454122.3454124>)
45. Liu, B., Qiu, H., Goiri, Í., Fonseca, R., Bianchini, R., Choukse, E. _Agentic Coding in the Wild: Characterizing GitHub Copilot Traces at Production Scale_. arXiv:2608.00101, 2026-07-30. <https://arxiv.org/abs/2608.00101>
46. Arabat, A., Sayagh, M. _Toward Instructions-as-Code: Understanding the Impact of Instruction Files on Agentic Pull Requests_. arXiv:2606.13449, 2026-06-11. <https://arxiv.org/abs/2606.13449>
47. Denisov-Blanch, Y., Agarwal, S., Azaletskiy, P., He, H., Schaeffer, R., Miranda, B., Vasilescu, B., Koyejo, S. _A Few Pages of Markdown: Committed AI Configuration and Lower Quality Cost after Coding-Agent Adoption_. arXiv:2608.25241, 2026-08-26. <https://arxiv.org/abs/2608.25241>
48. Shen, J. H., Tamkin, A. _How AI Impacts Skill Formation_. arXiv:2601.20245, 2026-01-28. <https://arxiv.org/abs/2601.20245> (Anthropic summary: <https://www.anthropic.com/research/AI-assistance-coding-skills>)
49. Pinna, G., Gong, J., Williams, D., Sarro, F. _Comparing AI Coding Agents: A Task-Stratified Analysis of Pull Request Acceptance_. arXiv:2602.08915, 2026-02-09. <https://arxiv.org/abs/2602.08915>
50. Takerngsaksiri, W., Duong, N., Barnett, S. _Who Finishes the Job? A Study of Follow-Up Fixes and Commit Authorship on AI Coding Agent Pull Requests_. arXiv:2609.26847, 2026-09-22. <https://arxiv.org/abs/2609.26847>
51. Sawada, S., Shirai, T., Kashiwa, Y., Yamaguchi, K., Iwata, H., Iida, H. _To What Extent Does Agent-generated Code Require Maintenance? An Empirical Study_. arXiv:2605.06464, 2026-05-07. <https://arxiv.org/abs/2605.06464>
52. Sakib, A. H. M. N., Banik, D., Jadliwala, M. _Trust but Verify? Uncovering the Security Debt of Autonomous Coding Agents_. arXiv:2607.12428, 2026-07-14. <https://arxiv.org/abs/2607.12428>
53. Nachuma, C., Zibran, M. _When AI Teammates Meet Code Review: Collaboration Signals Shaping the Integration of Agent-Authored Pull Requests_. arXiv:2602.19441, 2026-02-23. <https://arxiv.org/abs/2602.19441>
54. Selvanayagam, N., Ghaleb, T. A. _AI-to-AI Code Reviews of GitHub Pull Requests_. arXiv:2608.21311, 2026-08-21. <https://arxiv.org/abs/2608.21311>
55. Stolze, M., Strässle, M. _When Review Alone No Longer Scales: Layered Supervision in AI-Assisted Software Engineering_. arXiv:2608.26316, 2026-08-26. <https://arxiv.org/abs/2608.26316>
56. Monperrus, M. _The End of Code Review: Coding Agents Supersede Human Inspection_. arXiv:2606.13175, 2026-06-11. <https://arxiv.org/abs/2606.13175>
57. Siddiq, M. L., Zhao, X., Lopes, V. C., Casey, B., Santos, J. C. S. _Security in the Age of AI Teammates: An Empirical Study of Agentic Pull Requests on GitHub_. arXiv:2601.00477, 2026-01-01. <https://arxiv.org/abs/2601.00477>
58. Farrag, S. E. _The Productivity-Reliability Paradox: Specification-Driven Governance for AI-Augmented Software Development_. arXiv:2605.01160, 2026-05-01. <https://arxiv.org/abs/2605.01160>
