# Preguntas para Microsoft Forms: AI Maturity Assessment

🌐 [English](question-bank.md) · [Português (Brasil)](question-bank.pt-br.md) · Español

> Este documento contiene **LAS 158 preguntas** para crear el assessment en Microsoft Forms.
> Usa copy/paste sección por sección. Cada pregunta debe incluir:
>
> - **Tipo:** Choice (respuesta única) con las 6 opciones fijas y un campo Long Text para evidencia.

## Cómo Usar Este Documento

> [!IMPORTANT]
> Edición localizada: todas las etiquetas y preguntas están en español y todos los IDs se conservan.
> El importador encuentra cada pregunta por el prefijo de su ID, así que los formularios armados con el banco en portugués, inglés o español se importan igual.

1. Ve a <https://forms.office.com>
2. Crea un formulario nuevo en blanco
3. Título sugerido: `AI Maturity Assessment - <Nombre de la organización>`
4. Agrega **3 secciones** (una por pilar) usando `+ Add new` -> `Section`
5. Para cada pregunta, agrega 2 elementos:
   a. **Choice** (respuesta única) con el texto de la pregunta y las 6 opciones de abajo
   b. **Long Text** con etiqueta `Evidencia` (campo opcional)
6. Al final configura `Settings -> Anyone can respond` si compartirás por link
7. Comparte el link con el equipo
8. Cuando tengas respuestas, abre `Responses -> Open in Excel` para descargar el .xlsx

## Opciones Fijas para TODAS las Preguntas (Choice / Single answer)

Usa estas 6 opciones idénticas en cada pregunta (el orden importa para el parsing):

- **L0 - Inicial: Sin práctica establecida**
- **L1 - En desarrollo: Pilotos aislados (<25%)**
- **L2 - Definido: Cobertura 25-50% con directrices**
- **L3 - Gestionado: >75% con métricas de impacto**
- **L4 - Optimizando: Universal (>95%) con automatización continua**
- **NA - No sé / No aplica**

> ⚠️ **Importante:** mantén los prefijos `L0`, `L1`, ..., `L4`, `NA` al inicio de cada opción. La importación usa esos prefijos para mapear respuestas a valores numéricos (0-4 o null).

---

## Sección: Pilar P1: Productividad del desarrollador

_Esta sección tiene 53 preguntas en 9 capabilities._

### P1-C1: Asistentes de codificación con IA

#### Pregunta `P1-C1-Q1`

> **¿En qué medida tu organización utiliza herramientas de completado de código con IA (por ejemplo, GitHub Copilot)?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C1-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C1-Q2`

> **¿Con qué eficacia tu equipo aprovecha la IA para la revisión de código y la mejora de la calidad?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C1-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C1-Q3`

> **¿Cómo mide y da seguimiento tu organización al impacto de las herramientas de codificación con IA en la productividad?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C1-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C1-Q4`

> **¿Qué nivel de capabilities de pruebas asistidas por IA emplea tu organización?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C1-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C1-Q5`

> **¿Cómo gobierna tu organización el código generado por IA en términos de seguridad y cumplimiento?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C1-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P1-C2: Plataforma de experiencia del desarrollador

#### Pregunta `P1-C2-Q1`

> **¿Qué tan maduro es tu portal o plataforma interna para desarrolladores?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C2-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C2-Q2`

> **¿Con qué eficacia tus equipos usan entornos de desarrollo estandarizados?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C2-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C2-Q3`

> **¿En qué medida se ha adoptado la Plataforma de Experiencia del Desarrollador (IDP de autoservicio) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C2-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C2-Q4`

> **¿En qué medida se ha adoptado la Plataforma de Experiencia del Desarrollador (golden paths y plantillas) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C2-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C2-Q5`

> **¿En qué medida se ha adoptado la Plataforma de Experiencia del Desarrollador (portal de desarrolladores) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C2-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C2-Q6`

> **¿En qué medida se ha adoptado la Plataforma de Experiencia del Desarrollador (cumplimiento de políticas del camino trazado) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C2-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P1-C3: Gestión del conocimiento

#### Pregunta `P1-C3-Q1`

> **¿Con qué eficacia tu organización captura y comparte el conocimiento de desarrollo?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C3-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C3-Q2`

> **¿En qué medida se ha adoptado la Gestión del Conocimiento (búsqueda semántica de código) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C3-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C3-Q3`

> **¿En qué medida se ha adoptado la Gestión del Conocimiento (asistente de documentación basado en RAG) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C3-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C3-Q4`

> **¿En qué medida se ha adoptado la Gestión del Conocimiento (cobertura de runbooks y playbooks) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C3-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C3-Q5`

> **¿En qué medida se ha adoptado la Gestión del Conocimiento (ADR (registros de decisiones de arquitectura)) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C3-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C3-Q6`

> **¿En qué medida se ha adoptado la Gestión del Conocimiento (contenido de aprendizaje y rutas curadas) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C3-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P1-C4: Automatización de la revisión de código

#### Pregunta `P1-C4-Q1`

> **¿En qué medida se ha adoptado la Automatización de Revisión de Código (bot revisor de IA en cada PR) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C4-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C4-Q2`

> **¿En qué medida se ha adoptado la Automatización de Revisión de Código (linting estático y corrección automática de estilo) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C4-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C4-Q3`

> **¿En qué medida se ha adoptado la Automatización de Revisión de Código (revisión de seguridad automatizada) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C4-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C4-Q4`

> **¿En qué medida se ha adoptado la Automatización de Revisión de Código (reglas de revisores requeridos) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C4-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C4-Q5`

> **¿En qué medida se ha adoptado la Automatización de Revisión de Código (seguimiento de SLA de revisión) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C4-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C4-Q6`

> **¿En qué medida se ha adoptado la Automatización de Revisión de Código (cumplimiento del tamaño de los cambios) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C4-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C4-Q7`

> **¿En qué medida se ha adoptado la Automatización de Revisión de Código (balanceo de carga de revisores) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C4-Q7)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P1-C5: Onboarding y capacitación de desarrolladores

#### Pregunta `P1-C5-Q1`

> **¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (codespaces/dev containers para entorno instantáneo) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C5-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C5-Q2`

> **¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (playbook de onboarding estructurado) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C5-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C5-Q3`

> **¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (programa de mentoría por pares) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C5-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C5-Q4`

> **¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (currículo práctico y kata) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C5-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C5-Q5`

> **¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (rotación on-call en sombra) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C5-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C5-Q6`

> **¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (ciclo de feedback de onboarding) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C5-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C5-Q7`

> **¿En qué medida se ha adoptado el Onboarding y la Capacitación de Desarrolladores (medición del tiempo de adaptación) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C5-Q7)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P1-C6: Inner source y colaboración

#### Pregunta `P1-C6-Q1`

> **¿En qué medida se ha adoptado Inner Source y Colaboración (repos internos con contribución abierta) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C6-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C6-Q2`

> **¿En qué medida se ha adoptado Inner Source y Colaboración (estándares CONTRIBUTING.md) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C6-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C6-Q3`

> **¿En qué medida se ha adoptado Inner Source y Colaboración (portal de descubrimiento inner-source) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C6-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C6-Q4`

> **¿En qué medida se ha adoptado Inner Source y Colaboración (etiquetado good-first-issue) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C6-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C6-Q5`

> **¿En qué medida se ha adoptado Inner Source y Colaboración (revisiones de diseño entre equipos) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C6-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C6-Q6`

> **¿En qué medida se ha adoptado Inner Source y Colaboración (comunidad de práctica) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C6-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P1-C7: Automatización de la documentación

#### Pregunta `P1-C7-Q1`

> **¿En qué medida se ha adoptado la Automatización de Documentación (docs-as-code en Git) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C7-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C7-Q2`

> **¿En qué medida se ha adoptado la Automatización de Documentación (referencia de API generada automáticamente) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C7-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C7-Q3`

> **¿En qué medida se ha adoptado la Automatización de Documentación (redacción de documentación asistida por IA) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C7-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C7-Q4`

> **¿En qué medida se ha adoptado la Automatización de Documentación (linting de calidad de documentación) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C7-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C7-Q5`

> **¿En qué medida se ha adoptado la Automatización de Documentación (analítica de documentación) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C7-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P1-C8: Medición de productividad del desarrollador

#### Pregunta `P1-C8-Q1`

> **¿En qué medida se ha adoptado la Medición de Productividad del Desarrollador (cuatro métricas clave de DORA) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C8-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C8-Q2`

> **¿En qué medida se ha adoptado la Medición de Productividad del Desarrollador (encuestas de experiencia del desarrollador) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C8-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C8-Q3`

> **¿En qué medida se ha adoptado la Medición de Productividad del Desarrollador (tiempo del ciclo de feedback de build/test) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C8-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C8-Q4`

> **¿En qué medida se ha adoptado la Medición de Productividad del Desarrollador (adopción del framework SPACE) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C8-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C8-Q5`

> **¿En qué medida se ha adoptado la Medición de Productividad del Desarrollador (dashboards de flujo vs fricción) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C8-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C8-Q6`

> **¿En qué medida se ha adoptado la Medición de Productividad del Desarrollador (OKRs trimestrales de productividad) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C8-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P1-C9: Automatización de entornos y workspaces

#### Pregunta `P1-C9-Q1`

> **¿En qué medida se ha adoptado la Automatización de Entornos y Espacios de Trabajo (entornos locales reproducibles (devcontainers)) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C9-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C9-Q2`

> **¿En qué medida se ha adoptado la Automatización de Entornos y Espacios de Trabajo (workspaces en la nube (Codespaces/Gitpod)) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C9-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C9-Q3`

> **¿En qué medida se ha adoptado la Automatización de Entornos y Espacios de Trabajo (fijación de versiones de herramientas y SDK) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C9-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C9-Q4`

> **¿En qué medida se ha adoptado la Automatización de Entornos y Espacios de Trabajo (datos de prueba bajo demanda) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C9-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C9-Q5`

> **¿En qué medida se ha adoptado la Automatización de Entornos y Espacios de Trabajo (telemetría y salud del workspace) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P1-C9-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

---

## Sección: Pilar P2: Ciclo de vida DevOps

_Esta sección tiene 59 preguntas en 10 capabilities._

### P2-C1: Inteligencia de pipelines CI/CD

#### Pregunta `P2-C1-Q1`

> **¿Qué tan maduro es tu pipeline CI/CD en términos de automatización e integración de IA?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C1-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C1-Q2`

> **¿En qué medida se ha adoptado la Inteligencia de Pipeline CI/CD (pipeline-as-code everywhere) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C1-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C1-Q3`

> **¿En qué medida se ha adoptado la Inteligencia de Pipeline CI/CD (build caching and artifact reuse) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C1-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C1-Q4`

> **¿En qué medida se ha adoptado la Inteligencia de Pipeline CI/CD (trunk-based development) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C1-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C1-Q5`

> **¿En qué medida se ha adoptado la Inteligencia de Pipeline CI/CD (deployment frequency) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C1-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C1-Q6`

> **¿En qué medida se ha adoptado la Inteligencia de Pipeline CI/CD (feature flags for progressive delivery) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C1-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P2-C2: Infraestructura como código

#### Pregunta `P2-C2-Q1`

> **¿Qué porcentaje de tu infraestructura se gestiona como código?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C2-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C2-Q2`

> **¿En qué medida se ha adoptado Infraestructura como Código (Terraform/Bicep-based IaC) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C2-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C2-Q3`

> **¿En qué medida se ha adoptado Infraestructura como Código (module and pattern library) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C2-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C2-Q4`

> **¿En qué medida se ha adoptado Infraestructura como Código (GitOps for config drift) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C2-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C2-Q5`

> **¿En qué medida se ha adoptado Infraestructura como Código (policy-as-code (OPA/Conftest)) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C2-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C2-Q6`

> **¿En qué medida se ha adoptado Infraestructura como Código (ephemeral environment per PR) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C2-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P2-C3: Observabilidad y monitoreo

#### Pregunta `P2-C3-Q1`

> **¿Qué tan completa es tu stack de observabilidad (logs, métricas, trazas)?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C3-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C3-Q2`

> **¿En qué medida se ha adoptado Observabilidad y Monitoreo (structured logging w/ correlation IDs) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C3-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C3-Q3`

> **¿En qué medida se ha adoptado Observabilidad y Monitoreo (distributed tracing (OpenTelemetry)) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C3-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C3-Q4`

> **¿En qué medida se ha adoptado Observabilidad y Monitoreo (SLOs and error budgets) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C3-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C3-Q5`

> **¿En qué medida se ha adoptado Observabilidad y Monitoreo (synthetic monitoring) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C3-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C3-Q6`

> **¿En qué medida se ha adoptado Observabilidad y Monitoreo (anomaly detection with ML) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C3-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P2-C4: Integración de seguridad (DevSecOps)

#### Pregunta `P2-C4-Q1`

> **¿Qué tan integrada está la seguridad en tu pipeline de desarrollo y despliegue?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C4-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C4-Q2`

> **¿En qué medida se ha adoptado Integración de Seguridad (DevSecOps) (SAST in every pipeline) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C4-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C4-Q3`

> **¿En qué medida se ha adoptado Integración de Seguridad (DevSecOps) (SCA and dependency review) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C4-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C4-Q4`

> **¿En qué medida se ha adoptado Integración de Seguridad (DevSecOps) (secret scanning and push protection) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C4-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C4-Q5`

> **¿En qué medida se ha adoptado Integración de Seguridad (DevSecOps) (DAST and API security testing) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C4-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C4-Q6`

> **¿En qué medida se ha adoptado Integración de Seguridad (DevSecOps) (security champions program) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C4-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P2-C5: Estrategias de release y despliegue

#### Pregunta `P2-C5-Q1`

> **¿En qué medida se han adoptado Estrategias de Release y Despliegue (blue/green or canary deploys) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C5-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C5-Q2`

> **¿En qué medida se han adoptado Estrategias de Release y Despliegue (automated rollback) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C5-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C5-Q3`

> **¿En qué medida se han adoptado Estrategias de Release y Despliegue (feature flag platform) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C5-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C5-Q4`

> **¿En qué medida se han adoptado Estrategias de Release y Despliegue (release coordination via ChatOps) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C5-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C5-Q5`

> **¿En qué medida se han adoptado Estrategias de Release y Despliegue (progressive delivery across regions) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C5-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C5-Q6`

> **¿En qué medida se han adoptado Estrategias de Release y Despliegue (release metrics dashboard) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C5-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P2-C6: Automatización de pruebas

#### Pregunta `P2-C6-Q1`

> **¿En qué medida se ha adoptado Automatización de Pruebas (unit test coverage targets) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C6-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C6-Q2`

> **¿En qué medida se ha adoptado Automatización de Pruebas (integration test suites) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C6-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C6-Q3`

> **¿En qué medida se ha adoptado Automatización de Pruebas (end-to-end / journey tests) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C6-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C6-Q4`

> **¿En qué medida se ha adoptado Automatización de Pruebas (contract testing) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C6-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C6-Q5`

> **¿En qué medida se ha adoptado Automatización de Pruebas (AI-assisted test generation) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C6-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C6-Q6`

> **¿En qué medida se ha adoptado Automatización de Pruebas (flaky-test detection & quarantine) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C6-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C6-Q7`

> **¿En qué medida se ha adoptado Automatización de Pruebas (mutation testing) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C6-Q7)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P2-C7: Gestión de incidentes y SRE

#### Pregunta `P2-C7-Q1`

> **¿En qué medida se ha adoptado Gestión de Incidentes y SRE (on-call rotation with tooling) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C7-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C7-Q2`

> **¿En qué medida se ha adoptado Gestión de Incidentes y SRE (blameless postmortems) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C7-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C7-Q3`

> **¿En qué medida se ha adoptado Gestión de Incidentes y SRE (error budget policy) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C7-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C7-Q4`

> **¿En qué medida se ha adoptado Gestión de Incidentes y SRE (chaos engineering) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C7-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C7-Q5`

> **¿En qué medida se ha adoptado Gestión de Incidentes y SRE (incident commander role) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C7-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C7-Q6`

> **¿En qué medida se ha adoptado Gestión de Incidentes y SRE (SRE-dev partnership model) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C7-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C7-Q7`

> **¿En qué medida se ha adoptado Gestión de Incidentes y SRE (runbook automation) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C7-Q7)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P2-C8: Gestión de artefactos y paquetes

#### Pregunta `P2-C8-Q1`

> **¿En qué medida se ha adoptado Gestión de Artefactos y Paquetes (internal package registry) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C8-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C8-Q2`

> **¿En qué medida se ha adoptado Gestión de Artefactos y Paquetes (SBOM for every build) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C8-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C8-Q3`

> **¿En qué medida se ha adoptado Gestión de Artefactos y Paquetes (artifact signing (SLSA)) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C8-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C8-Q4`

> **¿En qué medida se ha adoptado Gestión de Artefactos y Paquetes (vulnerability scanning of artifacts) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C8-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C8-Q5`

> **¿En qué medida se ha adoptado Gestión de Artefactos y Paquetes (retention & promotion policies) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C8-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P2-C9: Gestión de cambios y GitOps

#### Pregunta `P2-C9-Q1`

> **¿En qué medida se ha adoptado Gestión de Cambios y GitOps (GitOps controllers in prod) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C9-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C9-Q2`

> **¿En qué medida se ha adoptado Gestión de Cambios y GitOps (automated change tickets) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C9-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C9-Q3`

> **¿En qué medida se ha adoptado Gestión de Cambios y GitOps (approvals in PR (not tickets)) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C9-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C9-Q4`

> **¿En qué medida se ha adoptado Gestión de Cambios y GitOps (environment promotion via PR) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C9-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C9-Q5`

> **¿En qué medida se ha adoptado Gestión de Cambios y GitOps (compliance evidence auto-collected) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C9-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P2-C10: Seguridad de dependencias y cadena de suministro

#### Pregunta `P2-C10-Q1`

> **¿En qué medida se ha adoptado Seguridad de Dependencias y Cadena de Suministro (dependabot or renovate on every repo) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C10-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C10-Q2`

> **¿En qué medida se ha adoptado Seguridad de Dependencias y Cadena de Suministro (allow-list registries only) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C10-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C10-Q3`

> **¿En qué medida se ha adoptado Seguridad de Dependencias y Cadena de Suministro (build provenance (SLSA level)) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C10-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C10-Q4`

> **¿En qué medida se ha adoptado Seguridad de Dependencias y Cadena de Suministro (critical dep response playbook) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C10-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C10-Q5`

> **¿En qué medida se ha adoptado Seguridad de Dependencias y Cadena de Suministro (vendor/OSS risk reviews) en todos los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P2-C10-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

---

## Sección: Pilar P3: Plataforma de aplicaciones

_Esta sección tiene 46 preguntas en 9 capabilities._

### P3-C1: Arquitectura cloud-native

#### Pregunta `P3-C1-Q1`

> **¿Qué tan madura es la adopción de arquitectura cloud-native?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C1-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C1-Q2`

> **¿En qué medida se ha adoptado la Arquitectura Cloud-Native (adopción de contenedores) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C1-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C1-Q3`

> **¿En qué medida se ha adoptado la Arquitectura Cloud-Native (service mesh / redes zero trust) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C1-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C1-Q4`

> **¿En qué medida se ha adoptado la Arquitectura Cloud-Native (arquitectura orientada a eventos) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C1-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C1-Q5`

> **¿En qué medida se ha adoptado la Arquitectura Cloud-Native (preferencia por servicios gestionados) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C1-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P3-C2: Gestión de API

#### Pregunta `P3-C2-Q1`

> **¿Qué tan madura es tu estrategia de gestión de APIs?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C2-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C2-Q2`

> **¿En qué medida se ha adoptado la Gestión de APIs (API gateway para todas las APIs externas) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C2-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C2-Q3`

> **¿En qué medida se ha adoptado la Gestión de APIs (contratos OpenAPI) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C2-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C2-Q4`

> **¿En qué medida se ha adoptado la Gestión de APIs (política de versionado & desuso) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C2-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C2-Q5`

> **¿En qué medida se ha adoptado la Gestión de APIs (portal para desarrolladores con claves de autoservicio) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C2-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P3-C3: Desarrollo de aplicaciones con IA

#### Pregunta `P3-C3-Q1`

> **¿Qué tan madura es la capacidad de tu organización para crear y desplegar aplicaciones con IA?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C3-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C3-Q2`

> **¿En qué medida se ha adoptado el Desarrollo de Aplicaciones de IA (frameworks de aplicaciones LLM) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C3-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C3-Q3`

> **¿En qué medida se ha adoptado el Desarrollo de Aplicaciones de IA (harness de evaluación para IA) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C3-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C3-Q4`

> **¿En qué medida se ha adoptado el Desarrollo de Aplicaciones de IA (base de datos vectorial / plataforma RAG) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C3-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C3-Q5`

> **¿En qué medida se ha adoptado el Desarrollo de Aplicaciones de IA (IA responsable / filtros de seguridad) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C3-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P3-C4: Plataforma de datos y lakehouse

#### Pregunta `P3-C4-Q1`

> **¿En qué medida se ha adoptado la Plataforma de Datos y Lakehouse (lakehouse o plataforma de datos en uso) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C4-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C4-Q2`

> **¿En qué medida se ha adoptado la Plataforma de Datos y Lakehouse (contratos de datos entre productores & consumidores) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C4-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C4-Q3`

> **¿En qué medida se ha adoptado la Plataforma de Datos y Lakehouse (catálogo y seguimiento de linaje) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C4-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C4-Q4`

> **¿En qué medida se ha adoptado la Plataforma de Datos y Lakehouse (analítica de autoservicio) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C4-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C4-Q5`

> **¿En qué medida se ha adoptado la Plataforma de Datos y Lakehouse (ingesta de streaming en tiempo real) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C4-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P3-C5: Aplicaciones agénticas

#### Pregunta `P3-C5-Q1`

> **¿En qué medida se han adoptado las Aplicaciones Agénticas (agentes con uso de herramientas en prod) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C5-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C5-Q2`

> **¿En qué medida se han adoptado las Aplicaciones Agénticas (framework de orquestación (Semantic Kernel, etc)) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C5-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C5-Q3`

> **¿En qué medida se han adoptado las Aplicaciones Agénticas (evaluación y seguridad para agentes) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C5-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C5-Q4`

> **¿En qué medida se han adoptado las Aplicaciones Agénticas (registro de tools/actions) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C5-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C5-Q5`

> **¿En qué medida se han adoptado las Aplicaciones Agénticas (controles human-in-the-loop) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C5-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C5-Q6`

> **¿En qué medida se han adoptado las Aplicaciones Agénticas (telemetría de costo y latencia de agentes) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C5-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P3-C6: Gestión de identidad y acceso

#### Pregunta `P3-C6-Q1`

> **¿En qué medida se ha adoptado la Gestión de Identidades y Accesos (SSO para todas las apps) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C6-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C6-Q2`

> **¿En qué medida se ha adoptado la Gestión de Identidades y Accesos (identidad de workload (sin secretos de larga duración)) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C6-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C6-Q3`

> **¿En qué medida se ha adoptado la Gestión de Identidades y Accesos (mínimo privilegio con elevación JIT) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C6-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C6-Q4`

> **¿En qué medida se ha adoptado la Gestión de Identidades y Accesos (políticas de acceso condicional) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C6-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C6-Q5`

> **¿En qué medida se ha adoptado la Gestión de Identidades y Accesos (revisiones de acceso y auditoría) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C6-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P3-C7: Multi-cloud y portabilidad

#### Pregunta `P3-C7-Q1`

> **¿En qué medida se ha adoptado Multi-Cloud y Portabilidad (cargas de trabajo basadas en contenedores para portabilidad) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C7-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C7-Q2`

> **¿En qué medida se ha adoptado Multi-Cloud y Portabilidad (capa de datos abstraída (Postgres, etc)) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C7-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C7-Q3`

> **¿En qué medida se ha adoptado Multi-Cloud y Portabilidad (capability de despliegue multirregión) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C7-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C7-Q4`

> **¿En qué medida se ha adoptado Multi-Cloud y Portabilidad (módulos IaC agnósticos de nube) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C7-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C7-Q5`

> **¿En qué medida se ha adoptado Multi-Cloud y Portabilidad (simulacros de recuperación ante desastres) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C7-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P3-C8: Rendimiento y escalabilidad

#### Pregunta `P3-C8-Q1`

> **¿En qué medida se ha adoptado Rendimiento y Escalabilidad (presupuestos de rendimiento por servicio) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C8-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C8-Q2`

> **¿En qué medida se ha adoptado Rendimiento y Escalabilidad (pruebas de carga/stress en CI) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C8-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C8-Q3`

> **¿En qué medida se ha adoptado Rendimiento y Escalabilidad (autoscaling basado en demanda real) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C8-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C8-Q4`

> **¿En qué medida se ha adoptado Rendimiento y Escalabilidad (profiling en producción) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C8-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C8-Q5`

> **¿En qué medida se ha adoptado Rendimiento y Escalabilidad (cadencia de planificación de capacidad) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C8-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

### P3-C9: FinOps y optimización de costos

#### Pregunta `P3-C9-Q1`

> **¿En qué medida se ha adoptado FinOps y Optimización de Costos (asignación de costos & showback) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C9-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C9-Q2`

> **¿En qué medida se ha adoptado FinOps y Optimización de Costos (uso comprometido / savings plans) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C9-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C9-Q3`

> **¿En qué medida se ha adoptado FinOps y Optimización de Costos (limpieza de recursos inactivos y no usados) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C9-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C9-Q4`

> **¿En qué medida se ha adoptado FinOps y Optimización de Costos (recomendaciones de rightsizing) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C9-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C9-Q5`

> **¿En qué medida se ha adoptado FinOps y Optimización de Costos (economía unitaria por producto) entre los equipos?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):

- Label: `Evidencia (P3-C9-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

---

## Resumen final

- **3 secciones** (1 por pilar)
- **28 capabilities** con encabezados
- **158 preguntas** (Choice) + **158 campos de evidencia** (Long Text opcional)
- **Total de elementos en Forms:** unos 324 (158 + 158 + 8 encabezados de sección y capability)

## Próximos pasos después de crear el formulario

1. Comparte el enlace con tu equipo (email, Teams, SharePoint)
2. Espera las respuestas (recomendado: al menos 3 personas encuestadas para reducir sesgos)
3. **Responses → Open in Excel** → descarga el `.xlsx`
4. Renómbralo a `forms-responses.xlsx` y colócalo en la raíz del kit
5. En Copilot Chat (modo Agent), escribe: `/import-responses`
6. La skill convierte el Excel en `responses.json` y promedia las respuestas de varias personas
7. Continúa el flujo normal: `/full-pipeline`
