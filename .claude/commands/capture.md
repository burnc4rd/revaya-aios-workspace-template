# /capture — Quick Content Idea Capture

> Capture a content idea and classify it as a stub in the pipeline.

## Variables

$ARGUMENTS (the raw idea, topic, or observation to capture)

## Instructions

You are capturing a content idea into the pipeline. Quick classification, duplicate check, store as stub. For full concept development, use `/develop`.

### Step 1: Understand the Idea

Extract the core in 1-2 sentences from the user's input.

### Step 2: Check for Duplicates

```bash
.venv/bin/python3 -c "
import sys, sqlite3; sys.path.insert(0, '.')
from scripts.content.db import get_connection
conn = get_connection()
rows = conn.execute(\"\"\"
    SELECT id, title, production_status FROM content_ideas
    WHERE title LIKE '%KEYWORD%' ORDER BY created_at DESC LIMIT 5
\"\"\").fetchall()
for r in rows: print(f'  #{r[\"id\"]} [{r[\"production_status\"]}] {r[\"title\"]}')
if not rows: print('  No duplicates found.')
conn.close()
"
```

Replace KEYWORD with the most distinctive word from the idea.

If duplicates exist, tell the user and ask if they want to proceed or develop the existing one instead.

### Step 3: Classify

Read `content/strategy.md` to understand their platform, pillars, and audience segments.

Determine:
- **Channel:** linkedin / youtube (primary or secondary platform for this idea)
- **Format:** Appropriate format for that channel (from strategy.md format types)
- **Content pillar:** Which of the 4 pillars this falls under (Operational Problems / Lived Experience / Practical Value / Personal Journey)
- **Audience segment:** Drowning Operator / AI-Curious Builder / Claude Power User
- **Funnel position:** awareness / consideration / conversion

Present the classification to the user for quick confirmation (one line: "LinkedIn post, Operational Problems pillar, ICP, awareness — sound right?").

### Step 4: Store as Stub

After confirmation:

```bash
.venv/bin/python3 -c "
import sys; sys.path.insert(0, '.')
from scripts.content.db import get_connection
from scripts.content.writer import write_content_idea

idea = {
    'title': 'TITLE_HERE',
    'description': 'DESCRIPTION_HERE',
    'channel': 'CHANNEL',
    'format_type': 'FORMAT',
    'source_type': 'manual',
    'content_pillar': 'PILLAR',
    'audience_segment': 'SEGMENT',
    'funnel_position': 'POSITION',
    'notes': 'NOTES',
}

conn = get_connection()
idea_id = write_content_idea(conn, idea)
conn.close()
print(f'Stored as stub #{idea_id}')
"
```

### Step 5: Regenerate Pipeline

```bash
.venv/bin/python3 scripts/content/generate_pipeline.py
```

### Step 6: Report

Tell the user:
- Stub #ID captured
- Channel + format + pillar
- "Run `/develop #ID` to develop it with full strategic positioning and packaging."

$ARGUMENTS
