# Update Journal

> Append a new build log entry to an Obsidian build journal after a work session.
> Usage: /update-journal [project-name]
> **Setup required:** Set your Obsidian vault path in Step 2 below before using this command.

## Run

1. Identify the project from the argument: $ARGUMENTS
   - Add your own project shortcuts here (e.g., "project-one" → `ProjectOne.md`)
   - If no argument or unclear, ask which project to update.

2. Read the current build journal from: `[YOUR_OBSIDIAN_VAULT_PATH]/Build Journals/[filename]`
   - Replace `[YOUR_OBSIDIAN_VAULT_PATH]` with your actual Obsidian vault path
   - Example on macOS with iCloud sync: `/Users/[username]/Library/Mobile Documents/iCloud~md~obsidian/Documents/`

3. Review the conversation history to identify what was done this session for this project:
   - What features were built, fixed, or shipped?
   - What decisions were made?
   - What blockers were encountered or resolved?
   - What's the next step?

4. Generate a new build log entry and append it to the Build Log section.

## Entry Format

```markdown
### [Date or Session label]
- [What was done — bullet points, raw and fast]
- [Each meaningful action gets its own bullet]

**Decided:** [Any decisions made this session, if applicable — omit if none]

**Next:** [The single most important next step]

**Post ideas:**
- "[Hook line]" ([Platform] — [angle])
```

## Additional Updates

After appending the log entry, also check and update:
- **Phase checklists:** Check off any features/tasks that were completed this session
- **Current phase/Status in header:** Update if phase changed
- **Open Questions:** Mark any that were resolved with [x], add new ones if discovered
- **Key Dates:** Add any new milestones reached
- **Decision Register:** Add any new architectural or design decisions made

## Rules

- Write in the same voice as existing entries — raw, fast, specific
- Never delete or modify existing log entries
- Post ideas should be specific to what was built, not generic
- Always include a **Next:** line — the journal should never end without a clear next step
- If nothing meaningful was done on this project, say so honestly — "No progress this session, still blocked on [X]"
