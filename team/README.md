# [YOUR_BUSINESS_NAME] Team — ACRA+2 Department Structure

This is the Execution Layer of the [YOUR_BUSINESS_NAME] OS — the AI workforce organized by customer lifecycle.

## Model: ACRA+2

| Department | Mission | Files |
|-----------|---------|-------|
| Attract | Bring the right people in | `attract/lead.md`, `attract/content-specialist.md` |
| Convert | Turn attention into buyers | `convert/lead.md`, `convert/discovery-specialist.md`, `convert/proposal-specialist.md`, `convert/conversion-copy-specialist.md` |
| Retain & Deliver | Keep clients and get results | `retain-deliver/lead.md`, `retain-deliver/delivery-specialist.md`, `retain-deliver/technical-specialist.md` |
| Ascend | Move clients up the value ladder | `ascend/lead.md`, `ascend/relationship-specialist.md` |
| Finance | Track performance, feed metrics | `finance/lead.md`, `finance/numbers-specialist.md` |
| AI HR | Build and optimize the AI workforce | `ai-hr/lead.md`, `ai-hr/build-specialist.md` |

Cross-functional: `research-analyst.md` — commissioned by any department.

## Lead vs Specialist

**Lead (Orchestrator):** Sets direction, makes decisions, orchestrates the specialists, hands off to other departments.

**Specialist:** Deep function expert. Works within the department. Refers decisions up to the Lead.

## /team Routing

Use `/team [request]` to route to the right role. The command reads the request and selects the best-fit department or specialist.

Quick guide:
- Content idea, brand question → Attract Lead
- LinkedIn post, YouTube script → Content Specialist
- Sales strategy, conversion question → Convert Lead
- Discovery call, deal qualification → Discovery Specialist
- Outreach, proposal building → Proposal Specialist
- Sales page, email sequence, VSL script → Conversion Copy Specialist
- Client delivery, project management → Retain & Deliver Lead
- Website build, technical work → Technical Specialist
- AIOS client delivery question → Delivery Specialist
- Upsell, client upgrade → Ascend Lead
- Client relationship check-in → Relationship Specialist
- Revenue, expenses, P&L → Finance Lead
- KPIs, data tracking → Numbers Specialist
- Agent architecture, system design → AI HR Lead
- Build an agent, automation work → Build Specialist
- Research (any area) → Research Analyst

## File Format

Each agent file follows this structure:
1. **Mission** — one clear statement of why this role exists
2. **What I Know** — embedded knowledge (ICP, platform specs, frameworks, offer stack, etc.)
3. **Pipeline** — how work flows through this role
4. **Decision Authority** — what it owns, advises on, and escalates
5. **Handoff** — standard handoff language

## Support Files

These are architecture-level files, not agent files:
- `acra-map.md` — all legacy roles mapped to ACRA+2 departments (reference)
- `ai-hr-protocol.md` — AI HR responsibilities and active workforce log
- `project-protocol.md` — cross-functional project kick-off and tracking
- `org-chart.md` — visual overview of current team structure

## Legacy Archive

The original 27-role functional org is archived at `reference/legacy-team-org/`. Reference it for deep workflow knowledge or client onboarding context.
