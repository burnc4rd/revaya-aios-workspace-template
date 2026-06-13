# Running Business AI OS with Gemini / Antigravity

Welcome! This workspace is optimized to run inside **Gemini / Antigravity** (and other IDE-based developer agents like Cursor) rather than being locked to the Claude Code CLI.

Because IDE agents have full read/write file access and terminal execution capabilities, they can run your commands and automate tasks directly inside your workspace.

---

## Quick Start Setup

### Step 1: Clone the Repository
If you haven't already, make sure you are in the workspace folder.

### Step 2: Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Open `.env` and fill in your details:
* **`OBSIDIAN_VAULT_PATH`**: Set the absolute path to your Obsidian vault (e.g., `/Users/your-username/Library/Mobile Documents/iCloud~md~obsidian/Documents`).
* **API Keys**: Add `AIRTABLE_TOKEN` (for content pipeline) or other keys if you plan to use those connectors.

### Step 3: Fill In Your Context Files
Provide context so your agent understands your goals:
1. `strategic-layer/oobg.md` — Fill in your One Objective, One Bottleneck, and One Goal.
2. `context/personal-info.md` — Fill in your background and preferences.
3. `context/business-info.md` — Describe your business.
4. `context/strategy.md` — Current execution strategy.

---

## Daily Operating Workflow

Open your IDE chat panel (e.g., Gemini or Cursor chat) and run your commands by typing them directly:

### 1. Initialize Session
At the start of a session, type:
> **`Run /prime`**

The agent will read your context, OOBG, and CLAUDE.md files, summarize its understanding, and confirm it's ready.

### 2. Get Your Focus Guide
After priming, type:
> **`Run /build-guide`**

The agent will scan your Obsidian build journals, score candidate tasks against the bottleneck defined in your `oobg.md`, and output today's Critical task.

### 3. Route to AI Departments
To execute a specific task or get advice in the voice of a department specialist:
> **`Run /team [your request here]`**

The agent will locate the corresponding specialist file in `team/` (e.g., content-specialist, discovery-specialist) and respond fully in their voice.

### 4. Capture Learning & Reflect
At the end of your session, type:
> **`Run /reflect`**

The agent will analyze the session history, write a markdown summary file to `knowledge/learnings/`, and update your workspace knowledge.

### 5. Commit Work
Save your changes and push to GitHub by typing:
> **`Run /commit "Updated project X"`**

The agent will update the changelog, stage your changes, and make the Git commit for you.

---

## Why Agentic execution is better

With the Claude Code CLI, commands are purely informational—the CLI prints what you should do next. 

With **Gemini / Antigravity**, you are working with an active assistant. When you run `/reflect` or `/create-plan`, the agent actually writes the files, formats them correctly, tracks tasks in `gtd/`, and performs the Git commands for you.
