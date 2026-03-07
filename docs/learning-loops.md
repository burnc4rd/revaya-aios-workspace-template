# Learning Loops — System Doc

> The feedback engine that makes the AIOS smarter over time. Structured reflection at every cadence turns experience into compounding advantage.

**Last Updated:** 2026-03-05

---

## What It Is

Learning Loops is the 7th sub-component of the Operations Center. It reviews what worked, what didn't, and what to change — then feeds those insights back into the Strategic Layer, Knowledge Management, and Execution Layer. This is how the system compounds.

**Three levels of compounding:**
1. Knowledge gets richer (more decisions and learnings captured over time)
2. Strategy gets sharper (OOBG refined by real performance data)
3. Execution gets more effective (patterns captured → processes improved)

---

## 5 Cadences

| Cadence | When | Command | Output |
|---------|------|---------|--------|
| 1. Daily Assessment | End of each significant session | `/reflect` | `knowledge/learnings/YYYY-MM-DD-daily-reflect.md` |
| 2. Weekly Synthesis | Fridays | `/review` Phase 4.4 | OOBG check, KPI trend review, AIOS improvement logged to GTD |
| 3. Monthly Strategic Reset | First review of each calendar month | `/review` Phase 4.5 | Revenue vs. target, strategy alignment, OOBG reset, content alignment, next month intention |
| 4. Quarterly Review | End of each quarter | Template (Phase 2) | Deep review across all 9 components |
| 5. Annual Review | End of year | Template (Phase 2) | Full strategic reset, direction update |

Cadence 3 is built as `/review` Phase 4.5. Cadences 4 and 5 remain Phase 2.

---

## Cadence 1: Daily Assessment (`/reflect`)

**Target:** 5-10 minutes. End of any significant work session.

What it captures:
- OOBG alignment score (🔴 Directly addressed Bottleneck / 🟡 Served Objective / 🟢 Maintenance / ⚪ Unclear)
- Top accomplishment (one sentence, specific)
- Top learning or insight
- Friction identified (logged to GTD inbox)
- Execution pattern worth capturing

Output: `knowledge/learnings/YYYY-MM-DD-daily-reflect.md`

---

## Cadence 2: Weekly Synthesis (`/review` Phase 4.4)

**Target:** During Friday `/review`, after GET CREATIVE phases.

What it reviews:
- Is the Bottleneck still accurate or has it shifted?
- Any KPI trending wrong? (`metrics/business-kpis.md`)
- Knowledge capture gaps from the week
- Which of the 7 Ops Center components were used vs idle
- One AIOS improvement for next week → logged to GTD inbox

---

## Cadence 3: Monthly Strategic Reset (`/review` Phase 4.5)

**Target:** First review of each calendar month. Runs inside `/review` — check "is this the first review of a new month?" and run if yes.

What it reviews:
1. **Revenue vs. Target** — did last month hit $15K/month profit? What was the gap?
2. **Strategy Alignment** — are current projects still the right bets? (`context/strategy.md`)
3. **OOBG Reset** — is the One Objective still correct? Has the Bottleneck been resolved? Set next one. **Write-back: update `strategic-layer/oobg.md`.**
4. **Content Alignment** — what content worked last month? Adjust pillar weight if needed.
5. **Next Month Intention** — set one clear OOBG for the month. Log to `strategic-layer/oobg.md`.

---

## What Fuels the Learning Loops

| Source | What It Provides |
|--------|----------------|
| Auto-Capture (`/commit` Step 1.5) | Decisions and learnings filed per session |
| `/reflect` (daily) | Structured end-of-session reflection |
| `metrics/business-kpis.md` | KPI trends and AIOS health data |
| GTD inbox | Friction items and improvement ideas |
| `knowledge/` | Accumulated context from all past sessions |

---

## Connection to Other Components

- **Fed by:** Auto-Capture, Metrics and Monitoring, Knowledge Management
- **Feeds:** Strategic Layer (OOBG refinement), Knowledge Management (new learnings), Execution Layer (process improvements)
- **The cycle:** Execution → Auto-Capture → Knowledge + Metrics → Learning Loops → Strategic Layer → better Prioritization → better Execution

---

## History

| Date | Change |
|------|--------|
| 2026-03-05 | Created as part of AIOS 9-component restructure. `/reflect` built for cadence 1. `/review` updated with Phase 4.4 for cadence 2. |
| 2026-03-05 | Cadence 3 (Monthly Strategic Reset) built as `/review` Phase 4.5 with full checklist. OOBG write-back added to cadence 2. `/prime` now loads `strategic-layer/oobg.md` at session start. |
