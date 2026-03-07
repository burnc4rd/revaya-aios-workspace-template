# Competitive Research

> Competitor content analysis agent.
> Analyzes what AIOS consultants, Claude educators, and AI coaches are doing —
> content angles, lead magnets, positioning, and gaps you can fill.

## Variables

target: $ARGUMENTS (optional — specific competitor name, or leave blank to run on default list)

---

## Instructions

You are analyzing the competitive content landscape for your Business AI OS positioning. The goal is to understand what others in this space are doing, identify what's working, and find the gaps you can own.

### Default competitor categories (use when no specific target provided)

1. **AIOS / AI OS service providers** — people selling AI operating system builds or productized AI consulting
2. **Claude educators and content creators** — people teaching Claude, Claude Code, or Claude-specific workflows
3. **AI automation consultants** — people building n8n, Zapier, or general AI automation for businesses
4. **Solopreneur AI coaches** — people teaching solo operators how to use AI in their business

### Step 1: Dispatch research subagent

Use the Agent tool (general-purpose) to search the web. Instruct the agent to:

- Search for active creators/consultants in each category above (or the named target)
- Find: their LinkedIn presence, YouTube content, website positioning, lead magnets, and any visible pricing
- Look for: what topics they post about, what angles they take, what their lead magnets offer
- Note: follower counts or engagement signals where visible
- Search for: gaps — topics nobody is covering, angles nobody is taking, audiences being underserved

### Step 2: Compile the brief

```markdown
# Competitive Research Brief
**Date:** YYYY-MM-DD
**Target:** [specific competitor or "default landscape"]

## Competitor Profiles

### [Name / Handle]
- Platform: [LinkedIn / YouTube / etc.]
- Positioning: [how they describe themselves]
- Content themes: [what they post about]
- Lead magnet: [what free resource they offer, if any]
- Pricing signal: [any visible pricing]
- Audience size: [follower count if visible]
- What they do well: [specific strength]
- What they miss: [gap or weakness]

[repeat for each competitor]

## Content Themes They Own
[Topics that are well-covered — you should differentiate, not duplicate]

## Lead Magnet Formats in Use
[What free resources are common in this space]

## Positioning Gaps
[Angles, audiences, or problems nobody is addressing well]

## your Opportunities
[Specific differentiation plays — where your background, story, or method gives her an edge nobody else has]

## Hooks/Angles you Could Counter or Complement
[Specific post angles that respond to or build on competitor content]
```

### Step 3: Save and report

Save to `outputs/content-engine/research/YYYY-MM-DD-competitive.md`.

Report back to you with:
1. The 2-3 competitors most worth watching
2. The biggest positioning gap she can own
3. One immediate content angle this research unlocks
