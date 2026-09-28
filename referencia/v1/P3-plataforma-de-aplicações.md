# AI Maturity Assessment: Pillar P3, Application Platform

🌐 English · [Português (Brasil)](P3-plataforma-de-aplicações.pt-br.md)

> Measures platform sophistication: cloud-native architecture, APIs, AI, data, agents, identity, multi-cloud, performance, and FinOps.

## Overview

- **Pillar:** `P3`: Application Platform
- **Capabilities:** 9
- **Total questions:** 46
- **Scale:** Likert L0 to L4 (Initial → Optimizing)
- **Question language:** English (translated from the Portuguese (Brazil) source)
- **KPI/context/evidence language:** English (universal technical terms)
- **Expected response per question:** 1 selected level + evidence text (recommended minimum 80 characters) + optional attachment

## How to interpret the scale

| Level | Label | Meaning |
|---|---|---|
| **L0** | Initial | No established practice; ad-hoc actions, no tool or policy. |
| **L1** | Developing | Isolated pilots, coverage <25%, no governance. |
| **L2** | Defined | Adoption in 25-50% of teams, with guidelines and basic training. |
| **L3** | Managed | Coverage >75% with impact metrics and shared libraries/templates. |
| **L4** | Optimizing | Near-universal coverage (>95%), automation, fine-tuning, measured continuous improvement. |

## Types of information collected per question

Each question simultaneously captures **three types of data**:

1. **Quantitative (KPI):** an explicit numeric metric (e.g., % active developers, MTTR, lead time, coverage rate). Use the suggested KPI to standardize comparison across teams.

2. **Qualitative (level description):** the respondent selects the L0 to L4 level whose description best represents the reality observed today (not the aspirational one).

3. **Evidence (text + attachments):** documentary proof, such as a pipeline link, dashboard screenshot, policy, runbook, license contract, or exported metric. The more specific, the higher the evidence quality (scale: none → minimal → adequate → detailed → exemplary).

## Evidence quality criteria

- **Minimal (<80 characters):** generic text, without a tool name, metric, or link.
- **Adequate (80-250):** mentions the tool + approximate coverage/scope.
- **Detailed (250-500):** includes a numeric metric + link/attachment + measurement period.
- **Exemplary (>500 or multiple attachments):** multiple corroborating sources, time series, before/after comparison.

## Capabilities of pillar P3

- **P3-C1**: Cloud-Native Architecture (5 questions)
- **P3-C2**: API Management (5 questions)
- **P3-C3**: AI Application Development (5 questions)
- **P3-C4**: Data Platform and Lakehouse (5 questions)
- **P3-C5**: Agentic Applications (6 questions)
- **P3-C6**: Identity and Access Management (5 questions)
- **P3-C7**: Multi-Cloud and Portability (5 questions)
- **P3-C8**: Performance and Scalability (5 questions)
- **P3-C9**: FinOps and Cost Optimization (5 questions)

---

## P3-C1: Cloud-Native Architecture

**5 questions in this capability.**

### P3-C1-Q1: How mature is the adoption of cloud-native architecture?

**Metadata**

- **Target audience:** Architect, Platform Engineer, product-owner
- **Weight:** 1.0
- **Professional Edition:** Yes
- **Primary KPI:** `% workloads containerized`

**Context**

- **What it measures (what):** Measures adoption of cloud-native patterns including containerization, orchestration, and service decomposition.
- **Why it matters (why):** Cloud-native architectures enable 10x faster scaling, 99.99% availability, and 50% infrastructure cost reduction.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | Monolithic applications deployed on VMs or bare metal. No containerization. | • No container adoption<br>• VM-based deployment topology<br>• Monolithic architecture in use |
| **L1** | Developing | Some applications containerized (<30%). Docker used for development but not production. | • <30% containerized rate measured<br>• Docker in dev only<br>• No orchestration platform |
| **L2** | Defined | 50-70% of workloads containerized. Kubernetes or container orchestration in production. Basic microservice decomposition. | • 50-70% containerized rate measured<br>• K8s in production<br>• Some microservices deployed |
| **L3** | Managed | >85% workloads cloud-native. Service mesh, GitOps deployment, automated scaling. Well-defined service boundaries. | • >85% cloud-native rate measured<br>• Service mesh deployed<br>• GitOps workflow adopted<br>• Automated scaling rules configured |
| **L4** | Optimizing | Full cloud-native with AI-optimized resource allocation, predictive auto-scaling, self-healing infrastructure, and serverless where appropriate. | • AI resource optimization<br>• Predictive automated scaling enabled<br>• Self-healing infrastructure enabled<br>• Serverless platform adoption |

---

### P3-C1-Q2: To what extent has Cloud-Native Architecture (container adoption) been adopted across teams?

**Metadata**

- **Target audience:** Architect, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% workloads containerized`

**Context**

- **What it measures (what):** Workloads run as containers on Kubernetes or managed platforms.
- **Why it matters (why):** Containers enable density, portability, and declarative deploys.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No container adoption implemented. Teams operate without this capability. | • No container adoption deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of container adoption with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | container adoption adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | container adoption standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | container adoption is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C1-Q3: To what extent has Cloud-Native Architecture (service mesh / zero trust networking) been adopted across teams?

**Metadata**

- **Target audience:** Architect, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services on mesh`

**Context**

- **What it measures (what):** Service mesh handles mTLS, retries, and traffic shaping.
- **Why it matters (why):** Mesh moves reliability and security out of app code.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No service mesh / zero trust networking implemented. Teams operate without this capability. | • No service mesh / zero trust networking deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of service mesh / zero trust networking with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | service mesh / zero trust networking adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | service mesh / zero trust networking standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | service mesh / zero trust networking is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C1-Q4: To what extent has Cloud-Native Architecture (event-driven architecture) been adopted across teams?

**Metadata**

- **Target audience:** Architect, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% flows async`

**Context**

- **What it measures (what):** Events and queues decouple services for resilience and scale.
- **Why it matters (why):** EDA enables loose coupling and graceful degradation.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No event-driven architecture implemented. Teams operate without this capability. | • No event-driven architecture deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of event-driven architecture with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | event-driven architecture adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | event-driven architecture standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | event-driven architecture is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C1-Q5: To what extent has Cloud-Native Architecture (managed services preference) been adopted across teams?

**Metadata**

- **Target audience:** Architect, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% managed vs self-hosted`

**Context**

- **What it measures (what):** Prefer managed databases, queues, and caches over self-operated.
- **Why it matters (why):** Managed services shift ops burden to the cloud provider.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No managed services preference implemented. Teams operate without this capability. | • No managed services preference deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of managed services preference with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | managed services preference adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | managed services preference standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | managed services preference is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C2: API Management

**5 questions in this capability.**

### P3-C2-Q1: How mature is your API management strategy?

**Metadata**

- **Target audience:** Architect, Platform Engineer, Developer, engineering-leader, Security
- **Weight:** 1.0
- **Professional Edition:** Yes
- **Primary KPI:** `% APIs with OpenAPI spec`

**Context**

- **What it measures (what):** Measures the maturity of API design, documentation, versioning, and governance practices.
- **Why it matters (why):** Well-managed APIs reduce integration time by 70% and enable partner ecosystem growth.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No API standards. APIs designed ad-hoc. No documentation beyond source code. | • No API standards<br>• Ad-hoc API design<br>• No API documentation |
| **L1** | Developing | Some APIs have basic documentation. No versioning strategy. Inconsistent error handling. | • Basic API docs exist<br>• No versioning policy<br>• Inconsistent error formats |
| **L2** | Defined | OpenAPI specs for >50% of APIs. API design guidelines documented. Versioning strategy defined. | • >50% APIs with OpenAPI<br>• Design guidelines doc<br>• API versioning strategy documented |
| **L3** | Managed | API gateway with centralized management. >80% APIs documented. Rate limiting, auth, and monitoring standardized. API lifecycle management. | • API gateway deployed<br>• >80% documented rate measured<br>• Standardized auth/rate limiting |
| **L4** | Optimizing | AI-powered API management: auto-generated docs from code, anomaly detection on API traffic, predictive capacity planning, automated backward compatibility checks. | • Auto-generated API docs<br>• Traffic anomaly detection<br>• Predictive capacity planning<br>• Auto compatibility checks |

---

### P3-C2-Q2: To what extent has API Management (API gateway for all external APIs) been adopted across teams?

**Metadata**

- **Target audience:** Architect, Platform Engineer, Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% APIs behind gateway`

**Context**

- **What it measures (what):** Gateway handles auth, rate limiting, and observability.
- **Why it matters (why):** A gateway centralizes cross-cutting API concerns.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No api gateway for all external apis implemented. Teams operate without this capability. | • No API gateway for all external APIs deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of api gateway for all external apis with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | API gateway for all external APIs adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | API gateway for all external APIs standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | API gateway for all external APIs is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C2-Q3: To what extent has API Management (OpenAPI contracts) been adopted across teams?

**Metadata**

- **Target audience:** Architect, Platform Engineer, Developer, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% APIs with spec`

**Context**

- **What it measures (what):** Every API has a machine-readable contract.
- **Why it matters (why):** Contracts enable codegen, mock servers, and compatibility testing.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No openapi contracts implemented. Teams operate without this capability. | • No OpenAPI contracts deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of openapi contracts with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | OpenAPI contracts adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | OpenAPI contracts standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | OpenAPI contracts is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C2-Q4: To what extent has API Management (versioning & deprecation policy) been adopted across teams?

**Metadata**

- **Target audience:** Architect, Platform Engineer, Developer, Security
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `deprecated APIs retired on time`

**Context**

- **What it measures (what):** Explicit versioning and deprecation schedules.
- **Why it matters (why):** Clear policy preserves customer trust and avoids breakage.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No versioning & deprecation policy implemented. Teams operate without this capability. | • No versioning & deprecation policy deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of versioning & deprecation policy with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | versioning & deprecation policy adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | versioning & deprecation policy standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | versioning & deprecation policy is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C2-Q5: To what extent has API Management (developer portal with self-serve keys) been adopted across teams?

**Metadata**

- **Target audience:** Architect, Platform Engineer, Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `time-to-first-call`

**Context**

- **What it measures (what):** Self-service key issuance and interactive docs.
- **Why it matters (why):** Dev portals accelerate partner integration.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No developer portal with self-serve keys implemented. Teams operate without this capability. | • No developer portal with self-serve keys deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of developer portal with self-serve keys with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | developer portal with self-serve keys adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | developer portal with self-serve keys standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | developer portal with self-serve keys is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C3: AI Application Development

**5 questions in this capability.**

### P3-C3-Q1: How mature is your organization's ability to build and deploy AI-powered applications?

**Metadata**

- **Target audience:** data-ai, Developer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `# AI features in production`

**Context**

- **What it measures (what):** Measures the organization's capability to develop, deploy, and maintain AI-powered application features.
- **Why it matters (why):** Organizations with mature AI application development ship AI features 5x faster and with 3x fewer production incidents.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No AI features in production applications. No team capability for AI development. | • No AI features deployed<br>• No ML/AI engineering skills<br>• No AI development tools |
| **L1** | Developing | Experimenting with AI APIs (OpenAI, Azure AI) in 1-2 applications. No MLOps practices. | • 1-2 AI experiments<br>• Direct API integration<br>• No MLOps tooling in place |
| **L2** | Defined | 3-5 AI-powered features in production. Basic prompt engineering practices. RAG pattern for knowledge retrieval. | • 3-5 AI features live<br>• Prompt engineering guidelines<br>• RAG implementation deployed |
| **L3** | Managed | Standardized AI development framework. Model evaluation pipeline. Prompt versioning and A/B testing. >10 AI features in production. | • AI dev framework docs<br>• Model evaluation pipeline<br>• Prompt versioning workflow<br>• >10 AI features |
| **L4** | Optimizing | AI-native applications with autonomous agents, multi-model orchestration, continuous model evaluation, and automated prompt optimization. AI features are core to product. | • Autonomous agent deployments<br>• Multi-model orchestration enabled<br>• Continuous model eval<br>• Automated prompt optimization |

---

### P3-C3-Q2: To what extent has AI Application Development (LLM application frameworks) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Developer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% AI apps on framework`

**Context**

- **What it measures (what):** Teams use frameworks (LangChain, Semantic Kernel) for LLM apps.
- **Why it matters (why):** Frameworks accelerate RAG, agents, and evaluation patterns.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No llm application frameworks implemented. Teams operate without this capability. | • No LLM application frameworks deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of llm application frameworks with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | LLM application frameworks adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | LLM application frameworks standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | LLM application frameworks is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C3-Q3: To what extent has AI Application Development (evaluation harness for AI) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Developer, Architect, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `evals per release`

**Context**

- **What it measures (what):** Automated evals run on every model or prompt change.
- **Why it matters (why):** AI evals catch regressions that unit tests cannot.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No evaluation harness for ai implemented. Teams operate without this capability. | • No evaluation harness for AI deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of evaluation harness for ai with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | evaluation harness for AI adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | evaluation harness for AI standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | evaluation harness for AI is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C3-Q4: To what extent has AI Application Development (vector database / RAG platform) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Developer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `RAG apps in prod`

**Context**

- **What it measures (what):** A shared vector store/RAG platform serves multiple apps.
- **Why it matters (why):** Centralized RAG reduces duplicated work across teams.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No vector database / rag platform implemented. Teams operate without this capability. | • No vector database / RAG platform deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of vector database / rag platform with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | vector database / RAG platform adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | vector database / RAG platform standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | vector database / RAG platform is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C3-Q5: To what extent has AI Application Development (responsible AI / safety filters) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Developer, Architect, Security
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% AI apps with guardrails`

**Context**

- **What it measures (what):** All AI apps integrate content safety and audit logging.
- **Why it matters (why):** Responsible AI is table stakes; retrofitting is expensive.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No responsible ai / safety filters implemented. Teams operate without this capability. | • No responsible AI / safety filters deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of responsible ai / safety filters with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | responsible AI / safety filters adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | responsible AI / safety filters standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | responsible AI / safety filters is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C4: Data Platform and Lakehouse

**5 questions in this capability.**

### P3-C4-Q1: To what extent has Data Platform and Lakehouse (lakehouse or data platform in use) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% data in platform`

**Context**

- **What it measures (what):** A lakehouse unifies structured and unstructured data.
- **Why it matters (why):** Lakehouses combine warehouse performance with lake flexibility.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No lakehouse or data platform in use implemented. Teams operate without this capability. | • No lakehouse or data platform in use deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of lakehouse or data platform in use with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | lakehouse or data platform in use adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | lakehouse or data platform in use standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | lakehouse or data platform in use is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C4-Q2: To what extent has Data Platform and Lakehouse (data contracts between producers & consumers) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Architect, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% pipelines with contracts`

**Context**

- **What it measures (what):** Data contracts declare schema and quality guarantees.
- **Why it matters (why):** Contracts prevent silent breakage between teams.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No data contracts between producers & consumers implemented. Teams operate without this capability. | • No data contracts between producers & consumers deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of data contracts between producers & consumers with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | data contracts between producers & consumers adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | data contracts between producers & consumers standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | data contracts between producers & consumers is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C4-Q3: To what extent has Data Platform and Lakehouse (catalog and lineage tracking) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Architect, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% datasets cataloged`

**Context**

- **What it measures (what):** Every dataset has ownership, lineage, and quality metadata.
- **Why it matters (why):** Catalogs accelerate discovery and investigations.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No catalog and lineage tracking implemented. Teams operate without this capability. | • No catalog and lineage tracking deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of catalog and lineage tracking with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | catalog and lineage tracking adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | catalog and lineage tracking standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | catalog and lineage tracking is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C4-Q4: To what extent has Data Platform and Lakehouse (self-service analytics) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% decisions using data`

**Context**

- **What it measures (what):** Business users query data themselves via governed tools.
- **Why it matters (why):** Self-service shifts the bottleneck off the data team.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No self-service analytics implemented. Teams operate without this capability. | • No self-service analytics deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of self-service analytics with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | self-service analytics adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | self-service analytics standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | self-service analytics is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C4-Q5: To what extent has Data Platform and Lakehouse (real-time streaming ingestion) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% use-cases real-time`

**Context**

- **What it measures (what):** Streaming is available for time-sensitive use cases.
- **Why it matters (why):** Real-time data enables fresher AI and operational decisions.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No real-time streaming ingestion implemented. Teams operate without this capability. | • No real-time streaming ingestion deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of real-time streaming ingestion with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | real-time streaming ingestion adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | real-time streaming ingestion standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | real-time streaming ingestion is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C5: Agentic Applications

**6 questions in this capability.**

### P3-C5-Q1: To what extent has Agentic Applications (agents with tool-use in prod) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Architect, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `agents in production`

**Context**

- **What it measures (what):** Agents call tools and APIs to perform multi-step work.
- **Why it matters (why):** Agentic workflows automate complex tasks humans used to route.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No agents with tool-use in prod implemented. Teams operate without this capability. | • No agents with tool-use in prod deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of agents with tool-use in prod with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | agents with tool-use in prod adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | agents with tool-use in prod standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | agents with tool-use in prod is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q2: To what extent has Agentic Applications (orchestration framework (Semantic Kernel, etc)) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Architect, Platform Engineer, product-owner
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% agents on framework`

**Context**

- **What it measures (what):** Agents are built on a standard orchestration runtime.
- **Why it matters (why):** Standard runtimes reduce per-agent engineering cost.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No orchestration framework (semantic kernel, etc) implemented. Teams operate without this capability. | • No orchestration framework (Semantic Kernel, etc) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of orchestration framework (semantic kernel, etc) with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | orchestration framework (Semantic Kernel, etc) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | orchestration framework (Semantic Kernel, etc) standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | orchestration framework (Semantic Kernel, etc) is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q3: To what extent has Agentic Applications (evaluation and safety for agents) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Architect, Platform Engineer, product-owner
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `eval scenarios per agent`

**Context**

- **What it measures (what):** Agents are evaluated for safety, cost, and task completion.
- **Why it matters (why):** Agent evaluation is different from LLM evaluation.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No evaluation and safety for agents implemented. Teams operate without this capability. | • No evaluation and safety for agents deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of evaluation and safety for agents with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | evaluation and safety for agents adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | evaluation and safety for agents standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | evaluation and safety for agents is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q4: To what extent has Agentic Applications (tool/action registry) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Architect, Platform Engineer, Security
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `tools available to agents`

**Context**

- **What it measures (what):** A governed registry lists tools agents may call.
- **Why it matters (why):** A registry controls blast radius and enables auditing.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No tool/action registry implemented. Teams operate without this capability. | • No tool/action registry deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of tool/action registry with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | tool/action registry adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | tool/action registry standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | tool/action registry is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q5: To what extent has Agentic Applications (human-in-the-loop controls) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Architect, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% agents with HITL`

**Context**

- **What it measures (what):** High-stakes actions require human confirmation.
- **Why it matters (why):** HITL lets teams ship agents safely while learning.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No human-in-the-loop controls implemented. Teams operate without this capability. | • No human-in-the-loop controls deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of human-in-the-loop controls with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | human-in-the-loop controls adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | human-in-the-loop controls standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | human-in-the-loop controls is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q6: To what extent has Agentic Applications (agent cost and latency telemetry) been adopted across teams?

**Metadata**

- **Target audience:** data-ai, Architect, Platform Engineer, product-owner
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `p95 agent step latency`

**Context**

- **What it measures (what):** Agent performance and cost are tracked per step.
- **Why it matters (why):** Telemetry is required to run agents profitably at scale.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No agent cost and latency telemetry implemented. Teams operate without this capability. | • No agent cost and latency telemetry deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of agent cost and latency telemetry with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | agent cost and latency telemetry adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | agent cost and latency telemetry standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | agent cost and latency telemetry is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C6: Identity and Access Management

**5 questions in this capability.**

### P3-C6-Q1: To what extent has Identity and Access Management (SSO for all apps) been adopted across teams?

**Metadata**

- **Target audience:** Security, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% apps behind SSO`

**Context**

- **What it measures (what):** All apps authenticate via central SSO.
- **Why it matters (why):** SSO is the foundation of user lifecycle and revocation.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No sso for all apps implemented. Teams operate without this capability. | • No SSO for all apps deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of sso for all apps with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | SSO for all apps adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | SSO for all apps standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | SSO for all apps is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C6-Q2: To what extent has Identity and Access Management (workload identity (no long-lived secrets)) been adopted across teams?

**Metadata**

- **Target audience:** Security, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% workloads using WI`

**Context**

- **What it measures (what):** Workloads use managed identity, not static keys.
- **Why it matters (why):** Managed identities eliminate an entire class of leak.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No workload identity (no long-lived secrets) implemented. Teams operate without this capability. | • No workload identity (no long-lived secrets) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of workload identity (no long-lived secrets) with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | workload identity (no long-lived secrets) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | workload identity (no long-lived secrets) standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | workload identity (no long-lived secrets) is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C6-Q3: To what extent has Identity and Access Management (least-privilege with JIT elevation) been adopted across teams?

**Metadata**

- **Target audience:** Security, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% access through JIT`

**Context**

- **What it measures (what):** Standing admin is replaced by just-in-time elevation.
- **Why it matters (why):** JIT dramatically reduces blast radius of compromised accounts.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No least-privilege with jit elevation implemented. Teams operate without this capability. | • No least-privilege with JIT elevation deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of least-privilege with jit elevation with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | least-privilege with JIT elevation adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | least-privilege with JIT elevation standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | least-privilege with JIT elevation is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C6-Q4: To what extent has Identity and Access Management (conditional access policies) been adopted across teams?

**Metadata**

- **Target audience:** Security, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% sessions policy-evaluated`

**Context**

- **What it measures (what):** Access is granted based on device, location, and risk.
- **Why it matters (why):** Conditional access adapts security to context.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No conditional access policies implemented. Teams operate without this capability. | • No conditional access policies deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of conditional access policies with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | conditional access policies adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | conditional access policies standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | conditional access policies is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C6-Q5: To what extent has Identity and Access Management (access reviews and audit) been adopted across teams?

**Metadata**

- **Target audience:** Security, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `access reviews per year`

**Context**

- **What it measures (what):** Access is reviewed at least quarterly and logged.
- **Why it matters (why):** Reviews prevent access drift from acquisitions and reorgs.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No access reviews and audit implemented. Teams operate without this capability. | • No access reviews and audit deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of access reviews and audit with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | access reviews and audit adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | access reviews and audit standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | access reviews and audit is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C7: Multi-Cloud and Portability

**5 questions in this capability.**

### P3-C7-Q1: To what extent has Multi-Cloud and Portability (container-based workloads for portability) been adopted across teams?

**Metadata**

- **Target audience:** Architect, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% workloads portable`

**Context**

- **What it measures (what):** Workloads run in containers on any cloud.
- **Why it matters (why):** Portability is a hedge against lock-in and outages.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No container-based workloads for portability implemented. Teams operate without this capability. | • No container-based workloads for portability deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of container-based workloads for portability with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | container-based workloads for portability adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | container-based workloads for portability standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | container-based workloads for portability is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C7-Q2: To what extent has Multi-Cloud and Portability (abstracted data tier (Postgres, etc)) been adopted across teams?

**Metadata**

- **Target audience:** Architect, Platform Engineer, product-owner
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% data on portable engines`

**Context**

- **What it measures (what):** Data services use open standards (Postgres, MySQL).
- **Why it matters (why):** Open engines keep migration costs bounded.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No abstracted data tier (postgres, etc) implemented. Teams operate without this capability. | • No abstracted data tier (Postgres, etc) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of abstracted data tier (postgres, etc) with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | abstracted data tier (Postgres, etc) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | abstracted data tier (Postgres, etc) standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | abstracted data tier (Postgres, etc) is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C7-Q3: To what extent has Multi-Cloud and Portability (multi-region deployment capability) been adopted across teams?

**Metadata**

- **Target audience:** Architect, Platform Engineer, Security
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services multi-region`

**Context**

- **What it measures (what):** Services can run active-active across regions.
- **Why it matters (why):** Multi-region capability is required for DR and compliance.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No multi-region deployment capability implemented. Teams operate without this capability. | • No multi-region deployment capability deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of multi-region deployment capability with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | multi-region deployment capability adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | multi-region deployment capability standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | multi-region deployment capability is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C7-Q4: To what extent has Multi-Cloud and Portability (cloud-agnostic IaC modules) been adopted across teams?

**Metadata**

- **Target audience:** Architect, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% modules cloud-agnostic`

**Context**

- **What it measures (what):** IaC modules abstract provider specifics where sensible.
- **Why it matters (why):** Thoughtful abstraction limits porting pain.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No cloud-agnostic iac modules implemented. Teams operate without this capability. | • No cloud-agnostic IaC modules deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of cloud-agnostic iac modules with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | cloud-agnostic IaC modules adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | cloud-agnostic IaC modules standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | cloud-agnostic IaC modules is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C7-Q5: To what extent has Multi-Cloud and Portability (disaster recovery drills) been adopted across teams?

**Metadata**

- **Target audience:** Architect, Platform Engineer, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `DR drills per year`

**Context**

- **What it measures (what):** Annual DR drills validate recovery time and process.
- **Why it matters (why):** Untested DR is not DR.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No disaster recovery drills implemented. Teams operate without this capability. | • No disaster recovery drills deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of disaster recovery drills with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | disaster recovery drills adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | disaster recovery drills standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | disaster recovery drills is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C8: Performance and Scalability

**5 questions in this capability.**

### P3-C8-Q1: To what extent has Performance and Scalability (performance budgets per service) been adopted across teams?

**Metadata**

- **Target audience:** devops, Architect, product-owner
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services with perf budget`

**Context**

- **What it measures (what):** Services declare latency and throughput budgets.
- **Why it matters (why):** Budgets turn performance into a first-class requirement.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No performance budgets per service implemented. Teams operate without this capability. | • No performance budgets per service deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of performance budgets per service with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | performance budgets per service adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | performance budgets per service standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | performance budgets per service is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C8-Q2: To what extent has Performance and Scalability (load/stress testing in CI) been adopted across teams?

**Metadata**

- **Target audience:** devops, Architect, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services load-tested`

**Context**

- **What it measures (what):** Load tests run on every release candidate.
- **Why it matters (why):** Catching regressions in CI beats catching them in prod.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No load/stress testing in ci implemented. Teams operate without this capability. | • No load/stress testing in CI deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of load/stress testing in ci with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | load/stress testing in CI adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | load/stress testing in CI standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | load/stress testing in CI is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C8-Q3: To what extent has Performance and Scalability (autoscaling based on real demand) been adopted across teams?

**Metadata**

- **Target audience:** devops, Architect, product-owner
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services autoscaled`

**Context**

- **What it measures (what):** Services autoscale on CPU, latency, or queue depth.
- **Why it matters (why):** Autoscaling matches cost to demand.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No autoscaling based on real demand implemented. Teams operate without this capability. | • No autoscaling based on real demand deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of autoscaling based on real demand with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | autoscaling based on real demand adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | autoscaling based on real demand standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | autoscaling based on real demand is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C8-Q4: To what extent has Performance and Scalability (profiling in production) been adopted across teams?

**Metadata**

- **Target audience:** devops, Arquiteto
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services continuously profiled`

**Context**

- **What it measures (what):** Always-on profiling (e.g., pyroscope, parca) runs in prod.
- **Why it matters (why):** Prod profiling surfaces bottlenecks real users hit.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No profiling in production implemented. Teams operate without this capability. | • No profiling in production deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of profiling in production with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | profiling in production adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | profiling in production standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | profiling in production is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C8-Q5: To what extent has Performance and Scalability (capacity planning cadence) been adopted across teams?

**Metadata**

- **Target audience:** devops, Arquiteto
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `capacity reviews per year`

**Context**

- **What it measures (what):** Capacity is reviewed with growth projections.
- **Why it matters (why):** Planning prevents painful migrations at peak load.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No capacity planning cadence implemented. Teams operate without this capability. | • No capacity planning cadence deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of capacity planning cadence with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | capacity planning cadence adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | capacity planning cadence standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | capacity planning cadence is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C9: FinOps and Cost Optimization

**5 questions in this capability.**

### P3-C9-Q1: To what extent has FinOps and Cost Optimization (cost allocation & showback) been adopted across teams?

**Metadata**

- **Target audience:** product-owner, engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% cost tagged to team`

**Context**

- **What it measures (what):** Every resource is tagged and attributed to a team.
- **Why it matters (why):** Showback creates ownership for cost.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No cost allocation & showback implemented. Teams operate without this capability. | • No cost allocation & showback deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of cost allocation & showback with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | cost allocation & showback adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | cost allocation & showback standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | cost allocation & showback is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C9-Q2: To what extent has FinOps and Cost Optimization (committed use / savings plans) been adopted across teams?

**Metadata**

- **Target audience:** product-owner, engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% eligible spend committed`

**Context**

- **What it measures (what):** Commit spend is used where usage is predictable.
- **Why it matters (why):** Commitments cut spend 20-50% at minimal risk.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No committed use / savings plans implemented. Teams operate without this capability. | • No committed use / savings plans deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of committed use / savings plans with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | committed use / savings plans adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | committed use / savings plans standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | committed use / savings plans is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C9-Q3: To what extent has FinOps and Cost Optimization (idle and unused resource cleanup) been adopted across teams?

**Metadata**

- **Target audience:** product-owner, engineering-leader, Platform Engineer, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `$/month saved by cleanup`

**Context**

- **What it measures (what):** Automation flags and removes idle resources.
- **Why it matters (why):** Cleanup is the highest-leverage FinOps activity.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No idle and unused resource cleanup implemented. Teams operate without this capability. | • No idle and unused resource cleanup deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of idle and unused resource cleanup with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | idle and unused resource cleanup adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | idle and unused resource cleanup standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | idle and unused resource cleanup is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C9-Q4: To what extent has FinOps and Cost Optimization (rightsizing recommendations) been adopted across teams?

**Metadata**

- **Target audience:** product-owner, engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% rightsizing applied`

**Context**

- **What it measures (what):** Automated recommendations drive continuous rightsizing.
- **Why it matters (why):** Rightsizing closes the gap between provisioned and needed.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No rightsizing recommendations implemented. Teams operate without this capability. | • No rightsizing recommendations deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of rightsizing recommendations with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | rightsizing recommendations adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | rightsizing recommendations standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | rightsizing recommendations is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C9-Q5: To what extent has FinOps and Cost Optimization (unit economics per product) been adopted across teams?

**Metadata**

- **Target audience:** product-owner, engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% products with $/user`

**Context**

- **What it measures (what):** Products track cost per user, request, or transaction.
- **Why it matters (why):** Unit economics align engineering and business decisions.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No unit economics per product implemented. Teams operate without this capability. | • No unit economics per product deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of unit economics per product with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | unit economics per product adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | unit economics per product standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | unit economics per product is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---


## How this section is scored

- Each question receives a numeric value from the selected level: L0=0, L1=1, L2=2, L3=3, L4=4.
- The capability score is the weighted average of its questions (default weight = 1.0; questions with weight 1.5 or 2.0 count more).
- The **P3** pillar score is the average of the 9 capabilities.
- The result is shown on a 0 to 4 scale and converted to a maturity % (level / 4 × 100).

## Quick glossary

- **Pillar:** strategic maturity dimension.
- **Capability:** functional subdomain within a pillar.
- **Question:** concrete assessment item, standard ID `P[1-3]-C[1-19]-Q[1-99]`.
- **Level (L0-L4):** point on the Likert maturity scale.
- **KPI:** key indicator that objectively validates the declared level.
- **Evidence:** qualitative (text) or quantitative (attachment) proof that supports the response.
