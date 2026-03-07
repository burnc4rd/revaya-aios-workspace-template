# Knowledge Management

> The organisation's long-term memory. Every insight, decision, and outcome is captured, structured, and retrievable — across all projects.

---

## The 5-Step Pipeline

Every piece of knowledge that enters this system flows through:

```
Capture → Structure → Filter & Reformat → Organise & Align → Ready for Execution
```

1. **Capture** — Raw input: voice memo via Telegram, session note, insight during execution
2. **Structure** — Claude formats it using the appropriate template (decision or learning)
3. **Filter and Reformat** — Remove noise, sharpen the signal, confirm it's worth keeping
4. **Organise and Align** — File it in the right directory with the right name
5. **Ready for Execution** — The knowledge is now retrievable and usable in future sessions

---

## Directory Structure

```
knowledge/
├── decisions/       # Key decisions made with context and rationale
│   └── _template.md
├── learnings/       # Lessons from execution — what worked, what didn't
│   └── _template.md
└── resources/       # Curated references that informed significant work
    └── README.md
```

---

## Naming Convention

All files: `YYYY-MM-DD-short-description.md`

Examples:
- `knowledge/decisions/2026-03-05-aios-9-component-architecture.md`
- `knowledge/learnings/2026-03-02-storytelling-outperforms-technical.md`

---

## When to Capture

**Decisions** — any time a significant choice was made that:
- Could be questioned later and needs documented rationale
- Eliminates an alternative that might be reconsidered
- Sets a pattern other work will follow

**Learnings** — any time execution produced a lesson:
- Something that worked better than expected
- Something that failed and why
- A pattern that should be reused or avoided
- An insight that changes how future work gets done

**Resources** — any reference that was critical to a significant piece of work (not every link, only those worth returning to).

---

## How Claude Searches This

To find relevant knowledge before starting work on a topic:

```
Grep pattern="[topic]" path="knowledge/" glob="*.md"
```

Each file is designed to be readable in isolation — no assumed context.

---

## How This Feeds the System

- **Knowledge Management → Strategic Layer**: Refined contextual knowledge refines OOBG and direction
- **Knowledge Management → Learning Loops**: Learning Loop cadences review and synthesise what's here
- **Knowledge Management → Execution**: Future sessions load relevant decisions to avoid re-solving solved problems

---

## Capture Triggers

Knowledge capture is prompted at two points:
1. **End of session** — `/commit` Step 1.5 asks: "Any significant decision or learning to capture?"
2. **End of day** — `/reflect` (Daily Assessment) extracts learnings and files them here

The goal: each project enriches the next.
