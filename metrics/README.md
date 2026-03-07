# Metrics and Monitoring

> Business pulse and system pulse — on demand.
> This is the 6th sub-component of the Operations Center.

---

## What This Is

The Metrics and Monitoring layer gives instant answers about what's working, what's not, and what to fix next. It combines clean, structured business data with AI queries — no rigid dashboards, just answers to the questions you actually have.

**The principle:** Ask questions in plain language. Get answers from the data. Build dashboards only when you need visualization.

---

## Data Sources

| Source | Data | Update Cadence |
|--------|------|---------------|
| `metrics/business-kpis.md` | Revenue, pipeline, content, AIOS health | Weekly (during `/review` Phase 5) |
| `context/current-data.md` | Pipeline detail, active builds, active clients | As-needed |
| `data/intel.db` | Meeting transcripts, Slack messages | Daily (via launchd) |
| Airtable — Revaya Content Engine | Post analytics, content pipeline | Manual (via `/mark-posted`, `/log-performance`) |

---

## How to Query

**Via `/metrics` command:**
- No argument: full KPI summary in plain language
- With question: `/metrics how is pipeline looking?`
- The command reads `metrics/business-kpis.md` and `context/current-data.md`, then answers

**Direct query (any session):**
- Ask: "What's our current pipeline value?" — Claude reads `context/current-data.md`
- Ask: "Have we hit our content target this week?" — Claude reads `metrics/business-kpis.md`

---

## Who Maintains This

**Finance department** is responsible for updating revenue and KPI data.

- Revenue and pipeline: updated after any deal closes or stage changes
- Content metrics: updated after each post goes live (pull from Airtable)
- AIOS health indicators: updated during `/reflect` (daily) and `/review` (weekly)

---

## Connection to Learning Loops

Metrics and Monitoring feeds Learning Loops directly:

- **Daily:** `/reflect` checks if work moved the bottleneck — pulls from this layer
- **Weekly:** `/review` Phase 4.4 (AIOS Weekly Synthesis) reads `business-kpis.md` to assess KPI trends
- **Monthly:** Strategic Reset reviews KPI movement against OOBG targets
- Anomalies and downward trends surface as inputs to the next cadence

---

## Files

| File | Purpose |
|------|---------|
| `metrics/README.md` | This file — system overview |
| `metrics/business-kpis.md` | All KPIs with current values, targets, and data sources |
