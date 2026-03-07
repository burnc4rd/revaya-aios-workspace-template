# Knowledge Management — System Doc

> The organisation's long-term memory. Every insight, decision, and outcome captured, structured, and retrievable.

**Last Updated:** 2026-03-05

---

## What It Is

Knowledge Management is the system that ensures the AIOS never forgets. It captures decisions and learnings as structured markdown files, making them searchable by Claude across sessions. It implements a 5-step pipeline:

**Capture → Structure → Filter and Reformat → Organise and Align → Ready for Execution**

---

## File Map

| Path | Purpose |
|------|---------|
| `knowledge/README.md` | Pipeline overview, naming convention, search patterns |
| `knowledge/decisions/` | Key decisions with context and rationale |
| `knowledge/decisions/_template.md` | Decision capture template |
| `knowledge/learnings/` | Lessons from execution — what worked, what didn't |
| `knowledge/learnings/_template.md` | Learning capture template |
| `knowledge/resources/` | Curated references worth returning to |
| `knowledge/resources/README.md` | Format for resource files |

---

## Naming Convention

All files: `YYYY-MM-DD-short-description.md`

Examples:
- `2026-03-01-workspace-architecture.md`
- `2026-03-05-daily-reflect.md`

---

## Capture Triggers (Auto-Capture Hooks)

| Trigger | Hook | What Gets Captured |
|---------|------|-------------------|
| `/commit` run | Step 1.5 Knowledge Capture Check | Sessions that produced significant decisions or learnings |
| `/reflect` run | Full output saved automatically | Daily assessment: OOBG alignment, top accomplishment, top learning, friction |
| Manual | Create file using template | Any decision or learning worth preserving |

---

## How Claude Searches Knowledge

To find relevant past decisions or learnings:

```
Grep with pattern="<topic>" path="knowledge/" glob="*.md"
```

Examples:
- "workspace architecture" — finds workspace structure decisions
- "storytelling" — finds LinkedIn content learnings
- "pricing" — finds any pricing-related decisions

---

## What Goes Where

| Content | Directory | When to Capture |
|---------|-----------|----------------|
| A choice was made that eliminates an alternative or sets a pattern | `knowledge/decisions/` | When a non-obvious decision is made |
| Something worked better or worse than expected | `knowledge/learnings/` | When execution produces a reusable insight |
| A reference was critical to important work | `knowledge/resources/` | When a source will be needed again |
| End-of-session reflection | `knowledge/learnings/` | Every significant session via `/reflect` |

---

## Connection to Other Components

- **Fed by:** Auto-Capture (`/commit` Step 1.5, `/reflect`)
- **Feeds:** Learning Loops (weekly synthesis reads `knowledge/` for gap check), Strategic Layer (learnings that change the OOBG)
- **Searched by:** Any session that needs past context

---

## History

| Date | Change |
|------|--------|
| 2026-03-05 | Created as part of AIOS 9-component restructure. Seeded with 3 decisions and 3 learnings. |
