# Preguntas para Microsoft Forms — AI Maturity Assessment

> Este documento contiene **LAS 158 preguntas** para crear el assessment en Microsoft Forms.
> Usa copy/paste sección por sección. Cada pregunta debe incluir:
> - **Tipo:** Choice (respuesta única) con las 6 opciones fijas y un campo Long Text para evidencia.

## Cómo Usar Este Documento

> [!IMPORTANT]
> Edición localizada runtime-safe: etiquetas de secciones/instrucciones en Español y todos los IDs preservados.
> Para mantener paridad estricta de scoring y auditoría, el wording canónico del assessment se conserva donde sea necesario.


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

- **L0 — Inicial — Sin práctica establecida**
- **L1 — En Desarrollo — Pilotos aislados (<25%)**
- **L2 — Definido — Cobertura 25-50% con directrices**
- **L3 — Gestionado — >75% con métricas de impacto**
- **L4 — Optimizando — Universal (>95%) con automatización continua**
- **NA — No sé / No aplica**

> ⚠️ **Importante:** mantén los prefijos `L0`, `L1`, ..., `L4`, `NA` al inicio de cada opción. La importación usa esos prefijos para mapear respuestas a valores numéricos (0-4 o null).

---

## Sección: Pillar P1 — Produtividade do Desenvolvedor

_Esta sección tiene 53 preguntas en 9 capabilities._

### P1-C1 — Assistentes de Codificação IA

#### Pregunta `P1-C1-Q1`

> **Em que medida sua organização utiliza ferramentas de completação de código com IA (ex. GitHub Copilot)?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C1-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C1-Q2`

> **Quão efetivamente sua equipe aproveita IA para revisão de código e melhoria de qualidade?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C1-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C1-Q3`

> **Como sua organização mede e rastreia o impacto das ferramentas de codificação IA na produtividade?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C1-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C1-Q4`

> **Qual nível de capacidades de testes assistidos por IA sua organização emprega?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C1-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C1-Q5`

> **Como sua organização governa o código gerado por IA em termos de segurança e conformidade?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C1-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P1-C2 — Plataforma de Experiência do Desenvolvedor

#### Pregunta `P1-C2-Q1`

> **Quão maduro é seu portal ou plataforma interna para desenvolvedores?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C2-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C2-Q2`

> **Quão efetivamente suas equipes usam ambientes de desenvolvimento padronizados?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C2-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C2-Q3`

> **Em que medida Plataforma de Experiência do Desenvolvedor (self-service IDP) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C2-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C2-Q4`

> **Em que medida Plataforma de Experiência do Desenvolvedor (golden paths and templates) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C2-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C2-Q5`

> **Em que medida Plataforma de Experiência do Desenvolvedor (developer portal) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C2-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C2-Q6`

> **Em que medida Plataforma de Experiência do Desenvolvedor (paved road policy enforcement) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C2-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P1-C3 — Gestão do Conhecimento

#### Pregunta `P1-C3-Q1`

> **Quão efetivamente sua organização captura e compartilha conhecimento de desenvolvimento?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C3-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C3-Q2`

> **Em que medida Gestão do Conhecimento (semantic code search) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C3-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C3-Q3`

> **Em que medida Gestão do Conhecimento (RAG-based docs assistant) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C3-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C3-Q4`

> **Em que medida Gestão do Conhecimento (runbook and playbook coverage) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C3-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C3-Q5`

> **Em que medida Gestão do Conhecimento (ADR (architecture decision records)) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C3-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C3-Q6`

> **Em que medida Gestão do Conhecimento (learning content & curated paths) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C3-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P1-C4 — Automação de Revisão de Código

#### Pregunta `P1-C4-Q1`

> **Em que medida Automação de Revisão de Código (AI reviewer bot on every PR) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C4-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C4-Q2`

> **Em que medida Automação de Revisão de Código (static linting and style auto-fix) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C4-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C4-Q3`

> **Em que medida Automação de Revisão de Código (automated security review) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C4-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C4-Q4`

> **Em que medida Automação de Revisão de Código (required-reviewer rules) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C4-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C4-Q5`

> **Em que medida Automação de Revisão de Código (review SLA tracking) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C4-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C4-Q6`

> **Em que medida Automação de Revisão de Código (change size enforcement) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C4-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C4-Q7`

> **Em que medida Automação de Revisão de Código (reviewer load balancing) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C4-Q7)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P1-C5 — Onboarding e Treinamento de Desenvolvedores

#### Pregunta `P1-C5-Q1`

> **Em que medida Onboarding e Treinamento de Desenvolvedores (codespaces/dev containers for instant env) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C5-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C5-Q2`

> **Em que medida Onboarding e Treinamento de Desenvolvedores (structured onboarding playbook) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C5-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C5-Q3`

> **Em que medida Onboarding e Treinamento de Desenvolvedores (mentor pairing program) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C5-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C5-Q4`

> **Em que medida Onboarding e Treinamento de Desenvolvedores (hands-on curriculum & kata) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C5-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C5-Q5`

> **Em que medida Onboarding e Treinamento de Desenvolvedores (shadow on-call rotation) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C5-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C5-Q6`

> **Em que medida Onboarding e Treinamento de Desenvolvedores (onboarding feedback loop) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C5-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C5-Q7`

> **Em que medida Onboarding e Treinamento de Desenvolvedores (ramp-time measurement) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C5-Q7)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P1-C6 — Inner Source e Colaboração

#### Pregunta `P1-C6-Q1`

> **Em que medida Inner Source e Colaboração (internal repos with open contribution) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C6-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C6-Q2`

> **Em que medida Inner Source e Colaboração (CONTRIBUTING.md standards) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C6-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C6-Q3`

> **Em que medida Inner Source e Colaboração (inner-source discovery portal) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C6-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C6-Q4`

> **Em que medida Inner Source e Colaboração (good-first-issue labeling) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C6-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C6-Q5`

> **Em que medida Inner Source e Colaboração (cross-team design reviews) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C6-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C6-Q6`

> **Em que medida Inner Source e Colaboração (community of practice) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C6-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P1-C7 — Automação de Documentação

#### Pregunta `P1-C7-Q1`

> **Em que medida Automação de Documentação (docs-as-code in Git) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C7-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C7-Q2`

> **Em que medida Automação de Documentação (auto-generated API reference) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C7-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C7-Q3`

> **Em que medida Automação de Documentação (AI-assisted doc drafting) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C7-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C7-Q4`

> **Em que medida Automação de Documentação (doc quality linting) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C7-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C7-Q5`

> **Em que medida Automação de Documentação (docs analytics) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C7-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P1-C8 — Medição de Produtividade do Desenvolvedor

#### Pregunta `P1-C8-Q1`

> **Em que medida Medição de Produtividade do Desenvolvedor (DORA four key metrics) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C8-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C8-Q2`

> **Em que medida Medição de Produtividade do Desenvolvedor (developer experience surveys) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C8-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C8-Q3`

> **Em que medida Medição de Produtividade do Desenvolvedor (build/test feedback loop time) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C8-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C8-Q4`

> **Em que medida Medição de Produtividade do Desenvolvedor (SPACE framework adoption) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C8-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C8-Q5`

> **Em que medida Medição de Produtividade do Desenvolvedor (flow vs friction dashboards) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C8-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C8-Q6`

> **Em que medida Medição de Produtividade do Desenvolvedor (quarterly productivity OKRs) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C8-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P1-C9 — Automação de Ambientes e Espaços de Trabalho

#### Pregunta `P1-C9-Q1`

> **Em que medida Automação de Ambientes e Espaços de Trabalho (reproducible local envs (devcontainers)) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C9-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C9-Q2`

> **Em que medida Automação de Ambientes e Espaços de Trabalho (cloud workspaces (Codespaces/Gitpod)) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C9-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C9-Q3`

> **Em que medida Automação de Ambientes e Espaços de Trabalho (tool and SDK version pinning) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C9-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C9-Q4`

> **Em que medida Automação de Ambientes e Espaços de Trabalho (on-demand test data) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C9-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P1-C9-Q5`

> **Em que medida Automação de Ambientes e Espaços de Trabalho (workspace telemetry & health) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P1-C9-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


---

## Sección: Pillar P2 — Ciclo de Vida DevOps

_Esta sección tiene 59 preguntas en 10 capabilities._

### P2-C1 — Inteligência de Pipeline CI/CD

#### Pregunta `P2-C1-Q1`

> **Quão maduro é seu pipeline CI/CD em termos de automação e integração de IA?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C1-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C1-Q2`

> **Em que medida Inteligência de Pipeline CI/CD (pipeline-as-code everywhere) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C1-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C1-Q3`

> **Em que medida Inteligência de Pipeline CI/CD (build caching and artifact reuse) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C1-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C1-Q4`

> **Em que medida Inteligência de Pipeline CI/CD (trunk-based development) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C1-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C1-Q5`

> **Em que medida Inteligência de Pipeline CI/CD (deployment frequency) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C1-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C1-Q6`

> **Em que medida Inteligência de Pipeline CI/CD (feature flags for progressive delivery) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C1-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P2-C2 — Infraestrutura como Código

#### Pregunta `P2-C2-Q1`

> **Qual porcentagem de sua infraestrutura é gerenciada por código?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C2-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C2-Q2`

> **Em que medida Infraestrutura como Código (Terraform/Bicep-based IaC) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C2-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C2-Q3`

> **Em que medida Infraestrutura como Código (module and pattern library) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C2-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C2-Q4`

> **Em que medida Infraestrutura como Código (GitOps for config drift) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C2-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C2-Q5`

> **Em que medida Infraestrutura como Código (policy-as-code (OPA/Conftest)) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C2-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C2-Q6`

> **Em que medida Infraestrutura como Código (ephemeral environment per PR) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C2-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P2-C3 — Observabilidade e Monitoramento

#### Pregunta `P2-C3-Q1`

> **Quão abrangente é sua stack de observabilidade (logs, métricas, traces)?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C3-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C3-Q2`

> **Em que medida Observabilidade e Monitoramento (structured logging w/ correlation IDs) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C3-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C3-Q3`

> **Em que medida Observabilidade e Monitoramento (distributed tracing (OpenTelemetry)) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C3-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C3-Q4`

> **Em que medida Observabilidade e Monitoramento (SLOs and error budgets) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C3-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C3-Q5`

> **Em que medida Observabilidade e Monitoramento (synthetic monitoring) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C3-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C3-Q6`

> **Em que medida Observabilidade e Monitoramento (anomaly detection with ML) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C3-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P2-C4 — Integração de Segurança (DevSecOps)

#### Pregunta `P2-C4-Q1`

> **Quão integrada está a segurança no seu pipeline de desenvolvimento e implantação?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C4-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C4-Q2`

> **Em que medida Integração de Segurança (DevSecOps) (SAST in every pipeline) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C4-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C4-Q3`

> **Em que medida Integração de Segurança (DevSecOps) (SCA and dependency review) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C4-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C4-Q4`

> **Em que medida Integração de Segurança (DevSecOps) (secret scanning and push protection) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C4-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C4-Q5`

> **Em que medida Integração de Segurança (DevSecOps) (DAST and API security testing) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C4-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C4-Q6`

> **Em que medida Integração de Segurança (DevSecOps) (security champions program) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C4-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P2-C5 — Estratégias de Release e Implantação

#### Pregunta `P2-C5-Q1`

> **Em que medida Estratégias de Release e Implantação (blue/green or canary deploys) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C5-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C5-Q2`

> **Em que medida Estratégias de Release e Implantação (automated rollback) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C5-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C5-Q3`

> **Em que medida Estratégias de Release e Implantação (feature flag platform) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C5-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C5-Q4`

> **Em que medida Estratégias de Release e Implantação (release coordination via ChatOps) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C5-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C5-Q5`

> **Em que medida Estratégias de Release e Implantação (progressive delivery across regions) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C5-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C5-Q6`

> **Em que medida Estratégias de Release e Implantação (release metrics dashboard) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C5-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P2-C6 — Automação de Testes

#### Pregunta `P2-C6-Q1`

> **Em que medida Automação de Testes (unit test coverage targets) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C6-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C6-Q2`

> **Em que medida Automação de Testes (integration test suites) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C6-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C6-Q3`

> **Em que medida Automação de Testes (end-to-end / journey tests) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C6-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C6-Q4`

> **Em que medida Automação de Testes (contract testing) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C6-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C6-Q5`

> **Em que medida Automação de Testes (AI-assisted test generation) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C6-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C6-Q6`

> **Em que medida Automação de Testes (flaky-test detection & quarantine) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C6-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C6-Q7`

> **Em que medida Automação de Testes (mutation testing) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C6-Q7)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P2-C7 — Gestão de Incidentes e SRE

#### Pregunta `P2-C7-Q1`

> **Em que medida Gestão de Incidentes e SRE (on-call rotation with tooling) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C7-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C7-Q2`

> **Em que medida Gestão de Incidentes e SRE (blameless postmortems) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C7-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C7-Q3`

> **Em que medida Gestão de Incidentes e SRE (error budget policy) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C7-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C7-Q4`

> **Em que medida Gestão de Incidentes e SRE (chaos engineering) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C7-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C7-Q5`

> **Em que medida Gestão de Incidentes e SRE (incident commander role) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C7-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C7-Q6`

> **Em que medida Gestão de Incidentes e SRE (SRE-dev partnership model) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C7-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C7-Q7`

> **Em que medida Gestão de Incidentes e SRE (runbook automation) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C7-Q7)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P2-C8 — Gestão de Artefatos e Pacotes

#### Pregunta `P2-C8-Q1`

> **Em que medida Gestão de Artefatos e Pacotes (internal package registry) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C8-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C8-Q2`

> **Em que medida Gestão de Artefatos e Pacotes (SBOM for every build) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C8-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C8-Q3`

> **Em que medida Gestão de Artefatos e Pacotes (artifact signing (SLSA)) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C8-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C8-Q4`

> **Em que medida Gestão de Artefatos e Pacotes (vulnerability scanning of artifacts) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C8-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C8-Q5`

> **Em que medida Gestão de Artefatos e Pacotes (retention & promotion policies) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C8-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P2-C9 — Gestão de Mudanças e GitOps

#### Pregunta `P2-C9-Q1`

> **Em que medida Gestão de Mudanças e GitOps (GitOps controllers in prod) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C9-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C9-Q2`

> **Em que medida Gestão de Mudanças e GitOps (automated change tickets) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C9-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C9-Q3`

> **Em que medida Gestão de Mudanças e GitOps (approvals in PR (not tickets)) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C9-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C9-Q4`

> **Em que medida Gestão de Mudanças e GitOps (environment promotion via PR) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C9-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C9-Q5`

> **Em que medida Gestão de Mudanças e GitOps (compliance evidence auto-collected) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C9-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P2-C10 — Segurança de Dependências e Cadeia de Suprimentos

#### Pregunta `P2-C10-Q1`

> **Em que medida Segurança de Dependências e Cadeia de Suprimentos (dependabot or renovate on every repo) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C10-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C10-Q2`

> **Em que medida Segurança de Dependências e Cadeia de Suprimentos (allow-list registries only) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C10-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C10-Q3`

> **Em que medida Segurança de Dependências e Cadeia de Suprimentos (build provenance (SLSA level)) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C10-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C10-Q4`

> **Em que medida Segurança de Dependências e Cadeia de Suprimentos (critical dep response playbook) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C10-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P2-C10-Q5`

> **Em que medida Segurança de Dependências e Cadeia de Suprimentos (vendor/OSS risk reviews) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P2-C10-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


---

## Sección: Pillar P3 — Plataforma de Aplicações

_Esta sección tiene 46 preguntas en 9 capabilities._

### P3-C1 — Arquitetura Cloud-Native

#### Pregunta `P3-C1-Q1`

> **Qual é a maturidade da adoção de arquitetura cloud-native?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C1-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C1-Q2`

> **Em que medida Arquitetura Nativa da Nuvem (container adoption) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C1-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C1-Q3`

> **Em que medida Arquitetura Nativa da Nuvem (service mesh / zero trust networking) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C1-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C1-Q4`

> **Em que medida Arquitetura Nativa da Nuvem (event-driven architecture) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C1-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C1-Q5`

> **Em que medida Arquitetura Nativa da Nuvem (managed services preference) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C1-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P3-C2 — Gestão de APIs

#### Pregunta `P3-C2-Q1`

> **Quão madura é sua estratégia de gestão de APIs?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C2-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C2-Q2`

> **Em que medida Gestão de APIs (API gateway for all external APIs) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C2-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C2-Q3`

> **Em que medida Gestão de APIs (OpenAPI contracts) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C2-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C2-Q4`

> **Em que medida Gestão de APIs (versioning & deprecation policy) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C2-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C2-Q5`

> **Em que medida Gestão de APIs (developer portal with self-serve keys) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C2-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P3-C3 — Desenvolvimento de Aplicações IA

#### Pregunta `P3-C3-Q1`

> **Quão madura é a capacidade da sua organização de construir e implantar aplicações com IA?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C3-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C3-Q2`

> **Em que medida Desenvolvimento de Aplicações de IA (LLM application frameworks) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C3-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C3-Q3`

> **Em que medida Desenvolvimento de Aplicações de IA (evaluation harness for AI) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C3-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C3-Q4`

> **Em que medida Desenvolvimento de Aplicações de IA (vector database / RAG platform) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C3-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C3-Q5`

> **Em que medida Desenvolvimento de Aplicações de IA (responsible AI / safety filters) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C3-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P3-C4 — Plataforma de Dados e Lakehouse

#### Pregunta `P3-C4-Q1`

> **Em que medida Plataforma de Dados e Lakehouse (lakehouse or data platform in use) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C4-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C4-Q2`

> **Em que medida Plataforma de Dados e Lakehouse (data contracts between producers & consumers) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C4-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C4-Q3`

> **Em que medida Plataforma de Dados e Lakehouse (catalog and lineage tracking) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C4-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C4-Q4`

> **Em que medida Plataforma de Dados e Lakehouse (self-service analytics) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C4-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C4-Q5`

> **Em que medida Plataforma de Dados e Lakehouse (real-time streaming ingestion) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C4-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P3-C5 — Aplicações Agênticas

#### Pregunta `P3-C5-Q1`

> **Em que medida Aplicações Agênticas (agents with tool-use in prod) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C5-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C5-Q2`

> **Em que medida Aplicações Agênticas (orchestration framework (Semantic Kernel, etc)) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C5-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C5-Q3`

> **Em que medida Aplicações Agênticas (evaluation and safety for agents) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C5-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C5-Q4`

> **Em que medida Aplicações Agênticas (tool/action registry) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C5-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C5-Q5`

> **Em que medida Aplicações Agênticas (human-in-the-loop controls) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C5-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C5-Q6`

> **Em que medida Aplicações Agênticas (agent cost and latency telemetry) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C5-Q6)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P3-C6 — Gestão de Identidades e Acessos

#### Pregunta `P3-C6-Q1`

> **Em que medida Gestão de Identidades e Acessos (SSO for all apps) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C6-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C6-Q2`

> **Em que medida Gestão de Identidades e Acessos (workload identity (no long-lived secrets)) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C6-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C6-Q3`

> **Em que medida Gestão de Identidades e Acessos (least-privilege with JIT elevation) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C6-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C6-Q4`

> **Em que medida Gestão de Identidades e Acessos (conditional access policies) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C6-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C6-Q5`

> **Em que medida Gestão de Identidades e Acessos (access reviews and audit) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C6-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P3-C7 — Multi-Cloud e Portabilidade

#### Pregunta `P3-C7-Q1`

> **Em que medida Multi-Cloud e Portabilidade (container-based workloads for portability) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C7-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C7-Q2`

> **Em que medida Multi-Cloud e Portabilidade (abstracted data tier (Postgres, etc)) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C7-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C7-Q3`

> **Em que medida Multi-Cloud e Portabilidade (multi-region deployment capability) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C7-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C7-Q4`

> **Em que medida Multi-Cloud e Portabilidade (cloud-agnostic IaC modules) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C7-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C7-Q5`

> **Em que medida Multi-Cloud e Portabilidade (disaster recovery drills) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C7-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P3-C8 — Desempenho e Escalabilidade

#### Pregunta `P3-C8-Q1`

> **Em que medida Desempenho e Escalabilidade (performance budgets per service) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C8-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C8-Q2`

> **Em que medida Desempenho e Escalabilidade (load/stress testing in CI) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C8-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C8-Q3`

> **Em que medida Desempenho e Escalabilidade (autoscaling based on real demand) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C8-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C8-Q4`

> **Em que medida Desempenho e Escalabilidade (profiling in production) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C8-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C8-Q5`

> **Em que medida Desempenho e Escalabilidade (capacity planning cadence) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C8-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


### P3-C9 — FinOps e Otimização de Custos

#### Pregunta `P3-C9-Q1`

> **Em que medida FinOps e Otimização de Custos (cost allocation & showback) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C9-Q1)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C9-Q2`

> **Em que medida FinOps e Otimização de Custos (committed use / savings plans) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C9-Q2)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C9-Q3`

> **Em que medida FinOps e Otimização de Custos (idle and unused resource cleanup) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C9-Q3)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C9-Q4`

> **Em que medida FinOps e Otimização de Custos (rightsizing recommendations) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C9-Q4)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`

#### Pregunta `P3-C9-Q5`

> **Em que medida FinOps e Otimização de Custos (unit economics per product) foi adotado entre as equipes?**

_Tipo: Choice (single answer). Opciones: usa las 6 opciones fijas listadas arriba._

**Campo de texto después de esta pregunta** (Long Text, opcional):
- Label: `Evidencia (P3-C9-Q5)`
- Placeholder: `Describe herramienta, % de cobertura, métrica y período`


---

## Resumo final

- **3 seções** (1 por pillar)
- **28 capabilities** com headers
- **158 perguntas** (Choice) + **158 campos de evidência** (Long Text opcional)
- **Total de elementos no Forms:** ~324 (158 + 158 + 8 headers de seção/capability)

## Próximos passos após criar o Forms

1. Compartilhe o link com sua equipe (via email, Teams, SharePoint)
2. Aguarde respostas (recomendado: ≥ 3 respondentes para reduzir viés)
3. **Responses → Open in Excel** → baixar `.xlsx`
4. Renomear para `respostas-forms.xlsx` e colocar na raiz do `kit-cliente/`
5. No Copilot Chat (modo Agent), digitar: `/importar-respostas-excel`
6. A skill converterá o Excel em `respostas.json` agregando múltiplos respondentes (média)
7. Continuar fluxo normal: `/pipeline-completo`
