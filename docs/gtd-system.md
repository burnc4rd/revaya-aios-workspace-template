# System: GTD — ProductivityOS

> Getting Things Done task management system. Captures, organizes, and tracks every commitment, project, and idea across the business.

## Architecture

```
Capture (inbox) --> Process (/process) --> Organize (next-actions/projects/waiting-for) --> Review (/review weekly)
                                                          |
                                                 refresh_dashboard.py
                                                          |
                                                   gtd/dashboard.md
```

## Key Files

| File | Purpose |
|------|---------|
| `gtd/dashboard.md` | Auto-refreshed operational overview — load at session start |
| `gtd/inbox.md` | Raw capture bucket — everything lands here first |
| `gtd/projects.md` | All active projects by area (Main Business, Side Projects, Personal) |
| `gtd/next-actions.md` | Next actions by context (@me, @claude, @calls, @team, @errands, @think, @record) |
| `gtd/waiting-for.md` | Delegated items and things expected from others |
| `gtd/someday-maybe.md` | Parked ideas by category (Business Ideas, Content Ideas, etc.) |
| `gtd/areas.md` | Areas of responsibility with health assessments |
| `gtd/review-checklist.md` | Weekly review protocol + decision tree + trigger lists |
| `scripts/inbox_writer.py` | Append items to inbox with file locking (used by /capture) |
| `scripts/refresh_dashboard.py` | Recompute dashboard counts from source files |
| `reference/gtd-methodology.md` | Full GTD methodology reference |

## How It Works

1. **Capture** — Anything on your mind goes into `gtd/inbox.md` (manually or via `/capture` from Telegram)
2. **Process** — Run `/process` to walk through inbox one item at a time using the GTD decision tree
3. **Organize** — Each item routed to: next-actions (by context), projects, waiting-for, someday-maybe, or trash
4. **Reflect** — Run `/review` weekly (Fridays) to keep lists current and trustworthy
5. **Engage** — Pick work by context: at computer → scan `@claude`, making calls → scan `@calls`, etc.

## Commands

| Command | What it does |
|---------|-------------|
| `/process` | Empty inbox using GTD decision tree — interactive, one item at a time |
| `/review` | Full weekly review: clear inbox, walk all lists, scan areas, rebuild dashboard |

## Telegram Integration

- `/capture [text]` — Direct inbox capture via bot, no AI round-trip (uses `inbox_writer.py`)
- "What's on my plate?" — Agent reads `gtd/dashboard.md` and summarizes
- "Process my inbox" — Agent runs the `/process` workflow
- "Brain dump: ..." — Agent captures multiple items to inbox

## Common Operations

**Refresh dashboard manually:**
```bash
python3 scripts/refresh_dashboard.py
```

**Capture from command line:**
```bash
python3 scripts/inbox_writer.py "Your task or idea here"
```

## Dependencies

- **Depends on:** Nothing (pure markdown + Python stdlib)
- **Used by:** CommandOS bot (`/capture` command), `/process`, `/review`

## History

| Date | Change |
|------|--------|
| 2026-03-03 | Initial install — ProductivityOS v1 |
