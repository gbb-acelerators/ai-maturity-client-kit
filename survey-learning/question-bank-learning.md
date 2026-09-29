# Microsoft Forms Questions: Learning & Growth Survey

🌐 English · [Português (Brasil)](question-bank-learning.pt-br.md) · [Español](question-bank-learning.es.md)

> **IDENTIFIED survey** (name + email) with 32 questions across 7 sections. Estimated time: **5-8 min**. Focuses on what developers want to LEARN, preferred formats, barriers, and Champions.

**How this differs from the other surveys:**

- Main Assessment: organizational maturity (Likert L0-L4)

- Developer Survey: anonymous behavioral baseline

- **This Learning Survey: IDENTIFIED training roadmap** (name + email required to invite people to the right workshops)

## How to Create the Form

1. Go to <https://forms.office.com> -> **+ New Form**
2. Title: `AI Learning & Growth: What do you want to learn in the next 6 months?`
3. Subtitle:

   > 5-8 min survey about your AI training plan. IDENTIFIED (we need name + email to invite you to the right workshops). Output: personalized training plan + cohorts + Champions Network.

   Add this privacy notice below the subtitle (fill in the angle brackets with your privacy or legal team):

   > **Privacy notice.** This survey collects your name, email, role, and squad to plan training, invite you to workshops, and build the Champions Network. Answers are not used for performance reviews. Controller and contact: `<team / email>`. Access: `<who can see individual answers>`. Retention: `<period>`, then deleted. You can ask to see, correct, or delete your answers at `<contact>`. By submitting, you agree to this use.

4. **Settings**:
   - ☐ **Anonymous responses** (OFF, this survey is identified)
   - ☑ **Only people in my organization** (recommended)
   - ☑ **One response per person**
   - ☑ **Accept responses**
   - ☑ Email notification of each response
5. Add 7 sections (one per L1..L7):
   - **L1: Identification** (4 questions)
   - **L2: AI maturity self-perception** (7 questions)
   - **L3: Where you want to grow** (2 questions)
   - **L4: Specific topics you want to learn** (5 questions)
   - **L5: Preferred format and cadence** (4 questions)
   - **L6: Champions and mentoring** (5 questions)
   - **L7: Barriers and wishlist** (5 questions)

6. For each question below:
   - **`choice`** -> Choice (Single answer)
   - **`multi`** -> Choice (Multiple answers)
   - **`text`** -> Long Text
   - **`text-short`** -> Short Text (one line)

7. The **TITLE** must always start with the ID + colon. Example: `L4-Q1: Which GitHub Copilot topics do you want to master?`

8. **Required**: mark L1-Q1 (name) and L1-Q2 (email) as required. All others are optional.
9. Share via **Send -> Link** with all developers in scope.
10. When responses are ready: **Responses -> Open in Excel** -> rename to `survey-learning-responses.xlsx` -> move to the kit root.

---

## L1: Identification

_IDENTIFIED survey. We use your name/email to invite you to the right workshops and cohorts. Individual answers are not shared publicly._

_4 questions in this section._

### Question `L1-Q1`: _Short Text (one line)_

> **L1-Q1: Your full name:**

### Question `L1-Q2`: _Short Text (one line)_

> **L1-Q2: Corporate email (for workshop invitations):**

### Question `L1-Q3`: _Choice (single answer)_

> **L1-Q3: Role:**

Options:

- Backend Developer

- Frontend Developer

- Full-Stack

- SRE / Platform Engineer

- Data Engineer / ML Engineer

- Architect

- Tech Lead

- Engineering Manager

- QA / SDET

- DevOps / DevEx

- Other

### Question `L1-Q4`: _Choice (single answer)_

> **L1-Q4: Team / Squad:**

Options:

- [Customize with the organization's team list]

- Other / I do not belong to a fixed squad

---

## L2: AI Maturity Self-Perception

_Rate your confidence TODAY in each of the 7 maturity-rubric dimensions. Honest answers make the plan better._

_7 questions in this section._

### Question `L2-Q1`: _Choice (single answer)_

> **L2-Q1: DS-D2 Copilot Adoption (Ask/Edit/Agent/Coding Agent modes, features, measured gains): what is your level?**

Options:

- L0: I have never used it or do not know it

- L1: I know the basics (inline completion)

- L2: I use Ask/Edit day to day

- L3: I use Agent + Spaces and measure gains

- L4: I master autonomous Coding Agent and the team's prompt library

### Question `L2-Q2`: _Choice (single answer)_

> **L2-Q2: DS-D3 Microsoft/GitHub Tooling (Foundry, Spaces, Coding Agent, MCP, Spec Kit, GHAS): what is your level?**

Options:

- L0: I do not know the ecosystem

- L1: I know the names only

- L2: I use 2-3 basic tools

- L3: I use 4+ advanced tools

- L4: I master the full ecosystem, including Foundry/MCP

### Question `L2-Q3`: _Choice (single answer)_

> **L2-Q3: DS-D4 AI Dev Practices (TDD with AI, SDD, pair programming, debugging with AI): what is your level?**

Options:

- L0: No structured practices

- L1: I use AI occasionally

- L2: I use TDD or SDD occasionally

- L3: I treat AI as a pair across multiple phases

- L4: Full pair-programmer mindset + SDD with Spec Kit

### Question `L2-Q4`: _Choice (single answer)_

> **L2-Q4: DS-D5 Agent Concepts (custom agents, skills, prompts, MCP, A2A, handoffs, subagents, Agentic DevOps personas): what is your level?**

Options:

- L0: I do not know what an agent is

- L1: I know only the basics

- L2: I know the Copilot modes

- L3: I have created custom agents/skills/prompts

- L4: I master MCP, A2A, subagents, and agent testing

### Question `L2-Q5`: _Choice (single answer)_

> **L2-Q5: DS-D6 Instructions / Memory (copilot-instructions.md, AGENTS.md, CLAUDE.md, Spaces, prompt library): what is your level?**

Options:

- L0: I do not use instruction files

- L1: I have 1 basic file

- L2: I use and update them occasionally

- L3: The team actively maintains them

- L4: Shared prompt library + collaborative Spaces

### Question `L2-Q6`: _Choice (single answer)_

> **L2-Q6: DS-D7 Best Practices (Champion, DORA/DX metrics, community, prompt sharing): what is your level?**

Options:

- L0: I do not have a structured AI culture

- L1: Isolated self-learning

- L2: I have a Champion in the team

- L3: I measure DORA/DX and share with peers

- L4: Active community + regular adoption review

### Question `L2-Q7`: _Choice (single answer)_

> **L2-Q7: DS-D8 Security & Governance (AI policy, GHAS, SBOM, JIT permissions, agent red-lines, audit): what is your level?**

Options:

- L0: No policy, no tools

- L1: Informal policy

- L2: GHAS active + basic policy

- L3: Mandatory scanners + SBOM + training

- L4: JIT permissions + red-lines docs + reviewed audit

---

## L3: Where You Want to Grow

_Thinking about the next 6 months, which dimensions do you MOST want to grow in?_

_2 questions in this section._

### Question `L3-Q1`: _Choice (multiple answers)_

> **L3-Q1: Select the 3 PRIORITY dimensions for your growth in the next 6 months (choose exactly 3):**

Options:

- DS-D2 Copilot Adoption (advanced modes, Coding Agent)

- DS-D3 MS/GH Tooling (Foundry, Spaces, Spec Kit, MCP)

- DS-D4 AI Dev Practices (TDD with AI, SDD)

- DS-D5 Agent Concepts (custom agents, MCP, A2A)

- DS-D6 Instructions / Memory (instruction files, prompt library)

- DS-D7 Best Practices (DORA, community, mentoring)

- DS-D8 Security & Governance (GHAS, SBOM, red-lines)

### Question `L3-Q2`: _Long Text (free response)_

> **L3-Q2: Why did you choose these 3 dimensions? (1-2 sentences, optional but very helpful)**

---

## L4: Specific Topics You Want to Learn

_Select ALL topics you would like to learn or deepen._

_5 questions in this section._

### Question `L4-Q1`: _Choice (multiple answers)_

> **L4-Q1: Which GitHub Copilot topics do you want to master?**

Options:

- Ask mode (effective questions)

- Edit mode (multi-file editing)

- Agent mode (autonomous in the IDE)

- Coding Agent (autonomous on GitHub.com, assigned issues, opens PRs)

- Copilot Spaces (shared context)

- PR review with Copilot

- Test generation

- Slash commands (/explain, /fix, /tests)

- Copilot CLI

- I already master all of this

### Question `L4-Q2`: _Choice (multiple answers)_

> **L4-Q2: Which Microsoft Foundry / Azure AI topics do you want to learn?**

Options:

- Microsoft Foundry overview

- Foundry Agent Service (create agents)

- Azure OpenAI Service (direct API)

- Embeddings + RAG

- MCP (Model Context Protocol) + Foundry MCP server

- A2A (Agent-to-Agent) protocol

- Multi-agent orchestration

- Connectors (Dynamics, SAP, SharePoint)

- Foundry Memory (long-term context)

- I am not interested in Foundry right now

### Question `L4-Q3`: _Choice (multiple answers)_

> **L4-Q3: Which AI practice topics do you want to learn?**

Options:

- TDD with AI (test-first with Copilot)

- SDD with Spec Kit (Spec-Driven Development)

- Prompt engineering (advanced techniques)

- Pair programming with AI (mindset + practices)

- Refactoring with AI

- Code review with AI before PR

- AI-assisted debugging

- Onboarding into a new project with AI + Spaces

- Automatic documentation

### Question `L4-Q4`: _Choice (multiple answers)_

> **L4-Q4: Which agent and primitive topics do you want to learn?**

Options:

- Create custom agents (.agent.md)

- Create custom skills (SKILL.md)

- Create prompt files (.prompt.md)

- Configure a custom MCP server

- Subagents (delegation)

- Handoffs between agents

- Agentic DevOps personas (System Designer, Agent Operator)

- Test agents (test suites for prompts/skills)

- Guardrails / agent red-lines

### Question `L4-Q5`: _Choice (multiple answers)_

> **L4-Q5: Which security and governance topics do you want to learn?**

Options:

- GitHub Advanced Security (CodeQL, secret scanning)

- SBOM (Software Bill of Materials)

- Microsoft Defender for DevOps / Cloud

- DLP for AI prompts

- JIT permissions for agents

- AI audit logs + analysis

- AI usage policy (templates)

- Common vulnerabilities in AI-generated code

- Compliance / LGPD / GDPR + AI

---

## L5: Preferred Format and Cadence

_How do you learn best?_

_4 questions in this section._

### Question `L5-Q1`: _Choice (multiple answers)_

> **L5-Q1: Which learning formats work best for you?**

Options:

- Hands-on workshop in person/remote (3-4h)

- Short workshop (1h, sandwich seminar)

- Self-paced online course (Coursera, Pluralsight, MS Learn)

- Pair programming with a Champion

- Weekly office hours (open Q&A)

- Short videos (YouTube, Microsoft Learn)

- Podcast

- Book club / paper club

- Internal hackathon

- Peer show & tell

- Written documentation + trial and error

### Question `L5-Q2`: _Choice (single answer)_

> **L5-Q2: How much time per WEEK would you dedicate to learning AI/Copilot?**

Options:

- < 1h/week

- 1-2h/week

- 2-4h/week

- 4-6h/week

- More than 6h/week

### Question `L5-Q3`: _Choice (multiple answers)_

> **L5-Q3: Which time/day works best for synchronous workshops?**

Options:

- Wednesday/Thursday morning

- Wednesday/Thursday afternoon

- Friday afternoon (low-stress)

- Lunch time (lunch & learn)

- After hours (with overtime)

- I cannot attend synchronous sessions, self-paced only

### Question `L5-Q4`: _Choice (single answer)_

> **L5-Q4: Do you prefer cohorts (fixed group learning together) or self-paced learning?**

Options:

- Cohort (fixed group, more accountability)

- Self-paced (my pace, more flexibility)

- Hybrid (self-paced modules + synchronous sessions)

- No preference

---

## L6: Champions and Mentoring

_About internal community and mentoring._

_5 questions in this section._

### Question `L6-Q1`: _Choice (single answer)_

> **L6-Q1: Would you volunteer as an AI Champion in your team/company (help others, organize workshops)?**

Options:

- Yes, I want to be an active Champion

- Yes, but only with dedicated support/training

- Maybe, I need to think about it

- I am not interested right now

### Question `L6-Q2`: _Long Text (free response)_

> **L6-Q2: Who in your team/company do you consider an AI reference today? (name optional, helps map natural champions)**

### Question `L6-Q3`: _Choice (single answer)_

> **L6-Q3: Would you like 1:1 mentoring with someone more experienced in AI?**

Options:

- Yes, senior AI mentor

- Yes, peer mentoring (same level, mutual exchange)

- No, I prefer self-learning

- Other (specify in free text)

### Question `L6-Q4`: _Choice (single answer)_

> **L6-Q4: Would you offer to mentor/teach OTHER people on any topic?**

Options:

- Yes, on several topics

- Yes, on 1 specific topic

- Maybe, depends on the topic

- I do not feel ready

### Question `L6-Q5`: _Long Text (free response)_

> **L6-Q5: If you answered yes to the previous question, which topic(s) would you feel comfortable mentoring on?**

---

## L7: Barriers and Wishlist

_What prevents you from learning more? Which workshop would you like to organize or attend?_

_5 questions in this section._

### Question `L7-Q1`: _Choice (multiple answers)_

> **L7-Q1: Which BARRIERS prevent you from learning more about AI today?**

Options:

- Lack of time (sprint pressure)

- Lack of Copilot license

- Lack of Foundry / Azure AI license

- Lack of space to experiment (sandbox / test repo)

- Lack of structured training

- Lack of Champion in the team

- Security policy blocks experiments

- I do not know where to start

- I do not see clear leadership priority

- Lack of budget for paid courses

- All good, no significant barriers

### Question `L7-Q2`: _Long Text (free response)_

> **L7-Q2: Which internal workshop would you like to exist (even if ambitious)?**

### Question `L7-Q3`: _Long Text (free response)_

> **L7-Q3: Which external speaker (internal/partner/community) would you like to bring?**

### Question `L7-Q4`: _Long Text (free response)_

> **L7-Q4: Anything else you want to share about your AI learning goals?**

### Question `L7-Q5`: _Choice (single answer)_

> **L7-Q5: Do you want to receive the consolidated training plan (result of this survey) by email?**

Options:

- Yes, I want to see the plan and suggested workshops

- No, thank you

---

## Summary

- **7 sections**
- **32 questions** (15 choice + 9 multi + 8 text)
- **Time:** 5-8 min
- **Identified** (requires name + email)

## Next Steps

1. Collect responses (1-2 weeks, send one reminder per week)
2. Export Excel -> rename `survey-learning-responses.xlsx` -> move to the kit root
3. In Copilot Chat (Agent mode):

   ```text
   /import-survey-learning
   /training-plan
   ```

4. Receive the prioritized training plan in `output/training-plan-<date>.md`
