# Strategic Layer — System Doc

> The brain of the AIOS. Every decision, task, and initiative is filtered through the OOBG.

**Last Updated:** 2026-03-05

---

## What It Is

The Strategic Layer is an active decision filter — not background context. It stores the One Objective, One Bottleneck, One Goal (OOBG) and applies it to every prioritization decision in the OS. It's the first thing the Prioritization Engine reads, and the last thing the Learning Loops update.

---

## File Map

| File | When to Load | Purpose |
|------|-------------|---------|
| `strategic-layer/README.md` | Orienting a new session | Explains the Strategic Layer and how Claude uses it |
| `strategic-layer/oobg.md` | Every `/build-guide` run | The OOBG filter — One Objective, One Bottleneck, One Goal |
| `strategic-layer/unique-vehicle.md` | Content creation, positioning work, sales conversations | Your specific differentiation |
| `strategic-layer/priorities.md` | Prioritization decisions, project routing | Current ranked priorities across all work |
| `strategic-layer/direction.md` | Strategic planning, big picture decisions | Long-term direction and success horizon |

---

## How Claude Uses It

1. **At every `/build-guide` run:** Load `oobg.md` first. Score all candidate tasks against the OOBG.
2. **During `/process`:** Apply the soft OOBG alignment check to actionable items.
3. **During `/review` Phase 4.4:** Check if the Bottleneck has shifted.
4. **During `/reflect`:** Score today's work against the OOBG.

**The filter question:** "Does this work directly address the current Bottleneck, serve the Objective, or is it maintenance?"

---

## How to Update

- **OOBG** (`oobg.md`): Update when the Bottleneck shifts (resolved or changed). Review monthly.
- **Unique Vehicle** (`unique-vehicle.md`): Update when your positioning changes. Review quarterly.
- **Priorities** (`priorities.md`): Update when priority order changes. Review weekly during `/review`.
- **Direction** (`direction.md`): Update during Monthly Strategic Reset or when major external conditions change.

---

## Connection to Other Components

- **Feeds:** Prioritization Engine (`/build-guide`) — loaded at every run
- **Fed by:** Learning Loops — `/review` Phase 4.4 updates OOBG when Bottleneck shifts
- **Loaded by:** `/reflect` (alignment scoring), `/process` (soft OOBG check)

---

## History

| Date | Change |
|------|--------|
| 2026-03-05 | Created as part of AIOS 9-component restructure |
