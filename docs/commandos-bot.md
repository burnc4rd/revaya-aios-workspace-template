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
| `apps/command/bot.py` | Aiogram message handlers, debounce buffer, /capture command |
| `apps/command/orchestrator.py` | Core engine — routes to CC agent sessions, delivers responses |
| `apps/command/worker.py` | Claude Code SDK execution (run_general_agent, run_general_prime) |
| `apps/command/session_manager.py` | Persistent session storage (JSON, survives restarts) |
| `apps/command/config.py` | Config from .env (ANTHROPIC_API_KEY, GROUP_ID, models, limits) |
| `apps/command/main.py` | Entry point — initializes bot and starts aiogram polling |
| `data/command/` | Session data, temp photos, logs |

## How It Works

1. Message arrives in Telegram group → `bot.py` validates (group + owner lock)
2. Voice notes transcribed via Whisper, photos downloaded as base64
3. Messages debounced (1.5s) to batch rapid-fire pastes
4. Routed: agent topic → `handle_agent_topic_message`, everything else → `handle_general_message`
5. Orchestrator checks for existing session → primes if none → runs CC agent
6. Response cleaned, segmented, sent back to Telegram
7. Created files (images, PDFs) sent as Telegram attachments

## Configuration

| Variable | Purpose | Required |
|----------|---------|----------|
| `ANTHROPIC_API_KEY` | Claude API access | Yes |
| `TELEGRAM_BOT_TOKEN` | Bot authentication | Yes |
| `TELEGRAM_GROUP_ID` | Authorized group (0 = discovery mode) | Yes (0 to discover) |
| `OPENAI_API_KEY` | Voice transcription (Whisper) | Optional |

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

- **Depends on:** ANTHROPIC_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_GROUP_ID, aiogram, Claude Code CLI
- **Python:** 3.13+ required (f-string backslash syntax in logger.py)
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
