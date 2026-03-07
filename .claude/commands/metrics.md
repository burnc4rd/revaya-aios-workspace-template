# Metrics

> On-demand business pulse. Reads live KPI data and answers questions in plain language.
> Part of the Metrics and Monitoring sub-component of the Operations Center.

## Variables

question: $ARGUMENTS (optional — specific question, or leave blank for full summary)

---

## Instructions

You are the AIOS metrics query layer. Load the data, answer the question (or provide a full summary), and surface any anomalies.

### Step 1: Load Data

Read both files:
1. `metrics/business-kpis.md` — current KPI values, targets, AIOS health
2. `context/current-data.md` — pipeline detail, active builds, client status

### Step 2: Answer the Question

**If `$ARGUMENTS` was provided:**
- Answer the specific question using the data loaded
- Be direct: one paragraph, specific numbers, no filler
- If the data to answer the question is stale or missing, say so explicitly

**If no argument provided:**
- Deliver a full business pulse summary in plain language covering:

**Revenue:**
- Closed revenue (all-time)
- Open pipeline value and composition
- Progress toward $15K/month target

**Content:**
- Posts published this month
- Any significant engagement or anomalies

**Product:**
- Status of Claude Lab and Business AIOS service
- Any blockers

**AIOS Health:**
- When was `/reflect` last run?
- When was `/review` (AIOS Weekly Synthesis) last run?
- Which Ops Center components were used this week?

**Three Core KPIs:**
- Away-from-desk autonomy
- Task automation %
- Revenue per person

### Step 3: Flag Anomalies

After the summary, explicitly flag:
- Any KPI moving in the wrong direction
- Any data that is stale (not updated in 2+ weeks)
- Any AIOS health indicator that's overdue
- Any action needed from Finance, CMO, or AI HR to update the data

Format anomaly flags as:
```
NEEDS ATTENTION: [what] — [why it matters] — [who updates it]
```

### Step 4: Data Quality Note

At the end, note the data freshness:
- "Data as of: [date from business-kpis.md Last Updated field]"
- "Pipeline detail from: [date range in current-data.md]"
- "To update: run `/review` and complete Phase 5"

---

## Output Format

```
## Business Pulse — [Today's Date]

### Revenue
[Summary]

### Content
[Summary]

### Product Status
[Summary]

### AIOS Health
[Summary]

### Core KPIs
[Summary]

---

NEEDS ATTENTION (if any):
- [Flag]

Data as of: [date]
```

---

## Notes

- This is v1: reads markdown files. v2 will query Airtable and intel.db directly.
- If asked a question about data this command doesn't have access to, say so clearly and suggest where to find it.
- Never fabricate numbers. If a value is unknown, state it as unknown.
