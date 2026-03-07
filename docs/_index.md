# Documentation Index

> Agents scan this file to find relevant docs before working on a system.
> Load only the docs that match your current task.
>
> **Update rule:** When you modify a documented system, update its doc.
> When you build a new system, create a doc and add it here.
>
> **Doc templates:** See `docs/_templates/` for system and integration doc templates.

---

## AIOS Core Components

| Condition | Doc | Summary |
|-----------|-----|---------|
| Working with strategic-layer/, oobg.md, /build-guide OOBG scoring, priorities | `docs/strategic-layer.md` | AIOS Strategic Layer — OOBG filter, file map, how Claude loads and uses each file |
| Working with knowledge/, decisions, learnings, /reflect, /commit knowledge capture | `docs/knowledge-management.md` | Knowledge Management — 5-step pipeline, naming convention, capture triggers, search patterns |
| Working with metrics/, business-kpis.md, /metrics command, KPI tracking | `docs/metrics.md` | Metrics and Monitoring — data sources, ownership, query patterns, v1 vs v2 |
| Working with /reflect, /review Phase 4.4, learning cadences, AIOS improvement | `docs/learning-loops.md` | Learning Loops — 5 cadences (daily to annual), what each produces, how outputs feed strategy |

## Systems

| Condition | Doc | Summary |
|-----------|-----|---------|
| Working with GTD files, /process, /review, inbox, dashboard | `docs/gtd-system.md` | GTD task management — inbox, projects, next-actions, weekly review |
| Working with CommandOS bot, Telegram, apps/command/ | `docs/commandos-bot.md` | Telegram AI assistant — persistent CC agent, /capture, session management |
| Working with AI Landscape Monitor, /update-ai-docs, scripts/ai-landscape/ | `docs/ai-landscape-monitor.md` | Daily AI model ranking scanner — LMArena, OpenRouter, TTS/STT arenas |
| Working with content pipeline, /capture, /develop, /schedule, scripts/content/, data/content.db | `docs/content-pipeline.md` | SQLite content production system — capture, develop, schedule, Airtable sync, 7-day context |
| Working with team roles, /team, /board, team/ directory, role files | `docs/ai-team.md` | AI Org — ACRA+2 departments, /team routing, /board exec sessions, Telegram integration |

## Integrations

| Condition | Doc | Summary |
|-----------|-----|---------|
| Auditing external integrations, adding/removing MCPs or connectors | `connectors.md` | External Connectors audit — all active integrations with justification and removal candidates |
