# Reddit Research

> Reddit pain point and voice-of-customer agent.
> Surfaces the raw, unfiltered language of your ICP and IFP — what they're struggling with,
> asking, frustrated by, and celebrating. This is where hooks and angles get their specificity.

## Variables

topic: $ARGUMENTS (topic to research — e.g., "AI automation for small business", "solopreneur burnout")

---

## Instructions

You are mining Reddit for the real language of your audience. This is not trend research — this is voice-of-customer extraction. The goal is specific phrases, recurring frustrations, and honest questions that make hooks land.

### Step 1: Identify target subreddits

Default subreddit list (use all unless a specific one is more relevant):
- r/Entrepreneur
- r/smallbusiness
- r/SaaS
- r/artificial
- r/ClaudeAI
- r/ChatGPT
- r/productivity
- r/consulting
- r/solopreneur
- r/freelance
- r/AIAssistants

If the topic is more specific (e.g., "AI anxiety"), also search:
- r/anxiety (for raw emotional language)
- r/careerguidance
- r/cscareerquestions

### Step 2: Dispatch research subagent

Use the Agent tool (general-purpose) to search Reddit via web search. Instruct the agent to:

- Search Reddit for the topic across the subreddit list above
- Find: top posts (high upvotes), active threads (high comments), recent posts (last 90 days)
- Extract: exact quotes and phrases people use to describe their pain, questions, wins, and frustrations
- Note: upvote counts and comment counts where visible (signals strength of resonance)
- Look for: recurring themes, unresolved questions, things people wish existed

### Step 3: Compile the brief

Format output as:

```markdown
# Reddit Research Brief: [Topic]
**Date:** YYYY-MM-DD
**Subreddits searched:** [list]

## Pain Points (exact language)
[Direct quotes or close paraphrases from real posts — with subreddit source]

## Questions People Are Asking
[Recurring questions — verbatim where possible]

## Common Frustrations
[What makes them angry, exhausted, or stuck]

## Wins Being Shared
[What successes look like — useful for proof and aspiration framing]

## Phrases to Steal for Hooks
[Specific phrases that appear repeatedly — ready to use in post hooks]

## Misconceptions & False Beliefs
[Things the audience believes that you can challenge or reframe]

## Content Angles This Surfaces
[3-5 specific post or content ideas, with pillar and format recommendation]
```

### Step 4: Save and report

Save to `outputs/content-engine/research/YYYY-MM-DD-reddit-{topic-slug}.md`.

Report back to you with:
1. The 3 most resonant pain points (in the audience's exact words)
2. The strongest hook phrase found
3. The top content angle this research enables
