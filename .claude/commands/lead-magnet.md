# Lead Magnet

> Lead magnet research, strategy, and creation agent.
> Three-phase workflow: research what's working → propose the right asset → draft it.
> Reads content-strategy.md and lead-magnets.md before doing anything.

## Variables

request: $ARGUMENTS (optional — specific idea or focus, e.g., "AI readiness checklist", or leave blank to start from research)

---

## Instructions

You are building a lead magnet for you. This is a three-phase process. Do not skip phases or rush to draft before strategy is approved.

### Phase 1: Research

**Step 1a: Check existing research**
Look in `outputs/content-engine/research/` for any existing briefs on lead magnets or competitor assets. If relevant research exists from the last 30 days, summarize it and proceed to Phase 2.

**Step 1b: If no brief exists, dispatch research subagent**
Use the Agent tool to research:
- What lead magnet formats are performing in AI/consulting/solopreneur space right now
- Specific examples with evidence of performance (downloads, engagement, testimonials)
- Title patterns that work (how they're worded)
- CTA mechanics being used (comment word, DM link, landing page)
- Formats: PDF, checklist, calculator, template, quiz, short guide, video workshop
- What's oversaturated vs. what's missing

Save research to `outputs/content-engine/research/YYYY-MM-DD-lead-magnet-research.md`.

---

### Phase 2: Strategy

Read both files before making any recommendations:
- `context/content-engine/content-strategy.md` — positioning, ICP/IFP audiences, tier system
- `context/content-engine/lead-magnets.md` — existing assets, audit decisions, roadmap

Recommend a specific lead magnet:

```
## Lead Magnet Recommendation

**Name:** [proposed title]
**Format:** [PDF / checklist / template / calculator / guide]
**Target audience:** [ICP / IFP / both — with description]
**Tier fit:** [how it fits the free-with-email-capture tier]
**Core problem it solves:** [one sentence]
**Distribution mechanic:** [comment CTA / featured section / DM / landing page]
**Success metric:** [# downloads / # email captures — what does good look like?]
**Why this one first:** [rationale based on research + current positioning]
**Estimated effort:** [low / medium / high to produce]
```

**Present to you for approval before proceeding.**
Do not draft anything until you approve the concept.

---

### Phase 3: Draft

Once you approve the concept:

**Step 3a: Write the asset**
- Apply your voice throughout (content-strategy.md voice rules)
- Match the format exactly (if PDF: structured sections; if checklist: scannable items; if guide: narrative)
- Keep it tight — Lara Acosta principle: simple beats polished. Screenshots and plain text outperform designed PDFs at this stage.
- Include a clear action at the end

**Step 3b: Write the distribution copy**
Produce all copy needed to distribute the lead magnet:
- LinkedIn post promoting it (comment CTA format — invoke `/draft-post` if needed)
- Comment CTA word suggestion
- DM response template ("Hey [name], here's your [resource]: [link]")
- Featured section title and description copy

**Step 3c: Save**
Save asset to `outputs/content-engine/lead-magnets/{name}.md`

**Step 3d: Update PM doc**
Update `context/content-engine/lead-magnets.md`:
- Move from backlog/roadmap to "Built" status
- Add to Lead Magnet Build Log with date and notes
