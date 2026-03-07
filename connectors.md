# External Connectors

> Audit of every external integration in this workspace.
> Every connector must be justified. Review monthly.

---

## Active Integrations

| Integration | Purpose | Where Used | Status | Remove If |
|-------------|---------|------------|--------|-----------|
| [YOUR_INTEGRATION_1] | [PURPOSE] | [FILES/SCRIPTS] | Active | [REMOVAL_CONDITION] |
| [YOUR_INTEGRATION_2] | [PURPOSE] | [FILES/SCRIPTS] | Active | [REMOVAL_CONDITION] |

---

## Common Integrations to Consider

| Integration | Purpose | Required Keys |
|-------------|---------|--------------|
| Airtable | Content pipeline tracking | `AIRTABLE_TOKEN` |
| Telegram | CommandOS bot (optional) | `TELEGRAM_BOT_TOKEN`, `TELEGRAM_GROUP_ID` |
| Anthropic API | Direct Claude API calls | `ANTHROPIC_API_KEY` |
| OpenAI | Voice notes transcription (Whisper) | `OPENAI_API_KEY` |
| Fireflies | Meeting transcript collection | `FIREFLIES_API_KEY` |

---

## Removed Integrations

| Integration | Removed | Reason |
|-------------|---------|--------|
| [INTEGRATION] | [DATE] | [REASON] |

---

## Review Protocol

Monthly review questions:
- Is every active integration still being used?
- Are API keys rotated on schedule?
- Has any integration changed pricing or terms?
- Are any integrations duplicating functionality?
