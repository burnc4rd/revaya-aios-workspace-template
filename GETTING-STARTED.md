# Getting Started

> Your first session with the Business AI OS workspace. This file walks you from clone to operational in one sitting.

---

## Prerequisites

- **Claude Code** — install from [claude.ai/code](https://claude.ai/code). This workspace is built for Claude Code specifically. It will not work in Claude.ai or any other interface.
- **Git** — for cloning and version control
- **Python 3.10+** (optional) — only needed if you want to use the content pipeline scripts

---

## Step 1: Clone the Repo

```bash
git clone https://github.com/revaya-ai/revaya-aios-workspace-template.git
cd revaya-aios-workspace-template
```

Then push it to your own private GitHub repo so your data stays yours:

```bash
git remote remove origin
git remote add origin https://github.com/YOUR_ORG/YOUR_REPO_NAME.git
git push -u origin main
```

---

## Step 2: Fill In Your Context (Before Anything Else)

These four files are what give Claude persistent knowledge about your business. Fill them in before running `/prime`. Start with `oobg.md` — it sets the decision filter for everything else.

### Priority Order

| File | What to Put In It | Time Estimate |
|------|------------------|---------------|
| `strategic-layer/oobg.md` | Your One Objective, One Bottleneck, One Goal | 15 min |
| `context/personal-info.md` | Who you are, your role, how you operate | 10 min |
| `context/business-info.md` | What your business does, who it serves, how it makes money | 15 min |
| `context/strategy.md` | What you're working toward right now — priorities and success criteria | 15 min |

Leave `context/current-data.md` until after your first session — it tracks live pipeline and metrics you'll fill in as you work.

### How to Fill In the Context Files

Every context file uses `[YOUR_...]` placeholders. Replace them with your actual information:

```
[YOUR_NAME] → Shannon Winnicki
[YOUR_BUSINESS_NAME] → Revaya AI
[YOUR_ONE_OBJECTIVE] → Own the Business AI OS category
```

Don't aim for perfect. Get enough in that Claude can orient itself. You'll refine these over the first few sessions.

---

## Step 3: Set Up Your OOBG

The OOBG (One Objective, One Bottleneck, One Goal) is the most important file in the workspace. Every task, plan, and prioritization decision is scored against it.

Open `strategic-layer/oobg.md` and fill in:

- **One Objective** — the single most important thing you're trying to accomplish in the next 3-6 months
- **One Bottleneck** — the one obstacle that, if removed, would most accelerate progress toward the Objective
- **One Goal** — a specific, measurable target with a deadline

Example:
```
Objective: Build a personal brand in the [your niche] space
Bottleneck: No consistent content system — posting is manual and irregular
Goal: $10,000/month revenue by December 2026
```

---

## Step 4: Open in Claude Code

Open the directory in your terminal:

```bash
cd revaya-aios-workspace-template
claude
```

Claude Code will launch. The workspace is automatically detected.

---

## Step 5: Run /prime

Type `/prime` and hit Enter.

Claude will:
1. Read `CLAUDE.md` and all context files
2. Summarize its understanding of who you are, what your business does, and what you're working toward
3. Confirm readiness to help

If the summary is off, go back and update your context files. The quality of Claude's responses is directly proportional to the quality of your context.

---

## Step 6: Run /build-guide

Type `/build-guide` and hit Enter.

Claude will:
1. Load your OOBG from `strategic-layer/oobg.md`
2. Scan your projects and priorities
3. Score tasks against the Bottleneck
4. Produce a prioritized daily focus — one Critical task, supporting tasks, blockers

This is your daily operating rhythm. Run `/prime` then `/build-guide` at the start of every working session.

---

## Step 7: Customize the Team

The workspace ships with a generic 14-agent ACRA+2 team in `team/`. The methodology is solid out of the box, but the agents will work better once you customize their "What I Know" sections to reflect your business:

- Your specific services and pricing
- Your target customer and their pain points
- Your competitive positioning
- Your sales process and discovery framework

Start with the agents you'll use most (likely `team/attract/lead.md` and `team/convert/lead.md`). Customize over time as you work.

Test the team with: `/team I need to draft a discovery call framework for my business`

---

## Step 8: Capture Your First Knowledge

After any meaningful work session, run:

```
/reflect
```

This captures your top learning, decision, and any friction — and files it in `knowledge/`. Over time, this becomes the institutional memory of your business.

---

## Session Workflow

Once you're set up, every session follows the same pattern:

```
/prime          → orient Claude to your workspace
/build-guide    → get your OOBG-scored daily focus
[work]          → build, plan, research, draft
/reflect        → capture what you learned
/commit         → save work, update docs, push to GitHub
```

---

## Optional: Content Engine Setup

If you want to use the content pipeline (`/capture`, `/develop`, `/draft-post`):

1. Fill in `content/strategy.md`, `content/brand-and-audience.md`
2. Set up a free [Airtable](https://airtable.com) base using the schema in `docs/content-pipeline.md`
3. Add your `AIRTABLE_TOKEN` to `.env`

The content scripts in `scripts/content/` handle database management and Airtable sync.

---

## Questions

The workspace is self-documenting. Ask Claude directly:

- "How does the knowledge management system work?"
- "What is the OOBG and how do I update it?"
- "Walk me through the /team command"
- "What should I fill in for context/business-info.md?"

Claude has full context on every system in this workspace.
