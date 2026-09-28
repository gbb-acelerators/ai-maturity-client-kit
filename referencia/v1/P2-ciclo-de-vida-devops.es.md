# AI Maturity Assessment (Pilar P2: Ciclo de vida DevOps)

🌐 [English](P2-ciclo-de-vida-devops.md) · [Português (Brasil)](P2-ciclo-de-vida-devops.pt-br.md) · Español

> Mide la madurez de pipelines, infraestructura como código, observabilidad, DevSecOps, releases, pruebas, incidentes y seguridad de la cadena de suministro.

## Resumen

- **Pilar:** `P2` (Ciclo de vida DevOps)
- **Capabilities incluidas:** 10
- **Total de preguntas:** 59
- **Escala:** Likert L0-L4 (Inicial a Optimizando)
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

2. **Cualitativo (descripción del nivel):** la persona encuestada selecciona el nivel L0-L4 cuya descripción representa mejor la realidad observada hoy (no la aspiracional).

3. **Evidencia (texto + adjuntos):** prueba documental, como un enlace de pipeline, captura de dashboard, política, runbook, contrato de licencias o métrica exportada. Cuanto más específica, mayor es la calidad de la evidencia (escala: ninguna a mínima a adecuada a detallada a ejemplar).

## Criterios de calidad de la evidencia

- **Mínima (<80 caracteres):** texto genérico, sin nombre de herramienta, métrica ni enlace.
- **Adecuada (80-250):** menciona la herramienta + cobertura/alcance aproximado.
- **Detallada (250-500):** incluye una métrica numérica + enlace/adjunto + periodo de medición.
- **Ejemplar (>500 o varios adjuntos):** múltiples fuentes corroborantes, serie temporal, comparación antes/después.

## Capabilities del pilar P2

- **P2-C1**: Inteligencia de pipelines CI/CD (6 preguntas)
- **P2-C2**: Infraestructura como código (6 preguntas)
- **P2-C3**: Observabilidad y monitoreo (6 preguntas)
- **P2-C4**: Integración de seguridad (DevSecOps) (6 preguntas)
- **P2-C5**: Estrategias de release y despliegue (6 preguntas)
- **P2-C6**: Automatización de pruebas (7 preguntas)
- **P2-C7**: Gestión de incidentes y SRE (7 preguntas)
- **P2-C8**: Gestión de artefactos y paquetes (5 preguntas)
- **P2-C9**: Gestión de cambios y GitOps (5 preguntas)
- **P2-C10**: Seguridad de dependencias y cadena de suministro (5 preguntas)

---

## P2-C1: Inteligencia de pipelines CI/CD

**6 preguntas en esta capability.**

### P2-C1-Q1: ¿Qué tan maduro es tu pipeline CI/CD en términos de automatización e integración de IA?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** Sí
- **KPI principal:** `Deployment frequency per week`

**Contexto**

- **Qué mide (what):** Mide el nivel de automatización y la inteligencia de los pipelines CI/CD.
- **Por qué importa (why):** Los pipelines CI/CD maduros permiten a los equipos desplegar con una frecuencia 200x mayor y con una tasa de fallas de cambio 3x menor (investigación de DORA).

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Builds y despliegues manuales. Sin pipeline de CI/CD. Los despliegues ocurren semanalmente o con menor frecuencia. | • Sin pipeline CI/CD<br>• Proceso de build manual<br>• Despliegues semanales o menos frecuentes |
| **L1** | En desarrollo | Pipeline de CI básico con builds automatizados y pruebas unitarias. Proceso de despliegue manual. Frecuencia de despliegue: semanal. | • Pipeline CI configurado<br>• Pruebas unitarias automatizadas<br>• Despliegues manuales semanales |
| **L2** | Definido | Pipeline de CI/CD completo con pruebas automatizadas, despliegue a staging y promoción manual a producción. Frecuencia de despliegue: diaria. | • Despliegue automatizado a staging<br>• Promoción manual a producción<br>• Cadencia de despliegues diarios en producción |
| **L3** | Gestionado | CI/CD inteligente: suites de pruebas con autoescalado, selección inteligente de pruebas (ejecutar solo pruebas afectadas), despliegues canary. Múltiples despliegues por día. | • Selección inteligente de pruebas<br>• Configuración de despliegue canary<br>• Múltiples despliegues diarios<br>• Análisis de impacto de pruebas |
| **L4** | Optimizando | Pipeline optimizado por IA: fallas de build predictivas, autorremediación de flaky tests, análisis canary impulsado por ML, despliegues self-healing. | • Modelo predictivo de fallas<br>• Scripts de remediación automatizada implementados<br>• Análisis canary con ML<br>• Documentación de despliegue self-healing |

---

### P2-C1-Q2: ¿En qué medida se ha adoptado la Inteligencia de Pipeline CI/CD (pipeline-as-code everywhere) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma, Seguridad, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% pipelines as code`

**Contexto**

- **Qué mide (what):** Todos los pipelines viven junto al código como YAML/HCL versionado.
- **Por qué importa (why):** Pipeline-as-code es auditable, revisable y reproducible.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin pipeline-as-code en todas partes implementado. Los equipos operan sin esta capability. | • Sin pipeline-as-code en todas partes implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de pipeline-as-code en todas partes con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | pipeline-as-code en todas partes adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | pipeline-as-code en todas partes estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | pipeline-as-code en todas partes está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C1-Q3: ¿En qué medida se ha adoptado la Inteligencia de Pipeline CI/CD (build caching and artifact reuse) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% cache hit ratio`

**Contexto**

- **Qué mide (what):** Las cachés de build remotas y los artefactos direccionados por contenido reducen el tiempo de build.
- **Por qué importa (why):** El caching reduce el tiempo de CI en 40-70% y disminuye el gasto en la nube.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin caché de builds y reutilización de artefactos implementado. Los equipos operan sin esta capability. | • Sin caché de build y reutilización de artefactos implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de caché de builds y reutilización de artefactos con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | caché de builds y reutilización de artefactos adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | caché de builds y reutilización de artefactos estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | caché de builds y reutilización de artefactos está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C1-Q4: ¿En qué medida se ha adoptado la Inteligencia de Pipeline CI/CD (trunk-based development) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `branches >7 days old`

**Contexto**

- **Qué mide (what):** Ramas de vida corta se fusionan al trunk varias veces al día.
- **Por qué importa (why):** Trunk-based dev reduce el infierno de merges y habilita la entrega continua.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin trunk-based development implementado. Los equipos operan sin esta capability. | • Sin desarrollo trunk-based implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de trunk-based development con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | trunk-based development adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | trunk-based development estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | trunk-based development está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C1-Q5: ¿En qué medida se ha adoptado la Inteligencia de Pipeline CI/CD (deployment frequency) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `deploys per day`

**Contexto**

- **Qué mide (what):** Los equipos DORA de élite despliegan muchas veces al día en producción.
- **Por qué importa (why):** Una alta frecuencia de deploy se correlaciona con una baja tasa de fallas de cambio.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin frecuencia de despliegue implementado. Los equipos operan sin esta capability. | • Sin frecuencia de despliegue implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de frecuencia de despliegue con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | frecuencia de despliegue adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | frecuencia de despliegue estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | frecuencia de despliegue está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C1-Q6: ¿En qué medida se ha adoptado la Inteligencia de Pipeline CI/CD (feature flags for progressive delivery) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `flags used per release`

**Contexto**

- **Qué mide (what):** Las feature flags desacoplan el despliegue del release.
- **Por qué importa (why):** Las flags habilitan dark launches, despliegues canary y rollback rápido.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin feature flags para entrega progresiva implementado. Los equipos operan sin esta capability. | • Sin feature flags para entrega progresiva implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de feature flags para entrega progresiva con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | feature flags para entrega progresiva adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | feature flags para entrega progresiva estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | feature flags para entrega progresiva está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P2-C2: Infraestructura como código

**6 preguntas en esta capability.**

### P2-C2-Q1: ¿Qué porcentaje de tu infraestructura se gestiona como código?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma, Seguridad, qa-test
- **Peso:** 1.0
- **Professional Edition:** Sí
- **KPI principal:** `% infrastructure as code`

**Contexto**

- **Qué mide (what):** Mide el grado en que el aprovisionamiento y la gestión de infraestructura están codificados y controlados por versiones.
- **Por qué importa (why):** IaC reduce los errores de aprovisionamiento en 90% y permite que los cambios de infraestructura se revisen, prueben y auditen como código de aplicación.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Toda la infraestructura se aprovisiona manualmente vía consola cloud o comandos CLI. Sin control de versiones para la infraestructura. | • Solo aprovisionamiento manual<br>• Sin archivos IaC en repos<br>• Flujo de gestión basado en consola |
| **L1** | En desarrollo | Parte de la infraestructura definida como código (<30%). Mezcla de aprovisionamiento manual y automatizado. Scripts sin control de versiones consistente. | • <30% de cobertura IaC<br>• Procesos mixtos manuales y automatizados<br>• Control de versiones inconsistente |
| **L2** | Definido | 50-75% de la infraestructura definida como código. Módulos IaC para patrones comunes. Revisión basada en PR para cambios de infraestructura. | • 50-75% de cobertura IaC<br>• Módulos IaC reutilizables<br>• Revisión de infraestructura basada en PR |
| **L3** | Gestionado | >90% de infraestructura como código. Detección de drift habilitada. Enforcement de policy-as-code. Aprovisionamiento de autoservicio vía plantillas. | • >90% de cobertura IaC<br>• Informes de detección de drift<br>• Reglas policy-as-code aplicadas<br>• Plantillas de autoservicio publicadas |
| **L4** | Optimizando | 100% IaC con recomendaciones de infraestructura generadas por IA. Autorremediación de drift. Sugerencias de optimización de costos. Escalado predictivo. | • 100% de cobertura IaC<br>• Recomendaciones de infraestructura con IA<br>• Remediación automatizada de drift habilitada<br>• Configuración de escalado predictivo |

---

### P2-C2-Q2: ¿En qué medida se ha adoptado Infraestructura como Código (Terraform/Bicep-based IaC) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% infra as code`

**Contexto**

- **Qué mide (what):** Toda la infraestructura de larga duración se declara como código.
- **Por qué importa (why):** IaC elimina los servidores snowflake y habilita entornos reproducibles.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin IaC basada en Terraform/Bicep implementado. Los equipos operan sin esta capability. | • Sin IaC basada en Terraform/Bicep implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de IaC basada en Terraform/Bicep con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | IaC basada en Terraform/Bicep adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | IaC basada en Terraform/Bicep estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | IaC basada en Terraform/Bicep está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C2-Q3: ¿En qué medida se ha adoptado Infraestructura como Código (module and pattern library) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% resources via modules`

**Contexto**

- **Qué mide (what):** Una biblioteca de módulos compartida codifica seguridad y redes con opiniones definidas.
- **Por qué importa (why):** Los módulos hacen cumplir los estándares y reducen la carga cognitiva por equipo.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin biblioteca de módulos y patrones implementado. Los equipos operan sin esta capability. | • Sin biblioteca de módulos y patrones implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de biblioteca de módulos y patrones con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | biblioteca de módulos y patrones adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | biblioteca de módulos y patrones estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | biblioteca de módulos y patrones está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C2-Q4: ¿En qué medida se ha adoptado Infraestructura como Código (GitOps for config drift) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% envs drift-detected`

**Contexto**

- **Qué mide (what):** Los controladores GitOps reconcilian el estado del clúster y de la nube con Git.
- **Por qué importa (why):** GitOps elimina la deriva y convierte a Git en la única fuente de verdad.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin GitOps para drift de configuración implementado. Los equipos operan sin esta capability. | • Sin GitOps para drift de configuración implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de GitOps para drift de configuración con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | GitOps para drift de configuración adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | GitOps para drift de configuración estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | GitOps para drift de configuración está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C2-Q5: ¿En qué medida se ha adoptado Infraestructura como Código (policy-as-code (OPA/Conftest)) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma, Seguridad, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `policies enforced in PR`

**Contexto**

- **Qué mide (what):** Las políticas se evalúan sobre los cambios de IaC antes del merge.
- **Por qué importa (why):** Policy-as-code desplaza la gobernanza a la izquierda y escala la revisión de seguridad.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin policy-as-code (OPA/Conftest) implementado. Los equipos operan sin esta capability. | • Sin policy-as-code (OPA/Conftest) implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de policy-as-code (OPA/Conftest) con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | policy-as-code (OPA/Conftest) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | policy-as-code (OPA/Conftest) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | policy-as-code (OPA/Conftest) está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C2-Q6: ¿En qué medida se ha adoptado Infraestructura como Código (ephemeral environment per PR) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `PR envs spun up`

**Contexto**

- **Qué mide (what):** Cada PR obtiene un entorno efímero para pruebas de integración.
- **Por qué importa (why):** Los entornos efímeros encuentran bugs antes y aceleran la revisión.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin entorno efímero por PR implementado. Los equipos operan sin esta capability. | • Sin entorno efímero por PR implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de entorno efímero por PR con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | entorno efímero por PR adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | entorno efímero por PR estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | entorno efímero por PR está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P2-C3: Observabilidad y monitoreo

**6 preguntas en esta capability.**

### P2-C3-Q1: ¿Qué tan completa es tu stack de observabilidad (logs, métricas, trazas)?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** Sí
- **KPI principal:** `MTTR in minutes`

**Contexto**

- **Qué mide (what):** Mide la madurez del stack de observabilidad, incluidos logs, métricas y trazado distribuido.
- **Por qué importa (why):** La observabilidad completa reduce el MTTR de horas a minutos y habilita la detección proactiva de problemas.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Logging mínimo. Sin monitoreo centralizado. Los problemas se descubren cuando los usuarios los reportan. | • Sin logging centralizado<br>• Sin dashboards de monitoreo<br>• Solo problemas reportados por usuarios |
| **L1** | En desarrollo | Logging centralizado (ELK/CloudWatch). Monitoreo básico de uptime. MTTR >60 minutos. | • Plataforma de logging centralizada<br>• Verificaciones básicas de disponibilidad<br>• MTTR >60 minutos |
| **L2** | Definido | Logging estructurado, métricas de aplicación (Prometheus/Datadog), alertas básicas. MTTR 30-60 minutos. | • Logging JSON estructurado<br>• Dashboard de métricas de aplicación<br>• MTTR 30-60 minutos |
| **L3** | Gestionado | Observabilidad completa: tracing distribuido, logs-métricas-traces correlacionados, alertas basadas en SLO. MTTR <15 minutos. | • Trazabilidad distribuida habilitada<br>• Stack de observabilidad correlacionada implementado<br>• Alertas basadas en SLO configuradas<br>• MTTR <15 minutos |
| **L4** | Optimizando | Observabilidad impulsada por IA: detección de anomalías, alertas predictivas, autocorrelación de incidentes, remediación sugerida. MTTR <5 minutos. | • Detección de anomalías con IA<br>• Alertas predictivas habilitadas<br>• Correlación automatizada de incidentes habilitada<br>• MTTR <5 minutos |

---

### P2-C3-Q2: ¿En qué medida se ha adoptado Observabilidad y Monitoreo (structured logging w/ correlation IDs) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services emitting structured logs`

**Contexto**

- **Qué mide (what):** Todos los logs siguen un esquema y llevan IDs de traza/correlación.
- **Por qué importa (why):** Los logs estructurados son buscables, agregables y legibles por máquina.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin logging estructurado con IDs de correlación implementado. Los equipos operan sin esta capability. | • Sin logging estructurado con IDs de correlación implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de logging estructurado con IDs de correlación con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | logging estructurado con IDs de correlación adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | logging estructurado con IDs de correlación estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | logging estructurado con IDs de correlación está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C3-Q3: ¿En qué medida se ha adoptado Observabilidad y Monitoreo (distributed tracing (OpenTelemetry)) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services instrumented`

**Contexto**

- **Qué mide (what):** Los SDKs de OTEL emiten trazas a través de los límites de servicio.
- **Por qué importa (why):** El trazado distribuido revela los contribuyentes de latencia en los microservicios.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin tracing distribuido (OpenTelemetry) implementado. Los equipos operan sin esta capability. | • Sin trazabilidad distribuida (OpenTelemetry) implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de tracing distribuido (OpenTelemetry) con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | tracing distribuido (OpenTelemetry) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | tracing distribuido (OpenTelemetry) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | tracing distribuido (OpenTelemetry) está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C3-Q4: ¿En qué medida se ha adoptado Observabilidad y Monitoreo (SLOs and error budgets) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services with SLOs`

**Contexto**

- **Qué mide (what):** Los objetivos de nivel de servicio con presupuestos de error impulsan decisiones de confiabilidad.
- **Por qué importa (why):** Los SLOs alinean las prioridades de ingeniería con la experiencia del usuario.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin SLOs y presupuestos de error implementado. Los equipos operan sin esta capability. | • Sin SLOs y presupuestos de error implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de SLOs y presupuestos de error con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | SLOs y presupuestos de error adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | SLOs y presupuestos de error estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | SLOs y presupuestos de error está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C3-Q5: ¿En qué medida se ha adoptado Observabilidad y Monitoreo (synthetic monitoring) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `journeys monitored`

**Contexto**

- **Qué mide (what):** Las sondas sintéticas ejercitan continuamente recorridos críticos de usuario.
- **Por qué importa (why):** Los synthetics detectan regresiones antes que los usuarios.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin monitoreo sintético implementado. Los equipos operan sin esta capability. | • Sin monitoreo sintético implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de monitoreo sintético con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | monitoreo sintético adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | monitoreo sintético estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | monitoreo sintético está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C3-Q6: ¿En qué medida se ha adoptado Observabilidad y Monitoreo (anomaly detection with ML) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `alerts auto-triaged`

**Contexto**

- **Qué mide (what):** Los modelos de ML detectan anomalías y suprimen ruido.
- **Por qué importa (why):** La detección basada en ML reduce la fatiga de alertas y acelera la respuesta.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin detección de anomalías con ML implementado. Los equipos operan sin esta capability. | • Sin detección de anomalías con ML implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de detección de anomalías con ML con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | detección de anomalías con ML adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | detección de anomalías con ML estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | detección de anomalías con ML está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P2-C4: Integración de seguridad (DevSecOps)

**6 preguntas en esta capability.**

### P2-C4-Q1: ¿Qué tan integrada está la seguridad en tu pipeline de desarrollo y despliegue?

**Metadatos**

- **Público objetivo:** Seguridad, devops, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% vulnerabilities caught pre-prod`

**Contexto**

- **Qué mide (what):** Mide la integración de prácticas de seguridad en el ciclo de vida de desarrollo (shift-left security).
- **Por qué importa (why):** Corregir vulnerabilidades en producción cuesta 30x más que detectarlas en desarrollo. DevSecOps reduce los incidentes de seguridad en 50%.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Seguridad revisada solo antes del release. Sin escaneo automatizado. Vulnerabilidades encontradas en producción. | • Sin escaneo de seguridad automatizado<br>• Revisiones solo previas al release<br>• Incidentes de vulnerabilidades en producción |
| **L1** | En desarrollo | Escaneo básico de dependencias en CI (Dependabot/Snyk). Revisión manual de seguridad para funcionalidades críticas. | • Escaneo de dependencias configurado<br>• Revisiones de seguridad manuales<br>• Sin escaneo SAST ni DAST |
| **L2** | Definido | SAST y escaneo de dependencias en pipeline de CI. Requisitos de seguridad en la definition of done. >50% de vulnerabilidades detectadas antes de producción. | • SAST en pipeline CI<br>• Seguridad en DoD<br>• >50% de tasa de detección pre-prod |
| **L3** | Gestionado | DevSecOps completo: SAST, DAST, SCA, escaneo de contenedores, detección de secretos. Los gates de seguridad bloquean el despliegue. Tasa de detección pre-prod >80%. | • SAST, DAST, SCA y escaneo de contenedores<br>• Detección de secretos habilitada<br>• >80% de tasa de detección pre-prod |
| **L4** | Optimizando | Seguridad impulsada por IA: modelado de amenazas automatizado, detección predictiva de vulnerabilidades, autoparcheo de CVEs conocidos, protección en runtime. Tasa de detección pre-prod >95%. | • Modelado de amenazas automatizado<br>• Detección predictiva de vulnerabilidades<br>• Pipeline de parchado automatizado habilitado<br>• >95% de tasa de detección pre-prod |

---

### P2-C4-Q2: ¿En qué medida se ha adoptado Integración de Seguridad (DevSecOps) (SAST in every pipeline) en todos los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos with SAST`

**Contexto**

- **Qué mide (what):** El análisis estático escanea cada PR en busca de vulnerabilidades.
- **Por qué importa (why):** SAST encuentra bugs a bajo costo durante la autoría.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin SAST en cada pipeline implementado. Los equipos operan sin esta capability. | • Sin SAST en cada pipeline implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de SAST en cada pipeline con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | SAST en cada pipeline adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | SAST en cada pipeline estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | SAST en cada pipeline está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C4-Q3: ¿En qué medida se ha adoptado Integración de Seguridad (DevSecOps) (SCA and dependency review) en todos los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos with SCA`

**Contexto**

- **Qué mide (what):** El análisis de composición de software marca dependencias vulnerables.
- **Por qué importa (why):** Las dependencias con vulnerabilidades conocidas son un vector de ataque principal.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin SCA y revisión de dependencias implementado. Los equipos operan sin esta capability. | • Sin SCA y revisión de dependencias implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de SCA y revisión de dependencias con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | SCA y revisión de dependencias adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | SCA y revisión de dependencias estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | SCA y revisión de dependencias está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C4-Q4: ¿En qué medida se ha adoptado Integración de Seguridad (DevSecOps) (secret scanning and push protection) en todos los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `secrets blocked per month`

**Contexto**

- **Qué mide (what):** Los secretos se detectan antes del commit y se bloquean en el push.
- **Por qué importa (why):** Los secretos filtrados son la fuente #1 de brechas en entornos de nube.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin escaneo de secretos y protección contra push implementado. Los equipos operan sin esta capability. | • Sin escaneo de secretos y push protection implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de escaneo de secretos y protección contra push con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | escaneo de secretos y protección contra push adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | escaneo de secretos y protección contra push estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | escaneo de secretos y protección contra push está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C4-Q5: ¿En qué medida se ha adoptado Integración de Seguridad (DevSecOps) (DAST and API security testing) en todos los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, devops, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% APIs DAST-tested`

**Contexto**

- **Qué mide (what):** Las pruebas dinámicas ejercitan la app en ejecución para detectar vulnerabilidades en runtime.
- **Por qué importa (why):** DAST detecta problemas que SAST no puede (auth, lógica, configuración).

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin DAST y pruebas de seguridad de APIs implementado. Los equipos operan sin esta capability. | • Sin DAST y pruebas de seguridad de API implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de DAST y pruebas de seguridad de APIs con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | DAST y pruebas de seguridad de APIs adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | DAST y pruebas de seguridad de APIs estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | DAST y pruebas de seguridad de APIs está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C4-Q6: ¿En qué medida se ha adoptado Integración de Seguridad (DevSecOps) (security champions program) en todos los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `champions per 20 devs`

**Contexto**

- **Qué mide (what):** Cada equipo tiene un champion de seguridad capacitado y con recursos.
- **Por qué importa (why):** Los champions escalan la experiencia de seguridad a cada equipo.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin programa de security champions implementado. Los equipos operan sin esta capability. | • Sin programa de security champions implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de programa de security champions con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | programa de security champions adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | programa de security champions estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | programa de security champions está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P2-C5: Estrategias de release y despliegue

**6 preguntas en esta capability.**

### P2-C5-Q1: ¿En qué medida se han adoptado Estrategias de Release y Despliegue (blue/green or canary deploys) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services with canary`

**Contexto**

- **Qué mide (what):** Los deploys canary o blue/green reducen el radio de impacto.
- **Por qué importa (why):** El rollout progresivo detecta problemas antes de la exposición completa.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin despliegues blue/green o canary implementado. Los equipos operan sin esta capability. | • Sin despliegues blue/green o canary implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de despliegues blue/green o canary con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | despliegues blue/green o canary adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | despliegues blue/green o canary estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | despliegues blue/green o canary está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C5-Q2: ¿En qué medida se han adoptado Estrategias de Release y Despliegue (automated rollback) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `median rollback time`

**Contexto**

- **Qué mide (what):** Una infracción de SLO o un pico de errores activa rollback automático.
- **Por qué importa (why):** El rollback automatizado limita el impacto en usuarios cuando los deploys salen mal.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin rollback automatizado implementado. Los equipos operan sin esta capability. | • Sin rollback automatizado implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de rollback automatizado con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | rollback automatizado adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | rollback automatizado estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | rollback automatizado está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C5-Q3: ¿En qué medida se han adoptado Estrategias de Release y Despliegue (feature flag platform) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `flags in active use`

**Contexto**

- **Qué mide (what):** Una plataforma de flags admite exposición progresiva y experimentos.
- **Por qué importa (why):** Las flags desacoplan el deploy del release.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin plataforma de feature flags implementado. Los equipos operan sin esta capability. | • Sin plataforma de feature flags implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de plataforma de feature flags con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | plataforma de feature flags adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | plataforma de feature flags estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | plataforma de feature flags está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C5-Q4: ¿En qué medida se han adoptado Estrategias de Release y Despliegue (release coordination via ChatOps) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% releases using ChatOps`

**Contexto**

- **Qué mide (what):** Los releases se coordinan mediante un bot de chat con aprobaciones.
- **Por qué importa (why):** ChatOps crea una pista de auditoría y reduce errores de handoff.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin coordinación de releases vía ChatOps implementado. Los equipos operan sin esta capability. | • Sin coordinación de releases vía ChatOps implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de coordinación de releases vía ChatOps con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | coordinación de releases vía ChatOps adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | coordinación de releases vía ChatOps estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | coordinación de releases vía ChatOps está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C5-Q5: ¿En qué medida se han adoptado Estrategias de Release y Despliegue (progressive delivery across regions) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `regions rolled out per release`

**Contexto**

- **Qué mide (what):** Los releases se propagan por regiones con checks de salud automatizados.
- **Por qué importa (why):** El rollout multirregional contiene fallas regionales.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin entrega progresiva entre regiones implementado. Los equipos operan sin esta capability. | • Sin entrega progresiva entre regiones implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de entrega progresiva entre regiones con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | entrega progresiva entre regiones adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | entrega progresiva entre regiones estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | entrega progresiva entre regiones está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C5-Q6: ¿En qué medida se han adoptado Estrategias de Release y Despliegue (release metrics dashboard) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% releases meeting SLO`

**Contexto**

- **Qué mide (what):** El éxito del despliegue y el impacto en SLO se rastrean por release.
- **Por qué importa (why):** Las retrospectivas de release basadas en datos impulsan la mejora continua.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin dashboard de métricas de release implementado. Los equipos operan sin esta capability. | • Sin dashboard de métricas de release implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de dashboard de métricas de release con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | dashboard de métricas de release adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | dashboard de métricas de release estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | dashboard de métricas de release está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P2-C6: Automatización de pruebas

**7 preguntas en esta capability.**

### P2-C6-Q1: ¿En qué medida se ha adoptado Automatización de Pruebas (unit test coverage targets) en todos los equipos?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos >80% coverage`

**Contexto**

- **Qué mide (what):** Cada repo tiene un objetivo de cobertura medible.
- **Por qué importa (why):** La cobertura es un proxy útil cuando se combina con mutation testing.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin objetivos de cobertura de pruebas unitarias implementado. Los equipos operan sin esta capability. | • Sin objetivos de cobertura de pruebas unitarias implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de objetivos de cobertura de pruebas unitarias con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | objetivos de cobertura de pruebas unitarias adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | objetivos de cobertura de pruebas unitarias estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | objetivos de cobertura de pruebas unitarias está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C6-Q2: ¿En qué medida se ha adoptado Automatización de Pruebas (integration test suites) en todos los equipos?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `integration tests in CI`

**Contexto**

- **Qué mide (what):** Las pruebas de integración ejercitan límites de servicios reales.
- **Por qué importa (why):** Las pruebas de integración detectan bugs de cableado que las unitarias no pueden detectar.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin suites de pruebas de integración implementado. Los equipos operan sin esta capability. | • Sin suites de pruebas de integración implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de suites de pruebas de integración con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | suites de pruebas de integración adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | suites de pruebas de integración estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | suites de pruebas de integración está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C6-Q3: ¿En qué medida se ha adoptado Automatización de Pruebas (end-to-end / journey tests) en todos los equipos?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `critical journeys automated`

**Contexto**

- **Qué mide (what):** Los recorridos críticos de usuario se ejecutan automáticamente en cada deploy.
- **Por qué importa (why):** Las pruebas E2E protegen flujos críticos para los ingresos.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin pruebas end-to-end / journey tests implementado. Los equipos operan sin esta capability. | • Sin pruebas end-to-end / journey implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de pruebas end-to-end / journey tests con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | pruebas end-to-end / journey tests adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | pruebas end-to-end / journey tests estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | pruebas end-to-end / journey tests está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C6-Q4: ¿En qué medida se ha adoptado Automatización de Pruebas (contract testing) en todos los equipos?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% service pairs with contract tests`

**Contexto**

- **Qué mide (what):** Las pruebas de contrato impulsadas por consumidores detectan rupturas de API.
- **Por qué importa (why):** Las pruebas de contrato protegen la compatibilidad de microservicios.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin contract testing implementado. Los equipos operan sin esta capability. | • Sin contract testing implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de contract testing con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | contract testing adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | contract testing estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | contract testing está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C6-Q5: ¿En qué medida se ha adoptado Automatización de Pruebas (AI-assisted test generation) en todos los equipos?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% tests AI-generated`

**Contexto**

- **Qué mide (what):** La IA propone pruebas para código nuevo y modificado.
- **Por qué importa (why):** Las pruebas generadas por IA elevan el piso de cobertura.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin generación de pruebas asistida por IA implementado. Los equipos operan sin esta capability. | • Sin generación de pruebas asistida por IA implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de generación de pruebas asistida por IA con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | generación de pruebas asistida por IA adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | generación de pruebas asistida por IA estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | generación de pruebas asistida por IA está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C6-Q6: ¿En qué medida se ha adoptado Automatización de Pruebas (flaky-test detection & quarantine) en todos los equipos?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `flaky test rate`

**Contexto**

- **Qué mide (what):** Las pruebas flaky se ponen en cuarentena automática y se trian.
- **Por qué importa (why):** Las pruebas flaky erosionan la confianza; la detección la restaura.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin detección & cuarentena de flaky tests implementado. Los equipos operan sin esta capability. | • Sin detección y cuarentena de pruebas flaky implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de detección & cuarentena de flaky tests con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | detección & cuarentena de flaky tests adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | detección & cuarentena de flaky tests estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | detección & cuarentena de flaky tests está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C6-Q7: ¿En qué medida se ha adoptado Automatización de Pruebas (mutation testing) en todos los equipos?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `mutation score of critical modules`

**Contexto**

- **Qué mide (what):** Mutation testing valida la calidad del conjunto de pruebas.
- **Por qué importa (why):** Los puntajes de mutación revelan si las pruebas realmente detectan bugs.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin mutation testing implementado. Los equipos operan sin esta capability. | • Sin mutation testing implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de mutation testing con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | mutation testing adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | mutation testing estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | mutation testing está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P2-C7: Gestión de incidentes y SRE

**7 preguntas en esta capability.**

### P2-C7-Q1: ¿En qué medida se ha adoptado Gestión de Incidentes y SRE (on-call rotation with tooling) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services with on-call`

**Contexto**

- **Qué mide (what):** Cada servicio de producción tiene una rotación on-call nombrada.
- **Por qué importa (why):** La propiedad clara es la base de la confiabilidad.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin rotación on-call con tooling implementado. Los equipos operan sin esta capability. | • Sin rotación on-call con herramientas implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de rotación on-call con tooling con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | rotación on-call con tooling adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | rotación on-call con tooling estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | rotación on-call con tooling está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C7-Q2: ¿En qué medida se ha adoptado Gestión de Incidentes y SRE (blameless postmortems) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% incidents with postmortem`

**Contexto**

- **Qué mide (what):** Los postmortems se enfocan en sistemas, no en personas.
- **Por qué importa (why):** La cultura blameless desbloquea el aprendizaje honesto.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin postmortems sin culpa implementado. Los equipos operan sin esta capability. | • Sin postmortems sin culpabilización implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de postmortems sin culpa con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | postmortems sin culpa adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | postmortems sin culpa estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | postmortems sin culpa está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C7-Q3: ¿En qué medida se ha adoptado Gestión de Incidentes y SRE (error budget policy) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Seguridad, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services using error budgets`

**Contexto**

- **Qué mide (what):** Los presupuestos de error regulan el trabajo de features frente al trabajo de confiabilidad.
- **Por qué importa (why):** Los presupuestos de error hacen que la confiabilidad sea una decisión de negocio compartida.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin política de presupuesto de error implementado. Los equipos operan sin esta capability. | • Sin política de presupuesto de error implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de política de presupuesto de error con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | política de presupuesto de error adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | política de presupuesto de error estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | política de presupuesto de error está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C7-Q4: ¿En qué medida se ha adoptado Gestión de Incidentes y SRE (chaos engineering) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `gamedays per quarter`

**Contexto**

- **Qué mide (what):** La inyección controlada de fallas ejercita la resiliencia.
- **Por qué importa (why):** Chaos engineering genera confianza en la recuperación.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin chaos engineering implementado. Los equipos operan sin esta capability. | • Sin chaos engineering implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de chaos engineering con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | chaos engineering adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | chaos engineering estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | chaos engineering está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C7-Q5: ¿En qué medida se ha adoptado Gestión de Incidentes y SRE (incident commander role) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% major incidents with IC`

**Contexto**

- **Qué mide (what):** Un incident commander coordina la respuesta.
- **Por qué importa (why):** Un único coordinador reduce la confusión durante incidentes.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin rol de incident commander implementado. Los equipos operan sin esta capability. | • Sin rol de incident commander implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de rol de incident commander con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | rol de incident commander adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | rol de incident commander estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | rol de incident commander está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C7-Q6: ¿En qué medida se ha adoptado Gestión de Incidentes y SRE (SRE-dev partnership model) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, engineering-leader, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% teams with SRE partner`

**Contexto**

- **Qué mide (what):** Los equipos de SRE y dev colaboran en roadmaps de confiabilidad.
- **Por qué importa (why):** La colaboración integrada supera al gatekeeping.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin modelo de colaboración SRE-dev implementado. Los equipos operan sin esta capability. | • Sin modelo de asociación SRE-dev implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de modelo de colaboración SRE-dev con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | modelo de colaboración SRE-dev adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | modelo de colaboración SRE-dev estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | modelo de colaboración SRE-dev está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C7-Q7: ¿En qué medida se ha adoptado Gestión de Incidentes y SRE (runbook automation) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% incidents with runbook run`

**Contexto**

- **Qué mide (what):** Los pasos de runbook se codifican y se ejecutan automáticamente.
- **Por qué importa (why):** La automatización de runbook reduce el MTTR y disminuye el error humano.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin automatización de runbooks implementado. Los equipos operan sin esta capability. | • Sin automatización de runbooks implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de automatización de runbooks con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | automatización de runbooks adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | automatización de runbooks estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | automatización de runbooks está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P2-C8: Gestión de artefactos y paquetes

**5 preguntas en esta capability.**

### P2-C8-Q1: ¿En qué medida se ha adoptado Gestión de Artefactos y Paquetes (internal package registry) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% packages via registry`

**Contexto**

- **Qué mide (what):** El registro interno aloja todos los paquetes; no hay dependencias solo públicas.
- **Por qué importa (why):** Un registro habilita controles de auditoría y disponibilidad.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin registro interno de paquetes implementado. Los equipos operan sin esta capability. | • Sin registro interno de paquetes implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de registro interno de paquetes con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | registro interno de paquetes adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | registro interno de paquetes estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | registro interno de paquetes está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C8-Q2: ¿En qué medida se ha adoptado Gestión de Artefactos y Paquetes (SBOM for every build) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% builds with SBOM`

**Contexto**

- **Qué mide (what):** Cada build genera una lista de materiales de software.
- **Por qué importa (why):** Los SBOMs ahora son un requisito regulatorio y de seguridad.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin SBOM para cada build implementado. Los equipos operan sin esta capability. | • Sin SBOM para cada build implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de SBOM para cada build con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | SBOM para cada build adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | SBOM para cada build estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | SBOM para cada build está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C8-Q3: ¿En qué medida se ha adoptado Gestión de Artefactos y Paquetes (artifact signing (SLSA)) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% artifacts signed`

**Contexto**

- **Qué mide (what):** Los artefactos se firman y verifican al deploy.
- **Por qué importa (why):** La firma previene la manipulación de la cadena de suministro.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin firma de artefactos (SLSA) implementado. Los equipos operan sin esta capability. | • Sin firma de artefactos (SLSA) implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de firma de artefactos (SLSA) con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | firma de artefactos (SLSA) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | firma de artefactos (SLSA) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | firma de artefactos (SLSA) está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C8-Q4: ¿En qué medida se ha adoptado Gestión de Artefactos y Paquetes (vulnerability scanning of artifacts) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% artifacts scanned`

**Contexto**

- **Qué mide (what):** Cada artefacto se escanea antes del despliegue.
- **Por qué importa (why):** El escaneo previo al deploy bloquea artefactos conocidos como malos.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin escaneo de vulnerabilidades en artefactos implementado. Los equipos operan sin esta capability. | • Sin escaneo de vulnerabilidades de artefactos implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de escaneo de vulnerabilidades en artefactos con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | escaneo de vulnerabilidades en artefactos adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | escaneo de vulnerabilidades en artefactos estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | escaneo de vulnerabilidades en artefactos está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C8-Q5: ¿En qué medida se ha adoptado Gestión de Artefactos y Paquetes (retention & promotion policies) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `artifacts promoted via policy`

**Contexto**

- **Qué mide (what):** Los artefactos avanzan por dev→stage→prod con gates de política.
- **Por qué importa (why):** Las políticas de promoción vinculan los deploys con la procedencia.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin políticas de retención & promoción implementado. Los equipos operan sin esta capability. | • Sin políticas de retención y promoción implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de políticas de retención & promoción con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | políticas de retención & promoción adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | políticas de retención & promoción estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | políticas de retención & promoción está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P2-C9: Gestión de cambios y GitOps

**5 preguntas en esta capability.**

### P2-C9-Q1: ¿En qué medida se ha adoptado Gestión de Cambios y GitOps (GitOps controllers in prod) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% clusters on GitOps`

**Contexto**

- **Qué mide (what):** El estado del clúster se reconcilia desde Git mediante un controlador.
- **Por qué importa (why):** GitOps hace que el cambio sea trazable, auditable y reversible.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin controladores GitOps en producción implementado. Los equipos operan sin esta capability. | • Sin controladores GitOps en prod implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de controladores GitOps en producción con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | controladores GitOps en producción adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | controladores GitOps en producción estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | controladores GitOps en producción está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C9-Q2: ¿En qué medida se ha adoptado Gestión de Cambios y GitOps (automated change tickets) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% changes ticketed automatically`

**Contexto**

- **Qué mide (what):** Los registros de cambio se crean automáticamente a partir de PRs.
- **Por qué importa (why):** La automatización mantiene registros precisos sin ralentizar la entrega.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin tickets de cambio automatizados implementado. Los equipos operan sin esta capability. | • Sin tickets de cambio automatizados implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de tickets de cambio automatizados con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | tickets de cambio automatizados adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | tickets de cambio automatizados estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | tickets de cambio automatizados está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C9-Q3: ¿En qué medida se ha adoptado Gestión de Cambios y GitOps (approvals in PR (not tickets)) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% approvals in PR`

**Contexto**

- **Qué mide (what):** Las aprobaciones de cambio ocurren en la revisión de código, no en tickets separados.
- **Por qué importa (why):** Approval-as-code reduce el tiempo de ciclo mientras mantiene la pista de auditoría.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin aprobaciones en PR (no tickets) implementado. Los equipos operan sin esta capability. | • Sin aprobaciones en PR (no tickets) implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de aprobaciones en PR (no tickets) con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | aprobaciones en PR (no tickets) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | aprobaciones en PR (no tickets) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | aprobaciones en PR (no tickets) está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C9-Q4: ¿En qué medida se ha adoptado Gestión de Cambios y GitOps (environment promotion via PR) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% envs promoted via PR`

**Contexto**

- **Qué mide (what):** Pasar de stage a prod es un PR, no un clic.
- **Por qué importa (why):** La promoción basada en PR hereda revisión y rollback.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin promoción de entornos vía PR implementado. Los equipos operan sin esta capability. | • Sin promoción de entorno vía PR implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de promoción de entornos vía PR con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | promoción de entornos vía PR adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | promoción de entornos vía PR estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | promoción de entornos vía PR está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C9-Q5: ¿En qué medida se ha adoptado Gestión de Cambios y GitOps (compliance evidence auto-collected) en todos los equipos?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `controls automated`

**Contexto**

- **Qué mide (what):** La evidencia para SOC2/ISO se recopila automáticamente desde CI.
- **Por qué importa (why):** La auto-evidencia convierte las auditorías en un efecto secundario del trabajo normal.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin evidencia de compliance recolectada automáticamente implementado. Los equipos operan sin esta capability. | • Sin evidencia de cumplimiento recopilada automáticamente implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de evidencia de compliance recolectada automáticamente con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | evidencia de compliance recolectada automáticamente adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | evidencia de compliance recolectada automáticamente estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | evidencia de compliance recolectada automáticamente está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P2-C10: Seguridad de dependencias y cadena de suministro

**5 preguntas en esta capability.**

### P2-C10-Q1: ¿En qué medida se ha adoptado Seguridad de Dependencias y Cadena de Suministro (dependabot or renovate on every repo) en todos los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos auto-updated`

**Contexto**

- **Qué mide (what):** Dependabot o Renovate abre PRs para dependencias desactualizadas.
- **Por qué importa (why):** Las actualizaciones automatizadas mantienen corta la ventana de CVE.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin Dependabot o Renovate en cada repo implementado. Los equipos operan sin esta capability. | • Sin dependabot o renovate en cada repo implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de Dependabot o Renovate en cada repo con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Dependabot o Renovate en cada repo adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Dependabot o Renovate en cada repo estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | Dependabot o Renovate en cada repo está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C10-Q2: ¿En qué medida se ha adoptado Seguridad de Dependencias y Cadena de Suministro (allow-list registries only) en todos los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% deps from allow-listed source`

**Contexto**

- **Qué mide (what):** Los registros proxy filtran paquetes de fuentes confiables.
- **Por qué importa (why):** El proxy bloquea typosquatting y paquetes maliciosos.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin solo registros en allow-list implementado. Los equipos operan sin esta capability. | • Sin registros solo allow-list implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de solo registros en allow-list con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | solo registros en allow-list adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | solo registros en allow-list estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | solo registros en allow-list está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C10-Q3: ¿En qué medida se ha adoptado Seguridad de Dependencias y Cadena de Suministro (build provenance (SLSA level)) en todos los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `SLSA level reached`

**Contexto**

- **Qué mide (what):** Los builds llevan metadatos de procedencia verificables.
- **Por qué importa (why):** La procedencia es la base de la confianza en la cadena de suministro.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin procedencia de build (nivel SLSA) implementado. Los equipos operan sin esta capability. | • Sin procedencia de build (nivel SLSA) implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de procedencia de build (nivel SLSA) con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | procedencia de build (nivel SLSA) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | procedencia de build (nivel SLSA) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | procedencia de build (nivel SLSA) está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C10-Q4: ¿En qué medida se ha adoptado Seguridad de Dependencias y Cadena de Suministro (critical dep response playbook) en todos los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `median time to patch critical`

**Contexto**

- **Qué mide (what):** Un playbook maneja eventos de clase Log4Shell.
- **Por qué importa (why):** La preparación vence a la improvisación en un zero-day.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin playbook de respuesta a dependencias críticas implementado. Los equipos operan sin esta capability. | • Sin playbook de respuesta a dependencias críticas implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de playbook de respuesta a dependencias críticas con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | playbook de respuesta a dependencias críticas adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | playbook de respuesta a dependencias críticas estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | playbook de respuesta a dependencias críticas está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P2-C10-Q5: ¿En qué medida se ha adoptado Seguridad de Dependencias y Cadena de Suministro (vendor/OSS risk reviews) en todos los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `critical vendors reviewed/year`

**Contexto**

- **Qué mide (what):** Los proveedores de alto riesgo y las dependencias OSS se revisan anualmente.
- **Por qué importa (why):** La revisión saca a la luz el riesgo antes de que se convierta en incidente.

**Formato de respuesta**

Escala Likert de 5 niveles (L0-L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin revisiones de riesgo de vendor/OSS implementado. Los equipos operan sin esta capability. | • Sin revisiones de riesgo de proveedor/OSS implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de revisiones de riesgo de vendor/OSS con <10% de cobertura de equipos y uso ad-hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | revisiones de riesgo de vendor/OSS adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | revisiones de riesgo de vendor/OSS estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | revisiones de riesgo de vendor/OSS está optimizado, automatizado y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## Cómo se puntúa esta sección

- Cada pregunta recibe un valor numérico a partir del nivel seleccionado: L0=0, L1=1, L2=2, L3=3, L4=4.
- La puntuación de la capability es el promedio ponderado de las preguntas (peso predeterminado = 1.0; las preguntas con peso 1.5 o 2.0 cuentan más).
- La puntuación del pilar **P2** es el promedio de las 10 capabilities.
- El resultado se muestra en una escala de 0-4 y se convierte a un % de madurez (nivel / 4 × 100).

## Glosario rápido

- **Pilar:** dimensión estratégica de madurez.
- **Capability:** subdominio funcional dentro de un pilar.
- **Pregunta:** elemento concreto de evaluación, ID estándar `P[1-3]-C[1-19]-Q[1-99]`.
- **Nivel (L0-L4):** punto en la escala Likert de madurez.
- **KPI:** indicador clave que valida objetivamente el nivel declarado.
- **Evidencia:** prueba cualitativa (texto) o cuantitativa (adjunto) que respalda la respuesta.
