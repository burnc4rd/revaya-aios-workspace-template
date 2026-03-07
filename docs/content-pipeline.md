# System: Content Pipeline

> SQLite-backed content production system — captures ideas, develops them into fully packaged concepts, schedules them, and tracks published posts with a 7-day context window.

## Architecture

```
Airtable (analytics/display)
    ↓ sync_airtable.py
data/content.db
    ├── content_ideas     ← /capture, /develop, /schedule
    └── published_content ← sync_airtable.py + log_published_content()
         ↓
context_aggregator.py    ← feeds 7-day context into /develop
         +
data/intel.db (meetings) ←
```

## Key Files

| File | Purpose |
|------|---------|
| `scripts/content/db.py` | SQLite schema, `get_connection()`, `init_db()` |
| `scripts/content/writer.py` | CRUD — `write_content_idea()`, `write_developed_idea()`, `update_status()`, `log_published_content()` |
| `scripts/content/context_aggregator.py` | Builds 7-day context window (recent posts + meetings + pipeline state) |
| `scripts/content/generate_pipeline.py` | Renders `content/pipeline.md` from database |
| `scripts/content/sync_airtable.py` | Syncs Airtable Posted records → `published_content` table |
| `data/content.db` | SQLite database (gitignored) |
| `content/pipeline.md` | Auto-generated view of all content ideas by stage |
| `content/concepts/` | Fully developed concept docs written by `/develop` |
| `content/strategy.md` | Platform cadence, pillars, format types, content rules |
| `content/brand-and-audience.md` | Brand positioning, 3 audience segments, proof points |
| `content/offers-and-funnels.md` | Offer stack, CTA paths, content→revenue mapping |
| `content/packaging-strategy.md` | YouTube/LinkedIn packaging frameworks, viral title elements |

## Source Types

| source_type | How it enters | Description |
|---|---|---|
| `manual` | `/capture` command | General content ideas captured manually |
| `build_moment` | `/reflect` Step 6 at session end | Build-in-public moments from workspace sessions. Distinct from manual captures. |
| `develop` | `/develop` command | Ideas created directly during concept development |
| `telegram` | CommandOS bot | Ideas captured via Telegram voice note or message |

## How It Works

1. **Capture** — `/capture` saves a raw idea as a stub in `content_ideas` (status: `stub`, source_type: `manual`). `/reflect` Step 6 saves build moments (source_type: `build_moment`).
2. **Develop** — `/develop #ID` reads strategy docs + 7-day context, builds strategic positioning + packaging, saves to `content_ideas` (status: `developed`) + writes `content/concepts/{id}-{slug}.md`
3. **Schedule** — `/schedule` assigns publish dates, calculates film-by dates, updates status to `scheduled`
4. **Publish** — Airtable tracks actual published posts; `sync_airtable.py` pulls them into `published_content`
5. **Context** — Every `/develop` run pulls the last 7 days of posts + meetings so Claude avoids topic overlap

## Configuration

| Variable | Purpose | Required |
|----------|---------|----------|
| `AIRTABLE_TOKEN` | Read access to Airtable Content Pipeline base | Yes (for sync) |

Airtable constants in `sync_airtable.py`:
- `BASE_ID = "[YOUR_AIRTABLE_BASE_ID]"`
- `TABLE_ID = "tblBOkOJLYRfM0q53"`
- Filters for `{Status} = 'Posted'`

## Common Operations

**Sync Airtable → SQLite (dry run):**
```bash
.venv/bin/python3 scripts/content/sync_airtable.py --dry-run
```

**Run full sync:**
```bash
.venv/bin/python3 scripts/content/sync_airtable.py
```

**Check context window:**
```bash
.venv/bin/python3 -c "
import sys; sys.path.insert(0, '.')
from scripts.content.context_aggregator import build_context_window, format_context_for_prompt
print(format_context_for_prompt(build_context_window(days=7)))
"
```

**Regenerate pipeline view:**
```bash
.venv/bin/python3 scripts/content/generate_pipeline.py
```

## Dependencies

- **Depends on:** `data/intel.db` (IntelOS meetings for context window), `AIRTABLE_TOKEN` in `.env`
- **Used by:** `/capture`, `/develop`, `/schedule`, `/draft-post`, Telegram `/content` command

## History

| Date | Change |
|------|--------|
| 2026-03-06 | Added build_moment source_type. /reflect Step 6 now captures build-in-public stubs at session end. 20 retroactive stubs mined from HISTORY.md and Obsidian journals. |
| 2026-03-03 | Initial install — hybrid SQLite + Airtable architecture. 11 historical posts synced. |
