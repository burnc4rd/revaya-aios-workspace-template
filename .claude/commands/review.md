# Review

> GTD Weekly Review + AIOS Weekly Synthesis — Learning Loops cadence 2 of 5.
> Processes inbox, walks through all project/action lists, scans areas and someday-maybe, rebuilds the dashboard, and runs a structured AIOS health check. Run weekly (Fridays recommended). Target: 45-75 minutes.

---

## Instructions

You are running a **GTD weekly review**. This is the most important habit in the system — it keeps the GTD files trustworthy and complete. Follow the phases below interactively.

---

## Phase 1: Load Context

Read all GTD files:

1. `gtd/dashboard.md` — Current state overview
2. `gtd/inbox.md` — Items to process
3. `gtd/projects.md` — Master project list
4. `gtd/next-actions.md` — Actions by context
5. `gtd/waiting-for.md` — Delegated items
6. `gtd/someday-maybe.md` — Back-burner ideas
7. `gtd/areas.md` — Areas of responsibility
8. `gtd/review-checklist.md` — Review protocol and trigger lists

---

## Phase 2: GET CLEAR

**Goal:** Empty all inboxes and capture everything floating in your head.

### 2.1 Process Inbox
1. Read `gtd/inbox.md`
2. If items exist, walk through each one using the GTD decision tree
3. Route each item to the correct GTD file
4. Empty inbox to zero

### 2.2 Mind Sweep
1. Present the trigger list categories from `gtd/review-checklist.md`
2. Go through each category — ask "Any open loops here?"
3. Capture everything new to inbox, then process it

**STOP after GET CLEAR and confirm before proceeding.**

---

## Phase 3: GET CURRENT

**Goal:** Ensure all lists reflect reality. Every project has a next action.

### 3.1 Review Calendar
- Ask about the past week: any follow-ups needed?
- Ask about the next 2 weeks: any preparation needed?

### 3.2 Walk Through Next Actions
- Present each context section from `gtd/next-actions.md`
- For each action: "Done? Still relevant? Needs updating?"
- Mark completed, remove stale, add new

### 3.3 Walk Through Waiting For
- Present each item from `gtd/waiting-for.md`
- Flag anything overdue — suggest follow-up
- Move received items to Completed section

### 3.4 Walk Through Projects
- Present each project from `gtd/projects.md`
- For each: "Still active? Any progress? Status change?"
- **Stuck project test:** Does every active project have at least one next action?
- Add new projects, move completed ones, kill dead ones

**STOP after GET CURRENT and confirm before proceeding.**

---

## Phase 4: GET CREATIVE

**Goal:** Look up and out. Spot neglected areas and fresh opportunities.

### 4.1 Scan Someday/Maybe
- Present categories from `gtd/someday-maybe.md`
- "Anything ready to activate? Anything to delete? New ideas?"

### 4.2 Scan Areas
- Present `gtd/areas.md` with current health notes
- "Any area being neglected? Any area missing a project?"

### 4.3 Open Brainstorm
- "Any big-picture ideas or strategic thoughts from this review?"
- Capture to appropriate GTD file

### 4.4 AIOS Weekly Synthesis (Learning Loops — cadence 2 of 5)

**Goal:** Assess the AI Operating System itself, not just the tasks inside it.

1. **OOBG Check** — Read `strategic-layer/oobg.md`
   - Is the Bottleneck still accurate, or has it shifted this week?
   - Are there any tasks completed this week that should update the OOBG?
   - Flag if the Bottleneck has been resolved — time to set a new one.
   - **Write-back:** If the Bottleneck has shifted or been resolved, update `strategic-layer/oobg.md` now — do not wait. A stale OOBG means every session runs on the wrong priority.

2. **Metrics Pulse** — Read `metrics/business-kpis.md`
   - Any KPI trending wrong? Any target at risk?
   - What metric most needs attention next week?
   - Note what data is stale and needs updating in Phase 5.

3. **Knowledge Capture Gap** — Scan `knowledge/` recent files
   - Any decision or learning from this week that wasn't captured?
   - Capture it now before it's lost.

4. **Ops Center Health** — Review the 7 sub-components:
   - Prioritization Engine: Was `/build-guide` run this week? Did it load the OOBG?
   - Knowledge Management: Were any decisions or learnings filed this week?
   - Execution Layer: Any GTD or workflow breakdowns?
   - Auto-Capture: Did `/reflect` or `/commit` knowledge checks run?
   - Communications Layer: Any friction in Telegram or terminal interface?
   - Metrics and Monitoring: Is `metrics/business-kpis.md` current?
   - Learning Loops: Was `/reflect` run at least once this week?
   - For each gap: is it a problem to fix, or was it appropriate to skip?

5. **AIOS Improvement** — Surface one specific improvement to the OS for next week
   - Log it to `gtd/inbox.md` for `/process` → becomes a next action or project

### 4.5 Monthly Strategic Reset (Learning Loops — cadence 3 of 5)

**Run only on the first review of each calendar month.**

Check: Is this the first review of a new month? If yes, run this section. If no, skip.

1. **Revenue vs. Target** — Read `metrics/business-kpis.md`
   - Did last month hit the $15K/month profit target?
   - What was the gap (positive or negative)?
2. **Strategy Alignment** — Read `context/strategy.md`
   - Are current projects still the right bets for hitting the annual goal?
   - Any strategy that was valid last month that should be revised?
3. **OOBG Reset** — Read `strategic-layer/oobg.md`
   - Is the One Objective still correct for this month?
   - Has the Bottleneck been resolved? Set the next one.
   - **Write-back:** Update `strategic-layer/oobg.md` with any changes.
4. **Content Alignment** — Review last month's content performance
   - What content worked? What didn't?
   - Any pillar that needs more or less weight next month?
5. **Next Month Intention** — Set one clear intention for the month
   - One Objective, one Bottleneck, one measurable Goal
   - Log to `strategic-layer/oobg.md`

**STOP after Phase 4 and confirm before proceeding.**

---

## Phase 5: REBUILD

**Goal:** Update the dashboard and metrics with fresh data.

1. Run `python3 scripts/refresh_dashboard.py` to recompute counts
2. Update the Flagged/Urgent section if needed
3. Set "Last Review" to today's date
4. Set "Next Review" to one week from today
5. Update `metrics/business-kpis.md` — record this week's data:
   - Revenue closed this week
   - Pipeline changes (new leads, closed deals, lost)
   - Content published (posts, videos)
   - Any KPI that moved since last review
   - Set "Last Updated" to today's date
6. Report summary:
   - Items processed from inbox
   - Projects added / completed / killed
   - Next actions added / completed
   - Waiting-for items flagged or resolved
   - Areas that need attention
   - Next review date

---

## Critical Rules

- **Interactive** — This is a conversation, not a monologue. Present lists, ask questions, wait for responses.
- **Don't skip phases** — Each serves a purpose. GET CLEAR before GET CURRENT before GET CREATIVE.
- **Specific actions** — Next actions must be physical and visible. "Think about pricing" is not an action. "Draft three pricing options in a doc" is.
- **Every project needs a next action** — The #1 failure mode.
- **Update files as you go** — Don't just discuss changes, write them.
- **Time-box** — If a topic goes deep, capture it and move on. The review is about breadth, not depth.
