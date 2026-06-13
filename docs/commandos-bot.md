# System: CommandOS — Telegram AI Assistant

> Persistent Claude Code agent running 24/7 via Telegram. Full workspace access, topic isolation, voice notes, photo analysis.

## Architecture

```
Telegram message --> bot.py (aiogram router) --> orchestrator.py --> Claude Code SDK
                          |                            |
                    /capture (direct)          persistent sessions
                    /reboot (direct)           (SessionManager)
                          |
                   inbox_writer.py (GTD)
```

## Key Files

| File | Purpose |
|------|---------|
| `apps/command/bot.py` | Aiogram message handlers, command routing, voice transcription hook |
| `apps/command/agent.py` | Gemini API integration, workspace file loader, command instructions executor |
| `apps/command/config.py` | Config from .env (GEMINI_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_GROUP_ID, OBSIDIAN_VAULT_PATH) |
| `apps/command/main.py` | Entry point — initializes bot and starts aiogram polling |

## How It Works

1. Message arrives in Telegram group → `bot.py` validates against `TELEGRAM_GROUP_ID` (locks group access for safety).
2. Voice notes are sent directly to Gemini as raw audio files using Gemini's native multimodal features (no separate OpenAI Whisper billing/setup required).
3. Commands (/prime, /build_guide, /team, /reflect, /capture) are mapped to their `.claude/commands/[command].md` files.
4. `agent.py` loads the command instructions, reads referenced workspace files, appends context, and calls the Gemini API.
5. If Gemini requests file writes (e.g. creating reflect files or project plans), the bot intercepts the custom formatting tags and writes them to the workspace.
6. Build moments captured during `/reflect` are written directly to the content SQLite database and `pipeline.md` is regenerated.

## Configuration

| Variable | Purpose | Required |
|----------|---------|----------|
| `GEMINI_API_KEY` | Gemini API access | Yes |
| `TELEGRAM_BOT_TOKEN` | Bot authentication | Yes |
| `TELEGRAM_GROUP_ID` | Authorized group (0 = discovery mode) | Yes (0 to discover) |
| `OBSIDIAN_VAULT_PATH` | Path to your Obsidian vault | Optional (for build-guide) |

**Discovery mode:** Set `TELEGRAM_GROUP_ID=0` to have the bot log and reply with the actual chat ID when it receives any message. Useful for first-time setup.

## Bot Commands

| Command | Handler | Description |
|---------|---------|-------------|
| `/new [sonnet\|opus]` | orchestrator | Spawn fresh agent in new forum topic |
| `/content [idea]` | bot.py → orchestrator | Spawn Content Strategist agent in new topic |
| `/example [content\|URL] \| [note]` | orchestrator | Save content inspiration to `content/inspiration/` |
| `/name` | orchestrator | Rename current topic via agent |
| `/compact` | orchestrator | Compress context window |
| `/reset` | orchestrator | Clear session, start fresh |
| `/capture [text]` | bot.py direct | GTD quick capture to inbox |
| `/reboot` | bot.py direct | Restart the bot process |
| `/help` | orchestrator | Show command list |

## Common Operations

**Start bot:**
```bash
launchctl load ~/Library/LaunchAgents/[YOUR_SERVICE_NAME].plist
```

**Stop bot:**
```bash
launchctl unload ~/Library/LaunchAgents/[YOUR_SERVICE_NAME].plist
```

**View logs:**
```bash
tail -f data/command.stdout.log
tail -f data/command.stderr.log
```

**Debug:**
- Check `data/command.stderr.log` for Python errors
- Sessions stored as JSON in `data/command/sessions/`
- If bot unresponsive: `/reboot` from Telegram or restart via launchctl

## Worker Types

| Worker | File | System Prompt | Use |
|--------|------|---------------|-----|
| General agent | `worker.py:run_general_agent` | Chief of staff — full workspace | All `/new` sessions |
| Content Strategist | `worker.py:run_content_agent` | Content pillars, voice rules, Airtable | `/content` sessions |

Sessions are routed by `session.name`: `"✍️ Content Strategist"` → content worker, all others → general worker.

## Dependencies

- **Depends on:** `GEMINI_API_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_GROUP_ID`, `aiogram`, `google-generativeai`
- **Python:** 3.10+ required
- **Used by:** GTD `/capture` command, all Telegram-based workflows

## History

| Date | Change |
|------|--------|
| 2026-02-28 | Initial install — CommandOS module |
| 2026-03-03 | Added /capture command for GTD inbox integration |
| 2026-03-03 | Added /content command — spawns Content Strategist agent in forum topic |
| 2026-03-03 | Added discovery mode (TELEGRAM_GROUP_ID=0) for first-time setup |
| 2026-03-03 | Migrated venv to Python 3.13 (f-string backslash compatibility) |
| 2026-03-03 | Added /example command — instant save of content inspiration to content/inspiration/ |
