# [YOUR_BUSINESS_NAME] Team — ACRA+2 Department System

**Condition:** Load when working with team roles, `/team`, `/board`, `team/` directory, or department agent files.

---

## What This Is

The [YOUR_BUSINESS_NAME] team is 14 specialized agents organized across 6 ACRA+2 departments + 1 cross-functional Research Analyst. Each agent file carries embedded methodology ("What I Know") so no external context files need loading for most tasks — the knowledge is already in the file.

This is not a literal team — it's a routing and persona system organized by customer lifecycle (Attract → Convert → Retain & Deliver → Ascend), supported by Finance and AI HR.

---

## Architecture

### Lead vs Specialist

- **Lead (Orchestrator):** Sets direction, makes decisions, routes to specialists, hands off to other departments. One per department.
- **Specialist:** Deep functional expert within a department. Refers decisions to the Lead.

### Agent File Structure

Every agent file follows this format:
1. **Mission** — one clear statement of why this role exists
2. **What I Know** — embedded methodology (ICP psychology, positioning, platform specs, offer stack, operating methods). The "no re-explaining per session" section.
3. **Pipeline** — how work flows through this role
4. **Decision Authority** — Owns / Advises / Escalates
5. **Handoff** — standard closing line with routing instruction

The "What I Know" section is the core innovation. It carries the *why* behind the *what* — not just reference data but embedded judgment. An agent with good "What I Know" can evaluate a new idea against positioning without loading any external files.

---

## Team Structure

| Department | Files | Mission |
|-----------|-------|---------|
| Attract | `attract/lead.md`, `attract/content-specialist.md` | Bring the right people in |
| Convert | `convert/lead.md`, `convert/discovery-specialist.md`, `convert/proposal-specialist.md`, `convert/conversion-copy-specialist.md` | Turn attention into signed clients |
| Retain & Deliver | `retain-deliver/lead.md`, `retain-deliver/delivery-specialist.md`, `retain-deliver/technical-specialist.md` | Keep clients and deliver results |
| Ascend | `ascend/lead.md`, `ascend/relationship-specialist.md` | Move clients up the value ladder |
| Finance | `finance/lead.md`, `finance/numbers-specialist.md` | Track performance, feed the Strategic Layer |
| AI HR | `ai-hr/lead.md`, `ai-hr/build-specialist.md` | Build and optimize the AI workforce |
| Cross-functional | `research-analyst.md` | Commissioned by any department |

---

## Commands

### `/team [request]`

Routes to a single best-fit role. Claude:
1. Reads the request and identifies domain + output type
2. Selects the role using the routing table in `.claude/commands/team.md`
3. Reads the role file (embedded knowledge loads — no additional context files needed for most tasks)
4. Responds in the role's voice, applying its decision authority
5. Ends with the role's handoff protocol if work continues

**When to use:** Single-department questions, execution tasks, analysis requests.

### `/board [decision]`

Convenes 2-4 Department Leads for cross-functional decisions. Claude:
1. Identifies which departments have a stake
2. Each Lead speaks in sequence within their domain
3. Synthesis presents options and a recommendation — [YOUR_NAME] decides

**When to use:** Decisions that cross departmental boundaries (capacity + finance + pipeline, etc.)

---

## Routing Quick Reference

| Task | Route to |
|------|---------|
| Content idea, brand, ICP | Attract Lead |
| LinkedIn post, YouTube script | Content Specialist |
| Sales strategy, pipeline, funnel | Convert Lead |
| Discovery call, deal qualification | Discovery Specialist |
| Outreach, proposals | Proposal Specialist |
| Sales page, email sequence, VSL | Conversion Copy Specialist |
| Client delivery, capacity | Retain & Deliver Lead |
| Website, builds, QA | Technical Specialist |
| Client onboarding, PM | Delivery Specialist |
| Upsell, upgrade strategy | Ascend Lead |
| Client relationship, referrals | Relationship Specialist |
| Pricing, financial decisions | Finance Lead |
| KPI tracking, P&L, expenses | Numbers Specialist |
| Agent architecture, system design | AI HR Lead |
| Build agents, automate workflows | Build Specialist |
| Research (any type) | Research Analyst |

---

## Support Files (not agent files)

| File | Purpose |
|------|---------|
| `team/README.md` | ACRA+2 model overview, Lead vs Specialist, routing guide |
| `team/org-chart.md` | Department structure, decision flow, routing quick reference |
| `team/acra-map.md` | Legacy role → ACRA+2 department mapping (historical reference) |
| `team/ai-hr-protocol.md` | AI HR responsibilities and active workforce log |
| `team/project-protocol.md` | Cross-functional project kick-off and tracking |

---

## Legacy Archive

The original 27-role functional org (executives, creative-marketing, engineering, client-services, business-dev, finance, platforms) is archived at `reference/legacy-team-org/`. Reference when you need deep workflow context from the original role files.

---

## History

| Date | Change |
|------|--------|
| 2026-03-04 | Initial build — 27 roles across 6 teams, /team + /board commands, CMO Telegram integration, 4 platform context files |
| 2026-03-05 | Full ACRA+2 rebuild — replaced 27-role functional org with 14 agents across 6 departments. New embedded methodology format ("What I Know"). Legacy org archived. /team and /board commands rewritten. |
