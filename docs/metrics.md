# Metrics and Monitoring — System Doc

> Business pulse and system pulse — on demand. Clean metrics combined with AI queries.

**Last Updated:** 2026-03-05

---

## What It Is

Metrics and Monitoring is the 6th sub-component of the Operations Center. It provides instant answers about what's working, what's not, and what to fix next — without rigid dashboards. Query with natural language; get answers from structured data.

---

## File Map

| Path | Purpose |
|------|---------|
| `metrics/README.md` | System overview, data sources, query patterns |
| `metrics/business-kpis.md` | All KPIs with current values, targets, and data sources |

---

## Data Sources

| Source | Data | Update Cadence |
|--------|------|---------------|
| `metrics/business-kpis.md` | Revenue, pipeline, content, product status, AIOS health | Weekly (Fridays, during `/review` Phase 5) |
| `context/current-data.md` | Pipeline detail, active builds, client status | As-needed |
| `data/intel.db` | Meeting transcripts, Slack messages | Daily (via launchd) |
| Airtable — Revaya Content Engine | Post analytics | Manual |

---

## How to Query

**Via `/metrics` command:**
- No argument: full KPI summary in plain language
- With question: `/metrics how is pipeline looking?`

**Direct question in any session:**
- "What's our current pipeline value?" — Claude reads `context/current-data.md`
- "How is AIOS health?" — Claude reads `metrics/business-kpis.md` AIOS Health section

---

## Ownership

| Data Domain | Owner | Update Trigger |
|-------------|-------|---------------|
| Revenue and pipeline | Finance dept (CFO, Finance Analyst) | After each deal closed or stage change |
| Content metrics | CMO | After each post published |
| AIOS health indicators | AI HR (CTO) | During `/reflect` and `/review` |
| Full KPI update | All | Friday `/review` Phase 5 |

---

## Connection to Other Components

- **Fed by:** Finance dept (revenue/pipeline), CMO (content), Auto-Capture (AIOS health), Airtable connector (post analytics)
- **Feeds:** Learning Loops — `/review` Phase 4.4 reads `business-kpis.md` to assess trends
- **Queried by:** `/metrics` command, `/review` AIOS Weekly Synthesis

---

## v1 vs v2

**v1 (current):** Markdown-based. Manual updates. Finance analyst and CMO maintain `business-kpis.md`. `/metrics` reads and interprets the file.

**v2 (Phase 2):** Live queries against Airtable (content metrics) and `intel.db` (meeting activity). Finance auto-updates from Airtable.

---

## History

| Date | Change |
|------|--------|
| 2026-03-05 | Created as part of AIOS 9-component restructure. `business-kpis.md` seeded with current data. |
