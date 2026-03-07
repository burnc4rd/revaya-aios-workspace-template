# Business AI OS — Workspace Template

> This is the actual system I use to run my consultancy. Every session, every command, every agent — live and in production. Fork it and build yours.

---

## The Problem

Most founders are trapped doing work their business should be doing for them. Not because they lack discipline. Because AI tools don't connect to how their business actually operates.

You can use ChatGPT for emails and Claude for summaries, but those are one-off interactions. There's no memory. No persistent context. No team. Every session starts from zero. The AI doesn't know your business, your strategy, your pipeline, or your priorities.

A Business AI OS fixes that. It's a structured workspace that gives AI everything it needs to function as a genuine operational partner — not just a smart search box.

---

## What Is a Business AI OS?

A Business AI OS is a Claude Code workspace configured specifically for your business. It contains:

- **Persistent context** — your business, role, strategy, and current data, always loaded
- **A decision filter** — One Objective, One Bottleneck, One Goal (OOBG) that scores every task
- **A team of specialized agents** — 14 agents organized across 6 departments (Attract, Convert, Retain & Deliver, Ascend, Finance, AI HR)
- **A command system** — 31 slash commands for every recurring workflow (planning, content, GTD, metrics, knowledge capture)
- **A learning system** — knowledge management and learning loops that make the OS smarter over time

The system runs locally. Your data stays yours. Nothing is a black box.

---

## What's Inside

```
.
├── CLAUDE.md                    # Master context — loaded every session
├── GETTING-STARTED.md           # Start here after cloning
├── .claude/commands/            # 31 slash commands
├── context/                     # Your business context (fill these in first)
│   ├── personal-info.md
│   ├── business-info.md
│   ├── strategy.md
│   └── current-data.md
├── strategic-layer/             # OOBG decision filter
│   ├── oobg.md                  # One Objective, One Bottleneck, One Goal
│   ├── priorities.md
│   ├── direction.md
│   └── unique-vehicle.md
├── team/                        # 14-agent ACRA+2 org
│   ├── attract/
│   ├── convert/
│   ├── retain-deliver/
│   ├── ascend/
│   ├── finance/
│   └── ai-hr/
├── knowledge/                   # Decision and learning capture
│   ├── decisions/
│   └── learnings/
├── metrics/                     # Business KPI tracking
├── gtd/                         # Getting Things Done system
├── content/                     # Content engine (strategy, pipeline, brand)
├── scripts/content/             # Content pipeline automation scripts
├── docs/                        # System documentation
├── plans/                       # Implementation plans
└── outputs/                     # Work products and deliverables
```

### The 9 Components

| Component | What It Does | Key Files |
|-----------|-------------|-----------|
| 1. Strategic Layer | Filters every decision through one lens — the OOBG | `strategic-layer/oobg.md` |
| 2. Prioritization Engine | Scores tasks against the OOBG daily | `/build-guide` command |
| 3. Knowledge Management | Captures decisions and learnings that persist across sessions | `knowledge/` |
| 4. Execution Layer | GTD system + slash commands + ACRA+2 team | `gtd/`, `.claude/commands/`, `team/` |
| 5. Auto-Capture | Session-end knowledge capture triggers | `/commit`, `/reflect` |
| 6. Communications Layer | Telegram AI assistant (optional) | `apps/` (not included — build your own) |
| 7. Metrics & Monitoring | KPI tracking, on-demand business pulse | `metrics/`, `/metrics` |
| 8. Learning Loops | 5 cadences from daily to annual — system improves over time | `/reflect`, `/review` |
| 9. External Connectors | APIs, MCPs, webhooks — audited and documented | `connectors.md` |

**The cycle:** Strategic Layer → Prioritization Engine → Execution → Auto-Capture → Knowledge + Metrics → Learning Loops → refines Strategic Layer

---

## This Is Real

This template is a generalized version of the workspace I use to run Revaya AI every day.

Every session is logged. Every decision has a rationale. The system has been running since February 2026 — through client projects, content production, product planning, and strategic pivots. It is not a demo. It is not a proof of concept. It is a live operating system.

I build Business AI OSes for service businesses. This is mine.

**Shannon Winnicki** — Founder, Revaya AI
[linkedin.com/in/shannonwinnicki](https://linkedin.com/in/shannonwinnicki) | [revaya.ai](https://revaya.ai)

---

## Get Started

**Three steps:**

1. Install [Claude Code](https://claude.ai/code)
2. Clone this repo: `git clone https://github.com/revaya-ai/revaya-aios-workspace-template.git`
3. Open the directory in Claude Code and run `/prime`

**Full walkthrough:** See [GETTING-STARTED.md](./GETTING-STARTED.md)

---

## The ACRA+2 Team

This workspace ships with a 14-agent team organized by the customer lifecycle:

| Department | Agents | What They Handle |
|------------|--------|-----------------|
| **Attract** | Lead + Content Specialist | Brand, content strategy, audience building |
| **Convert** | Lead + Discovery, Proposal, Copy Specialists | Sales process, proposals, conversion |
| **Retain & Deliver** | Lead + Delivery, Technical Specialists | Client delivery, technical execution |
| **Ascend** | Lead + Relationship Specialist | Client retention, expansion, referrals |
| **Finance** | Lead + Numbers Specialist | Revenue tracking, pricing, financials |
| **AI HR** | Lead + Build Specialist | Workforce planning, AI system improvements |
| **Research** | Research Analyst | Cross-functional research, commissioned by any dept |

Access the team with `/team [request]` — Claude routes to the right agent.
Convene multiple leads with `/board [decision]` — for cross-functional decisions.

---

## The Commands

31 slash commands cover every recurring workflow:

**Daily workflow:** `/prime` → `/build-guide` → work → `/reflect` → `/commit`

**Planning:** `/create-plan` → `/challenge` (mandatory) → `/implement`

**Content:** `/capture`, `/develop`, `/draft-post`, `/draft-content`, `/plan-content`

**Team:** `/team`, `/board`

**GTD:** `/process`, `/review`

**Research:** `/research`, `/reddit-research`, `/competitive-research`

See `CLAUDE.md` for the full command reference.

---

## License

MIT — use it, modify it, build on it. Attribution appreciated but not required.

---

## Contributing

If you build something useful on top of this, share it. The more examples of real Business AI OSes that exist in the world, the better the category becomes for everyone.
