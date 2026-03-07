# Reflect

> Daily Assessment — Learning Loops cadence 1 of 5.
> End-of-session or end-of-day capture. Target: 5–10 minutes.
> Output is filed to `knowledge/learnings/` and feeds the Ops Center's knowledge loop.

---

## Purpose

This is not journaling. It is structured data capture for the AIOS. Every session produces execution data. This command extracts it before it's lost. The Auto-Capture data layer feeds Knowledge Management, which feeds Learning Loops, which refines the Strategic Layer.

Run this at the end of any significant work session — especially before closing Claude Code.

---

## Step 1: Load the OOBG

Read `strategic-layer/oobg.md`.

Ask: Was today's work aligned with the One Objective? Did it address the current Bottleneck? Score it:
- 🔴 Directly addressed the Bottleneck
- 🟡 Served the Objective but didn't move the needle on the Bottleneck
- 🟢 Maintenance/required work, not bottleneck-breaking
- ⚪ Unclear — flag for review

---

## Step 2: Top Accomplishment

What was the single most important thing completed today?

One sentence. Specific. Not "worked on the plan" — "created the strategic-layer directory with all 4 files."

---

## Step 3: Top Learning or Insight

What's the most important thing learned or realised during today's execution?

Could be technical (a tool works differently than expected), strategic (a market insight), operational (a process that should change), or personal (a pattern in how you work).

If nothing significant: that's fine. Say so. Don't manufacture learnings.

---

## Step 4: Friction Identified

What slowed things down, created confusion, or felt harder than it should?

This is AIOS improvement data. Friction is a signal. Small frictions repeated over sessions compound into significant drag.

If friction was identified:
1. Note it here
2. Log it to `gtd/inbox.md` for the next `/process` session — it may become an improvement task

---

## Step 5: Execution Pattern

Did anything repeat today that could become a reusable knowledge chunk?

Examples: a way of structuring a type of file, a sequence of commands that worked well, a way of framing a problem that produced better output.

If yes, note it — it may become a `knowledge/learnings/` entry or even a new skill/command.

---

## Step 6: Build Moment Capture

Ask: "What from this session would a business owner building their first AI-powered business want to know?"

Run the moment through the 4-filter test (any ONE qualifies it):
- Surprise test: Did something work differently than expected, or fail in an interesting way?
- Decision test: Did you make a call with a real reason? ("I chose X over Y because Z")
- Ahead-of-you test: Would someone 6 months behind you building their first AI-powered business wish they'd known this?
- Proof test: Does it show the Business AI OS working in a specific, observable way?

If a moment qualifies — capture it as a stub using the 5-field model:
- moment (one sentence — what happened) → maps to title
- so_what (why someone else should care) → maps to description
- pillar (Operational Problems / Lived Experience / Practical Value / Personal Journey) → maps to content_pillar
- format (LinkedIn post / YouTube tutorial / LinkedIn article) → maps to format_type
- hook (first line if one comes naturally — optional) → maps to hook

Use channel: linkedin for posts, youtube for tutorials.

```bash
.venv/bin/python3 -c "
import sys; sys.path.insert(0, '.')
from scripts.content.db import get_connection
from scripts.content.writer import write_content_idea

idea = {
    'title': 'MOMENT_HERE',
    'description': 'SO_WHAT_HERE',
    'hook': 'HOOK_HERE_OR_NONE',
    'channel': 'CHANNEL',
    'format_type': 'FORMAT',
    'source_type': 'build_moment',
    'content_pillar': 'PILLAR',
    'audience_segment': 'Drowning Operator',
    'funnel_position': 'awareness',
}

conn = get_connection()
idea_id = write_content_idea(conn, idea)
conn.close()
print(f'Build moment captured as stub #{idea_id}')
"
```

Then regenerate the pipeline:
```bash
.venv/bin/python3 scripts/content/generate_pipeline.py
```

If no moment qualifies — that is fine. Say "No build moment identified this session." and move on. Do not manufacture content.

Reference: `reference/build-capture-filter.md`

---

## Step 7: File the Output

Save the structured output to `knowledge/learnings/YYYY-MM-DD-daily-reflect.md` using this format:

```markdown
# Daily Reflect: [Date]

**OOBG alignment:** [🔴/🟡/🟢/⚪] — [one sentence explanation]

**Top accomplishment:** [specific, one sentence]

**Top learning:** [what was learned, or "None significant"]

**Friction identified:** [description, or "None"]
- GTD inbox: [yes/no — what was logged]

**Execution pattern:** [pattern worth capturing, or "None"]

**Build moment captured:** [stub #ID — title] or [None]
```

---

## What Happens Next

The filed reflect entry:
- Feeds the Knowledge Management pipeline (captured → structured)
- Is reviewed during the Weekly Synthesis (`/review` Phase 4.4)
- Informs the Monthly Strategic Reset (are patterns emerging?)
- Feeds the Strategic Layer refinement (is the Bottleneck still accurate?)

Captured build moment stubs (source_type: build_moment) feed directly into the content pipeline. Run `/develop #ID` on any stub to build it into a full concept ready for production.

The difference between a tool and an OS: the OS gets smarter every session.
