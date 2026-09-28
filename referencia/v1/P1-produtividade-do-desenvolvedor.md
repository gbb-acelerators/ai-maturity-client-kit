# AI Maturity Assessment: Pillar P1, Developer Productivity

🌐 English · [Português (Brasil)](P1-produtividade-do-desenvolvedor.pt-br.md)

> Measures how much engineering adopts AI to accelerate the cycle of coding, documentation, review, onboarding, and internal collaboration.

## Overview

- **Pillar:** `P1`: Developer Productivity
- **Capabilities:** 9
- **Total questions:** 53
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

## Capabilities of pillar P1

- **P1-C1**: AI Coding Assistants (5 questions)
- **P1-C2**: Developer Experience Platform (6 questions)
- **P1-C3**: Knowledge Management (6 questions)
- **P1-C4**: Code Review Automation (7 questions)
- **P1-C5**: Developer Onboarding and Training (7 questions)
- **P1-C6**: Inner Source and Collaboration (6 questions)
- **P1-C7**: Documentation Automation (5 questions)
- **P1-C8**: Developer Productivity Measurement (6 questions)
- **P1-C9**: Environment and Workspace Automation (5 questions)

---

## P1-C1: AI Coding Assistants

**5 questions in this capability.**

### P1-C1-Q1: To what extent does your organization use AI code completion tools (e.g., GitHub Copilot)?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% developers using AI completion`

**Context**

- **What it measures (what):** Measures adoption of AI-powered code completion and suggestion tools across the development team.
- **Why it matters (why):** AI coding assistants can increase developer velocity by 30-55% on routine coding tasks, reducing time-to-market.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No AI coding tools implemented. All code is written manually without AI assistance. | • No AI tool licenses<br>• No AI tool policies<br>• Manual-only coding workflows |
| **L1** | Developing | Pilot implementation of an AI coding assistant for <10% of developers. Ad-hoc usage without guidelines. | • Pilot program documentation<br>• < 10% license allocation<br>• No usage policy defined |
| **L2** | Defined | AI coding assistant deployed to 25-50% of developers with usage guidelines and basic training. | • 25-50% license coverage<br>• Written usage guidelines<br>• Completion training materials |
| **L3** | Managed | AI coding assistant deployed to >75% of developers with measured productivity gains >15% and prompt libraries. | • >75% active users<br>• Productivity metrics showing >15% gain<br>• Shared prompt library repository |
| **L4** | Optimizing | Universal AI coding assistant (>95%) with custom model fine-tuning and measured velocity improvement >30%. | • >95% daily active usage<br>• Custom model fine-tuning config<br>• Measured >30% velocity improvement<br>• Automated suggestion quality tracking |

---

### P1-C1-Q2: How effectively does your team leverage AI for code review and quality improvement?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% PRs with AI review`

**Context**

- **What it measures (what):** Measures use of AI in code review processes to catch bugs, suggest improvements, and enforce standards.
- **Why it matters (why):** AI-assisted code review reduces review time by 40% and catches 20% more defects than manual-only review.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No AI involvement in code review. All reviews are manual peer reviews. | • Manual-only review process<br>• No AI review tools<br>• No automated quality gates |
| **L1** | Developing | Basic linting and static analysis tools in CI. No AI-driven review suggestions. | • CI linting configuration<br>• Static analysis tool setup<br>• No AI review bot configured |
| **L2** | Defined | AI review bot configured on 30-60% of repositories, providing automated code suggestions. | • AI review bot on 30-60% of repos<br>• PR suggestion examples<br>• Review bot configuration docs |
| **L3** | Managed | AI review integrated into >80% of repositories with custom rules aligned to team standards. | • >80% repo coverage<br>• Custom rule configuration<br>• Measured >25% review cycle reduction |
| **L4** | Optimizing | AI performs the first review on all PRs, automatically approving low-risk changes and escalating critical ones. | • 100% PR AI first-pass<br>• Auto-approval policy documented<br>• Risk classification model<br>• >50% cycle time reduction |

---

### P1-C1-Q3: How does your organization measure and track the impact of AI coding tools on productivity?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 0.8
- **Professional Edition:** No
- **Primary KPI:** `Productivity measurement maturity`

**Context**

- **What it measures (what):** Measures the organization's ability to quantify the value of AI coding tools.
- **Why it matters (why):** Without measurement, organizations cannot justify AI tool investment or optimize adoption strategies.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No measurement of AI tool impact. No baseline productivity metrics captured. | • No DORA metrics<br>• No productivity dashboards<br>• No AI tool usage tracking |
| **L1** | Developing | Anecdotal developer feedback on the usefulness of AI tools. No quantitative measurement. | • Developer survey results<br>• Informal feedback collection<br>• No quantitative data |
| **L2** | Defined | Basic DORA metrics tracked (deployment frequency, lead time). AI tool usage analytics available. | • DORA metrics dashboard<br>• Monthly usage analytics report<br>• Baseline measurements established |
| **L3** | Managed | Comprehensive developer productivity metrics including AI-specific measures: acceptance rate, time saved. | • >40% suggestion acceptance rate<br>• >20% time-to-merge improvement<br>• Defect density trend analysis |
| **L4** | Optimizing | Real-time productivity intelligence platform correlating AI tool usage with business outcomes. | • Real-time productivity dashboard<br>• Automated ROI reports<br>• Business outcome correlation analysis<br>• Per-team optimization recommendations |

---

### P1-C1-Q4: What level of AI-assisted testing capabilities does your organization employ?

**Metadata**

- **Target audience:** Developer, qa-test, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% test coverage from AI generation`

**Context**

- **What it measures (what):** Measures use of AI to generate, maintain, and optimize test suites.
- **Why it matters (why):** AI-generated tests can increase coverage from 40% to 80% in weeks, catching regressions that manual tests miss.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | All tests written manually. Test coverage below 40% on most projects. | • Manual test writing only<br>• <40% average coverage<br>• No AI test generation tools |
| **L1** | Developing | Occasional use of AI to generate unit test skeletons. Coverage remains below 50%. | • Ad-hoc AI test generation<br>• <50% coverage rate measured<br>• No systematic approach |
| **L2** | Defined | AI test generation integrated into the development workflow for 30-50% of new code. Coverage >60%. | • AI test generation in 30-50% of new code<br>• 60% coverage gates in CI<br>• Test generation guidelines |
| **L3** | Managed | AI generates >70% of unit tests with human review. Coverage >75%. AI identifies edge cases. | • >70% AI-generated tests<br>• >75% coverage across projects<br>• Edge case suggestion examples |
| **L4** | Optimizing | AI-driven test optimization: automatically generates regression suites, identifies flaky tests, and optimizes coverage. | • >85% coverage rate measured<br>• <5% flaky test rate<br>• Automated regression suite generation<br>• Mutation testing integration |

---

### P1-C1-Q5: How does your organization govern AI-generated code in terms of security and compliance?

**Metadata**

- **Target audience:** Developer, Security, product-owner, qa-test
- **Weight:** 1.1
- **Professional Edition:** No
- **Primary KPI:** `AI code governance maturity`

**Context**

- **What it measures (what):** Measures policies and controls around AI-generated code quality, security, and IP compliance.
- **Why it matters (why):** Without governance, AI-generated code can introduce vulnerabilities, license violations, and compliance risks.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No governance over AI-generated code. No policy exists. Developers use AI tools without restrictions. | • No AI code policy<br>• No security scanning of AI code<br>• No license compliance checks |
| **L1** | Developing | A basic policy exists prohibiting AI use in security-sensitive modules. No automation. | • Written AI usage policy<br>• Security-sensitive module list<br>• No automated enforcement |
| **L2** | Defined | AI-generated code goes through standard security analysis (SAST/DAST). License compliance checks in CI. | • SAST/DAST pipeline includes AI code<br>• License compliance scanning<br>• Policy enforcement in CI |
| **L3** | Managed | Dedicated code quality gates for AI: vulnerability scanning, license auditing, and code quality review. | • AI-specific quality gates<br>• Code provenance tracking<br>• <2% security flag rate<br>• Quarterly audit reports |
| **L4** | Optimizing | Real-time AI code governance: every suggestion scanned before display, blocked licenses, and tracked quality metrics. | • Pre-display content scanning enabled<br>• Auto-rejection of blocked licenses<br>• Zero unreviewed AI code policy<br>• Compliance certification achieved |

---

## P1-C2: Developer Experience Platform

**6 questions in this capability.**

### P1-C2-Q1: How mature is your internal developer portal or platform?

**Metadata**

- **Target audience:** Developer, Platform Engineer, Architect
- **Weight:** 1.0
- **Professional Edition:** Yes
- **Primary KPI:** `Developer portal adoption %`

**Context**

- **What it measures (what):** Measures the maturity of centralized developer portal for service catalog, docs, and self-service.
- **Why it matters (why):** A mature developer portal reduces onboarding time by 60% and eliminates context-switching between tools.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No developer portal. Documentation scattered across wikis, Slack, and email. | • No centralized portal<br>• Documentation in multiple tools<br>• No service catalog |
| **L1** | Developing | Basic wiki or Confluence space with some documentation. No service catalog or self-service capabilities. | • Central wiki exists<br>• Some API docs<br>• No service catalog |
| **L2** | Defined | Developer portal deployed (Backstage or similar) with service catalog covering >50% of services. Basic documentation templates. | • >50% services cataloged<br>• Portal deployment docs<br>• Documentation templates published |
| **L3** | Managed | Developer portal covers >80% of services with self-service scaffolding, automated API docs, and integrated CI/CD status. Onboarding time reduced >40%. | • >80% service coverage<br>• Self-service scaffolding tooling<br>• >40% onboarding time reduction |
| **L4** | Optimizing | AI-powered developer portal: natural language search across all docs, auto-generated architecture diagrams, predictive issue detection. >95% developer satisfaction. | • AI-powered search enabled<br>• Auto-generated architecture diagrams<br>• >95% satisfaction score<br>• Predictive issue detection |

---

### P1-C2-Q2: How effectively do your teams use standardized development environments?

**Metadata**

- **Target audience:** Developer, Platform Engineer
- **Weight:** 0.9
- **Professional Edition:** Yes
- **Primary KPI:** `Environment setup time (minutes)`

**Context**

- **What it measures (what):** Measures standardization of development environments across teams.
- **Why it matters (why):** Standardized environments eliminate 'works on my machine' issues and reduce setup time from days to minutes.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | Each developer maintains their own environment setup. No standardization. Setup takes >4 hours for new team members. | • No environment standardization<br>• Setup time >4 hours<br>• Manual dependency installation |
| **L1** | Developing | README with setup instructions. Some teams use Docker for local development. Setup time 1-4 hours. | • README setup guide<br>• Some Docker usage<br>• 1-4 hour setup time |
| **L2** | Defined | Docker Compose or devcontainer for >50% of projects. Setup time <30 minutes. Shared configurations. | • >50% projects with containers<br>• <30 min setup time<br>• Shared dev configs |
| **L3** | Managed | Standardized devcontainers for >80% of projects. Cloud-based dev environments available (Codespaces). Setup time <10 minutes. | • >80% devcontainer coverage<br>• Cloud dev environment available<br>• <10 min setup time |
| **L4** | Optimizing | One-click ephemeral dev environments with AI-configured dependencies. Zero manual setup. Environment parity with production guaranteed. | • One-click environment creation<br>• Zero manual setup steps<br>• Production parity verification documented<br>• AI dependency configuration |

---

### P1-C2-Q3: To what extent has Developer Experience Platform (self-service IDP) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Platform Engineer, Architect, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `Self-service catalog coverage`

**Context**

- **What it measures (what):** Internal developer platform (IDP) provides paved paths with self-service provisioning.
- **Why it matters (why):** IDPs reduce cognitive load and accelerate onboarding by 50-70%.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No self-service IDP implemented. Teams operate without this capability. | • No self-service IDP deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of self-service IDP with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Self-service IDP adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Self-service IDP standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Self-service IDP optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C2-Q4: To what extent has Developer Experience Platform (golden paths and templates) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Platform Engineer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services from templates`

**Context**

- **What it measures (what):** Golden-path templates encode opinionated defaults for new services.
- **Why it matters (why):** Standard templates reduce time-to-first-commit and enforce security baselines.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No golden paths and templates implemented. Teams operate without this capability. | • No golden paths and templates deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of golden paths and templates with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Golden paths and templates adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Golden paths and templates standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Golden paths and templates optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C2-Q5: To what extent has Developer Experience Platform (developer portal) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Platform Engineer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `Portal MAU (monthly active users)`

**Context**

- **What it measures (what):** A developer portal centralizes docs, APIs, and service catalog.
- **Why it matters (why):** A single pane of glass reduces context switching and improves discovery.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No developer portal implemented. Teams operate without this capability. | • No developer portal deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of developer portal with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Developer portal adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Developer portal standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Developer portal optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C2-Q6: To what extent has Developer Experience Platform (paved road policy enforcement) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Platform Engineer, Security, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `services on paved road`

**Context**

- **What it measures (what):** Platform policies are codified so teams must opt-out explicitly.
- **Why it matters (why):** Policy-as-code turns governance into an enabler, not a blocker.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No paved road policy enforcement implemented. Teams operate without this capability. | • No paved road policy enforcement deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of paved road policy enforcement with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Paved road policy enforcement adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Paved road policy enforcement standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Paved road policy enforcement optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C3: Knowledge Management

**6 questions in this capability.**

### P1-C3-Q1: How effectively does your organization capture and share development knowledge?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `Knowledge retrieval success rate %`

**Context**

- **What it measures (what):** Measures how well development knowledge is captured, organized, and accessible.
- **Why it matters (why):** Poor knowledge management causes 20% of developer time wasted searching for information or reinventing solutions.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | Knowledge lives in individual developers' heads. No documentation culture. High bus-factor risk. | • No documentation policy<br>• Knowledge in individuals<br>• High bus-factor risk |
| **L1** | Developing | Basic documentation exists for critical systems. Knowledge sharing through ad-hoc meetings and Slack threads. | • Some critical system docs<br>• Ad-hoc knowledge sharing<br>• Slack-based Q&A channel |
| **L2** | Defined | Structured documentation in central wiki. Regular tech talks or knowledge sharing sessions. Decision records for major changes. | • Central wiki with structure<br>• Regular tech talks<br>• ADR practice established |
| **L3** | Managed | Searchable knowledge base covering >70% of systems. AI-assisted documentation generation. Automated runbooks for common issues. | • >70% system documentation<br>• AI-assisted doc generation<br>• Automated runbooks published |
| **L4** | Optimizing | AI-powered knowledge graph linking code, docs, incidents, and decisions. Natural language queries return contextual answers. Knowledge freshness auto-monitored. | • Knowledge graph implementation<br>• NL query interface<br>• Automated freshness monitoring enabled<br>• Contextual answer system |

---

### P1-C3-Q2: To what extent has Knowledge Management (semantic code search) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% repos indexed`

**Context**

- **What it measures (what):** Organization-wide semantic search across repos, docs, and chats.
- **Why it matters (why):** Semantic search cuts duplicate work by making prior solutions discoverable.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No semantic code search implemented. Teams operate without this capability. | • No semantic code search deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of semantic code search with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Semantic code search adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Semantic code search standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Semantic code search optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q3: To what extent has Knowledge Management (RAG-based docs assistant) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `queries per developer/month`

**Context**

- **What it measures (what):** LLM-backed assistant answers dev questions from internal knowledge base.
- **Why it matters (why):** RAG assistants reduce interrupt load on senior engineers.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No RAG-based docs assistant implemented. Teams operate without this capability. | • No RAG-based docs assistant deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of RAG-based docs assistant with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | RAG-based docs assistant adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | RAG-based docs assistant standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | RAG-based docs assistant optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q4: To what extent has Knowledge Management (runbook and playbook coverage) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% critical services with runbook`

**Context**

- **What it measures (what):** Automated runbooks capture operational knowledge.
- **Why it matters (why):** Documented runbooks shorten MTTR and enable on-call rotation.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No runbook and playbook coverage implemented. Teams operate without this capability. | • No runbook and playbook coverage deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of runbook and playbook coverage with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Runbook and playbook coverage adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Runbook and playbook coverage standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Runbook and playbook coverage optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q5: To what extent has Knowledge Management (ADR (architecture decision records)) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services with ADRs`

**Context**

- **What it measures (what):** Architecture decisions are captured as ADRs in the repo.
- **Why it matters (why):** ADRs preserve institutional memory beyond individuals.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No ADR (architecture decision records) implemented. Teams operate without this capability. | • No ADR (architecture decision records) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of ADR (architecture decision records) with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | ADR (architecture decision records) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | ADR (architecture decision records) standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | ADR (architecture decision records) optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q6: To what extent has Knowledge Management (learning content & curated paths) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `completions per quarter`

**Context**

- **What it measures (what):** Curated learning paths tied to role and career ladder.
- **Why it matters (why):** Structured learning reduces ramp time and improves retention.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No learning content & curated paths implemented. Teams operate without this capability. | • No learning content & curated paths deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of learning content & curated paths with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Learning content & curated paths adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Learning content & curated paths standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Learning content & curated paths optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C4: Code Review Automation

**7 questions in this capability.**

### P1-C4-Q1: To what extent has Code Review Automation (AI reviewer bot on every PR) been adopted across teams?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% PRs AI-reviewed`

**Context**

- **What it measures (what):** A bot posts AI-generated review comments on every PR.
- **Why it matters (why):** AI reviewers catch issues before humans look at the code.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No AI reviewer bot on every PR implemented. Teams operate without this capability. | • No AI reviewer bot on every PR deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of AI reviewer bot on every PR with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | AI reviewer bot on every PR adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | AI reviewer bot on every PR standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | AI reviewer bot on every PR optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q2: To what extent has Code Review Automation (static linting and style auto-fix) been adopted across teams?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `lint violations per kLOC`

**Context**

- **What it measures (what):** Linters and formatters run automatically on every commit.
- **Why it matters (why):** Automated style removes bikeshedding from reviews.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No static linting and style auto-fix implemented. Teams operate without this capability. | • No static linting and style auto-fix deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of static linting and style auto-fix with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Static linting and style auto-fix adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Static linting and style auto-fix standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Static linting and style auto-fix optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q3: To what extent has Code Review Automation (automated security review) been adopted across teams?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `critical findings per PR`

**Context**

- **What it measures (what):** SAST comments inline on the PR diff.
- **Why it matters (why):** Inline findings are fixed 10x faster than backlog items.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No automated security review implemented. Teams operate without this capability. | • No automated security review deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of automated security review with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Automated security review adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Automated security review standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Automated security review optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q4: To what extent has Code Review Automation (required-reviewer rules) been adopted across teams?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% PRs meeting review rule`

**Context**

- **What it measures (what):** CODEOWNERS enforces domain-expert review per path.
- **Why it matters (why):** Right reviewer + right code = better catches.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No required-reviewer rules implemented. Teams operate without this capability. | • No required-reviewer rules deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of required-reviewer rules with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Required-reviewer rules adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Required-reviewer rules standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Required-reviewer rules optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q5: To what extent has Code Review Automation (review SLA tracking) been adopted across teams?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `median PR cycle time`

**Context**

- **What it measures (what):** PR cycle time is measured and targeted.
- **Why it matters (why):** Fast review cycles keep developers in flow.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No review SLA tracking implemented. Teams operate without this capability. | • No review SLA tracking deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of review SLA tracking with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Review SLA tracking adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Review SLA tracking standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Review SLA tracking optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q6: To what extent has Code Review Automation (change size enforcement) been adopted across teams?

**Metadata**

- **Target audience:** Developer, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `median PR size (LoC)`

**Context**

- **What it measures (what):** Pre-commit hooks encourage small PRs.
- **Why it matters (why):** Small PRs get better reviews and merge faster.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No change size enforcement implemented. Teams operate without this capability. | • No change size enforcement deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of change size enforcement with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Change size enforcement adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Change size enforcement standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Change size enforcement optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q7: To what extent has Code Review Automation (reviewer load balancing) been adopted across teams?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `review load balance index`

**Context**

- **What it measures (what):** Reviewer assignment balances load across the team.
- **Why it matters (why):** Balanced review load prevents burnout of top reviewers.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No reviewer load balancing implemented. Teams operate without this capability. | • No reviewer load balancing deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of reviewer load balancing with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Reviewer load balancing adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Reviewer load balancing standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Reviewer load balancing optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C5: Developer Onboarding and Training

**7 questions in this capability.**

### P1-C5-Q1: To what extent has Developer Onboarding and Training (codespaces/dev containers for instant env) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `time-to-first-commit (hours)`

**Context**

- **What it measures (what):** Cloud dev envs are ready in minutes.
- **Why it matters (why):** Fast env setup unblocks new hires on day one.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No codespaces/dev containers for instant env implemented. Teams operate without this capability. | • No codespaces/dev containers for instant env deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of codespaces/dev containers for instant env with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Codespaces/dev containers for instant env adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Codespaces/dev containers for instant env standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Codespaces/dev containers for instant env optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q2: To what extent has Developer Onboarding and Training (structured onboarding playbook) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% new hires completing onboarding`

**Context**

- **What it measures (what):** A documented 30/60/90-day onboarding plan per role.
- **Why it matters (why):** Structured onboarding reduces ramp time by 30-50%.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No structured onboarding playbook implemented. Teams operate without this capability. | • No structured onboarding playbook deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of structured onboarding playbook with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Structured onboarding playbook adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Structured onboarding playbook standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Structured onboarding playbook optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q3: To what extent has Developer Onboarding and Training (mentor pairing program) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `mentor:mentee ratio`

**Context**

- **What it measures (what):** Every new hire gets a senior mentor for 90 days.
- **Why it matters (why):** Mentoring shortens ramp and boosts retention.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No mentor pairing program implemented. Teams operate without this capability. | • No mentor pairing program deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of mentor pairing program with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Mentor pairing program adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Mentor pairing program standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Mentor pairing program optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q4: To what extent has Developer Onboarding and Training (hands-on curriculum & kata) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `katas completed per hire`

**Context**

- **What it measures (what):** Role-specific coding kata produce demonstrable skill.
- **Why it matters (why):** Deliberate practice builds skill faster than reading.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No hands-on curriculum & kata implemented. Teams operate without this capability. | • No hands-on curriculum & kata deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of hands-on curriculum & kata with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Hands-on curriculum & kata adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Hands-on curriculum & kata standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Hands-on curriculum & kata optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q5: To what extent has Developer Onboarding and Training (shadow on-call rotation) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `new hires who shadowed on-call`

**Context**

- **What it measures (what):** New hires shadow on-call to learn operational context.
- **Why it matters (why):** Operational context is the fastest way to understand the system.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No shadow on-call rotation implemented. Teams operate without this capability. | • No shadow on-call rotation deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of shadow on-call rotation with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Shadow on-call rotation adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Shadow on-call rotation standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Shadow on-call rotation optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q6: To what extent has Developer Onboarding and Training (onboarding feedback loop) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `NPS from new hires`

**Context**

- **What it measures (what):** New hires rate onboarding; results drive improvements.
- **Why it matters (why):** Feedback loops turn onboarding into a continuously improving product.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No onboarding feedback loop implemented. Teams operate without this capability. | • No onboarding feedback loop deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of onboarding feedback loop with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Onboarding feedback loop adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Onboarding feedback loop standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Onboarding feedback loop optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q7: To what extent has Developer Onboarding and Training (ramp-time measurement) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `median ramp-time to first deploy`

**Context**

- **What it measures (what):** Time-to-first-deploy is measured and improved for new hires.
- **Why it matters (why):** Measuring ramp turns onboarding improvements into ROI.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No ramp-time measurement implemented. Teams operate without this capability. | • No ramp-time measurement deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of ramp-time measurement with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Ramp-time measurement adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Ramp-time measurement standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Ramp-time measurement optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C6: Inner Source and Collaboration

**6 questions in this capability.**

### P1-C6-Q1: To what extent has Inner Source and Collaboration (internal repos with open contribution) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% repos open to all devs`

**Context**

- **What it measures (what):** Repos inside the org welcome PRs from other teams.
- **Why it matters (why):** Inner source breaks silos and increases reuse.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No internal repos with open contribution implemented. Teams operate without this capability. | • No internal repos with open contribution deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of internal repos with open contribution with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Internal repos with open contribution adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Internal repos with open contribution standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Internal repos with open contribution optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q2: To what extent has Inner Source and Collaboration (CONTRIBUTING.md standards) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% repos with CONTRIBUTING`

**Context**

- **What it measures (what):** Every repo documents how to contribute and review.
- **Why it matters (why):** Clear contribution norms lower friction for cross-team work.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No CONTRIBUTING.md standards implemented. Teams operate without this capability. | • No CONTRIBUTING.md standards deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of CONTRIBUTING.md standards with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | CONTRIBUTING.md standards adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | CONTRIBUTING.md standards standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | CONTRIBUTING.md standards optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q3: To what extent has Inner Source and Collaboration (inner-source discovery portal) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `cross-team PRs per month`

**Context**

- **What it measures (what):** A portal indexes inner-source projects seeking contributions.
- **Why it matters (why):** Discovery drives participation.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No inner-source discovery portal implemented. Teams operate without this capability. | • No inner-source discovery portal deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of inner-source discovery portal with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Inner-source discovery portal adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Inner-source discovery portal standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Inner-source discovery portal optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q4: To what extent has Inner Source and Collaboration (good-first-issue labeling) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `GFI issues closed per month`

**Context**

- **What it measures (what):** Starter issues help newcomers contribute confidently.
- **Why it matters (why):** Labeling lowers the bar for first-time contributors.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No good-first-issue labeling implemented. Teams operate without this capability. | • No good-first-issue labeling deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of good-first-issue labeling with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Good-first-issue labeling adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Good-first-issue labeling standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Good-first-issue labeling optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q5: To what extent has Inner Source and Collaboration (cross-team design reviews) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `reviews per quarter`

**Context**

- **What it measures (what):** Design docs are reviewed by multiple teams.
- **Why it matters (why):** Cross-team review catches assumptions and shares patterns.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No cross-team design reviews implemented. Teams operate without this capability. | • No cross-team design reviews deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of cross-team design reviews with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Cross-team design reviews adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Cross-team design reviews standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Cross-team design reviews optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q6: To what extent has Inner Source and Collaboration (community of practice) been adopted across teams?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `CoP active members`

**Context**

- **What it measures (what):** Guilds and CoPs build horizontal expertise.
- **Why it matters (why):** CoPs accelerate learning and de-risk hiring gaps.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No community of practice implemented. Teams operate without this capability. | • No community of practice deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of community of practice with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Community of practice adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Community of practice standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Community of practice optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C7: Documentation Automation

**5 questions in this capability.**

### P1-C7-Q1: To what extent has Documentation Automation (docs-as-code in Git) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services with docs in repo`

**Context**

- **What it measures (what):** Docs live with code and are reviewed in PRs.
- **Why it matters (why):** Docs-as-code prevents docs from rotting away from source.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No docs-as-code in Git implemented. Teams operate without this capability. | • No docs-as-code in Git deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of docs-as-code in Git with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Docs-as-code in Git adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Docs-as-code in Git standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Docs-as-code in Git optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q2: To what extent has Documentation Automation (auto-generated API reference) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% APIs with generated docs`

**Context**

- **What it measures (what):** API reference is generated from OpenAPI or source.
- **Why it matters (why):** Generated docs are always up to date.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No auto-generated API reference implemented. Teams operate without this capability. | • No auto-generated API reference deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of auto-generated API reference with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Auto-generated API reference adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Auto-generated API reference standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Auto-generated API reference optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q3: To what extent has Documentation Automation (AI-assisted doc drafting) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Architect, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% PRs with AI doc suggestions`

**Context**

- **What it measures (what):** AI suggests README and doc updates from code diffs.
- **Why it matters (why):** AI drafts raise the floor on documentation quality.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No AI-assisted doc drafting implemented. Teams operate without this capability. | • No AI-assisted doc drafting deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of AI-assisted doc drafting with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | AI-assisted doc drafting adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | AI-assisted doc drafting standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | AI-assisted doc drafting optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q4: To what extent has Documentation Automation (doc quality linting) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Architect, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `broken-link count`

**Context**

- **What it measures (what):** Link checks and style linters run in CI.
- **Why it matters (why):** Automated checks keep docs trustworthy.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No doc quality linting implemented. Teams operate without this capability. | • No doc quality linting deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of doc quality linting with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Doc quality linting adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Doc quality linting standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Doc quality linting optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q5: To what extent has Documentation Automation (docs analytics) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `top unanswered queries`

**Context**

- **What it measures (what):** Search analytics reveal what users cannot find.
- **Why it matters (why):** Analytics turn docs into a data-driven product.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No docs analytics implemented. Teams operate without this capability. | • No docs analytics deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of docs analytics with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Docs analytics adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Docs analytics standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Docs analytics optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C8: Developer Productivity Measurement

**6 questions in this capability.**

### P1-C8-Q1: To what extent has Developer Productivity Measurement (DORA four key metrics) been adopted across teams?

**Metadata**

- **Target audience:** engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `deploys/day, lead time, CFR, MTTR`

**Context**

- **What it measures (what):** Deployment frequency, lead time, change fail rate, MTTR are tracked.
- **Why it matters (why):** DORA metrics correlate with business outcomes.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No DORA four key metrics implemented. Teams operate without this capability. | • No DORA four key metrics deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of DORA four key metrics with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | DORA four key metrics adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | DORA four key metrics standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | DORA four key metrics optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q2: To what extent has Developer Productivity Measurement (developer experience surveys) been adopted across teams?

**Metadata**

- **Target audience:** engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `DX survey NPS`

**Context**

- **What it measures (what):** Quarterly surveys measure developer satisfaction.
- **Why it matters (why):** DX surveys surface friction that metrics miss.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No developer experience surveys implemented. Teams operate without this capability. | • No developer experience surveys deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of developer experience surveys with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Developer experience surveys adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Developer experience surveys standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Developer experience surveys optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q3: To what extent has Developer Productivity Measurement (build/test feedback loop time) been adopted across teams?

**Metadata**

- **Target audience:** engineering-leader, Platform Engineer, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `p95 CI duration`

**Context**

- **What it measures (what):** CI provides signal within 10 minutes for typical PRs.
- **Why it matters (why):** Fast feedback keeps developers in flow.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No build/test feedback loop time implemented. Teams operate without this capability. | • No build/test feedback loop time deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of build/test feedback loop time with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Build/test feedback loop time adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Build/test feedback loop time standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Build/test feedback loop time optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q4: To what extent has Developer Productivity Measurement (SPACE framework adoption) been adopted across teams?

**Metadata**

- **Target audience:** engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `SPACE dimensions tracked`

**Context**

- **What it measures (what):** Teams track Satisfaction, Performance, Activity, Communication, Efficiency.
- **Why it matters (why):** SPACE balances quantitative and qualitative signals.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No SPACE framework adoption implemented. Teams operate without this capability. | • No SPACE framework adoption deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of SPACE framework adoption with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | SPACE framework adoption adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | SPACE framework adoption standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | SPACE framework adoption optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q5: To what extent has Developer Productivity Measurement (flow vs friction dashboards) been adopted across teams?

**Metadata**

- **Target audience:** engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% teams viewing dashboard monthly`

**Context**

- **What it measures (what):** Leaders and teams see productivity data side by side.
- **Why it matters (why):** Shared data aligns improvements across teams.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No flow vs friction dashboards implemented. Teams operate without this capability. | • No flow vs friction dashboards deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of flow vs friction dashboards with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Flow vs friction dashboards adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Flow vs friction dashboards standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Flow vs friction dashboards optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q6: To what extent has Developer Productivity Measurement (quarterly productivity OKRs) been adopted across teams?

**Metadata**

- **Target audience:** engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% teams hitting DX OKRs`

**Context**

- **What it measures (what):** DX improvements are tracked as OKRs.
- **Why it matters (why):** OKRs make productivity a first-class investment.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No quarterly productivity OKRs implemented. Teams operate without this capability. | • No quarterly productivity OKRs deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of quarterly productivity OKRs with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Quarterly productivity OKRs adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Quarterly productivity OKRs standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Quarterly productivity OKRs optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C9: Environment and Workspace Automation

**5 questions in this capability.**

### P1-C9-Q1: To what extent has Environment and Workspace Automation (reproducible local envs (devcontainers)) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% repos with devcontainer`

**Context**

- **What it measures (what):** Every repo ships a devcontainer or Nix shell.
- **Why it matters (why):** Reproducible envs eliminate 'works on my machine' failures.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No reproducible local envs (devcontainers) implemented. Teams operate without this capability. | • No reproducible local envs (devcontainers) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of reproducible local envs (devcontainers) with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Reproducible local envs (devcontainers) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Reproducible local envs (devcontainers) standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Reproducible local envs (devcontainers) optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q2: To what extent has Environment and Workspace Automation (cloud workspaces (Codespaces/Gitpod)) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% devs using cloud workspace`

**Context**

- **What it measures (what):** Cloud workspaces are the default dev env.
- **Why it matters (why):** Cloud workspaces make env setup instant and consistent.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No cloud workspaces (Codespaces/Gitpod) implemented. Teams operate without this capability. | • No cloud workspaces (Codespaces/Gitpod) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of cloud workspaces (Codespaces/Gitpod) with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Cloud workspaces (Codespaces/Gitpod) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Cloud workspaces (Codespaces/Gitpod) standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Cloud workspaces (Codespaces/Gitpod) optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q3: To what extent has Environment and Workspace Automation (tool and SDK version pinning) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `tools pinned per repo`

**Context**

- **What it measures (what):** Language and tool versions are pinned and lockfiles committed.
- **Why it matters (why):** Pinned versions keep builds reproducible across machines.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No tool and SDK version pinning implemented. Teams operate without this capability. | • No tool and SDK version pinning deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of tool and SDK version pinning with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Tool and SDK version pinning adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Tool and SDK version pinning standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Tool and SDK version pinning optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q4: To what extent has Environment and Workspace Automation (on-demand test data) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Platform Engineer, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `time to get fresh test data`

**Context**

- **What it measures (what):** Developers can reset or provision realistic test data on demand.
- **Why it matters (why):** Fresh data unblocks testing and debugging.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No on-demand test data implemented. Teams operate without this capability. | • No on-demand test data deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of on-demand test data with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | On-demand test data adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | On-demand test data standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | On-demand test data optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q5: To what extent has Environment and Workspace Automation (workspace telemetry & health) been adopted across teams?

**Metadata**

- **Target audience:** Developer, Platform Engineer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% workspaces healthy`

**Context**

- **What it measures (what):** Workspace telemetry reveals setup failures and tool crashes.
- **Why it matters (why):** Telemetry lets platform teams fix friction proactively.

**Response format**

5-level Likert scale (L0 to L4). Select **one** level that best describes your organization today. Add text evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No workspace telemetry & health implemented. Teams operate without this capability. | • No workspace telemetry & health deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of workspace telemetry & health with <10% team coverage and ad-hoc usage. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | Workspace telemetry & health adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | Workspace telemetry & health standardized across >75% of teams with measured outcomes and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | Workspace telemetry & health optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---


## How this section is scored

- Each question receives a numeric value from the selected level: L0=0, L1=1, L2=2, L3=3, L4=4.
- The capability score is the weighted average of its questions (default weight = 1.0; questions with weight 1.5 or 2.0 count more).
- The **P1** pillar score is the average of the 9 capabilities.
- The result is shown on a 0 to 4 scale and converted to a maturity % (level / 4 × 100).

## Quick glossary

- **Pillar:** strategic maturity dimension.
- **Capability:** functional subdomain within a pillar.
- **Question:** concrete assessment item, standard ID `P[1-3]-C[1-19]-Q[1-99]`.
- **Level (L0-L4):** point on the Likert maturity scale.
- **KPI:** key indicator that objectively validates the declared level.
- **Evidence:** qualitative (text) or quantitative (attachment) proof that supports the response.
