# /schedule — Schedule Content

> Interactive scheduling session — pick developed ideas, assign dates, and manage the content calendar.

## Variables

$ARGUMENTS (optional: "review" to review existing schedule instead of scheduling new content)

## Instructions

You are running a **Scheduling Session** for the Content Pipeline. Help you pick which developed ideas to create next, assign dates, and manage the calendar.

### Setup — Load Current State

1. **Read the strategy:**
   - `content/strategy.md` — platform cadence, format types

2. **Query the pipeline:**
   ```bash
   .venv/bin/python3 -c "
   import sys, sqlite3; sys.path.insert(0, '.')
   from scripts.content.db import get_connection
   conn = get_connection()

   # Developed ideas ready to schedule
   developed = conn.execute(\"\"\"
       SELECT id, title, channel, format_type, priority_score,
              edit_turnaround_days, audience_segment, offer_alignment, created_at
       FROM content_ideas WHERE production_status = 'developed'
       ORDER BY COALESCE(priority_score, 0) DESC, created_at DESC
   \"\"\").fetchall()

   # Currently scheduled
   scheduled = conn.execute(\"\"\"
       SELECT id, title, channel, format_type, film_by_date,
              publish_date, production_status
       FROM content_ideas WHERE production_status IN ('scheduled', 'filmed', 'editing')
       ORDER BY publish_date ASC
   \"\"\").fetchall()

   print('=== DEVELOPED (ready to schedule) ===')
   for r in developed:
       p = f'P{r[\"priority_score\"]}' if r['priority_score'] else '—'
       print(f'  #{r[\"id\"]} [{r[\"channel\"] or \"?\"}] {r[\"title\"]} ({p})')

   print()
   print('=== CURRENTLY SCHEDULED ===')
   for r in scheduled:
       print(f'  #{r[\"id\"]} [{r[\"channel\"] or \"?\"}] {r[\"title\"]} — publish: {r[\"publish_date\"] or \"TBD\"} ({r[\"production_status\"]})')

   conn.close()
   "
   ```

3. **Read active campaigns** (if relevant):
   - `content/offers-and-funnels.md` — active campaigns to align scheduling with

---

### Stage 1: REVIEW CURRENT SCHEDULE

Present the current state:
- **Scheduled/In-progress items** with dates
- **Gaps** — days without content planned (reference their target cadence from strategy.md)
- **Channel balance** — LinkedIn vs YouTube mix

Format as a compact table.

---

### Stage 2: PRESENT DEVELOPED IDEAS

Show developed ideas ranked by priority:

```
Ready to Schedule:
| # | ID | Title | Channel | Format | Priority | Turnaround |
|---|-----|-------|---------|--------|----------|------------|
...
```

Suggest which ideas fit gaps in the schedule and align with any active campaigns.

**Ask: "Which ideas do you want to schedule? Give me the IDs and target publish dates."**

**STOP. Wait for your's picks.**

---

### Stage 3: CALCULATE DATES & CONFIRM

For each picked idea:
1. Calculate `film_by_date = publish_date - edit_turnaround_days`
2. Check for conflicts (two things due on the same creation date)
3. Present the schedule:

```
Content Schedule:
| Create By | Publish Date | Title | Channel | Format |
|-----------|-------------|-------|---------|--------|
...
```

**Ask: "Does this schedule work? Any date changes?"**

**STOP. Wait for confirmation.**

---

### Stage 4: UPDATE DATABASE

After confirmation:

```bash
.venv/bin/python3 -c "
import sys; sys.path.insert(0, '.')
from scripts.content.db import get_connection
from scripts.content.writer import update_status

conn = get_connection()
# Repeat for each scheduled idea:
update_status(conn, IDEA_ID, 'scheduled',
    film_by_date='YYYY-MM-DD', publish_date='YYYY-MM-DD')
conn.close()
print('Schedule updated.')
"
```

Then regenerate pipeline:
```bash
.venv/bin/python3 scripts/content/generate_pipeline.py
```

Report:
- Summary: X ideas scheduled
- Next creation date and what to create
- LinkedIn: "Remember to run `/draft-post #ID` before the create date."
- YouTube: "Script outline ready in `content/concepts/` — time to film."

---

### Review Mode

If `$ARGUMENTS` = "review":
- Show all scheduled/in-progress items
- Flag overdue items (film_by_date < today, still "scheduled")
- Allow status updates: mark as filmed, move to editing, mark published
- For published items: prompt to log the Airtable record for analytics tracking

---

### Critical Rules

- **Interactive** — always confirm before updating dates
- **Conflict detection** — flag if two items have the same creation date
- **Format-aware** — long_form YouTube needs 7 days lead time; LinkedIn post = 0
- **Never auto-schedule** — you picks what to schedule and when
- **Connect to Airtable** — when a LinkedIn post is published, remind you to update the Airtable record status to "Posted"

$ARGUMENTS
