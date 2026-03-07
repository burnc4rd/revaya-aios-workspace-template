# AI HR Protocol

> The team management department. Builds, documents, and optimizes the AI agent workforce.
> This is one of the ACRA+2 departments in the Execution Layer.

**Owner:** AI HR Lead (`team/ai-hr/lead.md`)
**Supporting:** Build Specialist (`team/ai-hr/build-specialist.md`)
**Review cadence:** Weekly Synthesis (`/review` Phase 4.4)

---

## What AI HR Owns

AI HR is responsible for everything related to the AI agent workforce — not the work the agents do, but the agents themselves.

### 1. AI Agent Creation and Configuration

When a new role, skill, or pipeline is needed:
- Define the agent's mission, decision authority, and context files
- Write the role file using the existing template in `team/`
- Name the file and folder following existing conventions
- Add the role to `team/org-chart.md` and `team/README.md`
- Test the role before deploying to production use
- Document in this protocol what was created and why

**Trigger:** A task can't be handled by any existing role, or a new department pipeline requires a new orchestrator or specialist agent.

### 2. Subagent Knowledge Base Maintenance

Every role file is a knowledge base. They go stale. AI HR owns keeping them current.

**What "stale" means:**
- Role's context files reference outdated information
- Role's handoff protocols don't match current workflow
- Role's "What I Know" section (when added) is out of date
- Role's decision authority doesn't match how it's actually used

**Maintenance cadence:**
- Flag stale roles during `/review` AIOS Weekly Synthesis
- Update roles immediately after significant changes to the systems they operate in
- Full audit quarterly (add to Quarterly Review cadence)

**Subagent KB = every file in `team/`**

### 3. Performance Evaluation of AI Systems

Not every agent or command is performing well. AI HR evaluates and improves.

**Evaluation questions:**
- Is this role being used? If not, why?
- When used, does it produce the right output?
- Are there patterns of failure or friction in this role?
- Is the role duplicating work another role already handles?

**Inputs for evaluation:**
- `/reflect` entries that mention specific roles
- Friction logged to GTD inbox
- Direct feedback from session work
- Weekly Synthesis observations

**Outputs:**
- Role file updates
- Deprecation recommendations (route to Someday/Maybe)
- New role proposals (route to GTD as a next action)

### 4. Onboarding New Tools and Capabilities

When a new MCP server, skill, or external connector is added:
- AI HR documents what it does and which roles can use it
- Updates the relevant role files with the new capability
- Adds to `connectors.md` if it's an external connector
- Assesses whether it justifies its existence (lean principle)

### 5. Peak Performance Maintenance

The AI workforce should get better every week. AI HR is the mechanism for that.

**Weekly habit (during `/review` Phase 4.4):**
1. Review which roles were used this week
2. Flag any that produced poor output or weren't used at all
3. Identify one improvement to implement before next review
4. Log it to GTD inbox

---

## AI HR Kickoff Template

When creating a new agent, document it here:

```
**Agent Name:** [role file name]
**Created:** YYYY-MM-DD
**Mission:** [one sentence]
**Department:** [ACRA+2 department]
**Context files:** [list]
**Why created:** [the gap it fills]
**Status:** Active / Experimental / Deprecated
```

---

## Active AI Workforce Log

| Agent | Department | Status | Last Updated | Notes |
|-------|-----------|--------|-------------|-------|
| CEO | Executives | Active | 2026-02-28 | [YOUR_NAME]'s executive role |
| CFO | Finance | Active | 2026-02-28 | Financial strategy |
| CMO | Attract | Active | 2026-02-28 | Content + marketing strategy |
| COO | Retain & Deliver | Active | 2026-02-28 | Ops oversight |
| CTO | AI HR | Active | 2026-02-28 | AI architecture + HR lead |
| CRO | Convert + Ascend | Active | 2026-02-28 | Revenue strategy |
| Creative Director | Attract | Active | 2026-02-28 | Creative assets |
| Content Strategist | Attract | Active | 2026-02-28 | Content planning |
| Copywriter | Attract + Convert | Active | 2026-02-28 | Written content |
| SEO Specialist | Attract | Active | 2026-02-28 | Search visibility |
| Social Media Manager | Attract | Active | 2026-02-28 | Platform execution |
| Website Designer | Attract | Active | 2026-02-28 | Visual design |
| Social Media Designer | Attract | Active | 2026-02-28 | Social visuals |
| Lead Magnet Designer | Attract | Active | 2026-02-28 | Lead magnet assets |
| AI Engineer | AI HR + all depts | Active | 2026-02-28 | Builds agent pipelines |
| Website Developer | Retain & Deliver | Active | 2026-02-28 | Website builds |
| QA Engineer | Retain & Deliver | Active | 2026-02-28 | Quality testing |
| AI Consultant | Retain & Deliver | Active | 2026-02-28 | AIOS delivery |
| Project Manager | Retain & Deliver | Active | 2026-02-28 | Project coordination |
| Account Manager | Retain & Deliver + Ascend | Active | 2026-02-28 | Client relationships |
| SDR | Convert | Active | 2026-02-28 | Prospecting + outreach |
| Account Executive | Convert + Ascend | Active | 2026-02-28 | Sales + upsells |
| Sales Enablement | Convert | Active | 2026-02-28 | Sales infrastructure |
| Finance Analyst | Finance | Active | 2026-02-28 | KPI tracking |
| Data Analyst | Finance | Active | 2026-02-28 | Performance analysis |
| Research Analyst | Cross-functional | Active | 2026-02-28 | VOC + competitive intel |
| Platform: LinkedIn | Attract | Active | 2026-02-28 | LinkedIn channel |
| Platform: YouTube Long-Form | Attract | Active | 2026-02-28 | YouTube channel |
| Platform: YouTube Shorts | Attract | Active | 2026-02-28 | Shorts channel |
| Platform: TikTok | Attract | Active | 2026-02-28 | TikTok channel |

**Total:** 30 role files (27 roles + 3 platform files)

---

## What AI HR Does NOT Own

- The work those agents do (that's each department's responsibility)
- Strategic decisions about which department to prioritize (that's the Prioritization Engine)
- Business KPI tracking (that's Finance)
- The GTD system or project coordination (that's the Execution Layer)
