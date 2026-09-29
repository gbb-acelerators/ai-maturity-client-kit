# Microsoft Forms Questions: Developer Survey (GitHub + AI)

🌐 English · [Português (Brasil)](question-bank-devs.pt-br.md) · [Español](question-bank-devs.es.md)

75 questions in 9 sections. Estimated time: **20-25 min**. ANONYMOUS, we do not ask for respondent name or email.

**Runtime note:** This localized bank translates instructions, question titles and answer options. `survey-devs/options.json` maps every English, Spanish and Portuguese option to the same canonical option, so scoring works for a form built in any of the three languages (older Portuguese forms with dashes in the options still parse). Keep all IDs (`Sx-Qy:`) unchanged in Microsoft Forms.

## How to Create the Form

1. Go to <https://forms.office.com> -> **+ New Form**.
2. Suggested title: `Developer Survey: How my team uses GitHub & AI today`.
3. Subtitle suggestion: Anonymous survey (20-25 min) about your GitHub Copilot practices, Copilot Chat modes (Ask/Edit/Agent), AI agents, instruction files, AI + Dev best practices, and security. Your answers will inform the team AI adoption roadmap.
4. Settings: enable **Anonymous responses**, disable **One response per person**, and keep **Accept responses** enabled.
5. Add 9 sections: S1 Respondent profile, S2 GitHub Copilot Adoption and Modes, S3 Other Microsoft / GitHub AI tools, S4 AI Development Practices, S5 Agent Concepts and Structure, S6 Markdown / Memory / Instructions, S7 Usability and Best Practices, S8 Security and Governance, S9 Pain Points & Wishlist.
6. For each question below, add the corresponding Forms type: `choice`, `multi`, or `text`.
7. The **TITLE** of each question must start with the ID + colon. Example: `S2-Q1: Do you have an active GitHub Copilot license?`
8. The ID is used by `/import-survey-devs` for mapping. DO NOT REMOVE it.
9. Share via **+ Send / Collect responses** -> copy link -> send via Slack/Teams/email.
10. When responses are ready, **Responses -> Open in Excel** -> rename to `survey-devs-responses.xlsx` -> move to the kit root.

---

## S1: Respondent profile

_Basic questions about you and your context. Anonymous: we will not ask for name or email._

_7 questions in this section._

### Question `S1-Q1`: _Choice (single answer)_

> **S1-Q1: What is your current role?**

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

### Question `S1-Q2`: _Choice (single answer)_

> **S1-Q2: Total time as a developer?**

Options:

- < 2 years
- 2-5 years
- 6-10 years
- 11-15 years
- > 15 years

### Question `S1-Q3`: _Choice (single answer)_

> **S1-Q3: How long have you used AI in development (Copilot, Cursor, Claude Code, etc.)?**

Options:

- Never used it
- < 3 months
- 3-12 months
- 1-2 years
- > 2 years

### Question `S1-Q4`: _Choice (multiple answers)_

> **S1-Q4: Main languages you use day to day?**

Options:

- TypeScript / JavaScript
- Python
- C# / .NET
- Java / Kotlin
- Go
- Rust
- C++
- Ruby
- PHP
- Swift
- SQL (primary focus)
- Other

### Question `S1-Q5`: _Choice (single answer)_

> **S1-Q5: How many hours per day do you spend coding on average?**

Options:

- < 2h
- 2-4h
- 4-6h
- 6-8h
- > 8h

### Question `S1-Q6`: _Choice (single answer)_

> **S1-Q6: What is the size of your immediate squad/team?**

Options:

- I work solo
- 2-4 people
- 5-9 people
- 10-15 people
- > 15 people

### Question `S1-Q7`: _Choice (single answer)_

> **S1-Q7: Work model?**

Options:

- 100% remote
- Hybrid (1-2 days in person)
- Hybrid (3-4 days)
- 100% in person

---

## S2: GitHub Copilot: Adoption and Modes

_Focus on GitHub Copilot. Includes current modes (Ask, Edit, Agent), autonomous Coding Agent, and Spaces for shared context._

_9 questions in this section._

### Question `S2-Q1`: _Choice (single answer)_

> **S2-Q1: Do you have an active GitHub Copilot license?**

Options:

- Yes, Copilot Enterprise
- Yes, Copilot Business
- Yes, Copilot Pro+ (individual)
- Yes, Copilot Pro (individual)
- Yes, Copilot Free
- I have a license but do not use it
- I do not have a license

### Question `S2-Q2`: _Choice (single answer)_

> **S2-Q2: How often do you use Copilot?**

Options:

- Daily (several hours)
- Daily (sporadic)
- Weekly
- Rarely
- Never

### Question `S2-Q3`: _Choice (multiple answers)_

> **S2-Q3: Which Copilot Chat MODES do you use? (select all that apply)**

Options:

- Ask (answer questions)
- Edit (multi-file editing in the IDE)
- Agent (autonomous in the IDE, runs tasks)
- Copilot Coding Agent (autonomous on GitHub.com, assigns issues, opens PRs on its own)
- Plan / Vision
- I do not use Chat, only inline completion
- I do not know these modes

### Question `S2-Q4`: _Choice (single answer)_

> **S2-Q4: Which MODE do you use MOST day to day?**

Options:

- Ask
- Edit
- Agent (in the IDE)
- Coding Agent (autonomous on GitHub)
- Plan / Vision
- Only inline completion
- I do not know the difference

### Question `S2-Q5`: _Choice (multiple answers)_

> **S2-Q5: Which Copilot features do you use?**

Options:

- Inline code completion
- Chat (questions in the IDE)
- Automatic Pull Request descriptions
- Pull Request review (Copilot review)
- Test generation
- Documentation generation
- Issue resolution (Coding Agent assigns issue)
- Slash commands in Chat (/explain, /fix, /tests)
- Copilot Spaces (shared context: repos + docs + custom instructions)
- Copilot Coding Agent (autonomous tasks)
- Copilot CLI (gh copilot)

### Question `S2-Q6`: _Choice (multiple answers)_

> **S2-Q6: Where do you use Copilot?**

Options:

- VS Code
- Visual Studio
- JetBrains (IntelliJ, PyCharm, etc.)
- Neovim
- Xcode
- GitHub.com (web)
- GitHub Mobile
- GitHub Codespaces
- CLI (gh copilot)

### Question `S2-Q7`: _Choice (single answer)_

> **S2-Q7: Perceived productivity gain with Copilot?**

Options:

- Negative (gets in the way)
- Neutral (no gain)
- +10-20%
- +20-40%
- +40-60%
- +60% or more
- I do not know how to measure it

### Question `S2-Q8`: _Choice (multiple answers)_

> **S2-Q8: For WHICH TASKS does Copilot help you the most?**

Options:

- Boilerplate / repetitive code
- Refactoring
- Writing tests
- Learning a new API/lib
- Debugging
- Explaining legacy code
- Documentation
- SQL / complex queries
- Regex
- Translation between languages
- Onboarding into a new project

### Question `S2-Q9`: _Long Text (free response)_

> **S2-Q9: In which tasks does Copilot NOT help you, or get in the way?**

---

## S3: Other Microsoft / GitHub AI tools

_Microsoft Foundry ecosystem and advanced GitHub features._

_7 questions in this section._

### Question `S3-Q1`: _Choice (multiple answers)_

> **S3-Q1: Which other Microsoft / GitHub AI tools do you use today?**

Options:

- Microsoft Foundry (formerly Azure AI Foundry)
- Foundry Agent Service (GA, built on OpenAI Responses API)
- Azure OpenAI Service (directly via API)
- Microsoft 365 Copilot
- GitHub Copilot Spaces
- GitHub Copilot Coding Agent (autonomous)
- GitHub Codespaces
- GitHub Models (multi-LLM playground)
- GitHub Advanced Security (GHAS)
- GitHub Actions with Copilot integration
- Visual Studio with advanced Copilot
- None of the above

### Question `S3-Q2`: _Choice (multiple answers)_

> **S3-Q2: WHAT do you use Microsoft Foundry / Azure OpenAI for, if you use it?**

Options:

- PoC / experimentation
- Production product feature
- Embeddings / RAG
- Foundry Agent Service for autonomous agents
- Multi-agent orchestration via MCP
- Fine-tuning
- Connectors (Dynamics, SAP, SharePoint, etc.)
- I do not use it

### Question `S3-Q3`: _Choice (single answer)_

> **S3-Q3: Do you know GitHub Copilot Coding Agent, the autonomous successor to Workspace that can pick up issues and open PRs?**

Options:

- I actively use it in production
- I have tested it but do not use it regularly
- I know it but have never used it
- I do not know it

### Question `S3-Q4`: _Choice (single answer)_

> **S3-Q4: Do you know Copilot Spaces, the shared-context feature that replaced Knowledge Bases?**

Options:

- I use and create Spaces for my team
- I use Spaces created by others
- I know it but do not use it
- I do not know it

### Question `S3-Q5`: _Choice (single answer)_

> **S3-Q5: Do you know GitHub Spec Kit (github/spec-kit) for Spec-Driven Development?**

Options:

- I use it
- I know it but do not use it
- I do not know it

### Question `S3-Q6`: _Choice (single answer)_

> **S3-Q6: Do you know MCP (Model Context Protocol), the standard for agents to consume tools/context?**

Options:

- I use MCP servers in my workflow
- I have configured a custom MCP server
- I know the concept
- I do not know it

### Question `S3-Q7`: _Choice (single answer)_

> **S3-Q7: Have you used GitHub Models to test different LLMs (gpt-4o, claude, llama, etc.)?**

Options:

- I use it regularly
- I have tested it
- I do not know it

---

## S4: AI Development Practices

_How you incorporate AI into your workflow: TDD, SDD, AI pair programming, and related practices._

_9 questions in this section._

### Question `S4-Q1`: _Choice (single answer)_

> **S4-Q1: Do you practice TDD with AI, writing tests first with Copilot?**

Options:

- Whenever possible
- Frequently
- Sometimes
- Rarely
- Never
- I do not know what TDD is

### Question `S4-Q2`: _Choice (single answer)_

> **S4-Q2: Do you practice SDD (Spec-Driven Development), writing a spec so AI generates code?**

Options:

- I actively use it (with Spec Kit or similar)
- I have tested it in some projects
- I know the concept but do not use it
- I have never heard of it

### Question `S4-Q3`: _Choice (multiple answers)_

> **S4-Q3: At WHICH moments do you consult AI while coding?**

Options:

- Before starting (plan architecture)
- During (autocomplete + questions)
- After implementing (review/refactor)
- When I get stuck (debugging)
- To write tests
- To write docs
- For code review of my own PR

### Question `S4-Q4`: _Choice (single answer)_

> **S4-Q4: Do you consider Copilot / an AI agent a pair programmer?**

Options:

- Yes, I treat it as a pair
- Sometimes (depends on the task)
- No, just an autocomplete tool
- I do not use it in a structured way

### Question `S4-Q5`: _Choice (single answer)_

> **S4-Q5: How often do you refactor code with AI help?**

Options:

- Every week
- A few times per month
- Rarely
- Never

### Question `S4-Q6`: _Choice (single answer)_

> **S4-Q6: Who maintains code documentation in your team?**

Options:

- AI generates it and the team reviews it
- Devs write it manually, AI helps sometimes
- The team maintains it manually, without AI
- Documentation is abandoned

### Question `S4-Q7`: _Choice (single answer)_

> **S4-Q7: When you face a difficult bug, what is your first action?**

Options:

- I ask Copilot Chat / Claude / another AI
- I look in logs / debugger
- I ask a human colleague
- Stack Overflow / documentation
- It depends on the bug

### Question `S4-Q8`: _Choice (single answer)_

> **S4-Q8: When onboarding into a new project, do you use AI (with Copilot Spaces or similar) to understand the codebase?**

Options:

- Always, the first thing I do
- Frequently
- Sometimes
- No, I read README and code manually

### Question `S4-Q9`: _Long Text (free response)_

> **S4-Q9: Describe one concrete AI practice that changed your productivity in the last 6 months:**

---

## S5: Agent Concepts and Structure

_Checks knowledge and use of structured AI agents, including Microsoft Agentic DevOps personas and agent testing/governance practices._

_11 questions in this section._

### Question `S5-Q1`: _Choice (single answer)_

> **S5-Q1: Do you know what an AI agent is, autonomous versus a reactive assistant?**

Options:

- Yes, I can explain it clearly
- Yes, vaguely
- I do not know the difference
- I do not know the term

### Question `S5-Q2`: _Choice (single answer)_

> **S5-Q2: Do you know the difference between Ask, Edit, Agent, and Coding Agent Copilot modes?**

Options:

- Yes, I use them consciously
- More or less
- I do not know the difference

### Question `S5-Q3`: _Choice (single answer)_

> **S5-Q3: Have you created or used a custom agent (.github/agents/*.agent.md or Claude/Cursor equivalent)?**

Options:

- I have created one
- I have used one but not created one
- I know they exist but have never used one
- I did not know it was possible

### Question `S5-Q4`: _Choice (single answer)_

> **S5-Q4: Do you know the concept of a skill (SKILL.md or equivalent reusable instruction block)?**

Options:

- I know it and use it
- I know it but do not use it
- I do not know it

### Question `S5-Q5`: _Choice (single answer)_

> **S5-Q5: Have you created prompt files (.prompt.md in .github/prompts/)?**

Options:

- Yes, several
- Yes, one or two
- No, but I plan to
- I do not know it

### Question `S5-Q6`: _Choice (single answer)_

> **S5-Q6: Do you know A2A (Agent-to-Agent protocol), agents communicating with each other?**

Options:

- I use it (e.g., Foundry A2A Tool)
- I know the concept
- I do not know it

### Question `S5-Q7`: _Choice (single answer)_

> **S5-Q7: Do you know handoffs between agents, where agent A passes context to agent B?**

Options:

- I use it
- I know the concept
- I do not know it

### Question `S5-Q8`: _Choice (single answer)_

> **S5-Q8: Do you know subagents, where a main agent delegates tasks to specialized subagents?**

Options:

- I use it
- I know the concept
- I do not know it

### Question `S5-Q9`: _Choice (single answer)_

> **S5-Q9: Do you know Microsoft Agentic DevOps personas: System Designer and Agent Operator?**

Options:

- Yes, I explicitly adopt them
- I know the concept
- I do not know it

### Question `S5-Q10`: _Choice (single answer)_

> **S5-Q10: Do you TEST your custom agents/prompts/skills before using them on real code?**

Options:

- Always, I have a test suite for my agents
- Frequently, manual but systematic
- Sometimes, only a sanity check
- Rarely / never
- I do not create agents/prompts/skills

### Question `S5-Q11`: _Choice (multiple answers)_

> **S5-Q11: Which primitives have you ALREADY CREATED for personal/team use?**

Options:

- Custom prompts (.prompt.md)
- Custom skills (SKILL.md)
- Custom agents (.agent.md)
- Custom MCP server
- Instructions files (copilot-instructions.md / AGENTS.md / CLAUDE.md)
- Shared Spaces
- None of the above

---

## S6: Markdown / Memory / Instructions

_About configuration files that teach the agent about your project._

_6 questions in this section._

### Question `S6-Q1`: _Choice (multiple answers)_

> **S6-Q1: Which instruction files do you use today?**

Options:

- .github/copilot-instructions.md
- .github/instructions/*.instructions.md
- AGENTS.md
- CLAUDE.md (project root)
- .cursorrules
- Custom instructions in Copilot Spaces
- None

### Question `S6-Q2`: _Choice (single answer)_

> **S6-Q2: Who maintains the instruction file(s) in your project?**

Options:

- The whole team contributes
- 1-2 dedicated people
- I maintain them alone
- Nobody maintains them, they are outdated
- We do not have it

### Question `S6-Q3`: _Choice (single answer)_

> **S6-Q3: How often are these files updated?**

Options:

- Every week
- Monthly
- Quarterly
- When something breaks
- I never update them

### Question `S6-Q4`: _Choice (multiple answers)_

> **S6-Q4: WHAT do you include in instruction files?**

Options:

- Code style / project conventions
- Domain knowledge (business rules)
- Stack / tools
- Forbidden patterns (what NOT to do)
- Examples (good vs bad code)
- Folder structure / architecture
- Common commands (test, build, deploy)
- I do not have instructions

### Question `S6-Q5`: _Choice (single answer)_

> **S6-Q5: Do you have a shared prompt library with your team (repo or dedicated Copilot Space)?**

Options:

- Yes, shared Copilot Space
- Yes, dedicated repo
- Yes, wiki/Confluence
- Each person maintains their own
- We do not share prompts

### Question `S6-Q6`: _Choice (single answer)_

> **S6-Q6: Do you use persistent agent memory (Foundry Memory, Claude memory, Copilot memory)?**

Options:

- I actively use it
- I have tested it
- I do not know it

---

## S7: Usability and Best Practices

_How you and your team learn and improve AI usage._

_9 questions in this section._

### Question `S7-Q1`: _Choice (multiple answers)_

> **S7-Q1: How did you LEARN to use Copilot/AI for development?**

Options:

- Self-learning (trial and error)
- Internal company workshop
- Official documentation
- YouTube videos
- Online course (Coursera, Udemy, MS Learn)
- Champion on the team
- Events / conferences (Microsoft Build, GitHub Universe)
- Communities / Discord / Slack

### Question `S7-Q2`: _Choice (single answer)_

> **S7-Q2: Is there an AI/Copilot Champion in your team/company who helps others?**

Options:

- Yes, I am
- Yes, someone else
- No, but we should have one
- No, everyone figures it out on their own

### Question `S7-Q3`: _Choice (single answer)_

> **S7-Q3: Is there an internal channel/community to discuss AI usage in engineering?**

Options:

- Yes, active (>5 messages/week)
- Yes, not very active
- We do not have a dedicated channel
- I do not know

### Question `S7-Q4`: _Choice (multiple answers)_

> **S7-Q4: Does your organization MEASURE developer productivity in a structured way?**

Options:

- DORA metrics (lead time, deployment freq, MTTR, change failure)
- DX index (developer experience)
- SPACE framework
- Copilot adoption metrics (active users)
- Periodic self-report (survey)
- We do not measure formally

### Question `S7-Q5`: _Choice (single answer)_

> **S7-Q5: How many prompt iterations do you typically need before you get a good result?**

Options:

- It gets it right on the 1st try
- 2-3 iterations
- 4-6 iterations
- 7+ iterations (frequent)

### Question `S7-Q6`: _Choice (single answer)_

> **S7-Q6: Do you trust AI-generated code enough to merge it WITHOUT reviewing line by line?**

Options:

- Never, I always review
- For trivial changes (yes)
- Frequently (I trust it)
- Almost always

### Question `S7-Q7`: _Choice (single answer)_

> **S7-Q7: How often do you detect hallucinations, where AI invents nonexistent APIs/methods?**

Options:

- Daily
- Weekly
- Rarely
- Almost never

### Question `S7-Q8`: _Choice (single answer)_

> **S7-Q8: Since adopting AI, do you feel you are learning more or less about engineering?**

Options:

- Learning MUCH MORE (AI accelerates it)
- A little more
- About the same
- Learning LESS (dependency)
- I do not know how to assess it

### Question `S7-Q9`: _Choice (single answer)_

> **S7-Q9: Do you share good prompts/usage examples with colleagues in Spaces, Slack, or Confluence?**

Options:

- Frequently, in a shared channel
- Sometimes, personally
- Rarely
- Never

---

## S8: Security and Governance

_Security practices for AI usage plus agent governance (scope, red-lines, JIT permissions, audit)._

_13 questions in this section._

### Question `S8-Q1`: _Choice (single answer)_

> **S8-Q1: Does your organization have a DOCUMENTED AI usage policy for engineering?**

Options:

- Yes, formal and clear policy
- Yes, but not very clear
- Informal policy (no document)
- We do not have a policy
- I do not know

### Question `S8-Q2`: _Choice (single answer)_

> **S8-Q2: Do you know WHICH DATA can go to external LLMs (Copilot, ChatGPT)?**

Options:

- I clearly know what can and CANNOT be used
- I have a general idea
- Vaguely
- I do not know

### Question `S8-Q3`: _Choice (multiple answers)_

> **S8-Q3: Which data types would you NEVER put into external AI prompts?**

Options:

- PII / customer personal data
- Secrets / API keys / tokens
- Strategic IP code
- Financial data
- Health data
- No restrictions (we do not have a policy)

### Question `S8-Q4`: _Choice (multiple answers)_

> **S8-Q4: Which SECURITY tools are active in your repository?**

Options:

- GitHub Advanced Security (GHAS)
- CodeQL scanning
- Secret scanning
- Dependabot / dependency review
- SBOM (Software Bill of Materials)
- Microsoft Defender for DevOps
- Microsoft Defender for Cloud
- Snyk / SonarQube / other SAST
- None

### Question `S8-Q5`: _Choice (single answer)_

> **S8-Q5: Does Code Scanning run on AI-GENERATED code in the PR or IDE?**

Options:

- Yes, mandatory gate in the PR
- Yes, optional
- Runs but does not block
- Does not run

### Question `S8-Q6`: _Choice (single answer)_

> **S8-Q6: Does your organization generate SBOMs for critical services?**

Options:

- Yes, automated
- Yes, manual when requested
- We do not generate them
- I do not know

### Question `S8-Q7`: _Choice (single answer)_

> **S8-Q7: Is there a formal REVIEW process for AI-generated code before merge?**

Options:

- Yes, mandatory review by another human + scanner
- Mandatory human review (no extra scanner)
- Optional review
- We do not have a process

### Question `S8-Q8`: _Choice (single answer)_

> **S8-Q8: When creating/using a custom agent, do you define explicit SCOPE and RED-LINES?**

Options:

- Always, documented scope + red-lines
- Frequently
- Sometimes
- Rarely / never
- I do not create/use custom agents

### Question `S8-Q9`: _Choice (single answer)_

> **S8-Q9: Does your organization use JIT (Just-In-Time) permissions for agents instead of persistent permissions?**

Options:

- Yes, JIT is mandatory for agents
- Yes, optional
- We do not have JIT
- I do not know

### Question `S8-Q10`: _Choice (single answer)_

> **S8-Q10: Does your organization have DLP configured to prevent sensitive data in prompts?**

Options:

- Yes, actively blocks
- Yes, alerts but does not block
- We do not have it
- I do not know

### Question `S8-Q11`: _Choice (single answer)_

> **S8-Q11: Does your organization have AUDIT LOGS for Copilot/AI agents, including autonomous agent decisions?**

Options:

- Yes, active and reviewed logs
- Active logs but not reviewed
- We do not have it
- I do not know

### Question `S8-Q12`: _Choice (single answer)_

> **S8-Q12: Have you received formal security training for AI usage?**

Options:

- Yes, mandatory annual training
- Yes, once (during onboarding)
- I have not received training
- I do not know

### Question `S8-Q13`: _Choice (single answer)_

> **S8-Q13: How often have you seen Copilot/AI suggest code with an obvious vulnerability?**

Options:

- Daily
- Weekly
- Monthly
- Almost never

---

## S9: Pain Points & Wishlist

_Your ideas and frustrations. Free text: feel free to be candid._

_4 questions in this section._

### Question `S9-Q1`: _Long Text (free response)_

> **S9-Q1: What frustrates you MOST today about using AI in your day-to-day engineering work?**

### Question `S9-Q2`: _Long Text (free response)_

> **S9-Q2: What CHANGE in tooling/process would double your productivity?**

### Question `S9-Q3`: _Long Text (free response)_

> **S9-Q3: Which Microsoft/GitHub feature/tool would you like to exist, or know better?**

### Question `S9-Q4`: _Choice (single answer)_

> **S9-Q4: Would you like to receive the consolidated version of this survey (team-wide aggregated insights)?**

Options:

- Yes, I want to see it
- No, thank you

---

## Final summary

- **9 sections** (1 per theme)
- **75 questions** (55 choice + 15 multi + 5 long text)
- **Estimated time:** 20-25 min (a quick pass takes about 10 min)
- **Expected responses:** the more developers, the better: minimum 5, ideal 15+

## Next steps

1. After collecting responses, go to **Responses → Open in Excel** in Microsoft Forms
2. Rename the Excel file to `survey-devs-responses.xlsx`
3. Move it to the kit root
4. In Copilot Chat (Agent mode): `/import-survey-devs`
5. Then run `/insights-developer-survey` to generate the consolidated report
