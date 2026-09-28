# AI Maturity Assessment (Pillar P2: DevOps Lifecycle)

🌐 English · [Português (Brasil)](P2-ciclo-de-vida-devops.pt-br.md)

> Measures the maturity of pipelines, infrastructure as code, observability, DevSecOps, releases, testing, incidents, and supply chain security.

## Overview

- **Pillar:** `P2` (DevOps Lifecycle)
- **Capabilities:** 10
- **Total questions:** 59
- **Scale:** Likert L0-L4 (Initial → Optimizing)
- **Question language:** Portuguese (Brazil) in `framework.json` (translated to English in this reference)
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

2. **Qualitative (level description):** the respondent selects the L0-L4 level whose description best represents the reality observed today (not the aspirational one).

3. **Evidence (text + attachments):** documentary proof, such as a pipeline link, dashboard screenshot, policy, runbook, license contract, or exported metric. The more specific, the higher the evidence quality (scale: none → minimal → adequate → detailed → exemplary).

## Evidence quality criteria

- **Minimal (<80 characters):** generic text, with no tool name, metric, or link.
- **Adequate (80-250):** mentions the tool + approximate coverage/scope.
- **Detailed (250-500):** includes a numeric metric + link/attachment + measurement period.
- **Exemplary (>500 or multiple attachments):** multiple corroborating sources, time series, before/after comparison.

## P2 pillar capabilities

- **P2-C1**: CI/CD Pipeline Intelligence (6 questions)
- **P2-C2**: Infrastructure as Code (6 questions)
- **P2-C3**: Observability and Monitoring (6 questions)
- **P2-C4**: Security Integration (DevSecOps) (6 questions)
- **P2-C5**: Release and Deployment Strategies (6 questions)
- **P2-C6**: Test Automation (7 questions)
- **P2-C7**: Incident Management and SRE (7 questions)
- **P2-C8**: Artifact and Package Management (5 questions)
- **P2-C9**: Change Management and GitOps (5 questions)
- **P2-C10**: Dependency and Supply Chain Security (5 questions)

---

## P2-C1: CI/CD Pipeline Intelligence

**6 questions in this capability.**

### P2-C1-Q1: How mature is your CI/CD pipeline in terms of automation and AI integration?

**Metadata**

- **Target audience:** devops, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** Yes
- **Primary KPI:** `Deployment frequency per week`

**Context**

- **What it measures (what):** Measures the automation level and intelligence of CI/CD pipelines.
- **Why it matters (why):** Mature CI/CD pipelines enable teams to deploy 200x more frequently with 3x lower change failure rate (DORA research).

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | Manual builds and deployments. No CI/CD pipeline. Deployments happen weekly or less frequently. | • No CI/CD pipeline<br>• Manual build process<br>• Weekly or less deployments |
| **L1** | Developing | Basic CI pipeline with automated builds and unit tests. Manual deployment process. Deployment frequency: weekly. | • CI pipeline configured<br>• Automated unit tests<br>• Manual deployments weekly |
| **L2** | Defined | Full CI/CD pipeline with automated testing, staging deployment, and manual production promotion. Deployment frequency: daily. | • Automated staging deployment<br>• Manual prod promotion<br>• Daily production deployments cadence |
| **L3** | Managed | Intelligent CI/CD: auto-scaling test suites, smart test selection (run only affected tests), canary deployments. Multiple deployments per day. | • Smart test selection<br>• Canary deployment config<br>• Multiple daily deployments<br>• Test impact analysis |
| **L4** | Optimizing | AI-optimized pipeline: predictive build failures, auto-remediation of flaky tests, ML-driven canary analysis, self-healing deployments. | • Predictive failure model<br>• Automated remediation scripts deployed<br>• ML canary analysis<br>• Self-healing deployment docs |

---

### P2-C1-Q2: To what extent has CI/CD Pipeline Intelligence (pipeline-as-code everywhere) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer, Security, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% pipelines as code`

**Context**

- **What it measures (what):** All pipelines live next to code as versioned YAML/HCL.
- **Why it matters (why):** Pipeline-as-code is auditable, reviewable, and reproducible.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No pipeline-as-code everywhere implemented. Teams operate without this capability. | • No pipeline-as-code everywhere deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of pipeline-as-code everywhere with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | pipeline-as-code everywhere adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | pipeline-as-code everywhere standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | pipeline-as-code everywhere is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C1-Q3: To what extent has CI/CD Pipeline Intelligence (build caching and artifact reuse) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer, product-owner
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% cache hit ratio`

**Context**

- **What it measures (what):** Remote build caches and content-addressed artifacts reduce build time.
- **Why it matters (why):** Caching cuts CI time by 40-70% and reduces cloud spend.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No build caching and artifact reuse implemented. Teams operate without this capability. | • No build caching and artifact reuse deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of build caching and artifact reuse with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | build caching and artifact reuse adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | build caching and artifact reuse standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | build caching and artifact reuse is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C1-Q4: To what extent has CI/CD Pipeline Intelligence (trunk-based development) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `branches >7 days old`

**Context**

- **What it measures (what):** Short-lived branches merged to trunk multiple times a day.
- **Why it matters (why):** Trunk-based dev reduces merge hell and enables continuous delivery.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No trunk-based development implemented. Teams operate without this capability. | • No trunk-based development deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of trunk-based development with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | trunk-based development adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | trunk-based development standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | trunk-based development is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C1-Q5: To what extent has CI/CD Pipeline Intelligence (deployment frequency) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `deploys per day`

**Context**

- **What it measures (what):** Elite DORA teams deploy many times per day to production.
- **Why it matters (why):** High deploy frequency correlates with low change fail rate.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No deployment frequency implemented. Teams operate without this capability. | • No deployment frequency deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of deployment frequency with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | deployment frequency adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | deployment frequency standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | deployment frequency is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C1-Q6: To what extent has CI/CD Pipeline Intelligence (feature flags for progressive delivery) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `flags used per release`

**Context**

- **What it measures (what):** Feature flags decouple deployment from release.
- **Why it matters (why):** Flags enable dark launches, canary rollouts, and fast rollback.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No feature flags for progressive delivery implemented. Teams operate without this capability. | • No feature flags for progressive delivery deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of feature flags for progressive delivery with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | feature flags for progressive delivery adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | feature flags for progressive delivery standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | feature flags for progressive delivery is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C2: Infrastructure as Code

**6 questions in this capability.**

### P2-C2-Q1: What percentage of your infrastructure is managed as code?

**Metadata**

- **Target audience:** devops, Platform Engineer, Security, qa-test
- **Weight:** 1.0
- **Professional Edition:** Yes
- **Primary KPI:** `% infrastructure as code`

**Context**

- **What it measures (what):** Measures the extent to which infrastructure provisioning and management is codified and version-controlled.
- **Why it matters (why):** IaC reduces provisioning errors by 90% and enables infrastructure changes to be reviewed, tested, and audited like application code.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | All infrastructure provisioned manually via cloud console or CLI commands. No version control for infra. | • Manual provisioning only<br>• No IaC files in repos<br>• Console-based management workflow |
| **L1** | Developing | Some infrastructure defined in code (<30%). Mix of manual and automated provisioning. Scripts not version controlled consistently. | • <30% IaC coverage<br>• Mixed manual and automated processes<br>• Inconsistent version control |
| **L2** | Defined | 50-75% of infrastructure defined in code. IaC modules for common patterns. PR-based review for infra changes. | • 50-75% IaC coverage<br>• Reusable IaC modules<br>• PR-based infra review |
| **L3** | Managed | >90% of infrastructure as code. Drift detection enabled. Policy-as-code enforcement. Self-service provisioning via templates. | • >90% IaC coverage<br>• Drift detection reports<br>• Policy-as-code rules enforced<br>• Self-service templates published |
| **L4** | Optimizing | 100% IaC with AI-generated infrastructure recommendations. Auto-remediation of drift. Cost optimization suggestions. Predictive scaling. | • 100% IaC coverage<br>• AI infra recommendations<br>• Automated drift remediation enabled<br>• Predictive scaling config |

---

### P2-C2-Q2: To what extent has Infrastructure as Code (Terraform/Bicep-based IaC) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% infra as code`

**Context**

- **What it measures (what):** All long-lived infra is declared as code.
- **Why it matters (why):** IaC eliminates snowflake servers and enables reproducible environments.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No terraform/bicep-based iac implemented. Teams operate without this capability. | • No Terraform/Bicep-based IaC deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of terraform/bicep-based iac with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Terraform/Bicep-based IaC adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Terraform/Bicep-based IaC standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Terraform/Bicep-based IaC is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C2-Q3: To what extent has Infrastructure as Code (module and pattern library) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer, Arquiteto
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% resources via modules`

**Context**

- **What it measures (what):** A shared module library encodes opinionated security and networking.
- **Why it matters (why):** Modules enforce standards and reduce per-team cognitive load.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No module and pattern library implemented. Teams operate without this capability. | • No module and pattern library deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of module and pattern library with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | module and pattern library adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | module and pattern library standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | module and pattern library is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C2-Q4: To what extent has Infrastructure as Code (GitOps for config drift) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% envs drift-detected`

**Context**

- **What it measures (what):** GitOps controllers reconcile cluster and cloud state to Git.
- **Why it matters (why):** GitOps eliminates drift and makes Git the single source of truth.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No gitops for config drift implemented. Teams operate without this capability. | • No GitOps for config drift deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of gitops for config drift with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | GitOps for config drift adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | GitOps for config drift standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | GitOps for config drift is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C2-Q5: To what extent has Infrastructure as Code (policy-as-code (OPA/Conftest)) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer, Security, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `policies enforced in PR`

**Context**

- **What it measures (what):** Policies are evaluated on IaC changes before merge.
- **Why it matters (why):** Policy-as-code shifts governance left and scales security review.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No policy-as-code (opa/conftest) implemented. Teams operate without this capability. | • No policy-as-code (OPA/Conftest) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of policy-as-code (opa/conftest) with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | policy-as-code (OPA/Conftest) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | policy-as-code (OPA/Conftest) standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | policy-as-code (OPA/Conftest) is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C2-Q6: To what extent has Infrastructure as Code (ephemeral environment per PR) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `PR envs spun up`

**Context**

- **What it measures (what):** Every PR gets an ephemeral environment for integration testing.
- **Why it matters (why):** Ephemeral envs find bugs earlier and speed up review.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No ephemeral environment per pr implemented. Teams operate without this capability. | • No ephemeral environment per PR deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of ephemeral environment per pr with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | ephemeral environment per PR adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | ephemeral environment per PR standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | ephemeral environment per PR is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C3: Observability and Monitoring

**6 questions in this capability.**

### P2-C3-Q1: How comprehensive is your observability stack (logs, metrics, traces)?

**Metadata**

- **Target audience:** devops
- **Weight:** 1.0
- **Professional Edition:** Yes
- **Primary KPI:** `MTTR in minutes`

**Context**

- **What it measures (what):** Measures the maturity of the observability stack including logging, metrics, and distributed tracing.
- **Why it matters (why):** Comprehensive observability reduces MTTR from hours to minutes and enables proactive issue detection.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | Minimal logging. No centralized monitoring. Issues discovered by users reporting them. | • No centralized logging<br>• No monitoring dashboards<br>• User-reported issues only |
| **L1** | Developing | Centralized logging (ELK/CloudWatch). Basic uptime monitoring. MTTR >60 minutes. | • Centralized log platform<br>• Basic uptime checks<br>• MTTR >60 minutes |
| **L2** | Defined | Structured logging, application metrics (Prometheus/Datadog), basic alerting. MTTR 30-60 minutes. | • Structured JSON logging<br>• Application metrics dashboard<br>• MTTR 30-60 minutes |
| **L3** | Managed | Full observability: distributed tracing, correlated logs-metrics-traces, SLO-based alerting. MTTR <15 minutes. | • Distributed tracing enabled<br>• Correlated observability stack deployed<br>• SLO-based alerts configured<br>• MTTR <15 minutes |
| **L4** | Optimizing | AI-powered observability: anomaly detection, predictive alerting, auto-correlation of incidents, suggested remediation. MTTR <5 minutes. | • AI anomaly detection<br>• Predictive alerting enabled<br>• Automated incident correlation enabled<br>• MTTR <5 minutes |

---

### P2-C3-Q2: To what extent has Observability and Monitoring (structured logging w/ correlation IDs) been adopted across teams?

**Metadata**

- **Target audience:** devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services emitting structured logs`

**Context**

- **What it measures (what):** All logs follow a schema and carry trace/correlation IDs.
- **Why it matters (why):** Structured logs are searchable, aggregatable, and machine-readable.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No structured logging w/ correlation ids implemented. Teams operate without this capability. | • No structured logging w/ correlation IDs deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of structured logging w/ correlation ids with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | structured logging w/ correlation IDs adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | structured logging w/ correlation IDs standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | structured logging w/ correlation IDs is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C3-Q3: To what extent has Observability and Monitoring (distributed tracing (OpenTelemetry)) been adopted across teams?

**Metadata**

- **Target audience:** devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services instrumented`

**Context**

- **What it measures (what):** OTEL SDKs emit traces across service boundaries.
- **Why it matters (why):** Distributed tracing reveals latency contributors across microservices.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No distributed tracing (opentelemetry) implemented. Teams operate without this capability. | • No distributed tracing (OpenTelemetry) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of distributed tracing (opentelemetry) with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | distributed tracing (OpenTelemetry) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | distributed tracing (OpenTelemetry) standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | distributed tracing (OpenTelemetry) is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C3-Q4: To what extent has Observability and Monitoring (SLOs and error budgets) been adopted across teams?

**Metadata**

- **Target audience:** devops, product-owner
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services with SLOs`

**Context**

- **What it measures (what):** Service-level objectives with error budgets drive reliability decisions.
- **Why it matters (why):** SLOs align engineering priorities with user experience.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No slos and error budgets implemented. Teams operate without this capability. | • No SLOs and error budgets deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of slos and error budgets with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | SLOs and error budgets adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | SLOs and error budgets standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | SLOs and error budgets is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C3-Q5: To what extent has Observability and Monitoring (synthetic monitoring) been adopted across teams?

**Metadata**

- **Target audience:** devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `journeys monitored`

**Context**

- **What it measures (what):** Synthetic probes exercise critical user journeys continuously.
- **Why it matters (why):** Synthetics catch regressions before users do.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No synthetic monitoring implemented. Teams operate without this capability. | • No synthetic monitoring deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of synthetic monitoring with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | synthetic monitoring adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | synthetic monitoring standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | synthetic monitoring is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C3-Q6: To what extent has Observability and Monitoring (anomaly detection with ML) been adopted across teams?

**Metadata**

- **Target audience:** devops, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `alerts auto-triaged`

**Context**

- **What it measures (what):** ML models detect anomalies and suppress noise.
- **Why it matters (why):** ML-based detection reduces alert fatigue and speeds response.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No anomaly detection with ml implemented. Teams operate without this capability. | • No anomaly detection with ML deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of anomaly detection with ml with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | anomaly detection with ML adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | anomaly detection with ML standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | anomaly detection with ML is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C4: Security Integration (DevSecOps)

**6 questions in this capability.**

### P2-C4-Q1: How integrated is security into your development and deployment pipeline?

**Metadata**

- **Target audience:** Security, devops, product-owner
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% vulnerabilities caught pre-prod`

**Context**

- **What it measures (what):** Measures the integration of security practices into the development lifecycle (shift-left security).
- **Why it matters (why):** Fixing vulnerabilities in production costs 30x more than catching them in development. DevSecOps reduces security incidents by 50%.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | Security reviewed only before release. No automated scanning. Vulnerabilities found in production. | • No automated security scanning<br>• Pre-release only reviews<br>• Production vulnerability incidents |
| **L1** | Developing | Basic dependency scanning in CI (Dependabot/Snyk). Manual security review for critical features. | • Dependency scanning configured<br>• Manual security reviews<br>• No SAST or DAST scanning |
| **L2** | Defined | SAST and dependency scanning in CI pipeline. Security requirements in definition of done. >50% vulnerabilities caught pre-production. | • SAST in CI pipeline<br>• Security in DoD<br>• >50% pre-prod catch rate |
| **L3** | Managed | Full DevSecOps: SAST, DAST, SCA, container scanning, secret detection. Security gates block deployment. >80% pre-prod catch rate. | • SAST, DAST, SCA, and container scanning<br>• Secret detection enabled<br>• >80% pre-prod catch rate |
| **L4** | Optimizing | AI-powered security: automated threat modeling, predictive vulnerability detection, auto-patching of known CVEs, runtime protection. >95% pre-prod catch rate. | • Automated threat modeling<br>• Predictive vulnerability detection<br>• Automated patching pipeline enabled<br>• >95% pre-prod catch rate |

---

### P2-C4-Q2: To what extent has Security Integration (DevSecOps) (SAST in every pipeline) been adopted across teams?

**Metadata**

- **Target audience:** Security, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% repos with SAST`

**Context**

- **What it measures (what):** Static analysis scans every PR for vulnerabilities.
- **Why it matters (why):** SAST finds bugs cheaply at authoring time.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No sast in every pipeline implemented. Teams operate without this capability. | • No SAST in every pipeline deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of sast in every pipeline with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | SAST in every pipeline adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | SAST in every pipeline standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | SAST in every pipeline is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C4-Q3: To what extent has Security Integration (DevSecOps) (SCA and dependency review) been adopted across teams?

**Metadata**

- **Target audience:** Security, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% repos with SCA`

**Context**

- **What it measures (what):** Software composition analysis flags vulnerable dependencies.
- **Why it matters (why):** Known-vuln dependencies are a top attack vector.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No sca and dependency review implemented. Teams operate without this capability. | • No SCA and dependency review deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of sca and dependency review with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | SCA and dependency review adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | SCA and dependency review standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | SCA and dependency review is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C4-Q4: To what extent has Security Integration (DevSecOps) (secret scanning and push protection) been adopted across teams?

**Metadata**

- **Target audience:** Security, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `secrets blocked per month`

**Context**

- **What it measures (what):** Secrets are detected pre-commit and blocked from push.
- **Why it matters (why):** Leaked secrets are the #1 source of breach in cloud environments.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No secret scanning and push protection implemented. Teams operate without this capability. | • No secret scanning and push protection deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of secret scanning and push protection with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | secret scanning and push protection adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | secret scanning and push protection standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | secret scanning and push protection is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C4-Q5: To what extent has Security Integration (DevSecOps) (DAST and API security testing) been adopted across teams?

**Metadata**

- **Target audience:** Security, devops, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% APIs DAST-tested`

**Context**

- **What it measures (what):** Dynamic testing exercises the running app for runtime vulns.
- **Why it matters (why):** DAST catches issues SAST cannot (auth, logic, configuration).

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No dast and api security testing implemented. Teams operate without this capability. | • No DAST and API security testing deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of dast and api security testing with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | DAST and API security testing adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | DAST and API security testing standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | DAST and API security testing is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C4-Q6: To what extent has Security Integration (DevSecOps) (security champions program) been adopted across teams?

**Metadata**

- **Target audience:** Security, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `champions per 20 devs`

**Context**

- **What it measures (what):** Every team has a security champion trained and resourced.
- **Why it matters (why):** Champions scale security expertise into every team.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No security champions program implemented. Teams operate without this capability. | • No security champions program deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of security champions program with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | security champions program adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | security champions program standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | security champions program is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C5: Release and Deployment Strategies

**6 questions in this capability.**

### P2-C5-Q1: To what extent has Release and Deployment Strategies (blue/green or canary deploys) been adopted across teams?

**Metadata**

- **Target audience:** devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services with canary`

**Context**

- **What it measures (what):** Canary or blue/green deploys reduce blast radius.
- **Why it matters (why):** Progressive rollout catches issues before full exposure.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No blue/green or canary deploys implemented. Teams operate without this capability. | • No blue/green or canary deploys deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of blue/green or canary deploys with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | blue/green or canary deploys adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | blue/green or canary deploys standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | blue/green or canary deploys is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q2: To what extent has Release and Deployment Strategies (automated rollback) been adopted across teams?

**Metadata**

- **Target audience:** devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `median rollback time`

**Context**

- **What it measures (what):** SLO breach or error spike triggers automatic rollback.
- **Why it matters (why):** Automated rollback limits user impact when deploys go wrong.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No automated rollback implemented. Teams operate without this capability. | • No automated rollback deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of automated rollback with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | automated rollback adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | automated rollback standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | automated rollback is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q3: To what extent has Release and Deployment Strategies (feature flag platform) been adopted across teams?

**Metadata**

- **Target audience:** devops, Arquiteto
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `flags in active use`

**Context**

- **What it measures (what):** A flag platform supports progressive exposure and experiments.
- **Why it matters (why):** Flags decouple deploy from release.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No feature flag platform implemented. Teams operate without this capability. | • No feature flag platform deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of feature flag platform with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | feature flag platform adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | feature flag platform standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | feature flag platform is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q4: To what extent has Release and Deployment Strategies (release coordination via ChatOps) been adopted across teams?

**Metadata**

- **Target audience:** devops, Security
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% releases using ChatOps`

**Context**

- **What it measures (what):** Releases are coordinated through a chat bot with approvals.
- **Why it matters (why):** ChatOps creates an audit trail and reduces handoff errors.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No release coordination via chatops implemented. Teams operate without this capability. | • No release coordination via ChatOps deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of release coordination via chatops with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | release coordination via ChatOps adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | release coordination via ChatOps standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | release coordination via ChatOps is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q5: To what extent has Release and Deployment Strategies (progressive delivery across regions) been adopted across teams?

**Metadata**

- **Target audience:** devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `regions rolled out per release`

**Context**

- **What it measures (what):** Releases ripple across regions with automated health checks.
- **Why it matters (why):** Multi-region rollout contains regional failures.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No progressive delivery across regions implemented. Teams operate without this capability. | • No progressive delivery across regions deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of progressive delivery across regions with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | progressive delivery across regions adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | progressive delivery across regions standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | progressive delivery across regions is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q6: To what extent has Release and Deployment Strategies (release metrics dashboard) been adopted across teams?

**Metadata**

- **Target audience:** devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% releases meeting SLO`

**Context**

- **What it measures (what):** Deployment success and SLO impact are tracked per release.
- **Why it matters (why):** Data-driven release retros drive continuous improvement.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No release metrics dashboard implemented. Teams operate without this capability. | • No release metrics dashboard deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of release metrics dashboard with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | release metrics dashboard adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | release metrics dashboard standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | release metrics dashboard is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C6: Test Automation

**7 questions in this capability.**

### P2-C6-Q1: To what extent has Test Automation (unit test coverage targets) been adopted across teams?

**Metadata**

- **Target audience:** qa-test, Developer, devops, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% repos >80% coverage`

**Context**

- **What it measures (what):** Every repo has a measurable coverage target.
- **Why it matters (why):** Coverage is a useful proxy when combined with mutation testing.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No unit test coverage targets implemented. Teams operate without this capability. | • No unit test coverage targets deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of unit test coverage targets with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | unit test coverage targets adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | unit test coverage targets standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | unit test coverage targets is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q2: To what extent has Test Automation (integration test suites) been adopted across teams?

**Metadata**

- **Target audience:** qa-test, Developer, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `integration tests in CI`

**Context**

- **What it measures (what):** Integration tests exercise real service boundaries.
- **Why it matters (why):** Integration tests catch wiring bugs that units cannot.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No integration test suites implemented. Teams operate without this capability. | • No integration test suites deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of integration test suites with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | integration test suites adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | integration test suites standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | integration test suites is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q3: To what extent has Test Automation (end-to-end / journey tests) been adopted across teams?

**Metadata**

- **Target audience:** qa-test, Developer, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `critical journeys automated`

**Context**

- **What it measures (what):** Critical user journeys run automatically on every deploy.
- **Why it matters (why):** E2E tests protect revenue-critical flows.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No end-to-end / journey tests implemented. Teams operate without this capability. | • No end-to-end / journey tests deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of end-to-end / journey tests with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | end-to-end / journey tests adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | end-to-end / journey tests standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | end-to-end / journey tests is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q4: To what extent has Test Automation (contract testing) been adopted across teams?

**Metadata**

- **Target audience:** qa-test, Developer, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% service pairs with contract tests`

**Context**

- **What it measures (what):** Consumer-driven contract tests catch API breakage.
- **Why it matters (why):** Contract tests protect microservice compatibility.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No contract testing implemented. Teams operate without this capability. | • No contract testing deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of contract testing with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | contract testing adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | contract testing standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | contract testing is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q5: To what extent has Test Automation (AI-assisted test generation) been adopted across teams?

**Metadata**

- **Target audience:** qa-test, Developer, devops, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% tests AI-generated`

**Context**

- **What it measures (what):** AI proposes tests for new and changed code.
- **Why it matters (why):** AI-generated tests raise the floor on coverage.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No ai-assisted test generation implemented. Teams operate without this capability. | • No AI-assisted test generation deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of ai-assisted test generation with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | AI-assisted test generation adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | AI-assisted test generation standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | AI-assisted test generation is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q6: To what extent has Test Automation (flaky-test detection & quarantine) been adopted across teams?

**Metadata**

- **Target audience:** qa-test, Developer, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `flaky test rate`

**Context**

- **What it measures (what):** Flaky tests are auto-quarantined and triaged.
- **Why it matters (why):** Flaky tests erode trust; detection restores it.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No flaky-test detection & quarantine implemented. Teams operate without this capability. | • No flaky-test detection & quarantine deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of flaky-test detection & quarantine with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | flaky-test detection & quarantine adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | flaky-test detection & quarantine standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | flaky-test detection & quarantine is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q7: To what extent has Test Automation (mutation testing) been adopted across teams?

**Metadata**

- **Target audience:** qa-test, Developer, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `mutation score of critical modules`

**Context**

- **What it measures (what):** Mutation testing validates the quality of the test suite.
- **Why it matters (why):** Mutation scores reveal whether tests actually catch bugs.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No mutation testing implemented. Teams operate without this capability. | • No mutation testing deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of mutation testing with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | mutation testing adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | mutation testing standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | mutation testing is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C7: Incident Management and SRE

**7 questions in this capability.**

### P2-C7-Q1: To what extent has Incident Management and SRE (on-call rotation with tooling) been adopted across teams?

**Metadata**

- **Target audience:** devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services with on-call`

**Context**

- **What it measures (what):** Every prod service has a named on-call rotation.
- **Why it matters (why):** Clear ownership is the foundation of reliability.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No on-call rotation with tooling implemented. Teams operate without this capability. | • No on-call rotation with tooling deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of on-call rotation with tooling with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | on-call rotation with tooling adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | on-call rotation with tooling standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | on-call rotation with tooling is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q2: To what extent has Incident Management and SRE (blameless postmortems) been adopted across teams?

**Metadata**

- **Target audience:** devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% incidents with postmortem`

**Context**

- **What it measures (what):** Postmortems focus on systems, not people.
- **Why it matters (why):** Blameless culture unlocks honest learning.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No blameless postmortems implemented. Teams operate without this capability. | • No blameless postmortems deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of blameless postmortems with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | blameless postmortems adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | blameless postmortems standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | blameless postmortems is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q3: To what extent has Incident Management and SRE (error budget policy) been adopted across teams?

**Metadata**

- **Target audience:** devops, Security, product-owner
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services using error budgets`

**Context**

- **What it measures (what):** Error budgets gate feature work vs reliability work.
- **Why it matters (why):** Error budgets make reliability a shared business decision.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No error budget policy implemented. Teams operate without this capability. | • No error budget policy deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of error budget policy with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | error budget policy adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | error budget policy standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | error budget policy is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q4: To what extent has Incident Management and SRE (chaos engineering) been adopted across teams?

**Metadata**

- **Target audience:** devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `gamedays per quarter`

**Context**

- **What it measures (what):** Controlled fault injection exercises resilience.
- **Why it matters (why):** Chaos engineering builds confidence in recovery.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No chaos engineering implemented. Teams operate without this capability. | • No chaos engineering deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of chaos engineering with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | chaos engineering adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | chaos engineering standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | chaos engineering is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q5: To what extent has Incident Management and SRE (incident commander role) been adopted across teams?

**Metadata**

- **Target audience:** devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% major incidents with IC`

**Context**

- **What it measures (what):** An incident commander coordinates response.
- **Why it matters (why):** A single coordinator reduces confusion during incidents.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No incident commander role implemented. Teams operate without this capability. | • No incident commander role deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of incident commander role with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | incident commander role adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | incident commander role standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | incident commander role is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q6: To what extent has Incident Management and SRE (SRE-dev partnership model) been adopted across teams?

**Metadata**

- **Target audience:** devops, engineering-leader, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% teams with SRE partner`

**Context**

- **What it measures (what):** SRE and dev teams collaborate on reliability roadmaps.
- **Why it matters (why):** Embedded partnership beats gatekeeping.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No sre-dev partnership model implemented. Teams operate without this capability. | • No SRE-dev partnership model deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of sre-dev partnership model with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | SRE-dev partnership model adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | SRE-dev partnership model standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | SRE-dev partnership model is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q7: To what extent has Incident Management and SRE (runbook automation) been adopted across teams?

**Metadata**

- **Target audience:** devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% incidents with runbook run`

**Context**

- **What it measures (what):** Runbook steps are codified and executed automatically.
- **Why it matters (why):** Runbook automation shrinks MTTR and reduces human error.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No runbook automation implemented. Teams operate without this capability. | • No runbook automation deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of runbook automation with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | runbook automation adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | runbook automation standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | runbook automation is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C8: Artifact and Package Management

**5 questions in this capability.**

### P2-C8-Q1: To what extent has Artifact and Package Management (internal package registry) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer, Security
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% packages via registry`

**Context**

- **What it measures (what):** Internal registry hosts all packages; no public-only deps.
- **Why it matters (why):** A registry enables auditing and availability controls.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No internal package registry implemented. Teams operate without this capability. | • No internal package registry deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of internal package registry with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | internal package registry adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | internal package registry standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | internal package registry is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C8-Q2: To what extent has Artifact and Package Management (SBOM for every build) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer, Security
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% builds with SBOM`

**Context**

- **What it measures (what):** Each build generates a software bill of materials.
- **Why it matters (why):** SBOMs are now a regulatory and security requirement.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No sbom for every build implemented. Teams operate without this capability. | • No SBOM for every build deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of sbom for every build with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | SBOM for every build adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | SBOM for every build standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | SBOM for every build is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C8-Q3: To what extent has Artifact and Package Management (artifact signing (SLSA)) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% artifacts signed`

**Context**

- **What it measures (what):** Artifacts are signed and verified on deploy.
- **Why it matters (why):** Signing prevents supply-chain tampering.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No artifact signing (slsa) implemented. Teams operate without this capability. | • No artifact signing (SLSA) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of artifact signing (slsa) with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | artifact signing (SLSA) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | artifact signing (SLSA) standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | artifact signing (SLSA) is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C8-Q4: To what extent has Artifact and Package Management (vulnerability scanning of artifacts) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% artifacts scanned`

**Context**

- **What it measures (what):** Every artifact is scanned before deployment.
- **Why it matters (why):** Pre-deploy scanning blocks known-bad artifacts.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No vulnerability scanning of artifacts implemented. Teams operate without this capability. | • No vulnerability scanning of artifacts deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of vulnerability scanning of artifacts with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | vulnerability scanning of artifacts adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | vulnerability scanning of artifacts standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | vulnerability scanning of artifacts is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C8-Q5: To what extent has Artifact and Package Management (retention & promotion policies) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer, Security
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `artifacts promoted via policy`

**Context**

- **What it measures (what):** Artifacts move through dev→stage→prod with policy gates.
- **Why it matters (why):** Promotion policies tie deploys to provenance.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No retention & promotion policies implemented. Teams operate without this capability. | • No retention & promotion policies deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of retention & promotion policies with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | retention & promotion policies adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | retention & promotion policies standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | retention & promotion policies is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C9: Change Management and GitOps

**5 questions in this capability.**

### P2-C9-Q1: To what extent has Change Management and GitOps (GitOps controllers in prod) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer, Security
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% clusters on GitOps`

**Context**

- **What it measures (what):** Cluster state is reconciled from Git by a controller.
- **Why it matters (why):** GitOps makes change traceable, auditable, and reversible.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No gitops controllers in prod implemented. Teams operate without this capability. | • No GitOps controllers in prod deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of gitops controllers in prod with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | GitOps controllers in prod adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | GitOps controllers in prod standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | GitOps controllers in prod is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C9-Q2: To what extent has Change Management and GitOps (automated change tickets) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% changes ticketed automatically`

**Context**

- **What it measures (what):** Change records are created from PRs automatically.
- **Why it matters (why):** Automation keeps records accurate without slowing delivery.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No automated change tickets implemented. Teams operate without this capability. | • No automated change tickets deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of automated change tickets with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | automated change tickets adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | automated change tickets standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | automated change tickets is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C9-Q3: To what extent has Change Management and GitOps (approvals in PR (not tickets)) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer, Security
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% approvals in PR`

**Context**

- **What it measures (what):** Change approvals happen in code review, not separate tickets.
- **Why it matters (why):** Approval-as-code cuts cycle time while keeping audit trail.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No approvals in pr (not tickets) implemented. Teams operate without this capability. | • No approvals in PR (not tickets) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of approvals in pr (not tickets) with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | approvals in PR (not tickets) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | approvals in PR (not tickets) standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | approvals in PR (not tickets) is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C9-Q4: To what extent has Change Management and GitOps (environment promotion via PR) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% envs promoted via PR`

**Context**

- **What it measures (what):** Moving from stage to prod is a PR, not a click.
- **Why it matters (why):** PR-based promotion inherits review and rollback.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No environment promotion via pr implemented. Teams operate without this capability. | • No environment promotion via PR deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of environment promotion via pr with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | environment promotion via PR adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | environment promotion via PR standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | environment promotion via PR is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C9-Q5: To what extent has Change Management and GitOps (compliance evidence auto-collected) been adopted across teams?

**Metadata**

- **Target audience:** devops, Platform Engineer, Security
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `controls automated`

**Context**

- **What it measures (what):** Evidence for SOC2/ISO is gathered automatically from CI.
- **Why it matters (why):** Auto-evidence turns audits into a side effect of normal work.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No compliance evidence auto-collected implemented. Teams operate without this capability. | • No compliance evidence auto-collected deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of compliance evidence auto-collected with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | compliance evidence auto-collected adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | compliance evidence auto-collected standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | compliance evidence auto-collected is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C10: Dependency and Supply Chain Security

**5 questions in this capability.**

### P2-C10-Q1: To what extent has Dependency and Supply Chain Security (dependabot or renovate on every repo) been adopted across teams?

**Metadata**

- **Target audience:** Security, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% repos auto-updated`

**Context**

- **What it measures (what):** Dependabot or Renovate opens PRs for outdated deps.
- **Why it matters (why):** Automated updates keep CVE window short.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No dependabot or renovate on every repo implemented. Teams operate without this capability. | • No dependabot or renovate on every repo deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of dependabot or renovate on every repo with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | dependabot or renovate on every repo adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | dependabot or renovate on every repo standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | dependabot or renovate on every repo is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C10-Q2: To what extent has Dependency and Supply Chain Security (allow-list registries only) been adopted across teams?

**Metadata**

- **Target audience:** Security, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% deps from allow-listed source`

**Context**

- **What it measures (what):** Proxy registries filter packages from trusted sources.
- **Why it matters (why):** Proxying blocks typosquatting and malicious packages.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No allow-list registries only implemented. Teams operate without this capability. | • No allow-list registries only deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of allow-list registries only with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | allow-list registries only adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | allow-list registries only standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | allow-list registries only is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C10-Q3: To what extent has Dependency and Supply Chain Security (build provenance (SLSA level)) been adopted across teams?

**Metadata**

- **Target audience:** Security, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `SLSA level reached`

**Context**

- **What it measures (what):** Builds carry verifiable provenance metadata.
- **Why it matters (why):** Provenance is the foundation of supply-chain trust.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No build provenance (slsa level) implemented. Teams operate without this capability. | • No build provenance (SLSA level) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of build provenance (slsa level) with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | build provenance (SLSA level) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | build provenance (SLSA level) standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | build provenance (SLSA level) is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C10-Q4: To what extent has Dependency and Supply Chain Security (critical dep response playbook) been adopted across teams?

**Metadata**

- **Target audience:** Security, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `median time to patch critical`

**Context**

- **What it measures (what):** A playbook handles Log4Shell-class events.
- **Why it matters (why):** Preparation beats improvisation in a zero-day.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No critical dep response playbook implemented. Teams operate without this capability. | • No critical dep response playbook deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of critical dep response playbook with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | critical dep response playbook adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | critical dep response playbook standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | critical dep response playbook is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C10-Q5: To what extent has Dependency and Supply Chain Security (vendor/OSS risk reviews) been adopted across teams?

**Metadata**

- **Target audience:** Security, devops
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `critical vendors reviewed/year`

**Context**

- **What it measures (what):** High-risk vendors and OSS dependencies are reviewed annually.
- **Why it matters (why):** Review surfaces risk before it becomes an incident.

**Response format**

5-level Likert scale (L0-L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No vendor/oss risk reviews implemented. Teams operate without this capability. | • No vendor/OSS risk reviews deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of vendor/oss risk reviews with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | vendor/OSS risk reviews adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | vendor/OSS risk reviews standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | vendor/OSS risk reviews is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---


## How this section is scored

- Each question receives a numeric value from the selected level: L0=0, L1=1, L2=2, L3=3, L4=4.
- The capability score is the weighted average of the questions (default weight = 1.0; questions with weight 1.5 or 2.0 count more).
- The **P2** pillar score is the average of the 10 capabilities.
- The result is displayed on a 0-4 scale and converted to a maturity % (level / 4 × 100).

## Quick glossary

- **Pillar:** strategic maturity dimension.
- **Capability:** functional subdomain within a pillar.
- **Question:** concrete assessment item, standard ID `P[1-3]-C[1-19]-Q[1-99]`.
- **Level (L0-L4):** point on the Likert maturity scale.
- **KPI:** key indicator that objectively validates the declared level.
- **Evidence:** qualitative (text) or quantitative (attachment) proof that supports the answer.
