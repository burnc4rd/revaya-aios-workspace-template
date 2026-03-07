# Update AI Docs

> Autonomous pipeline: pull live rankings, detect changes, research new leaders, update docs. No human interaction.

## Variables

target: $ARGUMENTS (optional — specific category to update, e.g., "code". If empty, checks all 10 categories for changes.)

## Instructions

Run this pipeline end-to-end with **zero stops, zero prompts, zero AskUserQuestion calls**. If nothing changed, report that and exit. If something changed, research it and update the docs — all automatically.

### Category Tiers

- **Tier 1 (LMArena):** `text`, `code`, `vision`, `text-to-image`, `image-edit`, `search`, `text-to-video`, `image-to-video`
- **Tier 2:** `text-to-speech` (TTS Arena V2), `speech-to-text` (Voice Writer Leaderboard)

Tier 1 uses ELO scores from arena.ai. Tier 2 uses ELO from TTS Arena (for TTS) and WER from Voice Writer (for STT, lower = better).

### Phase 1: PULL LIVE RANKINGS

**Tier 1 — LMArena (8 categories):**

For each of the 8 LMArena categories, fetch the current leaderboard:

```
WebFetch https://arena.ai/leaderboard/{category}
Prompt: "Extract the complete leaderboard table. For each model return: rank, model name, ELO score (Arena Score), number of votes, organization/provider. Return the top 20 models as a structured list."
```

**Tier 2 — TTS Arena + Voice Writer (2 categories):**

For text-to-speech:
```
WebFetch https://tts-agi-tts-arena-v2.hf.space/leaderboard
Prompt: "Extract the TTS model leaderboard. For each model return: rank, model name, ELO score, win rate, total votes. Return all models."
```

For speech-to-text:
```
WebFetch https://voicewriter.io/speech-recognition-leaderboard
Prompt: "Extract the speech-to-text comparison table. For each system return: name, Mean WER, Std Dev, Price per hour. Return all models."
```

If a specific `target` category was given, only fetch that one.

Also query OpenRouter DB data for pricing context on text/code models:
```sql
SELECT model_name, price_input, price_output, context_length
FROM ai_models
WHERE source = 'openrouter' AND date = (SELECT MAX(date) FROM ai_models WHERE source = 'openrouter')
AND category IN ('text', 'code')
ORDER BY category, rank_in_category
LIMIT 30
```

### Phase 2: READ CURRENT DOCS

For each `ai-docs/{category}/state-of-the-art.md`:
- If the file exists, read it and extract the currently documented leader (from the `> Leader:` header line)
- If the file doesn't exist, flag category as `no_docs`

### Phase 3: DIFF

For each category, compare:
- Live #1 vs documented #1
- Live top 3 vs documented top 3

Build a change list with change types:
- `new_leader` — #1 model changed
- `new_top3` — a new model entered top 3
- `no_docs` — state-of-the-art.md doesn't exist yet

**If no changes in any category** → output "All docs current — no ranking changes detected" and **EXIT immediately**.

**If a specific `target` was given** → always flag that category for update regardless of changes.

### Phase 4: RESEARCH CHANGES (parallel agents)

For each category with changes, spawn a **parallel Task agent** (subagent_type: `general-purpose`):

**Agent prompt:**
```
Research [MODEL NAME] for the [CATEGORY] AI category. It is currently #{RANK} on [SOURCE] with [METRIC] [SCORE] and [VOTES] votes.

Your job — do NOT write any files, just return research results:

1. WebSearch: "[model name] API pricing 2026", "[model name] documentation"
2. WebSearch: "[model name] review 2026", "[model name] vs [competitor]"
3. WebFetch: the official API documentation page to get the exact model ID and integration code
4. WebSearch: "[model name] reddit" for community sentiment

Return a structured report with:
- Model overview (2-3 sentences: what it is, who makes it, what makes it special)
- Best for (3-4 bullet points — ideal use cases)
- Not ideal for (1-2 bullet points — when to use something else)
- Pricing (exact $ per unit — tokens, images, seconds, characters, hours, etc.)
- API Model ID (the exact string you pass to the API)
- Integration code (Python, working example with exact model ID, SDK import, auth, and basic usage — use the provider's official SDK)
- Community sentiment (2-3 sentences from Reddit/X — what users love and complain about)
- Tips & gotchas (2-3 bullet points — rate limits, quirks, best practices)
- Official API docs URL
```

**Do this for each of the top 2-3 models in every changed category.** Spawn agents in parallel — one per changed category, each researching the top models in that category.

### Phase 5: UPDATE DOCS

For each researched category, write `ai-docs/{category}/state-of-the-art.md`.

**Tier 1 template (LMArena categories):**

```markdown
# [Category Display Name] — State of the Art

> Last updated: YYYY-MM-DD
> Source: [LMArena](https://arena.ai/leaderboard/{category}) | Crowdsourced, [total votes]+ votes
> Leader: [Model Name] ([Provider]) — ELO: [score] | [votes] votes

## Quick Pick

| Use Case | Best Model | Provider | API Model ID | Cost | ELO |
|----------|-----------|----------|-------------|------|-----|
| [primary use case] | [model] | [provider] | `[exact-id]` | $X/M in, $Y/M out | [score] |
| Budget option | [model] | [provider] | `[exact-id]` | $X/M in, $Y/M out | [score] |

## Rankings (LMArena Top 10)

| # | Model | Provider | ELO | Votes |
|---|-------|----------|-----|-------|

## Top Models — Deep Dive

### 1. [Model Name] — [Provider]
[Overview, specs, integration code, tips]

## Links
- [LMArena Leaderboard](https://arena.ai/leaderboard/{category})
```

**Tier 2 — TTS template:**

```markdown
# Text-to-Speech — State of the Art

> Last updated: YYYY-MM-DD
> Source: [TTS Arena V2](https://huggingface.co/spaces/tts-agi/tts-arena-v2) | Crowdsourced, blind A/B voting
> Leader: [Model Name] ([Provider]) — ELO: [score] | [votes] votes

## Quick Pick

| Use Case | Best Model | Provider | API Model ID | Cost | ELO |
|----------|-----------|----------|-------------|------|-----|
| Best overall | [model] | [provider] | `[exact-id]` | $X/1K chars | [score] |
| Best for agents | [model] | [provider] | `[exact-id]` | $X/1K chars | [score] |

## Rankings (TTS Arena V2 Top 10)

| # | Model | Provider | ELO | Win Rate | Votes |
|---|-------|----------|-----|----------|-------|
```

**Tier 2 — STT template:**

```markdown
# Speech-to-Text — State of the Art

> Last updated: YYYY-MM-DD
> Source: [Voice Writer](https://voicewriter.io/speech-recognition-leaderboard) | Independent real-world benchmark
> Leader: [Model Name] ([Provider]) — WER: [X]% | $[Y]/hr

## Quick Pick

| Use Case | Best Model | Provider | API Model ID | WER | Cost ($/hr) |
|----------|-----------|----------|-------------|-----|-------------|
| Best accuracy | [model] | [provider] | `[exact-id]` | [X]% | $[Y] |
| Best value | [model] | [provider] | `[exact-id]` | [X]% | $[Y] |

## Rankings (Voice Writer Leaderboard)

| # | System | WER | Std Dev | Price/hr | Provider |
|---|--------|-----|---------|----------|----------|
```

Then update `ai-docs/README.md` master index with:
- Current leader per category (all 10)
- Quick-pick matrix
- "Last scan" timestamp
- Changelog entry

### Phase 6: REPORT

Output a summary:
- Categories checked (all 10, or specific target)
- Changes detected (list)
- Docs updated (list of files)
- "No changes" if nothing happened

---

## Critical Rules

- **ZERO stops, ZERO prompts** — this runs unattended. No `STOP`, no `AskUserQuestion`.
- **API data is ground truth** — arena ELO/WER scores override subjective assessments.
- **Exit fast** — if nothing changed, just say so. Don't research or rewrite docs unnecessarily.
- **Parallel agents** — spawn research agents in parallel, one per changed category.
- **Agent-readable docs** — every doc must include working code an agent can copy-paste. Include exact API model IDs.
- **10 categories** — 8 Tier 1 (LMArena) + 2 Tier 2 (TTS Arena + Voice Writer).
- **Top 2-3 models** — quality over quantity. Don't document every model, just the leaders.
- **Provider diversity** — even if one provider sweeps rankings, document top models from 2-3 different providers per category.
- **Pricing in USD** — model pricing is quoted in USD.
- **Metric awareness** — TTS uses ELO (higher = better). STT uses WER % (lower = better). Don't mix them up.
