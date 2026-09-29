# AI Maturity Assessment: Pilar P1, Productividad del desarrollador

🌐 [English](P1-developer-productivity.md) · [Português (Brasil)](P1-developer-productivity.pt-br.md) · Español

> Mide cuánto adopta ingeniería la IA para acelerar el ciclo de codificación, documentación, revisión, onboarding y colaboración interna.

## Resumen

- **Pilar:** `P1`: Productividad del desarrollador
- **Capabilities incluidas:** 9
- **Total de preguntas:** 53
- **Escala:** Likert L0 a L4 (Inicial a Optimizando)
- **Idioma de las preguntas:** español (traducido de la redacción original en portugués de Brasil)
- **Idioma de los KPI:** inglés en todas las versiones (nombres de métrica, como en `framework.json`)
- **Respuesta esperada por pregunta:** 1 nivel seleccionado + texto de evidencia (mínimo recomendado de 80 caracteres) + adjunto opcional

## Cómo interpretar la escala

| Nivel | Etiqueta | Significado |
|---|---|---|
| **L0** | Inicial | No hay práctica establecida; acciones ad-hoc, sin herramienta ni política. |
| **L1** | En desarrollo | Pilotos aislados, cobertura <25%, sin gobernanza. |
| **L2** | Definido | Adopción en 25-50% de los equipos, con directrices y capacitación básica. |
| **L3** | Gestionado | Cobertura >75% con métricas de impacto y bibliotecas/plantillas compartidas. |
| **L4** | Optimizando | Cobertura casi universal (>95%), automatización, fine-tuning, mejora continua medida. |

## Tipos de información recopilada por pregunta

Cada pregunta captura simultáneamente **tres tipos de datos**:

1. **Cuantitativo (KPI):** una métrica numérica explícita (p. ej., % de desarrolladores activos, MTTR, lead time, tasa de cobertura). Usa el KPI sugerido para estandarizar la comparación entre equipos.

2. **Cualitativo (descripción del nivel):** la persona encuestada selecciona el nivel L0 a L4 cuya descripción representa mejor la realidad observada hoy (no la aspiracional).

3. **Evidencia (texto + adjuntos):** prueba documental, como un enlace de pipeline, captura de dashboard, política, runbook, contrato de licencias o métrica exportada. Cuanto más específica, mayor es la calidad de la evidencia (escala: ninguna a mínima a adecuada a detallada a ejemplar).

## Criterios de calidad de la evidencia

- **Mínima (<80 caracteres):** texto genérico, sin nombre de herramienta, métrica ni enlace.
- **Adecuada (80-250):** menciona la herramienta + cobertura/alcance aproximado.
- **Detallada (250-500):** incluye una métrica numérica + enlace/adjunto + periodo de medición.
- **Ejemplar (>500 o varios adjuntos):** múltiples fuentes corroborantes, serie temporal, comparación antes/después.

## Capabilities del pilar P1

- **P1-C1**: Asistentes de codificación con IA (5 preguntas)
- **P1-C2**: Plataforma de experiencia del desarrollador (6 preguntas)
- **P1-C3**: Gestión del conocimiento (6 preguntas)
- **P1-C4**: Automatización de la revisión de código (7 preguntas)
- **P1-C5**: Onboarding y capacitación de desarrolladores (7 preguntas)
- **P1-C6**: Inner source y colaboración (6 preguntas)
- **P1-C7**: Automatización de la documentación (5 preguntas)
- **P1-C8**: Medición de productividad del desarrollador (6 preguntas)
- **P1-C9**: Automatización de entornos y workspaces (5 preguntas)

---

## P1-C1: Asistentes de codificación con IA

**5 preguntas en esta capability.**

### P1-C1-Q1: ¿En qué medida tu organización utiliza herramientas de completado de código con IA (por ejemplo, GitHub Copilot)?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% developers using AI completion`

**Contexto**

- **Qué mide (what):** Mide la adopción de herramientas de completado de código y sugerencias impulsadas por IA en todo el equipo de desarrollo.
- **Por qué importa (why):** Los asistentes de codificación con IA pueden aumentar la velocidad de los desarrolladores en un 30-55% en tareas rutinarias de codificación, reduciendo el tiempo de salida al mercado.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin herramientas de codificación con IA implementadas. Todo el código se escribe manualmente sin asistencia de IA. | • Sin licencias de herramientas de IA<br>• Sin políticas de herramientas de IA<br>• Flujos de codificación solo manuales |
| **L1** | En desarrollo | Implementación piloto de un asistente de codificación con IA para <10% de los desarrolladores. Uso ad-hoc sin directrices. | • Documentación del programa piloto<br>• < 10% de asignación de licencias<br>• Sin política de uso definida |
| **L2** | Definido | Asistente de codificación con IA desplegado para 25-50% de los desarrolladores con directrices de uso y capacitación básica. | • 25-50% de cobertura de licencias<br>• Directrices de uso escritas<br>• Materiales de capacitación sobre completions |
| **L3** | Gestionado | Asistente de codificación con IA desplegado para >75% de los desarrolladores con ganancias de productividad medidas >15% y bibliotecas de prompts. | • >75% de usuarios activos<br>• Métricas de productividad que muestran >15% de ganancia<br>• Repositorio compartido de biblioteca de prompts |
| **L4** | Optimizando | Asistente de codificación con IA universal (>95%) con fine-tuning de modelo personalizado y mejora de velocidad medida >30%. | • >95% de uso activo diario<br>• Configuración de fine-tuning de modelo personalizado<br>• Mejora de velocidad medida >30%<br>• Seguimiento automatizado de calidad de sugerencias |

---

### P1-C1-Q2: ¿Con qué eficacia tu equipo aprovecha la IA para la revisión de código y la mejora de la calidad?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% PRs with AI review`

**Contexto**

- **Qué mide (what):** Mide el uso de IA en los procesos de revisión de código para detectar errores, sugerir mejoras y hacer cumplir estándares.
- **Por qué importa (why):** La revisión de código asistida por IA reduce el tiempo de revisión en un 40% y detecta un 20% más de defectos que la revisión solo manual.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin participación de IA en la revisión de código. Todas las revisiones son revisiones manuales entre pares. | • Proceso de revisión solo manual<br>• Sin herramientas de revisión con IA<br>• Sin quality gates automatizados |
| **L1** | En desarrollo | Linting básico y herramientas de análisis estático en CI. Sin sugerencias de revisión impulsadas por IA. | • Configuración de linting en CI<br>• Configuración de herramienta de análisis estático<br>• Sin bot de revisión con IA configurado |
| **L2** | Definido | Bot de revisión con IA configurado en 30-60% de los repositorios, que proporciona sugerencias automatizadas de código. | • Bot de revisión con IA en 30-60% de los repos<br>• Ejemplos de sugerencias en PR<br>• Documentación de configuración del bot de revisión |
| **L3** | Gestionado | Revisión con IA integrada en >80% de los repositorios con reglas personalizadas alineadas con los estándares del equipo. | • >80% de cobertura de repos<br>• Configuración de reglas personalizadas<br>• Reducción medida >25% del ciclo de revisión |
| **L4** | Optimizando | La IA realiza la primera revisión en todos los PRs, aprueba automáticamente cambios de bajo riesgo y escala los críticos. | • Primer pase de IA en el 100% de los PR<br>• Política de autoaprobación documentada<br>• Modelo de clasificación de riesgo<br>• Reducción >50% del tiempo de ciclo |

---

### P1-C1-Q3: ¿Cómo mide y da seguimiento tu organización al impacto de las herramientas de codificación con IA en la productividad?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 0.8
- **Professional Edition:** No
- **KPI principal:** `Productivity measurement maturity`

**Contexto**

- **Qué mide (what):** Mide la capacidad de la organización para cuantificar el valor de las herramientas de codificación con IA.
- **Por qué importa (why):** Sin medición, las organizaciones no pueden justificar la inversión en herramientas de IA ni optimizar las estrategias de adopción.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin medición del impacto de las herramientas de IA. No se capturan métricas base de productividad. | • Sin métricas DORA<br>• Sin dashboards de productividad<br>• Sin seguimiento del uso de herramientas de IA |
| **L1** | En desarrollo | Feedback anecdótico de desarrolladores sobre la utilidad de las herramientas de IA. Sin medición cuantitativa. | • Resultados de encuesta a desarrolladores<br>• Recopilación informal de feedback<br>• Sin datos cuantitativos |
| **L2** | Definido | Métricas DORA básicas rastreadas (frecuencia de despliegue, lead time). Analítica de uso de herramientas de IA disponible. | • Dashboard de métricas DORA<br>• Informe mensual de analítica de uso<br>• Mediciones de línea base establecidas |
| **L3** | Gestionado | Métricas integrales de productividad del desarrollador, incluidas medidas específicas de IA: tasa de aceptación, tiempo ahorrado. | • >40% de tasa de aceptación de sugerencias<br>• >20% de mejora en time-to-merge<br>• Análisis de tendencia de densidad de defectos |
| **L4** | Optimizando | Plataforma de inteligencia de productividad en tiempo real que correlaciona el uso de herramientas de IA con resultados de negocio. | • Dashboard de productividad en tiempo real<br>• Informes de ROI automatizados<br>• Análisis de correlación con resultados de negocio<br>• Recomendaciones de optimización por equipo |

---

### P1-C1-Q4: ¿Qué nivel de capabilities de pruebas asistidas por IA emplea tu organización?

**Metadatos**

- **Público objetivo:** Desarrollador, qa-test, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% test coverage from AI generation`

**Contexto**

- **Qué mide (what):** Mide el uso de IA para generar, mantener y optimizar suites de pruebas.
- **Por qué importa (why):** Las pruebas generadas por IA pueden aumentar la cobertura del 40% al 80% en semanas, detectando regresiones que las pruebas manuales no encuentran.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Todas las pruebas se escriben manualmente. Cobertura de pruebas inferior a 40% en la mayoría de los proyectos. | • Solo escritura manual de pruebas<br>• <40% de cobertura promedio<br>• Sin herramientas de generación de pruebas con IA |
| **L1** | En desarrollo | Uso ocasional de IA para generar esqueletos de pruebas unitarias. La cobertura permanece por debajo de 50%. | • Generación ad-hoc de pruebas con IA<br>• Tasa de cobertura medida <50%<br>• Sin enfoque sistemático |
| **L2** | Definido | Generación de pruebas con IA integrada en el flujo de desarrollo para 30-50% del código nuevo. Cobertura >60%. | • Generación de pruebas con IA en 30-50% del código nuevo<br>• Quality gates de 60% de cobertura en CI<br>• Directrices de generación de pruebas |
| **L3** | Gestionado | La IA genera >70% de las pruebas unitarias con revisión humana. Cobertura >75%. La IA identifica casos borde. | • >70% de pruebas generadas por IA<br>• >75% de cobertura en todos los proyectos<br>• Ejemplos de sugerencias para casos límite |
| **L4** | Optimizando | Optimización de pruebas impulsada por IA: genera suites de regresión automáticamente, identifica pruebas inestables, optimiza la cobertura. | • Tasa de cobertura medida >85%<br>• Tasa de pruebas flaky <5%<br>• Generación automatizada de suite de regresión<br>• Integración de mutation testing |

---

### P1-C1-Q5: ¿Cómo gobierna tu organización el código generado por IA en términos de seguridad y cumplimiento?

**Metadatos**

- **Público objetivo:** Desarrollador, Seguridad, product-owner, qa-test
- **Peso:** 1.1
- **Professional Edition:** No
- **KPI principal:** `AI code governance maturity`

**Contexto**

- **Qué mide (what):** Mide las políticas y controles en torno a la calidad, seguridad y cumplimiento de propiedad intelectual del código generado por IA.
- **Por qué importa (why):** Sin gobernanza, el código generado por IA puede introducir vulnerabilidades, infracciones de licencias y riesgos de cumplimiento.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin gobernanza sobre código generado por IA. No existe ninguna política. Los desarrolladores usan herramientas de IA sin restricciones. | • Sin política de código con IA<br>• Sin escaneo de seguridad del código con IA<br>• Sin verificaciones de cumplimiento de licencias |
| **L1** | En desarrollo | Existe una política básica que prohíbe el uso de IA en módulos sensibles a la seguridad. Sin automatización. | • Política escrita de uso de IA<br>• Lista de módulos sensibles a seguridad<br>• Sin aplicación automatizada |
| **L2** | Definido | El código generado por IA pasa por análisis de seguridad estándar (SAST/DAST). Verificación de cumplimiento de licencias en CI. | • Pipeline SAST/DAST incluye código con IA<br>• Escaneo de cumplimiento de licencias<br>• Aplicación de políticas en CI |
| **L3** | Gestionado | Gateways de calidad de código dedicados para IA: escaneo de vulnerabilidades, auditoría de licencias, revisión de calidad de código. | • Quality gates específicos para IA<br>• Seguimiento de procedencia del código<br>• Tasa de flags de seguridad <2%<br>• Informes trimestrales de auditoría |
| **L4** | Optimizando | Gobernanza de código de IA en tiempo real: cada sugerencia se escanea antes de mostrarse, las licencias se bloquean y las métricas de calidad se rastrean. | • Escaneo de contenido previo a la visualización habilitado<br>• Rechazo automático de licencias bloqueadas<br>• Política de cero código con IA sin revisar<br>• Certificación de cumplimiento lograda |

---

## P1-C2: Plataforma de experiencia del desarrollador

**6 preguntas en esta capability.**

### P1-C2-Q1: ¿Qué tan maduro es tu portal o plataforma interna para desarrolladores?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de plataforma, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** Sí
- **KPI principal:** `Developer portal adoption %`

**Contexto**

- **Qué mide (what):** Mide la madurez del portal centralizado para desarrolladores para catálogo de servicios, documentación y autoservicio.
- **Por qué importa (why):** Un portal de desarrolladores maduro reduce el tiempo de onboarding en un 60% y elimina el cambio de contexto entre herramientas.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin portal de desarrolladores. Documentación dispersa en wikis, Slack y correo electrónico. | • Sin portal centralizado<br>• Documentación en múltiples herramientas<br>• Sin catálogo de servicios |
| **L1** | En desarrollo | Wiki básica o espacio de Confluence con algo de documentación. Sin catálogo de servicios ni capabilities de autoservicio. | • Existe wiki central<br>• Algunos documentos de API<br>• Sin catálogo de servicios |
| **L2** | Definido | Portal de desarrolladores desplegado (Backstage o similar) con catálogo de servicios que cubre >50% de los servicios. Plantillas básicas de documentación. | • >50% de servicios catalogados<br>• Documentación de despliegue del portal<br>• Plantillas de documentación publicadas |
| **L3** | Gestionado | El portal de desarrolladores cubre >80% de los servicios con scaffolding de autoservicio, documentación de API automatizada y estado de CI/CD integrado. Tiempo de onboarding reducido >40%. | • >80% de cobertura de servicios<br>• Herramientas de scaffolding de autoservicio<br>• >40% de reducción del tiempo de onboarding |
| **L4** | Optimizando | Portal de desarrolladores impulsado por IA: búsqueda en lenguaje natural en toda la documentación, diagramas de arquitectura autogenerados, detección predictiva de problemas. Satisfacción de desarrolladores >95%. | • Búsqueda impulsada por IA habilitada<br>• Diagramas de arquitectura generados automáticamente<br>• Puntuación de satisfacción >95%<br>• Detección predictiva de problemas |

---

### P1-C2-Q2: ¿Con qué eficacia tus equipos usan entornos de desarrollo estandarizados?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de plataforma
- **Peso:** 0.9
- **Professional Edition:** Sí
- **KPI principal:** `Environment setup time (minutes)`

**Contexto**

- **Qué mide (what):** Mide la estandarización de los entornos de desarrollo en todos los equipos.
- **Por qué importa (why):** Los entornos estandarizados eliminan los problemas de 'funciona en mi máquina' y reducen el tiempo de configuración de días a minutos.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Cada desarrollador mantiene la configuración de su propio entorno. Sin estandarización. La configuración toma >4 horas para nuevos miembros del equipo. | • Sin estandarización de entornos<br>• Tiempo de configuración >4 horas<br>• Instalación manual de dependencias |
| **L1** | En desarrollo | README con instrucciones de configuración. Algunos equipos usan Docker para desarrollo local. Tiempo de configuración 1-4 horas. | • Guía de configuración en README<br>• Algo de uso de Docker<br>• Tiempo de configuración de 1-4 horas |
| **L2** | Definido | Docker Compose o devcontainer para >50% de los proyectos. Tiempo de configuración <30 minutos. Configuraciones compartidas. | • >50% de proyectos con contenedores<br>• Tiempo de configuración <30 min<br>• Configuraciones de desarrollo compartidas |
| **L3** | Gestionado | Devcontainers estandarizados para >80% de los proyectos. Entornos de desarrollo basados en la nube disponibles (Codespaces). Tiempo de configuración <10 minutos. | • >80% de cobertura de devcontainer<br>• Entorno de desarrollo en la nube disponible<br>• Tiempo de configuración <10 min |
| **L4** | Optimizando | Entornos de desarrollo efímeros de un clic con dependencias configuradas por IA. Cero configuración manual. Paridad del entorno con producción garantizada. | • Creación de entorno con un clic<br>• Cero pasos manuales de configuración<br>• Verificación de paridad con producción documentada<br>• Configuración de dependencias de IA |

---

### P1-C2-Q3: ¿En qué medida se ha adoptado la Plataforma de Experiencia del Desarrollador (IDP de autoservicio) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de plataforma, Arquitecto, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `Self-service catalog coverage`

**Contexto**

- **Qué mide (what):** La plataforma interna para desarrolladores (IDP) proporciona caminos trazados con aprovisionamiento de autoservicio.
- **Por qué importa (why):** Las IDP reducen la carga cognitiva y aceleran el onboarding en un 50-70%.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de IDP de autoservicio. Los equipos operan sin esta capability. | • Sin IDP de autoservicio implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de IDP de autoservicio con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de IDP de autoservicio se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de IDP de autoservicio está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de IDP de autoservicio está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C2-Q4: ¿En qué medida se ha adoptado la Plataforma de Experiencia del Desarrollador (golden paths y plantillas) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de plataforma, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services from templates`

**Contexto**

- **Qué mide (what):** Las plantillas de golden path codifican valores predeterminados con opinión para nuevos servicios.
- **Por qué importa (why):** Las plantillas estándar reducen el tiempo hasta el primer commit y hacen cumplir líneas base de seguridad.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de golden paths y plantillas. Los equipos operan sin esta capability. | • Sin golden paths y plantillas implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de golden paths y plantillas con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de golden paths y plantillas se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de golden paths y plantillas está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de golden paths y plantillas está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C2-Q5: ¿En qué medida se ha adoptado la Plataforma de Experiencia del Desarrollador (portal de desarrolladores) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de plataforma, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `Portal MAU (monthly active users)`

**Contexto**

- **Qué mide (what):** Un portal de desarrolladores centraliza documentación, APIs y catálogo de servicios.
- **Por qué importa (why):** Un panel único reduce el cambio de contexto y mejora el descubrimiento.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de portal de desarrolladores. Los equipos operan sin esta capability. | • Sin portal de desarrolladores implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de portal de desarrolladores con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de portal de desarrolladores se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de portal de desarrolladores está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de portal de desarrolladores está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C2-Q6: ¿En qué medida se ha adoptado la Plataforma de Experiencia del Desarrollador (cumplimiento de políticas del camino trazado) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de plataforma, Seguridad, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `services on paved road`

**Contexto**

- **Qué mide (what):** Las políticas de plataforma están codificadas para que los equipos deban optar por no usarlas de forma explícita.
- **Por qué importa (why):** Policy-as-code convierte la gobernanza en un habilitador, no en un bloqueador.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de cumplimiento de políticas de paved road. Los equipos operan sin esta capability. | • Sin aplicación de política de paved road implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de cumplimiento de políticas de paved road con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de cumplimiento de políticas de paved road se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de cumplimiento de políticas de paved road está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de cumplimiento de políticas de paved road está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P1-C3: Gestión del conocimiento

**6 preguntas en esta capability.**

### P1-C3-Q1: ¿Con qué eficacia tu organización captura y comparte el conocimiento de desarrollo?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `Knowledge retrieval success rate %`

**Contexto**

- **Qué mide (what):** Mide qué tan bien se captura, organiza y hace accesible el conocimiento de desarrollo.
- **Por qué importa (why):** Una mala gestión del conocimiento causa que se desperdicie el 20% del tiempo de los desarrolladores buscando información o reinventando soluciones.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | El conocimiento vive en la cabeza de desarrolladores individuales. Sin cultura de documentación. Alto riesgo por bus factor. | • Sin política de documentación<br>• Conocimiento en individuos<br>• Alto riesgo de bus factor |
| **L1** | En desarrollo | Existe documentación básica para sistemas críticos. Compartición de conocimiento mediante reuniones ad-hoc e hilos de Slack. | • Algunos documentos de sistemas críticos<br>• Intercambio de conocimiento ad-hoc<br>• Canal de preguntas y respuestas basado en Slack |
| **L2** | Definido | Documentación estructurada en una wiki central. Tech talks regulares o sesiones de intercambio de conocimiento. Registros de decisiones para cambios importantes. | • Wiki central con estructura<br>• Charlas técnicas regulares<br>• Práctica de ADR establecida |
| **L3** | Gestionado | Base de conocimiento buscable que cubre >70% de los sistemas. Generación de documentación asistida por IA. Runbooks automatizados para problemas comunes. | • >70% de documentación de sistemas<br>• Generación de documentación asistida por IA<br>• Runbooks automatizados publicados |
| **L4** | Optimizando | Grafo de conocimiento impulsado por IA que vincula código, documentación, incidentes y decisiones. Las consultas en lenguaje natural devuelven respuestas contextuales. La vigencia del conocimiento se monitorea automáticamente. | • Implementación de grafo de conocimiento<br>• Interfaz de consulta en lenguaje natural<br>• Monitoreo automatizado de vigencia habilitado<br>• Sistema de respuestas contextuales |

---

### P1-C3-Q2: ¿En qué medida se ha adoptado la Gestión del Conocimiento (búsqueda semántica de código) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos indexed`

**Contexto**

- **Qué mide (what):** Búsqueda semántica a nivel de la organización en repos, documentación y chats.
- **Por qué importa (why):** La búsqueda semántica reduce el trabajo duplicado al hacer detectables las soluciones previas.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de búsqueda semántica de código. Los equipos operan sin esta capability. | • Sin búsqueda semántica de código implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de búsqueda semántica de código con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de búsqueda semántica de código se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de búsqueda semántica de código está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de búsqueda semántica de código está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C3-Q3: ¿En qué medida se ha adoptado la Gestión del Conocimiento (asistente de documentación basado en RAG) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `queries per developer/month`

**Contexto**

- **Qué mide (what):** Un asistente respaldado por LLM responde preguntas de desarrollo desde la base de conocimiento interna.
- **Por qué importa (why):** Los asistentes RAG reducen la carga de interrupciones sobre los ingenieros senior.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de asistente de documentación basado en RAG. Los equipos operan sin esta capability. | • Sin asistente de documentación basado en RAG implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de asistente de documentación basado en RAG con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de asistente de documentación basado en RAG se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de asistente de documentación basado en RAG está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de asistente de documentación basado en RAG está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C3-Q4: ¿En qué medida se ha adoptado la Gestión del Conocimiento (cobertura de runbooks y playbooks) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% critical services with runbook`

**Contexto**

- **Qué mide (what):** Los runbooks automatizados capturan conocimiento operativo.
- **Por qué importa (why):** Los runbooks documentados acortan el MTTR y habilitan la rotación on-call.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de cobertura de runbooks y playbooks. Los equipos operan sin esta capability. | • Sin cobertura de runbooks y playbooks implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de cobertura de runbooks y playbooks con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de cobertura de runbooks y playbooks se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de cobertura de runbooks y playbooks está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de cobertura de runbooks y playbooks está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C3-Q5: ¿En qué medida se ha adoptado la Gestión del Conocimiento (ADR (registros de decisiones de arquitectura)) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services with ADRs`

**Contexto**

- **Qué mide (what):** Las decisiones de arquitectura se capturan como ADRs en el repo.
- **Por qué importa (why):** Los ADRs preservan la memoria institucional más allá de las personas.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de ADR (registros de decisiones de arquitectura). Los equipos operan sin esta capability. | • Sin ADR (registros de decisiones de arquitectura) implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de ADR (registros de decisiones de arquitectura) con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de ADR (registros de decisiones de arquitectura) se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de ADR (registros de decisiones de arquitectura) está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de ADR (registros de decisiones de arquitectura) está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C3-Q6: ¿En qué medida se ha adoptado la Gestión del Conocimiento (contenido de aprendizaje y rutas curadas) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `completions per quarter`

**Contexto**

- **Qué mide (what):** Rutas de aprendizaje curadas vinculadas al rol y a la escala de carrera.
- **Por qué importa (why):** El aprendizaje estructurado reduce el tiempo de adaptación y mejora la retención.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de contenido de aprendizaje y rutas curadas. Los equipos operan sin esta capability. | • Sin contenido de aprendizaje y rutas curadas implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de contenido de aprendizaje y rutas curadas con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de contenido de aprendizaje y rutas curadas se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de contenido de aprendizaje y rutas curadas está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de contenido de aprendizaje y rutas curadas está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P1-C4: Automatización de la revisión de código

**7 preguntas en esta capability.**

### P1-C4-Q1: ¿En qué medida se ha adoptado la Automatización de Revisión de Código (bot revisor de IA en cada PR) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% PRs AI-reviewed`

**Contexto**

- **Qué mide (what):** Un bot publica comentarios de revisión generados por IA en cada PR.
- **Por qué importa (why):** Los revisores de IA detectan problemas antes de que las personas miren el código.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de bot revisor de IA en cada PR. Los equipos operan sin esta capability. | • Sin bot revisor con IA en cada PR implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de bot revisor de IA en cada PR con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de bot revisor de IA en cada PR se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de bot revisor de IA en cada PR está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de bot revisor de IA en cada PR está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C4-Q2: ¿En qué medida se ha adoptado la Automatización de Revisión de Código (linting estático y corrección automática de estilo) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `lint violations per kLOC`

**Contexto**

- **Qué mide (what):** Los linters y formateadores se ejecutan automáticamente en cada commit.
- **Por qué importa (why):** El estilo automatizado elimina las discusiones subjetivas de las revisiones.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de linting estático y autocorrección de estilo. Los equipos operan sin esta capability. | • Sin linting estático y auto-fix de estilo implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de linting estático y autocorrección de estilo con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de linting estático y autocorrección de estilo se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de linting estático y autocorrección de estilo está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de linting estático y autocorrección de estilo está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C4-Q3: ¿En qué medida se ha adoptado la Automatización de Revisión de Código (revisión de seguridad automatizada) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `critical findings per PR`

**Contexto**

- **Qué mide (what):** SAST comenta en línea sobre el diff del PR.
- **Por qué importa (why):** Los hallazgos en línea se corrigen 10x más rápido que los elementos del backlog.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de revisión de seguridad automatizada. Los equipos operan sin esta capability. | • Sin revisión de seguridad automatizada implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de revisión de seguridad automatizada con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de revisión de seguridad automatizada se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de revisión de seguridad automatizada está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de revisión de seguridad automatizada está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C4-Q4: ¿En qué medida se ha adoptado la Automatización de Revisión de Código (reglas de revisores requeridos) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% PRs meeting review rule`

**Contexto**

- **Qué mide (what):** CODEOWNERS hace cumplir la revisión de expertos del dominio por ruta.
- **Por qué importa (why):** Revisor correcto + código correcto = mejores hallazgos.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de reglas de revisores requeridos. Los equipos operan sin esta capability. | • Sin reglas de revisores obligatorios implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de reglas de revisores requeridos con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de reglas de revisores requeridos se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de reglas de revisores requeridos está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de reglas de revisores requeridos está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C4-Q5: ¿En qué medida se ha adoptado la Automatización de Revisión de Código (seguimiento de SLA de revisión) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `median PR cycle time`

**Contexto**

- **Qué mide (what):** El tiempo de ciclo de PR se mide y se gestiona con objetivos.
- **Por qué importa (why):** Los ciclos de revisión rápidos mantienen a los desarrolladores en flujo.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de seguimiento del SLA de revisión. Los equipos operan sin esta capability. | • Sin seguimiento de SLA de revisión implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de seguimiento del SLA de revisión con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de seguimiento del SLA de revisión se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de seguimiento del SLA de revisión está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de seguimiento del SLA de revisión está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C4-Q6: ¿En qué medida se ha adoptado la Automatización de Revisión de Código (cumplimiento del tamaño de los cambios) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `median PR size (LoC)`

**Contexto**

- **Qué mide (what):** Los hooks de pre-commit fomentan PRs pequeños.
- **Por qué importa (why):** Los PRs pequeños reciben mejores revisiones y se fusionan más rápido.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de control del tamaño de cambios. Los equipos operan sin esta capability. | • Sin aplicación de tamaño de cambio implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de control del tamaño de cambios con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de control del tamaño de cambios se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de control del tamaño de cambios está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de control del tamaño de cambios está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C4-Q7: ¿En qué medida se ha adoptado la Automatización de Revisión de Código (balanceo de carga de revisores) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `review load balance index`

**Contexto**

- **Qué mide (what):** La asignación de revisores balancea la carga en todo el equipo.
- **Por qué importa (why):** Una carga de revisión balanceada previene el agotamiento de los principales revisores.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de balanceo de carga de revisores. Los equipos operan sin esta capability. | • Sin balanceo de carga de revisores implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de balanceo de carga de revisores con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de balanceo de carga de revisores se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de balanceo de carga de revisores está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de balanceo de carga de revisores está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P1-C5: Onboarding y capacitación de desarrolladores

**7 preguntas en esta capability.**

### P1-C5-Q1: ¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (codespaces/dev containers para entorno instantáneo) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `time-to-first-commit (hours)`

**Contexto**

- **Qué mide (what):** Los entornos de desarrollo en la nube están listos en minutos.
- **Por qué importa (why):** La configuración rápida del entorno desbloquea a las nuevas contrataciones desde el primer día.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de Codespaces/dev containers para entornos instantáneos. Los equipos operan sin esta capability. | • Sin codespaces/dev containers para entornos instantáneos implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de Codespaces/dev containers para entornos instantáneos con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de Codespaces/dev containers para entornos instantáneos se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de Codespaces/dev containers para entornos instantáneos está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de Codespaces/dev containers para entornos instantáneos está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C5-Q2: ¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (playbook de onboarding estructurado) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% new hires completing onboarding`

**Contexto**

- **Qué mide (what):** Un plan de onboarding documentado de 30/60/90 días por rol.
- **Por qué importa (why):** El onboarding estructurado reduce el tiempo de adaptación en un 30-50%.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de playbook estructurado de onboarding. Los equipos operan sin esta capability. | • Sin playbook estructurado de onboarding implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de playbook estructurado de onboarding con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de playbook estructurado de onboarding se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de playbook estructurado de onboarding está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de playbook estructurado de onboarding está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C5-Q3: ¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (programa de mentoría por pares) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `mentor:mentee ratio`

**Contexto**

- **Qué mide (what):** Cada nueva contratación recibe un mentor senior durante 90 días.
- **Por qué importa (why):** La mentoría acorta la adaptación e impulsa la retención.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de programa de emparejamiento con mentores. Los equipos operan sin esta capability. | • Sin programa de mentoría por pares implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de programa de emparejamiento con mentores con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de programa de emparejamiento con mentores se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de programa de emparejamiento con mentores está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de programa de emparejamiento con mentores está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C5-Q4: ¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (currículo práctico y kata) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `katas completed per hire`

**Contexto**

- **Qué mide (what):** Los kata de codificación específicos por rol producen habilidades demostrables.
- **Por qué importa (why):** La práctica deliberada desarrolla habilidades más rápido que la lectura.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de currículo práctico y kata. Los equipos operan sin esta capability. | • Sin currículo práctico y kata implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de currículo práctico y kata con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de currículo práctico y kata se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de currículo práctico y kata está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de currículo práctico y kata está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C5-Q5: ¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (rotación on-call en sombra) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `new hires who shadowed on-call`

**Contexto**

- **Qué mide (what):** Las nuevas contrataciones observan turnos on-call para aprender el contexto operativo.
- **Por qué importa (why):** El contexto operativo es la forma más rápida de entender el sistema.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de rotación shadow on-call. Los equipos operan sin esta capability. | • Sin rotación shadow on-call implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de rotación shadow on-call con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de rotación shadow on-call se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de rotación shadow on-call está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de rotación shadow on-call está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C5-Q6: ¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (ciclo de feedback de onboarding) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `NPS from new hires`

**Contexto**

- **Qué mide (what):** Las nuevas contrataciones califican el onboarding; los resultados impulsan mejoras.
- **Por qué importa (why):** Los ciclos de feedback convierten el onboarding en un producto que mejora continuamente.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de ciclo de feedback de onboarding. Los equipos operan sin esta capability. | • Sin bucle de feedback de onboarding implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de ciclo de feedback de onboarding con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de ciclo de feedback de onboarding se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de ciclo de feedback de onboarding está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de ciclo de feedback de onboarding está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C5-Q7: ¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (medición del tiempo de adaptación) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `median ramp-time to first deploy`

**Contexto**

- **Qué mide (what):** El tiempo hasta el primer deploy se mide y se mejora para las nuevas contrataciones.
- **Por qué importa (why):** Medir la adaptación convierte las mejoras de onboarding en ROI.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de medición del tiempo de ramp-up. Los equipos operan sin esta capability. | • Sin medición de tiempo de ramp-up implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de medición del tiempo de ramp-up con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de medición del tiempo de ramp-up se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de medición del tiempo de ramp-up está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de medición del tiempo de ramp-up está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P1-C6: Inner source y colaboración

**6 preguntas en esta capability.**

### P1-C6-Q1: ¿En qué medida se ha adoptado Inner Source y Colaboración (repos internos con contribución abierta) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos open to all devs`

**Contexto**

- **Qué mide (what):** Los repos dentro de la organización reciben PRs de otros equipos.
- **Por qué importa (why):** Inner source rompe silos y aumenta la reutilización.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de repositorios internos con contribución abierta. Los equipos operan sin esta capability. | • Sin repos internos con contribución abierta implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de repositorios internos con contribución abierta con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de repositorios internos con contribución abierta se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de repositorios internos con contribución abierta está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de repositorios internos con contribución abierta está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C6-Q2: ¿En qué medida se ha adoptado Inner Source y Colaboración (estándares CONTRIBUTING.md) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos with CONTRIBUTING`

**Contexto**

- **Qué mide (what):** Cada repo documenta cómo contribuir y revisar.
- **Por qué importa (why):** Las normas claras de contribución reducen la fricción para el trabajo entre equipos.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de estándares de CONTRIBUTING.md. Los equipos operan sin esta capability. | • Sin estándares CONTRIBUTING.md implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de estándares de CONTRIBUTING.md con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de estándares de CONTRIBUTING.md se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de estándares de CONTRIBUTING.md está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de estándares de CONTRIBUTING.md está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C6-Q3: ¿En qué medida se ha adoptado Inner Source y Colaboración (portal de descubrimiento inner-source) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `cross-team PRs per month`

**Contexto**

- **Qué mide (what):** Un portal indexa proyectos inner-source que buscan contribuciones.
- **Por qué importa (why):** El descubrimiento impulsa la participación.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de portal de descubrimiento inner source. Los equipos operan sin esta capability. | • Sin portal de descubrimiento inner source implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de portal de descubrimiento inner source con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de portal de descubrimiento inner source se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de portal de descubrimiento inner source está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de portal de descubrimiento inner source está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C6-Q4: ¿En qué medida se ha adoptado Inner Source y Colaboración (etiquetado good-first-issue) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `GFI issues closed per month`

**Contexto**

- **Qué mide (what):** Los issues iniciales ayudan a los recién llegados a contribuir con confianza.
- **Por qué importa (why):** El etiquetado reduce la barrera para quienes contribuyen por primera vez.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de etiquetado good-first-issue. Los equipos operan sin esta capability. | • Sin etiquetado good-first-issue implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de etiquetado good-first-issue con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de etiquetado good-first-issue se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de etiquetado good-first-issue está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de etiquetado good-first-issue está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C6-Q5: ¿En qué medida se ha adoptado Inner Source y Colaboración (revisiones de diseño entre equipos) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `reviews per quarter`

**Contexto**

- **Qué mide (what):** Los documentos de diseño son revisados por múltiples equipos.
- **Por qué importa (why):** La revisión entre equipos detecta supuestos y comparte patrones.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de revisiones de diseño entre equipos. Los equipos operan sin esta capability. | • Sin revisiones de diseño entre equipos implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de revisiones de diseño entre equipos con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de revisiones de diseño entre equipos se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de revisiones de diseño entre equipos está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de revisiones de diseño entre equipos está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C6-Q6: ¿En qué medida se ha adoptado Inner Source y Colaboración (comunidad de práctica) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `CoP active members`

**Contexto**

- **Qué mide (what):** Los gremios y CoPs desarrollan experiencia horizontal.
- **Por qué importa (why):** Las CoPs aceleran el aprendizaje y reducen el riesgo de brechas de contratación.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de comunidad de práctica. Los equipos operan sin esta capability. | • Sin comunidad de práctica implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de comunidad de práctica con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de comunidad de práctica se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de comunidad de práctica está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de comunidad de práctica está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P1-C7: Automatización de la documentación

**5 preguntas en esta capability.**

### P1-C7-Q1: ¿En qué medida se ha adoptado la Automatización de Documentación (docs-as-code en Git) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services with docs in repo`

**Contexto**

- **Qué mide (what):** La documentación vive con el código y se revisa en PRs.
- **Por qué importa (why):** Docs-as-code evita que la documentación se degrade lejos del código fuente.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de docs-as-code en Git. Los equipos operan sin esta capability. | • Sin docs-as-code en Git implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de docs-as-code en Git con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de docs-as-code en Git se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de docs-as-code en Git está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de docs-as-code en Git está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C7-Q2: ¿En qué medida se ha adoptado la Automatización de Documentación (referencia de API generada automáticamente) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% APIs with generated docs`

**Contexto**

- **Qué mide (what):** La referencia de API se genera desde OpenAPI o desde el código fuente.
- **Por qué importa (why):** La documentación generada siempre está actualizada.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de referencia de API autogenerada. Los equipos operan sin esta capability. | • Sin referencia de API autogenerada implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de referencia de API autogenerada con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de referencia de API autogenerada se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de referencia de API autogenerada está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de referencia de API autogenerada está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C7-Q3: ¿En qué medida se ha adoptado la Automatización de Documentación (redacción de documentación asistida por IA) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Arquitecto, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% PRs with AI doc suggestions`

**Contexto**

- **Qué mide (what):** La IA sugiere actualizaciones de README y documentación a partir de diffs de código.
- **Por qué importa (why):** Los borradores de IA elevan el nivel base de la calidad de la documentación.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de redacción de documentación asistida por IA. Los equipos operan sin esta capability. | • Sin redacción de documentación asistida por IA implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de redacción de documentación asistida por IA con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de redacción de documentación asistida por IA se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de redacción de documentación asistida por IA está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de redacción de documentación asistida por IA está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C7-Q4: ¿En qué medida se ha adoptado la Automatización de Documentación (linting de calidad de documentación) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Arquitecto, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `broken-link count`

**Contexto**

- **Qué mide (what):** Las verificaciones de enlaces y los linters de estilo se ejecutan en CI.
- **Por qué importa (why):** Las verificaciones automatizadas mantienen confiable la documentación.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de linting de calidad de documentación. Los equipos operan sin esta capability. | • Sin linting de calidad de documentación implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de linting de calidad de documentación con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de linting de calidad de documentación se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de linting de calidad de documentación está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de linting de calidad de documentación está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C7-Q5: ¿En qué medida se ha adoptado la Automatización de Documentación (analítica de documentación) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `top unanswered queries`

**Contexto**

- **Qué mide (what):** La analítica de búsqueda revela lo que los usuarios no pueden encontrar.
- **Por qué importa (why):** La analítica convierte la documentación en un producto orientado por datos.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de analítica de documentación. Los equipos operan sin esta capability. | • Sin analítica de documentación implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de analítica de documentación con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de analítica de documentación se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de analítica de documentación está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de analítica de documentación está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P1-C8: Medición de productividad del desarrollador

**6 preguntas en esta capability.**

### P1-C8-Q1: ¿En qué medida se ha adoptado la Medición de Productividad del Desarrollador (cuatro métricas clave de DORA) en todos los equipos?

**Metadatos**

- **Público objetivo:** engineering-leader, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `deploys/day, lead time, CFR, MTTR`

**Contexto**

- **Qué mide (what):** Se da seguimiento a la frecuencia de despliegue, lead time, tasa de fallas por cambios y MTTR.
- **Por qué importa (why):** Las métricas DORA se correlacionan con los resultados de negocio.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de cuatro métricas clave DORA. Los equipos operan sin esta capability. | • Sin cuatro métricas clave de DORA implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de cuatro métricas clave DORA con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de cuatro métricas clave DORA se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de cuatro métricas clave DORA está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de cuatro métricas clave DORA está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C8-Q2: ¿En qué medida se ha adoptado la Medición de Productividad del Desarrollador (encuestas de experiencia del desarrollador) en todos los equipos?

**Metadatos**

- **Público objetivo:** engineering-leader, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `DX survey NPS`

**Contexto**

- **Qué mide (what):** Las encuestas trimestrales miden la satisfacción de los desarrolladores.
- **Por qué importa (why):** Las encuestas DX revelan fricciones que las métricas no capturan.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de encuestas de experiencia de desarrolladores. Los equipos operan sin esta capability. | • Sin encuestas de experiencia del desarrollador implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de encuestas de experiencia de desarrolladores con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de encuestas de experiencia de desarrolladores se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de encuestas de experiencia de desarrolladores está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de encuestas de experiencia de desarrolladores está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C8-Q3: ¿En qué medida se ha adoptado la Medición de Productividad del Desarrollador (tiempo del ciclo de feedback de build/test) en todos los equipos?

**Metadatos**

- **Público objetivo:** engineering-leader, Ingeniero de plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `p95 CI duration`

**Contexto**

- **Qué mide (what):** CI proporciona señal en menos de 10 minutos para PRs típicos.
- **Por qué importa (why):** El feedback rápido mantiene a los desarrolladores en flujo.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de tiempo del ciclo de feedback de build/test. Los equipos operan sin esta capability. | • Sin tiempo de bucle de feedback de build/test implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de tiempo del ciclo de feedback de build/test con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de tiempo del ciclo de feedback de build/test se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de tiempo del ciclo de feedback de build/test está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de tiempo del ciclo de feedback de build/test está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C8-Q4: ¿En qué medida se ha adoptado la Medición de Productividad del Desarrollador (adopción del framework SPACE) en todos los equipos?

**Metadatos**

- **Público objetivo:** engineering-leader, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `SPACE dimensions tracked`

**Contexto**

- **Qué mide (what):** Los equipos dan seguimiento a Satisfacción, Rendimiento, Actividad, Comunicación y Eficiencia.
- **Por qué importa (why):** SPACE equilibra señales cuantitativas y cualitativas.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de adopción del framework SPACE. Los equipos operan sin esta capability. | • Sin adopción del framework SPACE implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de adopción del framework SPACE con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de adopción del framework SPACE se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de adopción del framework SPACE está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de adopción del framework SPACE está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C8-Q5: ¿En qué medida se ha adoptado la Medición de Productividad del Desarrollador (dashboards de flujo vs fricción) en todos los equipos?

**Metadatos**

- **Público objetivo:** engineering-leader, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% teams viewing dashboard monthly`

**Contexto**

- **Qué mide (what):** Líderes y equipos ven datos de productividad lado a lado.
- **Por qué importa (why):** Los datos compartidos alinean mejoras entre equipos.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de dashboards de flujo vs fricción. Los equipos operan sin esta capability. | • Sin dashboards de flujo vs. fricción implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de dashboards de flujo vs fricción con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de dashboards de flujo vs fricción se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de dashboards de flujo vs fricción está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de dashboards de flujo vs fricción está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C8-Q6: ¿En qué medida se ha adoptado la Medición de Productividad del Desarrollador (OKRs trimestrales de productividad) en todos los equipos?

**Metadatos**

- **Público objetivo:** engineering-leader, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% teams hitting DX OKRs`

**Contexto**

- **Qué mide (what):** Las mejoras de DX se siguen como OKRs.
- **Por qué importa (why):** Los OKRs convierten la productividad en una inversión de primera clase.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de OKRs trimestrales de productividad. Los equipos operan sin esta capability. | • Sin OKR trimestrales de productividad implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de OKRs trimestrales de productividad con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de OKRs trimestrales de productividad se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de OKRs trimestrales de productividad está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de OKRs trimestrales de productividad está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P1-C9: Automatización de entornos y workspaces

**5 preguntas en esta capability.**

### P1-C9-Q1: ¿En qué medida se ha adoptado la Automatización de Entornos y Espacios de Trabajo (entornos locales reproducibles (devcontainers)) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos with devcontainer`

**Contexto**

- **Qué mide (what):** Cada repo incluye un devcontainer o shell de Nix.
- **Por qué importa (why):** Los entornos reproducibles eliminan las fallas de 'funciona en mi máquina'.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de entornos locales reproducibles (devcontainers). Los equipos operan sin esta capability. | • Sin entornos locales reproducibles (devcontainers) implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de entornos locales reproducibles (devcontainers) con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de entornos locales reproducibles (devcontainers) se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de entornos locales reproducibles (devcontainers) está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de entornos locales reproducibles (devcontainers) está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C9-Q2: ¿En qué medida se ha adoptado la Automatización de Entornos y Espacios de Trabajo (workspaces en la nube (Codespaces/Gitpod)) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% devs using cloud workspace`

**Contexto**

- **Qué mide (what):** Los workspaces en la nube son el entorno de desarrollo predeterminado.
- **Por qué importa (why):** Los workspaces en la nube hacen que la configuración del entorno sea instantánea y consistente.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de workspaces en la nube (Codespaces/Gitpod). Los equipos operan sin esta capability. | • Sin workspaces en la nube (Codespaces/Gitpod) implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de workspaces en la nube (Codespaces/Gitpod) con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de workspaces en la nube (Codespaces/Gitpod) se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de workspaces en la nube (Codespaces/Gitpod) está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de workspaces en la nube (Codespaces/Gitpod) está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C9-Q3: ¿En qué medida se ha adoptado la Automatización de Entornos y Espacios de Trabajo (fijación de versiones de herramientas y SDK) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `tools pinned per repo`

**Contexto**

- **Qué mide (what):** Las versiones de lenguajes y herramientas están fijadas y los lockfiles están confirmados.
- **Por qué importa (why):** Las versiones fijadas mantienen builds reproducibles entre máquinas.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de fijación de versiones de herramientas y SDK. Los equipos operan sin esta capability. | • Sin fijación de versiones de herramientas y SDK implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de fijación de versiones de herramientas y SDK con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de fijación de versiones de herramientas y SDK se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de fijación de versiones de herramientas y SDK está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de fijación de versiones de herramientas y SDK está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C9-Q4: ¿En qué medida se ha adoptado la Automatización de Entornos y Espacios de Trabajo (datos de prueba bajo demanda) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `time to get fresh test data`

**Contexto**

- **Qué mide (what):** Los desarrolladores pueden restablecer o aprovisionar datos de prueba realistas bajo demanda.
- **Por qué importa (why):** Los datos frescos desbloquean las pruebas y la depuración.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de datos de prueba bajo demanda. Los equipos operan sin esta capability. | • Sin datos de prueba bajo demanda implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de datos de prueba bajo demanda con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de datos de prueba bajo demanda se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de datos de prueba bajo demanda está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de datos de prueba bajo demanda está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P1-C9-Q5: ¿En qué medida se ha adoptado la Automatización de Entornos y Espacios de Trabajo (telemetría y salud del workspace) en todos los equipos?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de plataforma, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% workspaces healthy`

**Contexto**

- **Qué mide (what):** La telemetría del workspace revela fallas de configuración y caídas de herramientas.
- **Por qué importa (why):** La telemetría permite que los equipos de plataforma corrijan fricciones de forma proactiva.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin implementación de telemetría y salud del workspace. Los equipos operan sin esta capability. | • Sin telemetría y salud del workspace implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Piloto de la capability de telemetría y salud del workspace con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | La capability de telemetría y salud del workspace se adoptó en 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | La capability de telemetría y salud del workspace está estandarizada en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La capability de telemetría y salud del workspace está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## Cómo se puntúa esta sección

- Cada pregunta recibe un valor numérico a partir del nivel seleccionado: L0=0, L1=1, L2=2, L3=3, L4=4.
- La puntuación de la capability es el promedio ponderado de sus preguntas (peso predeterminado = 1.0; las preguntas con peso 1.5 o 2.0 cuentan más).
- La puntuación del pilar **P1** es el promedio de las 9 capabilities.
- El resultado se muestra en una escala de 0 a 4 y se convierte a un % de madurez (nivel / 4 × 100).

## Glosario rápido

- **Pilar:** dimensión estratégica de madurez.
- **Capability:** subdominio funcional dentro de un pilar.
- **Pregunta:** elemento concreto de evaluación, ID estándar `P[1-3]-C[1-19]-Q[1-99]`.
- **Nivel (L0-L4):** punto en la escala Likert de madurez.
- **KPI:** indicador clave que valida objetivamente el nivel declarado.
- **Evidencia:** prueba cualitativa (texto) o cuantitativa (adjunto) que respalda la respuesta.
