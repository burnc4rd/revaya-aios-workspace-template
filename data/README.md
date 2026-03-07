# data/

> SQLite databases and generated data files live here.
> This directory is gitignored — databases are never committed to version control.

---

## What Gets Created Here

| File | Created By | Purpose |
|------|-----------|---------|
| `content.db` | `scripts/content/db.py` on first run | Content ideas and published content tracking |
| `intel.db` | IntelOS collection scripts (optional) | Meeting transcripts and Slack messages |

---

## Setup

The databases are created automatically on first script run. You don't need to create them manually.

To initialize the content database:

```bash
python3 scripts/content/db.py
```

## Note on .gitignore

`data/*.db` is already in `.gitignore`. Your data stays local and private.
