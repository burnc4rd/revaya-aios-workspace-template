# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

---

## What This Is

This is a **Business AI OS Workspace** — a structured environment designed for working with Claude Code as a powerful agent assistant across sessions. Use `/prime` at the start of each session to load essential context without bloat.

**This file (CLAUDE.md) is the foundation.** It is automatically loaded at the start of every session. Keep it current — it is the single source of truth for how Claude should understand and operate within this workspace.

---

## The Claude-User Relationship

Claude operates as an **agent assistant** with access to the workspace folders, context files, commands, and outputs. The relationship is:

- **User**: Defines goals, provides context about their role/function, and directs work through commands
- **Claude**: Reads context, understands objectives, executes commands, produces outputs, and maintains workspace consistency

Claude should always orient itself through `/prime` at session start, then act with full awareness of who the user is, what they're trying to achieve, and how this workspace supports that.

---

## Workspace Structure

```
.
├── CLAUDE.md              # This file — core context, always loaded
├── GETTING-STARTED.md     # First-session walkthrough
├── .claude/
│   └── commands/          # Slash commands Claude can execute
├── context/               # Background context about the user and project
│   ├── personal-info.md
│   ├── business-info.md
│   ├── strategy.md
│   └── current-data.md
├── strategic-layer/       # AIOS Strategic Layer — the decision filter for all work
│   ├── README.md
│   ├── oobg.md            # One Objective, One Bottleneck, One Goal
│   ├── unique-vehicle.md
│   ├── priorities.md
│   └── direction.md
├── knowledge/             # Knowledge Management — decisions and learnings
│   ├── README.md
│   ├── decisions/
│   └── learnings/
├── metrics/               # Metrics and Monitoring — business KPIs
│   ├── README.md
│   └── business-kpis.md
├── docs/                  # Auto-generated technical documentation
│   └── _index.md
├── gtd/                   # GTD system — inbox, projects, next actions
├── content/               # Content engine — strategy, brand, pipeline
├── scripts/content/       # Content pipeline automation scripts
├── team/                  # ACRA+2 AI org — 14 agents across 6 departments
├── plans/                 # Implementation plans created by /create-plan
├── outputs/               # Work products and deliverables
├── reference/             # Templates, examples, reusable patterns
├── data/                  # SQLite databases (gitignored, generated on first run)
├── connectors.md          # External integrations audit
├── .env.example           # Template showing required API keys
└── .gitignore             # Git security defaults
```

---

## Commands

### /prime

**Purpose:** Initialize a new session with full context awareness.

Run at the start of every session. Claude will read CLAUDE.md, context files, and the OOBG, then summarize understanding and confirm readiness.

### /build-guide

**Purpose:** Daily strategic build guide — scores tasks against the OOBG.

Run after `/prime`. Loads `strategic-layer/oobg.md`, scans active projects, scores tasks against the Bottleneck, and surfaces the one Critical task for the day.

### /reflect

**Purpose:** End-of-session learning capture — Learning Loops cadence 1.

Captures top accomplishment, top learning, friction, and execution patterns. Saves to `knowledge/learnings/`.

### /metrics [question]

**Purpose:** On-demand business pulse query.

No argument: full KPI summary. With question: specific answer from `metrics/business-kpis.md`.

### /create-plan [request]

**Purpose:** Create a detailed implementation plan before making changes.

Produces a thorough plan in `plans/`. Always follow with `/challenge` before `/implement`.

### /challenge [file]

**Purpose:** Pressure-test any work before shipping. Mandatory between `/create-plan` and `/implement`.

### /implement [plan-path]

**Purpose:** Execute a challenged, approved plan.

### /commit [message]

**Purpose:** Save work, update documentation, keep the changelog current.

### /update-journal [project-name]

**Purpose:** Append a new build log entry to an Obsidian build journal after a work session.

Requires: Obsidian installed with a Build Journals vault at `[YOUR_OBSIDIAN_VAULT_PATH]/Build Journals/`. Configure the path in the command file.

### /team [request]

**Purpose:** Route a request to the best-fit ACRA+2 department agent.

### /board [decision]

**Purpose:** Convene 2-4 Department Leads for a cross-functional decision.

### /brainstorm [topic]

**Purpose:** Workspace scanner and opportunity finder.

### /explore [idea]

**Purpose:** Interactive feature discovery — shapes an idea into a scoped concept.

### /research [topic]

**Purpose:** Deep research agent. Saves brief to `outputs/`.

### /reddit-research [topic]

**Purpose:** Voice-of-customer research from Reddit communities.

### /competitive-research [competitor]

**Purpose:** Competitor content and positioning analysis.

### /draft-post [topic]

**Purpose:** LinkedIn post copywriter in your brand voice.

### /draft-content [format + topic]

**Purpose:** Multi-platform content (YouTube scripts, blog posts, newsletters).

### /capture [idea]

**Purpose:** Quick content idea capture to `data/content.db`.

### /develop [#ID or idea]

**Purpose:** Full concept development with packaging and positioning.

### /schedule [review]

**Purpose:** Interactive content scheduling session.

### /plan-content [scope]

**Purpose:** Generate or update the rolling monthly content calendar.

### /lead-magnet [idea]

**Purpose:** Three-phase lead magnet workflow: research → strategy → draft.

### /task-audit

**Purpose:** Map every recurring task to build your Task Automation % scoreboard.

### /process

**Purpose:** GTD inbox processing — decision tree walkthrough.

### /review

**Purpose:** GTD weekly review — get clear, get current, get creative.

### /share [target]

**Purpose:** Package a system or feature for sharing.

### /install [module-path]

**Purpose:** Install an AIOS module into this workspace.

---

## AI Organization (Team)

This workspace runs on a 6-department ACRA+2 structure — 14 agents organized by customer lifecycle.

**Access via:**
- `/team [request]` — route to one role for execution or analysis
- `/board [decision]` — convene Department Leads for cross-functional decisions

**Team structure:**
- `team/attract/` — Attract Lead, Content Specialist
- `team/convert/` — Convert Lead, Discovery Specialist, Proposal Specialist, Conversion Copy Specialist
- `team/retain-deliver/` — Retain & Deliver Lead, Delivery Specialist, Technical Specialist
- `team/ascend/` — Ascend Lead, Relationship Specialist
- `team/finance/` — Finance Lead, Numbers Specialist
- `team/ai-hr/` — AI HR Lead, Build Specialist
- `team/research-analyst.md` — cross-functional, commissioned by any department

**Reference docs:** `team/README.md` | `team/org-chart.md`

---

## Session Workflow

1. **Start**: Run `/prime`
2. **Orient**: Run `/build-guide` for OOBG-scored daily focus
3. **Work**: Use commands or direct Claude
4. **Plan changes**: Use `/create-plan` before significant additions
5. **Challenge**: Run `/challenge [plan-path]` — mandatory before any `/implement`
6. **Execute**: Use `/implement` on challenged plans only
7. **Reflect**: Run `/reflect` at session end
8. **Save**: Run `/commit`

---

## AIOS Architecture — 9 Components

| Component | Implementation | Files |
|-----------|---------------|-------|
| 1. Strategic Layer | OOBG filter for all decisions | `strategic-layer/` |
| 2. Prioritization Engine | `/build-guide` with OOBG scoring | `.claude/commands/build-guide.md` |
| 3. Knowledge Management | 5-step pipeline (Capture → Ready for Execution) | `knowledge/` |
| 4. Execution Layer | GTD + plans + ACRA departments | `gtd/`, `plans/`, `team/` |
| 5. Auto-Capture | `/commit` Step 1.5 + `/reflect` | `.claude/commands/commit.md`, `reflect.md` |
| 6. Communications Layer | Telegram bot (optional, not included) | Build your own using `apps/` pattern |
| 7. Metrics and Monitoring | KPI tracking + `/metrics` command | `metrics/` |
| 8. Learning Loops | 5 cadences (Daily → Annual) | `/reflect` (daily), `/review` (weekly) |
| 9. External Connectors | APIs, MCPs, webhooks — audited | `connectors.md` |

**The cycle:** Strategic Layer → Prioritization Engine → Execution Layer → Auto-Capture → Knowledge + Metrics → Learning Loops → refines Strategic Layer

---

## AIOS Build Phases

**Phase 1 — Habit-based (start here):**
The system works when you run the right command. Every capability exists, but the trigger is a human action. Discipline drives the system.

**Phase 2 — Automated (build after Phase 1 is stable):**
Voice memos auto-convert to knowledge chunks. Metrics pull live. Telegram routes to departments. Build Phase 2 only after Phase 1 runs cleanly for 30+ days.

**Phase 1 completion checklist:**

| Component | What's Needed |
|-----------|---------------|
| Strategic Layer | Set your OOBG in `strategic-layer/oobg.md` |
| Prioritization Engine | Run `/build-guide` daily for one week |
| Knowledge Management | File one decision, one learning |
| Execution Layer | Use GTD + `/team` for a real task |
| Auto-Capture | Run `/commit` + `/reflect` after a session |
| Metrics | Update `metrics/business-kpis.md` with real data |
| Learning Loops | Run `/reflect` daily, `/review` weekly |

---

## Active Initiatives

> **Fill this section in with your current projects and priorities.**

Use this structure:

### [Project Name] — [Status]
- **What it is:** [Brief description]
- **Current phase:** [Where you are]
- **Next action:** [The one thing to do next]
- **Codebase:** [Path or repo URL if applicable]

---

## GTD System

Getting Things Done system for managing tasks, projects, and commitments.

**Files (all in `gtd/`):**
- `dashboard.md` — Operational overview
- `inbox.md` — Raw capture bucket
- `projects.md` — Active projects
- `next-actions.md` — Next actions by context
- `waiting-for.md` — Delegated items
- `someday-maybe.md` — Parked ideas
- `areas.md` — Areas of responsibility
- `review-checklist.md` — Weekly review protocol

**Commands:** `/process` (empty inbox) | `/review` (weekly review)

---

## Content Engine Commands

### /research [topic]
General deep research. Saves to `outputs/`.

### /draft-post [topic]
LinkedIn post in your brand voice.

### /draft-content [format + topic]
Multi-platform long-form content.

### /capture [idea]
Quick content idea capture to SQLite database.

### /develop [#ID or idea]
Full concept development with packaging.

### /schedule [review]
Interactive scheduling session.

### /plan-content [scope]
Monthly content calendar generator.

---

## Critical Instruction: Maintain This File

**Whenever changes are made to the workspace, consider whether CLAUDE.md needs updating.**

After any change, ask:
1. Does this add new functionality users need to know about?
2. Does it modify the workspace structure?
3. Should a new command be listed?

If yes to any, update the relevant sections.

---

## Notes

- Keep context minimal but sufficient — avoid bloat
- Plans live in `plans/` with dated filenames
- Outputs are organized by type/purpose in `outputs/`
- Public template: `revaya-ai/revaya-aios-workspace-template` — generalized version for distribution
