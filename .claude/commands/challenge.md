# /challenge — "Is This the Best You Can Do?"

A quality gate for any work produced in your workspace. Run this against a plan, prompt, deliverable, script, or any output before considering it final.

## Philosophy

When someone brings you work to review, the first question is: "Is this the best you can do?" If the answer is no, send them back to improve it. If the answer is yes, *then* your review drives growth — not remedial fixes.

This command forces that self-critique so work reaches "best I can do" quality before you review it. The goal is version 1 that's already been pressure-tested — not version 4 after three rounds of "what did we miss?"

## When to Use

- After a planning command produces a plan — before approving it
- After writing a prompt, system message, or agent configuration
- After producing a client deliverable, proposal, or email
- After building a workflow, template, or command
- Anytime something feels "done" but hasn't been stress-tested

## How to Run

- `/challenge path/to/file.md` — challenge a specific file
- `/challenge` then paste content — challenge something from outside the workspace
- After any command that produces output — run `/challenge` to gut-check it

## Steps

1. Read your workspace config (e.g., CLAUDE.md or equivalent) for conventions and priorities
2. Read the work being challenged — fully, not skimming
3. Identify what this work is (plan, prompt, script, deliverable, code, template, etc.) and what it's trying to accomplish
4. Read any relevant context — project state files, the brief it was built from, the problem it's solving. Don't critique in a vacuum.

5. Switch into critical reviewer mode. Not adversarial — rigorous. The goal is to surface everything that a thoughtful expert would catch. Evaluate across these dimensions, adapting weight based on what's being reviewed:

### Completeness
- Does it cover everything it should? What's missing?
- Are there edge cases, failure modes, or scenarios that were ignored?
- Would someone executing this hit a dead end because something wasn't addressed?
- Are there unstated assumptions that need to be made explicit?

### Clarity
- Is every part unambiguous? Could anything be misread or misinterpreted?
- Would someone unfamiliar with the backstory know exactly what to do?
- Is anything vague where it should be specific?
- Are instructions actionable or just directional?

### Logic & Structure
- Does the reasoning hold up? Are there logical gaps or unjustified leaps?
- Is the sequence right? Are dependencies respected?
- Is there unnecessary complexity that could be simplified without losing quality?
- Does the structure serve the content or fight against it?

### Fit for Purpose
- Does this actually solve the problem it's supposed to solve?
- Is it aligned with the goals, priorities, and constraints of the project?
- Does it account for real-world constraints — time, tools, skill level, budget?
- Is it the right level of depth for its audience?

### Risk & Blind Spots
- What could go wrong that isn't addressed?
- What assumptions is this built on — and are they actually valid?
- Is there a "what if" scenario that would break this?
- What would someone trying to poke holes in this say?

### The Bar
- If the creator was asked "is this honestly the best you could do?" — would the answer be yes?
- What separates this from genuinely excellent work of the same type?
- What would make someone look at this and say "this person knows what they're doing"?

6. Produce the Challenge Report:

```
## Challenge Report — {what's being reviewed}

### What's Strong
{Specific things done well — genuine, not just softening for the critique}

### What Needs Work
1. **{Issue}** — {What's wrong and why it matters}
   → Fix: {Specific, actionable change}
2. ...

### What's Missing
{Things that should exist but don't — real gaps, not nice-to-haves}

### The Hard Question
Is this the best you can do? {Direct yes/no with reasoning}

### Verdict
{One of:}
- SHIP IT — Solid work. Suggestions above are polish, not problems.
- REWORK — Good foundation, real gaps. Fix the issues and re-evaluate.
- RETHINK — The approach itself has problems. Step back before fixing details.
```

7. **If the work was produced by Claude in this session** (a plan, a prompt, a draft — something Claude wrote):
   - If verdict is REWORK: apply all fixes, then re-run the challenge evaluation on the improved version.
   - If verdict is RETHINK: explain the fundamental issue, propose a revised approach, get the user's input before rebuilding.
   - If verdict is SHIP IT: move to step 9.
   - **Hard cap: 3 cycles maximum** (initial critique + up to 2 rework passes). After cycle 3, stop iterating regardless of verdict. If it's not there in 3 rounds, the approach needs rethinking, not more polishing.

8. **If the work was pasted in or is external** (something the user wrote, a client deliverable, third-party content):
   - Present the challenge report as-is. The user decides what to do with the feedback.
   - Do not auto-fix. The point is to give the critique — the user drives the improvements.
   - Skip to step 9.

9. **Always produce the Final Challenge Report.** This is what the user sees — every time, no exceptions.

```
## Final Challenge Report — {what was reviewed}

### Iteration Summary
- Cycles run: {1-3}
- Starting verdict: {SHIP IT / REWORK / RETHINK}
- Final verdict: {SHIP IT / REWORK (cap reached) / RETHINK}

### What Was Improved (if iterations occurred)
{Numbered list of specific changes made across cycles — what changed and why}

### What's Strong
{Specific things done well in the final version}

### Remaining Findings
{Anything the final critique pass still flagged — things that weren't critical enough
to justify another cycle, or items left when the cap was reached. Each item includes:}
1. **{Finding}** — {What it is, why it matters, and what the fix would be}
   Severity: {Critical / Worth addressing / Minor polish}
2. ...
{If nothing remains, say so: "None — final version passed clean."}

### Your Call
The work above is the best this process could produce. Remaining findings
(if any) are yours to act on or set aside. Options:
- **Accept as-is** — ship the current version
- **Address specific items** — tell me which remaining findings to implement
- **Send it back** — if something fundamental still bothers you
```

The user always gets the final say. The challenge process does the heavy lifting, but it never ships without approval.

## Rules

- **Be specific.** "This could be better" is useless. "Step 3 doesn't account for empty API responses — add a fallback for when the API returns no results" is useful. Every issue needs a concrete fix.
- **Be honest.** The entire point is to find real problems. If the work is genuinely good, say so. If it's not, say that too. No rubber-stamping.
- **Stay in scope.** A plan critique stays about the plan. Don't redesign the business strategy, rewrite the workspace, or expand into adjacent concerns. Challenge what's in front of you.
- **Don't nitpick.** Style preferences, formatting opinions, and "you could also..." suggestions are not issues. Focus on substance — things that affect whether this work actually succeeds at its job.
- **Know when to stop.** Diminishing returns are real. If iteration changes are getting smaller and more subjective, it's time to ship. Perfectionism is a stall trigger — this command should fight it, not feed it. The 3-cycle hard cap enforces this.
- **Track iterations.** If it takes all 3 cycles without reaching SHIP IT, note that prominently in the Final Challenge Report. It signals the original approach needed rethinking, not just polishing — that's useful information for improving the first attempt next time.
- **Credit what's good.** "What's Strong" is not a formality. If the work nails something, name it. People need to see what's working, not just what's broken.
