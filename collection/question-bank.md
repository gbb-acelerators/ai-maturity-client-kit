# Microsoft Forms question bank: AI-Assisted SDLC Maturity Assessment v2

🌐 English · [Português (Brasil)](question-bank.pt-br.md) · [Español](question-bank.es.md)

> Generated from `framework.v2.json` (version 2.0.2) by `scripts/generate_v2_collection.py`. Do not edit by hand. Source of the wording: [AI-Maturity-Form-Questions_v2.md](AI-Maturity-Form-Questions_v2.md). The v1 bank (158 questions) is archived in [v1/](v1/).

## How to build the form

1. Go to <https://forms.office.com> and create a blank form. Suggested title: `AI-Assisted SDLC Maturity Assessment v2 - <Organization>`.
2. Paste the privacy notice from [FORMS-INSTRUCTIONS.md](FORMS-INSTRUCTIONS.md) into the form description.
3. Add **10 sections**: Section 0 (profile) and one per dimension, D1 to D9.
4. Section 0: add the 5 profile questions as **Choice**. `R-Q3` allows multiple answers. They are not scored.
5. For each scored question add 2 elements: a **Choice** (single answer) whose title starts with the ID and a colon (for example `D4-Q3: ...`), with the 6 options below in order; and an optional **Long Text** titled `Evidence (<ID>)`.
6. Paste the **L3 looks like** and **L4 looks like** lines into the question subtitle.
7. Share the link. Aim for at least 3 respondents per role (`R-Q1`).
8. `Responses` > `Open in Excel`, download the file, then run `make import XLSX=<file>`.

Element count: 5 profile + 61 scored + 61 optional evidence fields = 127 elements.

## The 6 options for every scored question

- **L0 - Not started: No practice yet, or AI not permitted for this activity**
- **L1 - Exploring: Individual or ad hoc use, no agreed guidance (more than 0% and up to 25% of teams)**
- **L2 - Adopting: Team-level practice with written guidance (26-50% of teams)**
- **L3 - Scaling: Organization standard, governed and measured (51-90% of teams)**
- **L4 - AI-native: Universal (>90%), continuously evaluated and improved, tied to outcomes**
- **NA - I do not know / Not applicable**

> Keep the `L0` to `L4` and `NA` prefix at the start of each option and the ID at the start of each title: the importer relies on both.

## How to answer

- Read every question as "to what extent is this true?".
- Answer at the highest level where **every** part of the question is true.
- If coverage, governance and measurement point to different levels, pick the lowest.
- Choose `L0` when the practice could apply but does not exist yet; choose `NA` only when you do not know or the activity does not exist in your scope.

---

## Section 0: Respondent profile (not scored)

### R-Q1: Primary role

**R-Q1: Which option best describes your primary role?**

_Choice, single answer_

- Software engineer / developer
- Engineering manager / tech lead
- Architect
- Platform / DevOps / SRE engineer
- Security / AppSec
- QA / test engineer
- Product / program manager
- Executive (CTO, VP, Director)
- Other

### R-Q2: Scope of your answers

**R-Q2: Which scope are your answers based on?**

_Choice, single answer_

- A single team
- Several teams in one business unit
- One business unit
- The whole organization

### R-Q3: Primary AI coding tools

**R-Q3: Which AI tools do you use at least weekly for software work? (multiple answers)**

_Choice, multiple answers_

- GitHub Copilot in the IDE (completions, chat, agent mode)
- GitHub Copilot cloud agent / code review / CLI
- Claude Code or Claude in other clients
- Microsoft Foundry / Azure OpenAI based internal tools
- Other commercial AI coding tools
- Internal or self-hosted models
- None

### R-Q4: Professional experience

**R-Q4: How many years of professional software experience do you have?**

_Choice, single answer_

- Less than 2
- 2-5
- 6-10
- More than 10

### R-Q5: Hands-on time

**R-Q5: In a typical week, how much of your time is hands-on building (code, configuration, tests)?**

_Choice, single answer_

- Less than 20%
- 20-50%
- 51-80%
- More than 80%

---

## Section D1: AI Strategy, Policy and Governance

_7 questions. Why it matters: DORA identifies a "clear and communicated AI stance" as an amplifier of AI benefits [1], [2]; Microsoft CAF states that "every agent must be observable, governed, and secure" [19]._

### D1-Q1: AI strategy for software engineering

**D1-Q1: Is there a documented AI strategy for software engineering that is sponsored by leadership, states explicit goals, and is communicated to every engineering team?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** Strategy published and reviewed at least yearly; goals (for example delivery, quality, developer experience) have owners; most engineers can say where to find it.
- **L4 looks like:** Strategy is revised from measured results (D9) and linked to business OKRs; progress is reported to leadership on a fixed cadence.
- **Evidence examples:** Strategy document, leadership communication, OKR entries.
- **Evidence field:** `Evidence (D1-Q1)` · _Tool, % coverage, metric, time window, link_

### D1-Q2: Acceptable-use policy

**D1-Q2: Is it clear to engineers how they are and are not allowed to use AI at work, including which data can be shared with AI tools?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** Written acceptable-use policy covers code, customer data, secrets and third-party IP; it is part of onboarding; exceptions have an owner.
- **L4 looks like:** Policy is enforced by technical controls (for example content exclusion, data loss prevention, allowlists) and audited; violations trigger automated alerts.
- **Evidence examples:** Policy link, onboarding checklist, control configuration.
- **Evidence field:** `Evidence (D1-Q2)` · _Tool, % coverage, metric, time window, link_

### D1-Q3: Approved tools and models

**D1-Q3: Is there a maintained catalog of approved AI tools, features and models for software development, managed through enterprise or organization policies?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** Enterprise/organization policies enable only approved features and models; the catalog lists owner, data handling and review date for each tool.
- **L4 looks like:** New models and tools go through a defined evaluation per task type (quality, cost, security) before enablement; retired ones are removed on schedule.
- **Evidence examples:** Copilot policy settings, tool catalog, model evaluation records.
- **Evidence field:** `Evidence (D1-Q3)` · _Tool, % coverage, metric, time window, link_

### D1-Q4: Data protection, IP and residency

**D1-Q4: Are data residency, retention, intellectual property and privacy requirements defined and applied to the AI tools and agents used in the SDLC?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** Requirements are documented per tool; sensitive repositories or files are excluded from AI context; logs and memory retention follow policy.
- **L4 looks like:** Compliance is assessed continuously (for example with a compliance manager) and mapped to regulations such as the EU AI Act where applicable.
- **Evidence examples:** Data processing records, exclusion settings, retention policy.
- **Evidence field:** `Evidence (D1-Q4)` · _Tool, % coverage, metric, time window, link_

### D1-Q5: Autonomy levels for AI work

**D1-Q5: Has the organization defined which tasks are developer-led, developer-with-agent, or fully agent-led, and the controls required for each level?**

- **Scope note:** Measures the policy that defines autonomy levels. How tasks are written for agents is D3-Q3; how often work is delegated is D4-Q3.
- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** A published matrix maps task types (for example dependency upgrades, test generation, feature work, production changes) to autonomy levels and required approvals.
- **L4 looks like:** The matrix is enforced by platform rules (for example branch protection, required reviewers per path) and updated from incident and quality data.
- **Evidence examples:** Autonomy matrix, repository rulesets, change records.
- **Evidence field:** `Evidence (D1-Q5)` · _Tool, % coverage, metric, time window, link_

### D1-Q6: Responsible AI and risk framework

**D1-Q6: Is AI use in software engineering governed by a responsible AI standard and a recognized risk framework (for example Microsoft Responsible AI Standard, NIST AI RMF, ISO/IEC 42001)?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** A named framework is adopted; AI-related risks are in the risk register with owners and reviews.
- **L4 looks like:** Framework controls are audited internally or externally; results feed back into policy and tooling.
- **Evidence examples:** Framework mapping, risk register entries, audit reports.
- **Evidence field:** `Evidence (D1-Q6)` · _Tool, % coverage, metric, time window, link_

### D1-Q7: Agent registry and identity

**D1-Q7: Is every AI agent used in the SDLC (coding agents, review agents, custom agents, pipeline agents) registered with an owner, a purpose, a distinct identity and a defined access scope?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** A single inventory lists all agents with owner, platform and permissions; each agent runs under its own identity, not a shared human account.
- **L4 looks like:** Unregistered ("shadow") agents are detected automatically; identity lifecycle (creation, review, removal) is automated.
- **Evidence examples:** Agent inventory, identity configuration (for example Microsoft Entra Agent ID), access reviews.
- **Evidence field:** `Evidence (D1-Q7)` · _Tool, % coverage, metric, time window, link_

---

## Section D2: Enablement, Skills and Culture

_6 questions. Why it matters: Gartner expects GenAI to require 80% of the engineering workforce to upskill through 2027 [30]; DORA asks about training, peer learning and support for experimentation [2]._

### D2-Q1: Structured AI training

**D2-Q1: Do engineers receive structured training on the approved AI tools and agent workflows, beyond the vendor's default onboarding?**

- **Coverage unit:** engineers
- **L3 looks like:** Role-based curriculum (developer, reviewer, platform, security) with completion tracked; training is required before agent features are enabled; it teaches learning-preserving patterns (ask for explanations, attempt first, then compare) and not only full delegation.
- **L4 looks like:** Curriculum is updated each quarter from usage data and failure patterns; advanced tracks exist (agent orchestration, evaluation).
- **Evidence examples:** Learning paths, completion rates, enablement gating rules.
- **Evidence field:** `Evidence (D2-Q1)` · _Tool, % coverage, metric, time window, link_

### D2-Q2: Peer learning and champions

**D2-Q2: Are there regular peer-learning formats (demos, brown bags, office hours) and a network of AI champions across teams?**

- **Coverage unit:** teams
- **L3 looks like:** Champions exist in most teams; sessions run at least monthly; recordings and examples are shared in one place.
- **L4 looks like:** A community of practice curates reusable assets (instructions, prompt files, agents) and measures their reuse.
- **Evidence examples:** Champion list, session calendar, shared repository of examples.
- **Evidence field:** `Evidence (D2-Q2)` · _Tool, % coverage, metric, time window, link_

### D2-Q3: Support for experimentation

**D2-Q3: Does the organization give engineers time, sandboxes and budget to experiment safely with new AI tools and agent patterns?**

- **Coverage unit:** teams
- **L3 looks like:** Sandboxed environments and a lightweight request path exist; experiments are logged and their results shared.
- **L4 looks like:** Successful experiments move into the approved catalog (D1-Q3) through a defined path within weeks.
- **Evidence examples:** Sandbox subscriptions, experiment log, promotion records.
- **Evidence field:** `Evidence (D2-Q3)` · _Tool, % coverage, metric, time window, link_

### D2-Q4: Context-engineering skills

**D2-Q4: Are engineers trained to give AI tools the right context (clear task scoping, relevant files, constraints, examples) and to keep context lean?**

- **Coverage unit:** engineers
- **L3 looks like:** Guidance and examples on context engineering are part of training; teams review their instructions and prompts for quality.
- **L4 looks like:** Context practices are measured (for example success rate or token use per task) and improved over time.
- **Evidence examples:** Guidance pages, review checklists, before/after metrics.
- **Evidence field:** `Evidence (D2-Q4)` · _Tool, % coverage, metric, time window, link_

### D2-Q5: Roles and career paths

**D2-Q5: Have job descriptions, career frameworks and performance expectations been updated for AI-assisted and agentic engineering (for example directing agents, reviewing AI output, AI engineering)?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** Updated role profiles are published; performance reviews recognize effective AI use and review quality, not raw output volume.
- **L4 looks like:** Dedicated roles exist (for example AI engineer, agent platform owner) with a clear growth path.
- **Evidence examples:** Career framework, role descriptions.
- **Evidence field:** `Evidence (D2-Q5)` · _Tool, % coverage, metric, time window, link_

### D2-Q6: AI-assisted onboarding

**D2-Q6: Do new engineers use AI tools to understand codebases and become productive, with ramp-up time measured?**

- **Coverage unit:** engineers
- **L3 looks like:** Onboarding includes AI-guided codebase tours and repository instructions; time to first merged PR is tracked; new engineers are checked on code reading and debugging, not only output.
- **L4 looks like:** Ramp-up and skill metrics are compared across cohorts and used to improve onboarding material and instructions.
- **Evidence examples:** Onboarding playbook, time-to-first-PR data, skill check results.
- **Evidence field:** `Evidence (D2-Q6)` · _Tool, % coverage, metric, time window, link_

---

## Section D3: Plan, Specify and Design

_6 questions. Why it matters: in agentic coding, "people make most of the planning decisions (what to do) and Claude makes most of the execution decisions (how to do it)" [24]; the quality of the task definition drives the quality of agent output [8], [27]._

### D3-Q1: AI in backlog refinement

**D3-Q1: Is AI used to draft and refine issues or user stories, including acceptance criteria, with a human owner who approves them?**

- **Coverage unit:** teams
- **L3 looks like:** Most teams use AI to draft or improve work items; acceptance criteria are mandatory before work starts.
- **L4 looks like:** Work-item quality (clarity, testability) is measured and linked to rework and cycle time.
- **Evidence examples:** Issue templates, sample work items, quality checks.
- **Evidence field:** `Evidence (D3-Q1)` · _Tool, % coverage, metric, time window, link_

### D3-Q2: Specification before implementation

**D3-Q2: For non-trivial changes, is a written plan or specification produced and reviewed before an AI agent implements the change?**

- **Coverage unit:** teams
- **L3 looks like:** Plans or specs are stored in the repository or linked to the issue, and are reviewed by a human before agent implementation.
- **L4 looks like:** Specs are the contract for automated verification (tests, checks) and are kept in sync with the code.
- **Evidence examples:** Spec files, plan reviews, PRs that reference specs.
- **Evidence field:** `Evidence (D3-Q2)` · _Tool, % coverage, metric, time window, link_

### D3-Q3: Task scoping for agents

**D3-Q3: Are tasks given to coding agents well scoped (small, with clear acceptance criteria and pointers to relevant code) before assignment?**

- **Scope note:** Measures how tasks are scoped for agents. The autonomy policy is D1-Q5; delegation volume is D4-Q3.
- **Coverage unit:** teams
- **L3 looks like:** Teams follow written guidance for agent-ready issues; oversized tasks are split before assignment.
- **L4 looks like:** Agent task success and rework rates are tracked per task type and used to refine the guidance.
- **Evidence examples:** Agent task guidelines, issue samples, success-rate data.
- **Evidence field:** `Evidence (D3-Q3)` · _Tool, % coverage, metric, time window, link_

### D3-Q4: Architecture and design decisions

**D3-Q4: Is AI used to support design work (option analysis, threat and failure modes, architecture decision records) while decisions stay with accountable humans?**

- **Coverage unit:** teams
- **L3 looks like:** ADRs are versioned; AI-assisted analysis is attached; a named human approves each decision.
- **L4 looks like:** Agents check new changes against recorded decisions and flag conflicts automatically.
- **Evidence examples:** ADR repository, design review records.
- **Evidence field:** `Evidence (D3-Q4)` · _Tool, % coverage, metric, time window, link_

### D3-Q5: User-centric focus

**D3-Q5: Is AI-assisted work tied to clear user outcomes and informed by user feedback?**

- **Coverage unit:** teams
- **L3 looks like:** Work items reference the user problem and success measure; feedback is reviewed before prioritization.
- **L4 looks like:** User-outcome metrics are part of the definition of done for AI-assisted delivery.
- **Evidence examples:** Product briefs, feedback loop records, outcome dashboards.
- **Evidence field:** `Evidence (D3-Q5)` · _Tool, % coverage, metric, time window, link_

### D3-Q6: AI-assisted modernization

**D3-Q6: Are AI tools and agents used to understand, upgrade and migrate legacy code (for example framework or runtime upgrades, cloud migration), with results verified by tests?**

- **Coverage unit:** teams
- **L3 looks like:** A repeatable AI-assisted modernization process exists for common upgrade types, with test gates.
- **L4 looks like:** Modernization backlog is burned down continuously by agents under human review, with tracked success rates.
- **Evidence examples:** Upgrade runbooks, migration PRs, test results.
- **Evidence field:** `Evidence (D3-Q6)` · _Tool, % coverage, metric, time window, link_

---

## Section D4: Code and Context Engineering

_8 questions. Why it matters: GitHub measures adoption depth as a progression from "Code first" to "Agent first" to "Multi-agent" [6]; Anthropic describes context as "a finite resource with diminishing marginal returns" [25]._

### D4-Q1: Depth of AI use across surfaces

**D4-Q1: How deeply do engineers use AI across surfaces: completions and agent edits in the IDE, GitHub agent surfaces (cloud agent, code review, CLI), and several agents together?**

- **Scope note:** Measures how deeply AI is used. Whether that use is measured is D9-Q1.
- **Coverage unit:** engineers
- **L1 to L2 look like:** Mostly completions and agent edits in the IDE ("Code first"); chat-only use counts as Passive in GitHub's cohorts.
- **L3 looks like:** Many engineers regularly use at least one GitHub agent surface ("Agent first"), confirmed by usage metrics.
- **L4 looks like:** Multi-agent use is normal ("Multi-agent"), with cohort distribution tracked monthly.
- **Evidence examples:** Copilot usage metrics dashboard or API: adoption cohort distribution, daily/weekly active users.
- **Evidence field:** `Evidence (D4-Q1)` · _Tool, % coverage, metric, time window, link_

### D4-Q2: Agent mode for multi-file work

**D4-Q2: Do engineers use IDE agent mode (or equivalent) for multi-file changes, and review every change before committing?**

- **Coverage unit:** engineers
- **L3 looks like:** Agent mode is the default for multi-file refactors and features in most teams; changes are reviewed in the diff before commit.
- **L4 looks like:** Teams share agent-mode patterns that work and track where it fails; tool permissions are tuned per repository.
- **Evidence examples:** Usage by feature/mode, team guidelines.
- **Evidence field:** `Evidence (D4-Q2)` · _Tool, % coverage, metric, time window, link_

### D4-Q3: Coding agent delegation

**D4-Q3: Are coding agents (for example Copilot cloud agent) assigned issues and producing pull requests that are merged after human review?**

- **Scope note:** Measures how much work is delegated to coding agents. The autonomy policy is D1-Q5; task scoping is D3-Q3.
- **Coverage unit:** teams
- **L3 looks like:** Most teams delegate suitable issues to a coding agent; the share of merged PRs that are agent-authored is tracked.
- **L4 looks like:** Agent PR merge rate, rework and post-merge fix rate are tracked by task type; delegation rules (D1-Q5) are tuned from this data.
- **Evidence examples:** Agent-authored PR counts, merge rate, time to merge, follow-up fixes.
- **Evidence field:** `Evidence (D4-Q3)` · _Tool, % coverage, metric, time window, link_

### D4-Q4: Repository instructions

**D4-Q4: Do repositories contain versioned, reviewed custom instructions for AI tools (for example `.github/copilot-instructions.md`, `AGENTS.md`) describing build, test, conventions and constraints?**

- **Coverage unit:** repositories
- **L3 looks like:** Most active repositories have structured instructions (build, test, conventions, constraints) with an owner; changes go through PR review; files are updated when the codebase changes rather than committed once.
- **L4 looks like:** Instructions are generated from a shared baseline, checked for staleness, and their effect on agent merge rate and code quality is measured, since instruction files alone do not guarantee better results.
- **Evidence examples:** Instruction files, coverage across repositories, change history, before/after agent PR metrics.
- **Evidence field:** `Evidence (D4-Q4)` · _Tool, % coverage, metric, time window, link_

### D4-Q5: Reusable prompts, agents and skills

**D4-Q5: Is there a curated, shared library of reusable prompt files, custom agents and skills, with owners and versioning?**

- **Coverage unit:** teams
- **L3 looks like:** A central repository holds approved prompt files and custom agents; teams reuse them instead of copying.
- **L4 looks like:** Assets are evaluated before release (quality, cost), usage is tracked, and unused assets are retired.
- **Evidence examples:** Library repository, custom agent profiles, reuse metrics.
- **Evidence field:** `Evidence (D4-Q5)` · _Tool, % coverage, metric, time window, link_

### D4-Q6: MCP server governance

**D4-Q6: Are MCP servers and other agent tools governed through an allowlist or registry, with scoped tools and named owners?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** An enterprise MCP allowlist or custom registry is enforced; each server has an owner, a security review and limited tools.
- **L4 looks like:** Tool calls are logged and reviewed; new servers pass automated security checks before being added.
- **Evidence examples:** Allowlist or registry policy, MCP configuration, review records.
- **Evidence field:** `Evidence (D4-Q6)` · _Tool, % coverage, metric, time window, link_

### D4-Q7: AI access to internal knowledge

**D4-Q7: Can AI tools and agents securely use internal sources (code, documentation, wikis, work items) as context, through approved connectors?**

- **Coverage unit:** teams
- **L3 looks like:** Approved connectors give AI tools permission-aware access to the main internal sources; responses cite internal material.
- **L4 looks like:** Knowledge sources are curated for AI use (freshness, ownership) and retrieval quality is evaluated.
- **Evidence examples:** Connector configuration, retrieval evaluations.
- **Evidence field:** `Evidence (D4-Q7)` · _Tool, % coverage, metric, time window, link_

### D4-Q8: Model selection and routing

**D4-Q8: Is model choice matched to task complexity (smaller models for routine work, frontier models for complex work), by guidance or automatic routing?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** Written guidance maps task types to models; default models are set by policy.
- **L4 looks like:** Automatic routing is in place and tuned from cost and quality data.
- **Evidence examples:** Model guidance, policy settings, routing configuration.
- **Evidence field:** `Evidence (D4-Q8)` · _Tool, % coverage, metric, time window, link_

---

## Section D5: Review, Quality and Testing

_7 questions. Why it matters: DORA links AI-driven change volume to instability unless strong control systems exist [3]; GitHub requires human review before agent PRs merge [7]; 46% of developers distrust AI output accuracy [37]._

### D5-Q1: AI-assisted code review

**D5-Q1: Is AI code review (for example Copilot code review) applied to pull requests, with a human reviewer still accountable for approval?**

- **Coverage unit:** repositories
- **L3 looks like:** AI review runs automatically on most PRs; teams track useful vs dismissed suggestions.
- **L4 looks like:** Review rules are tuned per repository from suggestion outcomes; review time and escaped defects are tracked; PRs where only AI reviewed AI-authored code are visible and governed.
- **Evidence examples:** Repository rulesets, code review adoption metrics, suggestion outcomes.
- **Evidence field:** `Evidence (D5-Q1)` · _Tool, % coverage, metric, time window, link_

### D5-Q2: Human-in-the-loop for agent changes

**D5-Q2: Do agent-authored pull requests require independent human approval (not the requester), with workflow runs approved before they execute?**

- **Coverage unit:** repositories
- **L3 looks like:** Default protections are kept: agent PRs need an independent human approver (Copilot approvals, if enabled, do not count); "Approve and run workflows" is not disabled without a documented risk decision.
- **L4 looks like:** Approval requirements scale with risk (D1-Q5) and are audited; exceptions expire automatically.
- **Evidence examples:** Rulesets, branch protection, agent settings.
- **Evidence field:** `Evidence (D5-Q2)` · _Tool, % coverage, metric, time window, link_

### D5-Q3: Same quality gates for AI and human code

**D5-Q3: Do AI-generated and agent-authored changes pass the same required checks (build, tests, linting, security scans, coverage) as human changes?**

- **Coverage unit:** repositories
- **L3 looks like:** Required checks are enforced by rulesets on the protected branches of most repositories, with no bypass for agent identities.
- **L4 looks like:** Gates are policy as code, applied across all repositories (>90%) and reviewed after incidents.
- **Evidence examples:** Rulesets, required checks, bypass lists.
- **Evidence field:** `Evidence (D5-Q3)` · _Tool, % coverage, metric, time window, link_

### D5-Q4: Small batches

**D5-Q4: Are changes kept small (limits on PR size, one concern per PR), including changes produced by agents?**

- **Scope note:** Measures the size of AI-assisted changes. How often code is committed and how fast it is rolled back is D8-Q2.
- **Coverage unit:** teams
- **L3 looks like:** PR size guidance is enforced or monitored; oversized agent PRs are split before review.
- **L4 looks like:** Batch size is tracked against change failure rate and review time and used to adjust limits.
- **Evidence examples:** PR size distribution, bot or ruleset configuration.
- **Evidence field:** `Evidence (D5-Q4)` · _Tool, % coverage, metric, time window, link_

### D5-Q5: AI-assisted testing

**D5-Q5: Is AI used to generate and maintain tests, with test quality checked (for example coverage of changed code, mutation testing) rather than only test count?**

- **Scope note:** Measures AI used to write and improve tests. Whether automated tests act as a gate is D8-Q7.
- **Coverage unit:** teams
- **L3 looks like:** Most teams use AI to write tests; coverage of changed lines is a required check.
- **L4 looks like:** Test effectiveness (mutation score, escaped defects) is tracked; flaky tests are detected and quarantined automatically.
- **Evidence examples:** Coverage reports, mutation-testing results, flaky-test dashboard.
- **Evidence field:** `Evidence (D5-Q5)` · _Tool, % coverage, metric, time window, link_

### D5-Q6: Verification culture and calibrated trust

**D5-Q6: Do engineers systematically verify AI output (run it, test it, read it) and is trust in AI output measured over time?**

- **Scope note:** Measures review behaviour and trust calibration. How developer experience is surveyed is D9-Q4.
- **Coverage unit:** teams
- **L3 looks like:** Review guidelines explain what to check in AI output; trust in AI output is part of the developer survey.
- **L4 looks like:** Trust and accuracy are compared with real defect data, and guidance is updated where they diverge.
- **Evidence examples:** Review guidelines, survey results, defect analysis.
- **Evidence field:** `Evidence (D5-Q6)` · _Tool, % coverage, metric, time window, link_

### D5-Q7: Code health of AI-generated code

**D5-Q7: Is the long-term health of AI-generated code monitored (duplication, churn, complexity, maintainability)?**

- **Coverage unit:** repositories
- **L3 looks like:** Code-health metrics are collected for most repositories and reviewed in team retrospectives; AI-generated code has a named human owner.
- **L4 looks like:** Health trends (for example cognitive complexity, static-analysis warnings) are compared between AI-heavy and other code, with corrective actions tracked.
- **Evidence examples:** Static analysis dashboards, churn reports, ownership files.
- **Evidence field:** `Evidence (D5-Q7)` · _Tool, % coverage, metric, time window, link_

---

## Section D6: Security and AI Supply Chain

_7 questions. Why it matters: OWASP lists prompt injection (LLM01:2025), supply chain (LLM03:2025) and excessive agency (LLM06:2025) among the top risks [38], and agent goal hijack (ASI01) first for agentic applications [39]; NIST SP 800-218A adds practices for AI model development to the SSDF [40]._

### D6-Q1: Baseline scanning on every repository

**D6-Q1: Are code scanning (SAST), secret scanning with push protection, and dependency review applied to all repositories, including agent branches?**

- **Coverage unit:** repositories
- **L3 looks like:** Enabled by default for all new and most existing repositories; push protection applies to every commit, human or agent; alerts have owners and service-level targets.
- **L4 looks like:** Coverage is near complete and verified automatically; mean time to remediate is tracked.
- **Evidence examples:** Security coverage dashboard, remediation time.
- **Evidence field:** `Evidence (D6-Q1)` · _Tool, % coverage, metric, time window, link_

### D6-Q2: AI-assisted remediation

**D6-Q2: Is AI-assisted remediation (for example autofix for code scanning) used to fix vulnerabilities, with fixes reviewed and tested before merge?**

- **Coverage unit:** repositories
- **L3 looks like:** Autofix suggestions are enabled for most repositories; acceptance and reopen rates are tracked.
- **L4 looks like:** Security campaigns use AI remediation at scale, and remediation time is reported to leadership.
- **Evidence examples:** Autofix settings, remediation metrics.
- **Evidence field:** `Evidence (D6-Q2)` · _Tool, % coverage, metric, time window, link_

### D6-Q3: Prompt injection defenses for agents

**D6-Q3: Are agents protected against prompt injection and goal hijack (untrusted content treated as data, hidden instructions filtered, network egress restricted)?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** Agent firewalls and egress restrictions are kept on; guidance tells teams which content sources are untrusted.
- **L4 looks like:** Agents are red-teamed regularly against OWASP LLM01:2025 and ASI01 scenarios; findings are tracked to closure.
- **Evidence examples:** Firewall configuration, red-team reports.
- **Evidence field:** `Evidence (D6-Q3)` · _Tool, % coverage, metric, time window, link_

### D6-Q4: Least privilege for agents

**D6-Q4: Do agents run with least privilege (scoped tokens, no production secrets, restricted branches, sandboxed environments)?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** Agent permissions are documented and reviewed; agents cannot reach production credentials or push to protected branches.
- **L4 looks like:** Permissions are just-in-time and time-bound; access is reviewed automatically.
- **Evidence examples:** Agent environment configuration, token scopes, access reviews.
- **Evidence field:** `Evidence (D6-Q4)` · _Tool, % coverage, metric, time window, link_

### D6-Q5: AI supply chain

**D6-Q5: Are models, MCP servers, IDE extensions and agent tools vetted before use, with provenance and SBOMs for what you build and ship?**

- **Coverage unit:** repositories
- **L3 looks like:** A review process covers AI components; SBOMs and build provenance are produced for most builds.
- **L4 looks like:** Provenance is verified at deployment (for example SLSA level targets); unvetted components are blocked automatically.
- **Evidence examples:** Component review records, SBOM and attestation samples.
- **Evidence field:** `Evidence (D6-Q5)` · _Tool, % coverage, metric, time window, link_

### D6-Q6: Threat modeling for AI features and agents

**D6-Q6: Are AI features and agentic workflows threat-modeled with AI-specific risks (OWASP LLM and Agentic Top 10, NIST SP 800-218A)?**

- **Coverage unit:** services
- **L3 looks like:** Threat models are required for new AI features and agent workflows and reviewed by security.
- **L4 looks like:** Threat models are updated after incidents and red-team exercises; controls are verified by automated tests.
- **Evidence examples:** Threat model documents, security review records.
- **Evidence field:** `Evidence (D6-Q6)` · _Tool, % coverage, metric, time window, link_

### D6-Q7: Audit trail for agent actions

**D6-Q7: Are agent sessions and actions (prompts, tool calls, commits, approvals) logged, attributable to an identity, and retained according to policy?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** Agent activity is logged centrally and linked to the requesting user and the agent identity.
- **L4 looks like:** Logs feed anomaly detection; audits can reconstruct any agent change end to end.
- **Evidence examples:** Audit log configuration, sample investigation.
- **Evidence field:** `Evidence (D6-Q7)` · _Tool, % coverage, metric, time window, link_

---

## Section D7: Deliver and Operate

_6 questions. Why it matters: more AI-generated change needs strong delivery safety nets [3], [5]; Microsoft recommends continuous observation of agent activity [19] and is extending agents to cloud operations [22]._

### D7-Q1: AI in CI/CD pipelines

**D7-Q1: Is AI used to author, maintain and troubleshoot CI/CD pipelines (for example explaining failed runs, proposing fixes), on top of pipeline-as-code?**

- **Coverage unit:** repositories
- **L3 looks like:** Pipelines are code in most repositories; AI-assisted failure analysis is available to all teams.
- **L4 looks like:** Agents propose pipeline fixes and optimizations automatically, under review, with build time and failure rate tracked.
- **Evidence examples:** Pipeline repositories, failure-analysis usage, build metrics.
- **Evidence field:** `Evidence (D7-Q1)` · _Tool, % coverage, metric, time window, link_

### D7-Q2: Progressive delivery and rollback

**D7-Q2: Can teams release AI-assisted changes safely through progressive delivery (feature flags, canary or blue/green) and automated rollback?**

- **Coverage unit:** services
- **L3 looks like:** Most services use feature flags or staged rollout; rollback is automated for critical services.
- **L4 looks like:** Rollout decisions are driven by health signals automatically; change failure rate and recovery time are tracked per service.
- **Evidence examples:** Feature flag platform, rollout configuration, rollback records.
- **Evidence field:** `Evidence (D7-Q2)` · _Tool, % coverage, metric, time window, link_

### D7-Q3: AI-assisted incident response

**D7-Q3: Is AI used in incident response (alert correlation, summarization, root-cause hypotheses, post-incident review drafts) with humans in command?**

- **Coverage unit:** services
- **L3 looks like:** On-call engineers in most teams use AI for triage and summaries; post-incident reviews record whether AI helped.
- **L4 looks like:** Operations agents run approved diagnostics automatically; time to restore is compared before and after adoption.
- **Evidence examples:** Incident tooling configuration, incident timelines, time-to-restore data.
- **Evidence field:** `Evidence (D7-Q3)` · _Tool, % coverage, metric, time window, link_

### D7-Q4: Observability of agents

**D7-Q4: Are AI agents in the SDLC observable (traces of runs and tool calls, latency, failures, cost), for example through OpenTelemetry?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** Agent runs emit telemetry to the central observability stack; dashboards show failures and cost per agent.
- **L4 looks like:** Alerts fire on agent drift, error spikes or cost anomalies; findings feed governance (D1).
- **Evidence examples:** Telemetry dashboards, alert rules.
- **Evidence field:** `Evidence (D7-Q4)` · _Tool, % coverage, metric, time window, link_

### D7-Q5: Infrastructure as code with guardrails

**D7-Q5: Is AI used to write and review infrastructure as code, with policy-as-code guardrails that block non-compliant changes?**

- **Coverage unit:** services
- **L3 looks like:** Most infrastructure is code; AI-generated IaC passes the same policy checks and plan reviews.
- **L4 looks like:** Drift is detected and corrected through GitOps; policy violations by AI-generated IaC are tracked and trending down.
- **Evidence examples:** IaC repositories, policy-as-code rules, drift reports.
- **Evidence field:** `Evidence (D7-Q5)` · _Tool, % coverage, metric, time window, link_

### D7-Q6: Agent-driven operational automation

**D7-Q6: Are operational tasks (runbooks, remediation, dependency and patch updates) automated by agents under defined approval rules?**

- **Coverage unit:** services
- **L3 looks like:** Common runbooks and dependency updates are automated; approvals follow the autonomy matrix (D1-Q5).
- **L4 looks like:** Most routine operations run automatically with audited approvals; human effort shifts to exceptions.
- **Evidence examples:** Automation catalog, approval logs.
- **Evidence field:** `Evidence (D7-Q6)` · _Tool, % coverage, metric, time window, link_

---

## Section D8: Engineering Foundations (AI amplifiers)

_7 questions. Why it matters: DORA finds that these capabilities amplify the benefits of AI adoption, and that a high-quality internal platform correlates with the ability to unlock AI value [1], [3]._

### D8-Q1: Version control for everything

**D8-Q1: Are application code, configuration, build automation, system configuration and AI prompts/instructions all stored in version control?**

- **Coverage unit:** teams
- **L3 looks like:** All five asset types are versioned for most services.
- **L4 looks like:** Nothing reaches production without a versioned source; checks confirm this automatically.
- **Evidence examples:** Repository inventory, configuration sources.
- **Evidence field:** `Evidence (D8-Q1)` · _Tool, % coverage, metric, time window, link_

### D8-Q2: Commit frequency and fast rollback

**D8-Q2: Do engineers commit small changes frequently and rely on fast undo/revert when experimenting with AI output?**

- **Scope note:** Measures commit frequency and rollback speed. The size of AI-assisted changes is D5-Q4.
- **Coverage unit:** teams
- **L3 looks like:** Most engineers commit at least daily; reverting a change is routine and fast.
- **L4 looks like:** Trunk-based development with short-lived branches is the norm; revert time is measured.
- **Evidence examples:** Commit frequency data, branch age.
- **Evidence field:** `Evidence (D8-Q2)` · _Tool, % coverage, metric, time window, link_

### D8-Q3: Quality internal platform

**D8-Q3: Is there an internal developer platform that is easy to use, abstracts infrastructure, and makes the secure and compliant path the default for humans and agents?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** A dedicated platform team offers self-service golden paths used by most teams; the team acts on feedback.
- **L4 looks like:** Agents use the same platform APIs and guardrails as humans; platform satisfaction is measured and improving.
- **Evidence examples:** Platform catalog, golden paths, satisfaction survey.
- **Evidence field:** `Evidence (D8-Q3)` · _Tool, % coverage, metric, time window, link_

### D8-Q4: Healthy data ecosystem

**D8-Q4: Can engineers and AI tools find and use reliable internal data (not siloed, good quality, answerable quickly)?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** Key data is cataloged with owners and quality indicators; most questions can be answered within an hour.
- **L4 looks like:** Data quality is monitored automatically; lineage and contracts are in place for critical data.
- **Evidence examples:** Data catalog, quality dashboards.
- **Evidence field:** `Evidence (D8-Q4)` · _Tool, % coverage, metric, time window, link_

### D8-Q5: Reproducible environments for humans and agents

**D8-Q5: Are development environments reproducible (devcontainers, cloud workspaces, pinned toolchains) so that humans and agents build and test the same way?**

- **Coverage unit:** repositories
- **L3 looks like:** Most repositories define a reproducible environment; agents use the same definition.
- **L4 looks like:** Environments start in minutes for any repository; drift from the definition is detected.
- **Evidence examples:** Devcontainer files, environment start-up times.
- **Evidence field:** `Evidence (D8-Q5)` · _Tool, % coverage, metric, time window, link_

### D8-Q6: Documentation as AI-ready context

**D8-Q6: Is documentation kept as code, current and owned, so it can serve as reliable context for AI tools?**

- **Coverage unit:** repositories
- **L3 looks like:** Docs live next to code with owners; stale docs are flagged in reviews.
- **L4 looks like:** Freshness is checked automatically; AI-generated doc changes are reviewed like code.
- **Evidence examples:** Docs repositories, freshness checks.
- **Evidence field:** `Evidence (D8-Q6)` · _Tool, % coverage, metric, time window, link_

### D8-Q7: Automated testing as a control system

**D8-Q7: Is automated testing deep and fast enough to catch regressions from high volumes of AI-generated change (unit, integration, end-to-end, contract)?**

- **Scope note:** Measures automated tests as a control system. AI used to write tests is D5-Q5.
- **Coverage unit:** services
- **L3 looks like:** Most services have layered automated tests that run on every PR within agreed time budgets.
- **L4 looks like:** Test suites are tuned from escaped-defect data; feedback time is tracked and improving.
- **Evidence examples:** Test suite inventory, pipeline durations, escaped-defect data.
- **Evidence field:** `Evidence (D8-Q7)` · _Tool, % coverage, metric, time window, link_

---

## Section D9: Measurement, Value and AI FinOps

_7 questions. Why it matters: controlled studies range from 55.8% faster [33] and 26.08% more completed tasks [34] to 19% slower with a strong perception gap [35], so organizations need their own objective measurement; Gartner predicts AI coding costs will overtake the average developer's salary by 2028 [32]._

### D9-Q1: Adoption depth metrics

**D9-Q1: Is AI adoption tracked with telemetry beyond seat counts (active users, engagement by feature, adoption cohorts)?**

- **Scope note:** Measures whether adoption is tracked. How deeply AI is used is D4-Q1.
- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** Usage metrics (for example the Copilot usage metrics API or dashboard) are reviewed monthly by engineering leadership.
- **L4 looks like:** Cohort movement is a managed target; enablement actions are evaluated by their effect on cohorts.
- **Evidence examples:** Usage dashboards, cohort trend reports.
- **Evidence field:** `Evidence (D9-Q1)` · _Tool, % coverage, metric, time window, link_

### D9-Q2: Delivery outcome metrics

**D9-Q2: Are software delivery metrics (lead time, deployment frequency, change failure rate, time to restore) tracked and compared before and after AI adoption?**

- **Coverage unit:** services
- **L3 looks like:** DORA metrics are collected automatically for most services and reviewed with AI adoption data.
- **L4 looks like:** Delivery metrics are part of AI investment decisions; regressions trigger corrective action.
- **Evidence examples:** DORA dashboards, baseline vs current comparison.
- **Evidence field:** `Evidence (D9-Q2)` · _Tool, % coverage, metric, time window, link_

### D9-Q3: Pull request flow metrics

**D9-Q3: Are PR throughput, time to merge and the share and merge rate of AI- or agent-authored PRs tracked?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** PR lifecycle metrics are reported per organization; agent-authored PRs are identified separately, including their post-merge fix rate.
- **L4 looks like:** Flow metrics are tied to quality metrics (D5) so that faster flow is not bought with instability.
- **Evidence examples:** PR lifecycle metrics, agent PR reports, follow-up fix analysis.
- **Evidence field:** `Evidence (D9-Q3)` · _Tool, % coverage, metric, time window, link_

### D9-Q4: Developer experience and friction

**D9-Q4: Is developer experience measured regularly (perceived productivity, friction, trust in AI, satisfaction), using a recognized framework such as SPACE or the DORA outcome questions?**

- **Scope note:** Measures the developer experience survey. Review behaviour and trust calibration is D5-Q6.
- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** A survey runs at least twice a year with good participation; results are shared and acted on.
- **L4 looks like:** Survey results are combined with telemetry (D9-Q1 to Q3) to find and remove friction.
- **Evidence examples:** Survey instrument, participation rate, action log.
- **Evidence field:** `Evidence (D9-Q4)` · _Tool, % coverage, metric, time window, link_

### D9-Q5: Controlled measurement of impact

**D9-Q5: Is AI impact estimated with controlled or cohort-based comparisons (for example pilot vs control, adoption cohorts, before/after with a baseline) rather than only self-reported estimates?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** At least one controlled or cohort comparison has been run and documented, with its limitations.
- **L4 looks like:** Comparisons run continuously for major tools and practices; decisions cite them.
- **Evidence examples:** Study design, results, decision records.
- **Evidence field:** `Evidence (D9-Q5)` · _Tool, % coverage, metric, time window, link_

### D9-Q6: AI cost governance (AI FinOps)

**D9-Q6: Are AI costs (seats, premium requests, tokens, agent runs) budgeted, monitored per team and use case, with thresholds and regular reviews?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** Budgets and alert thresholds exist per organization or team; high-consumption workflows are reviewed in retrospectives.
- **L4 looks like:** Cost per outcome (for example per merged PR) is tracked; routing and context practices are tuned to reduce waste.
- **Evidence examples:** Cost dashboards, budget alerts, retrospective notes.
- **Evidence field:** `Evidence (D9-Q6)` · _Tool, % coverage, metric, time window, link_

### D9-Q7: Business value linkage

**D9-Q7: Are AI engineering outcomes connected to business value (business case, ROI assumptions, OKRs) and reviewed with finance or business stakeholders?**

- **Coverage unit:** organization-wide practice (use the governance and measurement columns)
- **L3 looks like:** A business case with explicit assumptions exists and is reviewed at least yearly.
- **L4 looks like:** Value is reported on a fixed cadence with measured inputs from D9-Q1 to Q6; investment is adjusted from results.
- **Evidence examples:** Business case, value reports.
- **Evidence field:** `Evidence (D9-Q7)` · _Tool, % coverage, metric, time window, link_
