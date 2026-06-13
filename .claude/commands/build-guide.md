# Build Guide

> Generate a daily strategic build guide covering all active projects.
> Powered by the Prioritization Engine — scored against the OOBG.

## Run

> OOBG and priorities are already loaded by `/prime`. Use them as the filter — do not re-read.

Read the following files to understand current state across all builds:

1. All build journals in the Obsidian vault: `[OBSIDIAN_VAULT_PATH]/Build Journals/*.md`
2. `strategic-layer/priorities.md` — current ranked priorities
3. `context/current-data.md` — current pipeline and metrics

## Analysis

For each build journal:
1. Find the **Current phase** and **Status** in the header
2. Find the latest **Build Log** entry and its **Next:** line
3. Check for incomplete checkboxes in the current phase
4. Note any **Open Questions** that are blocking progress

Then apply OOBG scoring to all candidate tasks:
- **🔴 Critical** — directly addresses the current Bottleneck or enables the One Objective
- **🟡 Important** — necessary but not bottleneck-breaking
- **🟢 Maintenance** — required to keep existing commitments
- **⚪ Question** — unclear connection to OOBG; flag it

Prioritize ruthlessly:
- The Bottleneck from `oobg.md` determines today's #1 focus — not project order
- Blocked projects (waiting on client feedback) get one-line status, not a full focus section
- Route today's focus task to its ACRA department or pipeline (Attract / Convert / Retain and Deliver / Ascend / Finance / AI HR)
- **Exclude InfluencerOS** — on hold, do not surface in project status

## Output

Generate a **BUILD GUIDE** with these sections:

### 1. Today's Focus
The single most important thing to work on today — scored Critical against the OOBG.
- Name the OOBG Bottleneck it addresses
- State the task clearly
- Name which ACRA department owns it (Attract / Convert / etc.)
- 2–3 sentences of context on why it matters today specifically

### 2. Project Status (all active builds)
One line per project: name, current phase, status, what's next or what's blocking.

Format:
```
- **Project** — Phase X (status) → Next: [action] [🔴/🟡/🟢]
```

### 3. Alignment Check
Flag any project or task that does NOT connect to the OOBG Objective or Bottleneck.
- "⚪ [Project/Task] — unclear OOBG connection. Consider: kill it, park it, or challenge the priority."
- If nothing to flag: "All active work connects to the OOBG."

### 4. Blockers and Prerequisites
Check across all projects for anything blocking productive work:
- Incomplete manual steps
- Missing API keys, accounts, or infrastructure
- Client feedback not yet received
- Long lead-time items
If nothing is blocking, say "Clear — no blockers."

### 5. Strategic Context
Connect today's work to the OOBG directly. Name the Objective and the Bottleneck.
Keep it to 2–3 sentences. No generic motivational filler.

### 6. Open Questions
Surface 1–3 unresolved decisions from any project's Open Questions section.

## Format

```
BUILD GUIDE — [Day of week], [Month] [Day], [Year]

**OOBG:** [One Objective] | Bottleneck: [current bottleneck]

**Today's focus (🔴 Critical):** [one clear task]
Department: [ACRA dept] | Bottleneck addressed: [yes/how]
[2-3 sentences of context]

**All projects:**
- **Project** — Phase X (status) → Next: [action] [🔴/🟡/🟢]

**Alignment check:** [flag or "All work connects to OOBG"]

**Blockers:** [status]

**Strategic context:** [2-3 sentences referencing OOBG]

**Open questions:**
- [question 1]
```

Keep the entire output under 350 words. This is a compass, not a report.
