# AI Maturity Assessment: Pilar P3, Plataforma de aplicaciones

🌐 [English](P3-application-platform.md) · [Português (Brasil)](P3-application-platform.pt-br.md) · Español

> Mide la sofisticación de la plataforma: arquitectura cloud-native, APIs, IA, datos, agentes, identidad, multi-cloud, rendimiento y FinOps.

## Resumen

- **Pilar:** `P3`: Plataforma de aplicaciones
- **Capabilities incluidas:** 9
- **Total de preguntas:** 46
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

## Capabilities del pilar P3

- **P3-C1**: Arquitectura cloud-native (5 preguntas)
- **P3-C2**: Gestión de API (5 preguntas)
- **P3-C3**: Desarrollo de aplicaciones con IA (5 preguntas)
- **P3-C4**: Plataforma de datos y lakehouse (5 preguntas)
- **P3-C5**: Aplicaciones agénticas (6 preguntas)
- **P3-C6**: Gestión de identidad y acceso (5 preguntas)
- **P3-C7**: Multi-cloud y portabilidad (5 preguntas)
- **P3-C8**: Rendimiento y escalabilidad (5 preguntas)
- **P3-C9**: FinOps y optimización de costos (5 preguntas)

---

## P3-C1: Arquitectura cloud-native

**5 preguntas en esta capability.**

### P3-C1-Q1: ¿Qué tan madura es la adopción de arquitectura cloud-native?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Sí
- **KPI principal:** `% workloads containerized`

**Contexto**

- **Qué mide (what):** Mide la adopción de patrones cloud-native, incluida la contenerización, la orquestación y la descomposición de servicios.
- **Por qué importa (why):** Las arquitecturas cloud-native habilitan un escalamiento 10x más rápido, 99.99% de disponibilidad y una reducción de 50% en costos de infraestructura.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Aplicaciones monolíticas desplegadas en VM o bare metal. Sin contenedorización. | • Sin adopción de contenedores<br>• Topología de despliegue basada en VM<br>• Arquitectura monolítica en uso |
| **L1** | En desarrollo | Algunas aplicaciones contenedorizadas (<30%). Docker usado para desarrollo, pero no para producción. | • Tasa de contenerización medida <30%<br>• Docker solo en desarrollo<br>• Sin plataforma de orquestación |
| **L2** | Definido | 50-70% de las cargas de trabajo contenedorizadas. Kubernetes u orquestación de contenedores en producción. Descomposición básica en microservicios. | • Tasa de contenerización medida de 50-70%<br>• K8s en producción<br>• Algunos microservicios implementados |
| **L3** | Gestionado | >85% de las cargas de trabajo cloud-native. Service mesh, despliegue GitOps, escalado automatizado. Límites de servicio bien definidos. | • Tasa cloud-native medida >85%<br>• Service mesh implementado<br>• Flujo GitOps adoptado<br>• Reglas de escalado automatizado configuradas |
| **L4** | Optimizando | Cloud-native completo con asignación de recursos optimizada por IA, autoscaling predictivo, infraestructura self-healing y serverless cuando corresponde. | • Optimización de recursos con IA<br>• Escalado automatizado predictivo habilitado<br>• Infraestructura self-healing habilitada<br>• Adopción de plataforma serverless |

---

### P3-C1-Q2: ¿En qué medida se ha adoptado la Arquitectura Cloud-Native (adopción de contenedores) entre los equipos?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% workloads containerized`

**Contexto**

- **Qué mide (what):** Las cargas de trabajo se ejecutan como contenedores en Kubernetes o plataformas gestionadas.
- **Por qué importa (why):** Los contenedores habilitan densidad, portabilidad y despliegues declarativos.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado adopción de contenedores. Los equipos operan sin esta capability. | • Sin adopción de contenedores implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de adopción de contenedores con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de adopción de contenedores por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de adopción de contenedores en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de adopción de contenedores está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C1-Q3: ¿En qué medida se ha adoptado la Arquitectura Cloud-Native (service mesh / redes zero trust) entre los equipos?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services on mesh`

**Contexto**

- **Qué mide (what):** Service mesh gestiona mTLS, reintentos y modelado de tráfico.
- **Por qué importa (why):** Mesh saca la confiabilidad y la seguridad del código de la app.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado service mesh / redes zero trust. Los equipos operan sin esta capability. | • Sin service mesh / red zero trust implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de service mesh / redes zero trust con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de service mesh / redes zero trust por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de service mesh / redes zero trust en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de service mesh / redes zero trust está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C1-Q4: ¿En qué medida se ha adoptado la Arquitectura Cloud-Native (arquitectura orientada a eventos) entre los equipos?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% flows async`

**Contexto**

- **Qué mide (what):** Los eventos y las colas desacoplan servicios para lograr resiliencia y escala.
- **Por qué importa (why):** EDA habilita bajo acoplamiento y degradación controlada.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado arquitectura orientada a eventos. Los equipos operan sin esta capability. | • Sin arquitectura orientada a eventos implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de arquitectura orientada a eventos con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de arquitectura orientada a eventos por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de arquitectura orientada a eventos en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de arquitectura orientada a eventos está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C1-Q5: ¿En qué medida se ha adoptado la Arquitectura Cloud-Native (preferencia por servicios gestionados) entre los equipos?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% managed vs self-hosted`

**Contexto**

- **Qué mide (what):** Prefiere bases de datos, colas y cachés gestionados en lugar de operarlos internamente.
- **Por qué importa (why):** Los servicios gestionados trasladan la carga operativa al proveedor de nube.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado preferencia por servicios administrados. Los equipos operan sin esta capability. | • Sin preferencia por servicios gestionados implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de preferencia por servicios administrados con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de preferencia por servicios administrados por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de preferencia por servicios administrados en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de preferencia por servicios administrados está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P3-C2: Gestión de API

**5 preguntas en esta capability.**

### P3-C2-Q1: ¿Qué tan madura es tu estrategia de gestión de APIs?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma, Desarrollador, engineering-leader, Seguridad
- **Peso:** 1.0
- **Professional Edition:** Sí
- **KPI principal:** `% APIs with OpenAPI spec`

**Contexto**

- **Qué mide (what):** Mide la madurez de las prácticas de diseño, documentación, versionado y gobernanza de APIs.
- **Por qué importa (why):** Las APIs bien gestionadas reducen el tiempo de integración en 70% y habilitan el crecimiento del ecosistema de socios.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin estándares de API. API diseñadas ad hoc. Sin documentación más allá del código fuente. | • Sin estándares de API<br>• Diseño de API ad-hoc<br>• Sin documentación de API |
| **L1** | En desarrollo | Algunas API tienen documentación básica. Sin estrategia de versionado. Manejo de errores inconsistente. | • Existen documentos básicos de API<br>• Sin política de versionado<br>• Formatos de error inconsistentes |
| **L2** | Definido | Especificaciones OpenAPI para >50% de las API. Directrices de diseño de API documentadas. Estrategia de versionado definida. | • >50% de APIs con OpenAPI<br>• Documento de directrices de diseño<br>• Estrategia de versionado de API documentada |
| **L3** | Gestionado | API gateway con gestión centralizada. >80% de las API documentadas. Rate limiting, autenticación y monitoreo estandarizados. Gestión del ciclo de vida de API. | • API gateway implementado<br>• Tasa documentada medida >80%<br>• Autenticación/rate limiting estandarizados |
| **L4** | Optimizando | Gestión de API impulsada por IA: documentación autogenerada desde el código, detección de anomalías en el tráfico de API, planificación predictiva de capacidad, comprobaciones automatizadas de compatibilidad hacia atrás. | • Documentación de API autogenerada<br>• Detección de anomalías de tráfico<br>• Planificación predictiva de capacidad<br>• Verificaciones automáticas de compatibilidad |

---

### P3-C2-Q2: ¿En qué medida se ha adoptado la Gestión de APIs (API gateway para todas las APIs externas) entre los equipos?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma, Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% APIs behind gateway`

**Contexto**

- **Qué mide (what):** El gateway gestiona autenticación, rate limiting y observabilidad.
- **Por qué importa (why):** Un gateway centraliza las preocupaciones transversales de las APIs.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado API gateway para todas las API externas. Los equipos operan sin esta capability. | • Sin API gateway para todas las APIs externas implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de API gateway para todas las API externas con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de API gateway para todas las API externas por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de API gateway para todas las API externas en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de API gateway para todas las API externas está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C2-Q3: ¿En qué medida se ha adoptado la Gestión de APIs (contratos OpenAPI) entre los equipos?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma, Desarrollador, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% APIs with spec`

**Contexto**

- **Qué mide (what):** Cada API tiene un contrato legible por máquina.
- **Por qué importa (why):** Los contratos habilitan codegen, servidores mock y pruebas de compatibilidad.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado contratos OpenAPI. Los equipos operan sin esta capability. | • Sin contratos OpenAPI implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de contratos OpenAPI con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de contratos OpenAPI por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de contratos OpenAPI en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de contratos OpenAPI está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C2-Q4: ¿En qué medida se ha adoptado la Gestión de APIs (política de versionado & desuso) entre los equipos?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma, Desarrollador, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `deprecated APIs retired on time`

**Contexto**

- **Qué mide (what):** Versionado explícito y calendarios de desuso.
- **Por qué importa (why):** Una política clara preserva la confianza del cliente y evita rupturas.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado política de versionado y de obsolescencia. Los equipos operan sin esta capability. | • Sin política de versionado y deprecación implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de política de versionado y de obsolescencia con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de política de versionado y de obsolescencia por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de política de versionado y de obsolescencia en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de política de versionado y de obsolescencia está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C2-Q5: ¿En qué medida se ha adoptado la Gestión de APIs (portal para desarrolladores con claves de autoservicio) entre los equipos?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma, Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `time-to-first-call`

**Contexto**

- **Qué mide (what):** Emisión de claves de autoservicio y documentación interactiva.
- **Por qué importa (why):** Los portales para desarrolladores aceleran la integración de socios.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado portal para desarrolladores con claves de autoservicio. Los equipos operan sin esta capability. | • Sin portal de desarrolladores con claves de autoservicio implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de portal para desarrolladores con claves de autoservicio con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de portal para desarrolladores con claves de autoservicio por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de portal para desarrolladores con claves de autoservicio en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de portal para desarrolladores con claves de autoservicio está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P3-C3: Desarrollo de aplicaciones con IA

**5 preguntas en esta capability.**

### P3-C3-Q1: ¿Qué tan madura es la capacidad de tu organización para crear y desplegar aplicaciones con IA?

**Metadatos**

- **Público objetivo:** data-ai, Desarrollador, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `# AI features in production`

**Contexto**

- **Qué mide (what):** Mide la capability de la organización para desarrollar, desplegar y mantener características de aplicaciones con IA.
- **Por qué importa (why):** Las organizaciones con desarrollo maduro de aplicaciones de IA entregan características de IA 5x más rápido y con 3x menos incidentes en producción.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | Sin funcionalidades de IA en aplicaciones de producción. Sin capability de equipo para desarrollo de IA. | • Sin características de IA implementadas<br>• Sin habilidades de ingeniería de ML/IA<br>• Sin herramientas de desarrollo de IA |
| **L1** | En desarrollo | Experimentación con API de IA (OpenAI, Azure AI) en 1-2 aplicaciones. Sin prácticas de MLOps. | • 1-2 experimentos de IA<br>• Integración directa con API<br>• Sin herramientas MLOps en marcha |
| **L2** | Definido | 3-5 funcionalidades impulsadas por IA en producción. Prácticas básicas de prompt engineering. Patrón RAG para recuperación de conocimiento. | • 3-5 características de IA en vivo<br>• Directrices de prompt engineering<br>• Implementación de RAG desplegada |
| **L3** | Gestionado | Framework de desarrollo de IA estandarizado. Pipeline de evaluación de modelos. Versionado de prompts y pruebas A/B. >10 funcionalidades de IA en producción. | • Documentación del framework de desarrollo de IA<br>• Pipeline de evaluación de modelos<br>• Flujo de versionado de prompts<br>• >10 características de IA |
| **L4** | Optimizando | Aplicaciones AI-native con agentes autónomos, orquestación multimodelo, evaluación continua de modelos y optimización automatizada de prompts. Las funcionalidades de IA son centrales para el producto. | • Despliegues de agentes autónomos<br>• Orquestación multimodelo habilitada<br>• Evaluación continua de modelos<br>• Optimización automatizada de prompts |

---

### P3-C3-Q2: ¿En qué medida se ha adoptado el Desarrollo de Aplicaciones de IA (frameworks de aplicaciones LLM) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Desarrollador, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% AI apps on framework`

**Contexto**

- **Qué mide (what):** Los equipos usan frameworks (LangChain, Semantic Kernel) para apps LLM.
- **Por qué importa (why):** Los frameworks aceleran patrones de RAG, agentes y evaluación.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado frameworks de aplicaciones LLM. Los equipos operan sin esta capability. | • Sin frameworks de aplicaciones LLM implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de frameworks de aplicaciones LLM con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de frameworks de aplicaciones LLM por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de frameworks de aplicaciones LLM en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de frameworks de aplicaciones LLM está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C3-Q3: ¿En qué medida se ha adoptado el Desarrollo de Aplicaciones de IA (harness de evaluación para IA) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Desarrollador, Arquitecto, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `evals per release`

**Contexto**

- **Qué mide (what):** Las evaluaciones automatizadas se ejecutan en cada cambio de modelo o prompt.
- **Por qué importa (why):** Las evaluaciones de IA detectan regresiones que las pruebas unitarias no pueden detectar.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado banco de pruebas de evaluación para IA. Los equipos operan sin esta capability. | • Sin harness de evaluación para IA implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de banco de pruebas de evaluación para IA con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de banco de pruebas de evaluación para IA por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de banco de pruebas de evaluación para IA en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de banco de pruebas de evaluación para IA está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C3-Q4: ¿En qué medida se ha adoptado el Desarrollo de Aplicaciones de IA (base de datos vectorial / plataforma RAG) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Desarrollador, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `RAG apps in prod`

**Contexto**

- **Qué mide (what):** Un almacén vectorial/plataforma RAG compartido atiende a varias apps.
- **Por qué importa (why):** RAG centralizado reduce el trabajo duplicado entre equipos.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado base de datos vectorial / plataforma RAG. Los equipos operan sin esta capability. | • Sin base de datos vectorial / plataforma RAG implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de base de datos vectorial / plataforma RAG con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de base de datos vectorial / plataforma RAG por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de base de datos vectorial / plataforma RAG en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de base de datos vectorial / plataforma RAG está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C3-Q5: ¿En qué medida se ha adoptado el Desarrollo de Aplicaciones de IA (IA responsable / filtros de seguridad) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Desarrollador, Arquitecto, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% AI apps with guardrails`

**Contexto**

- **Qué mide (what):** Todas las apps de IA integran seguridad de contenido y registros de auditoría.
- **Por qué importa (why):** La IA responsable es un requisito básico; incorporarla después es caro.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado IA responsable / filtros de seguridad. Los equipos operan sin esta capability. | • Sin IA responsable / filtros de seguridad implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de IA responsable / filtros de seguridad con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de IA responsable / filtros de seguridad por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de IA responsable / filtros de seguridad en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de IA responsable / filtros de seguridad está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P3-C4: Plataforma de datos y lakehouse

**5 preguntas en esta capability.**

### P3-C4-Q1: ¿En qué medida se ha adoptado la Plataforma de Datos y Lakehouse (lakehouse o plataforma de datos en uso) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% data in platform`

**Contexto**

- **Qué mide (what):** Un lakehouse unifica datos estructurados y no estructurados.
- **Por qué importa (why):** Los lakehouses combinan el rendimiento del warehouse con la flexibilidad del lake.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado lakehouse o plataforma de datos en uso. Los equipos operan sin esta capability. | • Sin lakehouse o plataforma de datos en uso implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de lakehouse o plataforma de datos en uso con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de lakehouse o plataforma de datos en uso por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de lakehouse o plataforma de datos en uso en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de lakehouse o plataforma de datos en uso está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C4-Q2: ¿En qué medida se ha adoptado la Plataforma de Datos y Lakehouse (contratos de datos entre productores & consumidores) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% pipelines with contracts`

**Contexto**

- **Qué mide (what):** Los contratos de datos declaran esquema y garantías de calidad.
- **Por qué importa (why):** Los contratos evitan rupturas silenciosas entre equipos.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado contratos de datos entre productores y consumidores. Los equipos operan sin esta capability. | • Sin contratos de datos entre productores y consumidores implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de contratos de datos entre productores y consumidores con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de contratos de datos entre productores y consumidores por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de contratos de datos entre productores y consumidores en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de contratos de datos entre productores y consumidores está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C4-Q3: ¿En qué medida se ha adoptado la Plataforma de Datos y Lakehouse (catálogo y seguimiento de linaje) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% datasets cataloged`

**Contexto**

- **Qué mide (what):** Cada dataset tiene propiedad, linaje y metadatos de calidad.
- **Por qué importa (why):** Los catálogos aceleran el descubrimiento y las investigaciones.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado catálogo y seguimiento de linaje. Los equipos operan sin esta capability. | • Sin catálogo y seguimiento de linaje implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de catálogo y seguimiento de linaje con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de catálogo y seguimiento de linaje por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de catálogo y seguimiento de linaje en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de catálogo y seguimiento de linaje está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C4-Q4: ¿En qué medida se ha adoptado la Plataforma de Datos y Lakehouse (analítica de autoservicio) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% decisions using data`

**Contexto**

- **Qué mide (what):** Los usuarios de negocio consultan datos por sí mismos mediante herramientas gobernadas.
- **Por qué importa (why):** El autoservicio quita el cuello de botella del equipo de datos.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado analítica de autoservicio. Los equipos operan sin esta capability. | • Sin analítica de autoservicio implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de analítica de autoservicio con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de analítica de autoservicio por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de analítica de autoservicio en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de analítica de autoservicio está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C4-Q5: ¿En qué medida se ha adoptado la Plataforma de Datos y Lakehouse (ingesta de streaming en tiempo real) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% use-cases real-time`

**Contexto**

- **Qué mide (what):** El streaming está disponible para casos de uso sensibles al tiempo.
- **Por qué importa (why):** Los datos en tiempo real habilitan IA más actualizada y decisiones operativas.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado ingesta de streaming en tiempo real. Los equipos operan sin esta capability. | • Sin ingesta streaming en tiempo real implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de ingesta de streaming en tiempo real con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de ingesta de streaming en tiempo real por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de ingesta de streaming en tiempo real en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de ingesta de streaming en tiempo real está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P3-C5: Aplicaciones agénticas

**6 preguntas en esta capability.**

### P3-C5-Q1: ¿En qué medida se han adoptado las Aplicaciones Agénticas (agentes con uso de herramientas en prod) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `agents in production`

**Contexto**

- **Qué mide (what):** Los agentes llaman a herramientas y APIs para realizar trabajo de varios pasos.
- **Por qué importa (why):** Los flujos de trabajo agénticos automatizan tareas complejas que antes las personas enrutaban.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado agentes con uso de herramientas en producción. Los equipos operan sin esta capability. | • Sin agentes con uso de herramientas en prod implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de agentes con uso de herramientas en producción con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de agentes con uso de herramientas en producción por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de agentes con uso de herramientas en producción en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de agentes con uso de herramientas en producción está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C5-Q2: ¿En qué medida se han adoptado las Aplicaciones Agénticas (framework de orquestación (Semantic Kernel, etc)) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, Ingeniero de plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% agents on framework`

**Contexto**

- **Qué mide (what):** Los agentes se crean sobre un runtime de orquestación estándar.
- **Por qué importa (why):** Los runtimes estándar reducen el costo de ingeniería por agente.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado framework de orquestación (Semantic Kernel, etc). Los equipos operan sin esta capability. | • Sin framework de orquestación (Semantic Kernel, etc) implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de framework de orquestación (Semantic Kernel, etc) con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de framework de orquestación (Semantic Kernel, etc) por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de framework de orquestación (Semantic Kernel, etc) en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de framework de orquestación (Semantic Kernel, etc) está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C5-Q3: ¿En qué medida se han adoptado las Aplicaciones Agénticas (evaluación y seguridad para agentes) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, Ingeniero de plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `eval scenarios per agent`

**Contexto**

- **Qué mide (what):** Los agentes se evalúan por seguridad, costo y finalización de tareas.
- **Por qué importa (why):** La evaluación de agentes es diferente de la evaluación de LLM.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado evaluación y seguridad para agentes. Los equipos operan sin esta capability. | • Sin evaluación y seguridad para agentes implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de evaluación y seguridad para agentes con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de evaluación y seguridad para agentes por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de evaluación y seguridad para agentes en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de evaluación y seguridad para agentes está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C5-Q4: ¿En qué medida se han adoptado las Aplicaciones Agénticas (registro de tools/actions) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, Ingeniero de plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `tools available to agents`

**Contexto**

- **Qué mide (what):** Un registro gobernado enumera las herramientas que los agentes pueden llamar.
- **Por qué importa (why):** Un registro controla el radio de impacto y habilita la auditoría.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado registro de herramientas/acciones. Los equipos operan sin esta capability. | • Sin registro de herramientas/acciones implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de registro de herramientas/acciones con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de registro de herramientas/acciones por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de registro de herramientas/acciones en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de registro de herramientas/acciones está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C5-Q5: ¿En qué medida se han adoptado las Aplicaciones Agénticas (controles human-in-the-loop) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% agents with HITL`

**Contexto**

- **Qué mide (what):** Las acciones de alto impacto requieren confirmación humana.
- **Por qué importa (why):** HITL permite que los equipos entreguen agentes de forma segura mientras aprenden.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado controles human-in-the-loop. Los equipos operan sin esta capability. | • Sin controles human-in-the-loop implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de controles human-in-the-loop con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de controles human-in-the-loop por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de controles human-in-the-loop en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de controles human-in-the-loop está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C5-Q6: ¿En qué medida se han adoptado las Aplicaciones Agénticas (telemetría de costo y latencia de agentes) entre los equipos?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, Ingeniero de plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `p95 agent step latency`

**Contexto**

- **Qué mide (what):** El rendimiento y el costo de los agentes se rastrean por paso.
- **Por qué importa (why):** La telemetría es necesaria para operar agentes de forma rentable a escala.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado telemetría de costo y latencia de agentes. Los equipos operan sin esta capability. | • Sin telemetría de costo y latencia de agentes implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de telemetría de costo y latencia de agentes con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de telemetría de costo y latencia de agentes por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de telemetría de costo y latencia de agentes en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de telemetría de costo y latencia de agentes está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P3-C6: Gestión de identidad y acceso

**5 preguntas en esta capability.**

### P3-C6-Q1: ¿En qué medida se ha adoptado la Gestión de Identidades y Accesos (SSO para todas las apps) entre los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% apps behind SSO`

**Contexto**

- **Qué mide (what):** Todas las apps se autentican mediante SSO central.
- **Por qué importa (why):** SSO es la base del ciclo de vida de usuarios y la revocación.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado SSO para todas las aplicaciones. Los equipos operan sin esta capability. | • Sin SSO para todas las aplicaciones implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de SSO para todas las aplicaciones con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de SSO para todas las aplicaciones por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de SSO para todas las aplicaciones en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de SSO para todas las aplicaciones está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C6-Q2: ¿En qué medida se ha adoptado la Gestión de Identidades y Accesos (identidad de workload (sin secretos de larga duración)) entre los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% workloads using WI`

**Contexto**

- **Qué mide (what):** Las cargas de trabajo usan identidad gestionada, no claves estáticas.
- **Por qué importa (why):** Las identidades gestionadas eliminan una clase completa de filtración.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado identidad de carga de trabajo (sin secretos de larga duración). Los equipos operan sin esta capability. | • Sin identidad de workload (sin secretos de larga duración) implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de identidad de carga de trabajo (sin secretos de larga duración) con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de identidad de carga de trabajo (sin secretos de larga duración) por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de identidad de carga de trabajo (sin secretos de larga duración) en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de identidad de carga de trabajo (sin secretos de larga duración) está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C6-Q3: ¿En qué medida se ha adoptado la Gestión de Identidades y Accesos (mínimo privilegio con elevación JIT) entre los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% access through JIT`

**Contexto**

- **Qué mide (what):** La administración permanente se reemplaza por elevación just-in-time.
- **Por qué importa (why):** JIT reduce drásticamente el radio de impacto de cuentas comprometidas.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado privilegio mínimo con elevación JIT. Los equipos operan sin esta capability. | • Sin privilegio mínimo con elevación JIT implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de privilegio mínimo con elevación JIT con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de privilegio mínimo con elevación JIT por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de privilegio mínimo con elevación JIT en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de privilegio mínimo con elevación JIT está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C6-Q4: ¿En qué medida se ha adoptado la Gestión de Identidades y Accesos (políticas de acceso condicional) entre los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% sessions policy-evaluated`

**Contexto**

- **Qué mide (what):** El acceso se concede según dispositivo, ubicación y riesgo.
- **Por qué importa (why):** El acceso condicional adapta la seguridad al contexto.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado políticas de acceso condicional. Los equipos operan sin esta capability. | • Sin políticas de acceso condicional implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de políticas de acceso condicional con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de políticas de acceso condicional por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de políticas de acceso condicional en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de políticas de acceso condicional está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C6-Q5: ¿En qué medida se ha adoptado la Gestión de Identidades y Accesos (revisiones de acceso y auditoría) entre los equipos?

**Metadatos**

- **Público objetivo:** Seguridad, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `access reviews per year`

**Contexto**

- **Qué mide (what):** El acceso se revisa al menos trimestralmente y queda registrado.
- **Por qué importa (why):** Las revisiones evitan la deriva de acceso por adquisiciones y reorganizaciones.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado revisiones de acceso y auditoría. Los equipos operan sin esta capability. | • Sin revisiones de acceso y auditoría implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de revisiones de acceso y auditoría con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de revisiones de acceso y auditoría por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de revisiones de acceso y auditoría en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de revisiones de acceso y auditoría está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P3-C7: Multi-cloud y portabilidad

**5 preguntas en esta capability.**

### P3-C7-Q1: ¿En qué medida se ha adoptado Multi-Cloud y Portabilidad (cargas de trabajo basadas en contenedores para portabilidad) entre los equipos?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% workloads portable`

**Contexto**

- **Qué mide (what):** Las cargas de trabajo se ejecutan en contenedores en cualquier nube.
- **Por qué importa (why):** La portabilidad es una cobertura contra lock-in e interrupciones.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado cargas de trabajo basadas en contenedores para portabilidad. Los equipos operan sin esta capability. | • Sin workloads basados en contenedores para portabilidad implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de cargas de trabajo basadas en contenedores para portabilidad con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de cargas de trabajo basadas en contenedores para portabilidad por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de cargas de trabajo basadas en contenedores para portabilidad en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de cargas de trabajo basadas en contenedores para portabilidad está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C7-Q2: ¿En qué medida se ha adoptado Multi-Cloud y Portabilidad (capa de datos abstraída (Postgres, etc)) entre los equipos?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% data on portable engines`

**Contexto**

- **Qué mide (what):** Los servicios de datos usan estándares abiertos (Postgres, MySQL).
- **Por qué importa (why):** Los motores abiertos mantienen acotados los costos de migración.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado capa de datos abstraída (Postgres, etc). Los equipos operan sin esta capability. | • Sin capa de datos abstraída (Postgres, etc) implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de capa de datos abstraída (Postgres, etc) con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de capa de datos abstraída (Postgres, etc) por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de capa de datos abstraída (Postgres, etc) en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de capa de datos abstraída (Postgres, etc) está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C7-Q3: ¿En qué medida se ha adoptado Multi-Cloud y Portabilidad (capability de despliegue multirregión) entre los equipos?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services multi-region`

**Contexto**

- **Qué mide (what):** Los servicios pueden ejecutarse active-active entre regiones.
- **Por qué importa (why):** La capability multirregión es necesaria para DR y cumplimiento.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado capability de despliegue multirregión. Los equipos operan sin esta capability. | • Sin capacidad de despliegue multi-región implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de capability de despliegue multirregión con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de capability de despliegue multirregión por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de capability de despliegue multirregión en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de capability de despliegue multirregión está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C7-Q4: ¿En qué medida se ha adoptado Multi-Cloud y Portabilidad (módulos IaC agnósticos de nube) entre los equipos?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% modules cloud-agnostic`

**Contexto**

- **Qué mide (what):** Los módulos IaC abstraen detalles específicos del proveedor cuando tiene sentido.
- **Por qué importa (why):** Una abstracción cuidadosa limita el dolor de portar.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado módulos IaC agnósticos de la nube. Los equipos operan sin esta capability. | • Sin módulos IaC cloud-agnostic implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de módulos IaC agnósticos de la nube con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de módulos IaC agnósticos de la nube por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de módulos IaC agnósticos de la nube en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de módulos IaC agnósticos de la nube está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C7-Q5: ¿En qué medida se ha adoptado Multi-Cloud y Portabilidad (simulacros de recuperación ante desastres) entre los equipos?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `DR drills per year`

**Contexto**

- **Qué mide (what):** Los simulacros anuales de DR validan el tiempo y el proceso de recuperación.
- **Por qué importa (why):** DR sin probar no es DR.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado simulacros de recuperación ante desastres. Los equipos operan sin esta capability. | • Sin simulacros de recuperación ante desastres implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de simulacros de recuperación ante desastres con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de simulacros de recuperación ante desastres por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de simulacros de recuperación ante desastres en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de simulacros de recuperación ante desastres está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P3-C8: Rendimiento y escalabilidad

**5 preguntas en esta capability.**

### P3-C8-Q1: ¿En qué medida se ha adoptado Rendimiento y Escalabilidad (presupuestos de rendimiento por servicio) entre los equipos?

**Metadatos**

- **Público objetivo:** devops, Arquitecto, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services with perf budget`

**Contexto**

- **Qué mide (what):** Los servicios declaran presupuestos de latencia y throughput.
- **Por qué importa (why):** Los presupuestos convierten el rendimiento en un requisito de primera clase.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado presupuestos de rendimiento por servicio. Los equipos operan sin esta capability. | • Sin presupuestos de rendimiento por servicio implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de presupuestos de rendimiento por servicio con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de presupuestos de rendimiento por servicio por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de presupuestos de rendimiento por servicio en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de presupuestos de rendimiento por servicio está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C8-Q2: ¿En qué medida se ha adoptado Rendimiento y Escalabilidad (pruebas de carga/stress en CI) entre los equipos?

**Metadatos**

- **Público objetivo:** devops, Arquitecto, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services load-tested`

**Contexto**

- **Qué mide (what):** Las pruebas de carga se ejecutan en cada candidato de release.
- **Por qué importa (why):** Detectar regresiones en CI es mejor que detectarlas en prod.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado pruebas de carga/estrés en CI. Los equipos operan sin esta capability. | • Sin pruebas de carga/estrés en CI implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de pruebas de carga/estrés en CI con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de pruebas de carga/estrés en CI por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de pruebas de carga/estrés en CI en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de pruebas de carga/estrés en CI está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C8-Q3: ¿En qué medida se ha adoptado Rendimiento y Escalabilidad (autoscaling basado en demanda real) entre los equipos?

**Metadatos**

- **Público objetivo:** devops, Arquitecto, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services autoscaled`

**Contexto**

- **Qué mide (what):** Los servicios autoscalan según CPU, latencia o profundidad de cola.
- **Por qué importa (why):** Autoscaling ajusta el costo a la demanda.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado autoscaling basado en demanda real. Los equipos operan sin esta capability. | • Sin autoscaling basado en demanda real implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de autoscaling basado en demanda real con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de autoscaling basado en demanda real por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de autoscaling basado en demanda real en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de autoscaling basado en demanda real está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C8-Q4: ¿En qué medida se ha adoptado Rendimiento y Escalabilidad (profiling en producción) entre los equipos?

**Metadatos**

- **Público objetivo:** devops, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services continuously profiled`

**Contexto**

- **Qué mide (what):** El profiling siempre activo (e.g., pyroscope, parca) se ejecuta en prod.
- **Por qué importa (why):** El profiling en prod revela cuellos de botella que afectan a usuarios reales.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado profiling en producción. Los equipos operan sin esta capability. | • Sin profiling en producción implementado<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de profiling en producción con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de profiling en producción por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de profiling en producción en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de profiling en producción está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C8-Q5: ¿En qué medida se ha adoptado Rendimiento y Escalabilidad (cadencia de planificación de capacidad) entre los equipos?

**Metadatos**

- **Público objetivo:** devops, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `capacity reviews per year`

**Contexto**

- **Qué mide (what):** La capacidad se revisa con proyecciones de crecimiento.
- **Por qué importa (why):** La planificación evita migraciones dolorosas en picos de carga.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado cadencia de planificación de capacidad. Los equipos operan sin esta capability. | • Sin cadencia de planificación de capacidad implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de cadencia de planificación de capacidad con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de cadencia de planificación de capacidad por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de cadencia de planificación de capacidad en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de cadencia de planificación de capacidad está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## P3-C9: FinOps y optimización de costos

**5 preguntas en esta capability.**

### P3-C9-Q1: ¿En qué medida se ha adoptado FinOps y Optimización de Costos (asignación de costos & showback) entre los equipos?

**Metadatos**

- **Público objetivo:** product-owner, engineering-leader, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% cost tagged to team`

**Contexto**

- **Qué mide (what):** Cada recurso se etiqueta y se atribuye a un equipo.
- **Por qué importa (why):** Showback crea propiedad sobre el costo.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado asignación de costos y showback. Los equipos operan sin esta capability. | • Sin asignación de costos y showback implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de asignación de costos y showback con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de asignación de costos y showback por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de asignación de costos y showback en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de asignación de costos y showback está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C9-Q2: ¿En qué medida se ha adoptado FinOps y Optimización de Costos (uso comprometido / savings plans) entre los equipos?

**Metadatos**

- **Público objetivo:** product-owner, engineering-leader, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% eligible spend committed`

**Contexto**

- **Qué mide (what):** El gasto comprometido se usa donde el uso es predecible.
- **Por qué importa (why):** Los compromisos reducen el gasto 20-50% con riesgo mínimo.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado uso comprometido / planes de ahorro. Los equipos operan sin esta capability. | • Sin uso comprometido / savings plans implementados<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de uso comprometido / planes de ahorro con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de uso comprometido / planes de ahorro por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de uso comprometido / planes de ahorro en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de uso comprometido / planes de ahorro está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C9-Q3: ¿En qué medida se ha adoptado FinOps y Optimización de Costos (limpieza de recursos inactivos y no usados) entre los equipos?

**Metadatos**

- **Público objetivo:** product-owner, engineering-leader, Ingeniero de plataforma, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `$/month saved by cleanup`

**Contexto**

- **Qué mide (what):** La automatización marca y elimina recursos inactivos.
- **Por qué importa (why):** La limpieza es la actividad FinOps de mayor apalancamiento.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado limpieza de recursos idle y no utilizados. Los equipos operan sin esta capability. | • Sin limpieza de recursos inactivos y no utilizados implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de limpieza de recursos idle y no utilizados con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de limpieza de recursos idle y no utilizados por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de limpieza de recursos idle y no utilizados en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de limpieza de recursos idle y no utilizados está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C9-Q4: ¿En qué medida se ha adoptado FinOps y Optimización de Costos (recomendaciones de rightsizing) entre los equipos?

**Metadatos**

- **Público objetivo:** product-owner, engineering-leader, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% rightsizing applied`

**Contexto**

- **Qué mide (what):** Las recomendaciones automatizadas impulsan el rightsizing continuo.
- **Por qué importa (why):** Rightsizing cierra la brecha entre lo aprovisionado y lo necesario.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado recomendaciones de rightsizing. Los equipos operan sin esta capability. | • Sin recomendaciones de rightsizing implementadas<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de recomendaciones de rightsizing con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de recomendaciones de rightsizing por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de recomendaciones de rightsizing en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de recomendaciones de rightsizing está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

### P3-C9-Q5: ¿En qué medida se ha adoptado FinOps y Optimización de Costos (economía unitaria por producto) entre los equipos?

**Metadatos**

- **Público objetivo:** product-owner, engineering-leader, Ingeniero de plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% products with $/user`

**Contexto**

- **Qué mide (what):** Los productos rastrean el costo por usuario, solicitud o transacción.
- **Por qué importa (why):** La economía unitaria alinea las decisiones de ingeniería y de negocio.

**Formato de respuesta**

Escala Likert de 5 niveles (L0 a L4). Selecciona **un** nivel que describa mejor a tu organización hoy. Agrega evidencia textual y/o adjuntos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencia esperada**

| Nivel | Etiqueta | Descripción | Evidencia sugerida |
|---|---|---|---|
| **L0** | Inicial | No se ha implementado economía unitaria por producto. Los equipos operan sin esta capability. | • Sin economía unitaria por producto implementada<br>• Sin política documentada<br>• Sin responsable asignado |
| **L1** | En desarrollo | Implementación piloto de economía unitaria por producto con <10% de cobertura de equipos y uso ad hoc. | • Documentación del programa piloto<br>• <10% de cobertura de equipos<br>• Sin política formal |
| **L2** | Definido | Adopción de economía unitaria por producto por 25-50% de los equipos con directrices básicas y capacitación. | • Tasa de adopción medida de 25-50%<br>• Directrices de uso publicadas<br>• Existen materiales de onboarding |
| **L3** | Gestionado | Estandarización de economía unitaria por producto en >75% de los equipos con resultados medidos y gobernanza. | • Tasa de adopción medida >75%<br>• KPI con seguimiento mensual<br>• Revisiones de gobernanza en marcha |
| **L4** | Optimizando | La práctica de economía unitaria por producto está optimizada, automatizada y se mejora continuamente con insights basados en datos. | • Tasa de adopción medida >95%<br>• Bucles automatizados de feedback de telemetría<br>• Programa de mejora continua |

---

## Cómo se puntúa esta sección

- Cada pregunta recibe un valor numérico a partir del nivel seleccionado: L0=0, L1=1, L2=2, L3=3, L4=4.
- La puntuación de la capability es el promedio ponderado de sus preguntas (peso predeterminado = 1.0; las preguntas con peso 1.5 o 2.0 cuentan más).
- La puntuación del pilar **P3** es el promedio de las 9 capabilities.
- El resultado se muestra en una escala de 0 a 4 y se convierte a un % de madurez (nivel / 4 × 100).

## Glosario rápido

- **Pilar:** dimensión estratégica de madurez.
- **Capability:** subdominio funcional dentro de un pilar.
- **Pregunta:** elemento concreto de evaluación, ID estándar `P[1-3]-C[1-19]-Q[1-99]`.
- **Nivel (L0-L4):** punto en la escala Likert de madurez.
- **KPI:** indicador clave que valida objetivamente el nivel declarado.
- **Evidencia:** prueba cualitativa (texto) o cuantitativa (adjunto) que respalda la respuesta.
