# Research

> Deep research agent. Searches the web thoroughly on any topic and returns a structured brief.
> Use before drafting content, building lead magnets, or making strategic decisions.

## Variables

topic: $ARGUMENTS (the topic to research — e.g., "AI anxiety in small businesses", "Claude Code for solopreneurs")

---

## Instructions

You are running a deep research session on the provided topic. Dispatch a research subagent to search broadly and return a structured brief you can use to inform content creation, strategy, or product decisions.

### Step 1: Check for existing research

Before running new research, check `outputs/content-engine/research/` for any existing briefs on this topic. If a relevant brief exists from the last 14 days, summarize what's already known and ask you if she wants a fresh search or to build on what exists.

### Step 2: Dispatch research subagent

Use the Agent tool (general-purpose) to search the web thoroughly. Instruct the agent to:

- Search for the latest articles, expert opinions, data, and examples on the topic
- Look for what's working (examples with evidence), what's trending, and what's changing
- Find specific statistics, named examples, and concrete data points — not vague summaries
- Look across: industry publications, creator content, business publications, and practitioner takes
- Depth: aim for 8-12 high-quality sources minimum

### Step 3: Compile the brief

Format the output as a structured research brief:

```markdown
# Research Brief: [Topic]
**Date:** YYYY-MM-DD
**Query:** [exact topic searched]

## Key Findings
[3-5 most important things to know — specific, not generic]

## Data & Stats
[Specific numbers, percentages, study findings — with sources]

## Expert Takes
[Quotes or perspectives from credible voices — named, not anonymous]

## Examples Worth Noting
[Specific examples — named companies, named people, real outcomes]

## What's Changing
[Trends, shifts, what's new vs. what's established]

## Implications for your Content
[3-5 specific angles or hooks this research enables]

## Suggested Content Angles
[Ranked list of content ideas this research supports, with format recommendation]
```

### Step 4: Save and report

Save the brief to `outputs/content-engine/research/YYYY-MM-DD-{topic-slug}.md`.

Report back to you with:
1. The top 3 findings she needs to know
2. The strongest content angle this research surfaces
3. The full brief path for reference
