# Project Protocol

> Cross-functional orchestrated missions.
> This is the Projects component of the Execution Layer — distinct from ongoing department work.

---

## What a Project Is

A **project** in the AIOS sense is:
- **Temporary** — it has a clear beginning and a clear end
- **Cross-functional** — it requires multiple ACRA departments working together
- **Orchestrated** — coordinated through the Operations Center, not just one department's work
- **Mission-driven** — one clear objective that defines when it's done

Projects are NOT:
- Ongoing department work (that's what departments do continuously)
- Single-team tasks (those stay in the relevant department)
- Vague "initiatives" with no defined end state

---

## Project vs Department Work

| Criteria | Department Work | Project |
|----------|----------------|---------|
| Duration | Ongoing, indefinite | Temporary, defined end |
| Scope | Within one department | Crosses department lines |
| Coordination | Department orchestrator | Ops Center coordinates all teams |
| Example | Publishing weekly LinkedIn posts | Launching Claude Lab Course v1 |
| Artifact | None needed | Plan in `plans/` |

---

## When to Create a Project

Create a project when:
1. The work requires resources from 2+ ACRA departments
2. There's a clear "done" state that ends the project
3. The work is significant enough to warrant its own plan and tracking
4. Shared context needs to be documented for all teams involved

---

## Project Kick-Off Template

When starting a new project, create a plan in `plans/` and include this header:

```markdown
## Project Brief

**Project Name:** [clear, specific name]
**Objective:** [one sentence — what does "done" look like?]
**Departments Involved:** [list ACRA departments]
**Roles Involved:** [specific role files from team/]
**Shared Context Needed:** [files all teams need to read]
**Ops Center Coordination:** [which commands/workflows manage this]
**Start Date:** YYYY-MM-DD
**End State:** [specific, measurable — when is this project complete?]
**Related Plan:** [path to full plan in plans/]
```

---

## Active Projects

| Project | Departments | Status | Plan | End State |
|---------|------------|--------|------|-----------|
| Claude Lab Course v1 | Attract, Convert, AI HR | Planning | TBD | First course live and selling |
| InfluencerOS Delivery | Retain & Deliver | In Progress | `plans/influencer-os/` | Site live, client approved |
| Dale's Pipeline OS | Retain & Deliver | In Progress | `plans/dale-pipeline-os/` | Prototype wired to live data, client approved |
| AIOS Architecture Restructure | AI HR | In Progress | `plans/2026-03-05-aios-9-component-restructure.md` | All 9 components implemented |

---

## Example: Multi-Department Project

**"Launch Claude Lab Course v1"**

- **CMO** (Attract): Content strategy for launch — build-in-public posts, YouTube content about the build
- **Copywriter** (Convert): Sales page copy, email sequence for launch
- **AI Engineer** (AI HR): Build the course infrastructure and any agents that run it
- **CFO** (Finance): Pricing strategy, revenue targets for launch
- **CRO** (Convert): Conversion optimization — landing page, CTA, checkout flow
- **Account Executive** (Convert): Outreach to warm leads for early access

This requires all five departments. No single department can run it. The Ops Center (`/create-plan` + `/implement`) coordinates the work. The plan lives in `plans/claude-lab/`.

---

## How Projects Connect to the Ops Center

```
Ops Center Logic (Execution Layer)
    ↓ coordinates
ACRA Departments (execute in their domains)
    ↓ generate activity that flows into
Auto-Capture (feeds Knowledge Management + Metrics)
    ↓ feeds
Learning Loops (reviews what worked, refines the next project)
```

Projects are the mechanism by which the system produces its most significant outputs. They're not separate from the OS — they run through it.

---

## Closing a Project

When a project reaches its end state:
1. Update the plan status to `Completed`
2. Run `/reflect` or `/commit` with knowledge capture — what was learned?
3. Archive any reusable patterns to `knowledge/learnings/`
4. Remove from Active Projects table above
5. Note in HISTORY.md
