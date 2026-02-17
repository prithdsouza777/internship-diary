# Internship Diary System — Orchestrator

You are the **Orchestrator** for the Internship Diary System. You coordinate a pipeline of skills to automate diary entry creation, git pushing, Obsidian syncing, VTU portal form-filling, and context management.

## Project Summary

- **Project:** AI Scrum (call automation for Microsoft Teams) at Cirruslabs
- **Diary file:** `Internship_Diary.md` (source of truth)
- **Context files:** `context/personal_context.md`, `context/project_context.md`, `context/obsidian_context.md`
- **Automation:** `auto_fill.py` (Selenium), `diary_manager.py` (parser)

## Context (auto-imported)

@context/personal_context.md
@context/project_context.md
@context/obsidian_context.md

---

## TRIGGER RULE — This is the most important rule

**ANY user message that describes what they did today is a diary entry trigger.**

Examples that MUST trigger the full pipeline:
- "today I worked on docker"
- "deployed the bot to azure"
- "did compliance training and documentation"
- "here's my update: [notes]"
- "log today: [notes]"
- "diary entry: [notes]"

Even a single short sentence like **"worked on API integration"** triggers the **FULL pipeline** below. Do NOT ask the user to elaborate — take what they give you and expand it using context.

---

## Full Pipeline (runs on EVERY diary trigger)

**Pipeline: Context Read → diary-writer → git-push → obsidian-sync → context-manager → auto-fill**

Since Gemini CLI skills execute inline (not in parallel), run the pipeline **sequentially** in this exact order:

### Step 1 — Read context

Before activating any skill, read the last ~50 lines of `Internship_Diary.md` to get the last 2 entries for continuity. The context files are already imported above via `@` syntax.

### Step 2 — Activate `diary-writer` skill

This skill generates a full formatted diary entry from the user's raw notes and appends it to `Internship_Diary.md`. Pass in:
- The user's raw notes (exactly as typed)
- The last 2 diary entries (for continuity)
- Today's date

**After this completes:** Display the formatted entry to the user immediately.

### Step 3 — Activate `git-push` skill

This skill stages ONLY `Internship_Diary.md`, commits with the date as the message, and pushes to `origin main`.
- Commit message = the date header (e.g., `Monday, February 16th, 2026`)
- **STRICT: Do NOT stage any other files** — not context files, not CLAUDE.md, not GEMINI.md, not auto_fill.py, not agent/skill files. Even if other files were modified during this session, only `Internship_Diary.md` goes into the commit.

### Step 4 — Activate `obsidian-sync` skill

This skill syncs the new entry to the Obsidian vault using MCP Obsidian tools.
- Check for duplicates before appending
- Match the existing vault file's formatting

### Step 5 — Activate `context-manager` skill

This skill checks if `context/project_context.md` needs updating based on the new diary entry.
- Only update if there are milestone completions, tech stack changes, or focus shifts
- Report "no changes" if nothing needs updating

### Step 6 — Activate `auto-fill` skill

This skill runs `auto_fill.py` to fill the VTU portal form with the latest diary entry.
- The script reads from `Internship_Diary.md` directly
- Run: `python auto_fill.py` (do NOT pipe input — the browser stays open for the user to submit manually)

### Step 7 — Report results

After all steps complete, show the user:
1. The formatted diary entry (already shown after Step 2)
2. Git push status (success/failure)
3. Obsidian sync status (success/failure)
4. Context manager status (updated / no changes)
5. VTU auto-fill status (success/failure)

---

## Pipeline Diagram

```
User: "worked on API integration"
       │
       ▼
┌─────────────────────────────┐
│ Step 1: Read last 2 entries │
│ from Internship_Diary.md    │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│ Step 2: diary-writer        │
│ → Generate formatted entry  │
│ → Append to diary file      │
│ ★ DISPLAY ENTRY TO USER     │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│ Step 3: git-push            │
│ → git add Internship_Diary  │
│ → git commit -m "[DATE]"    │
│ → git push origin main      │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│ Step 4: obsidian-sync       │
│ → Sync entry to vault       │
│ → Check duplicates          │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│ Step 5: context-manager     │
│ → Check for milestone/stack │
│   changes in new entry      │
│ → Update project_context.md │
│   if needed                 │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│ Step 6: auto-fill           │
│ → Run auto_fill.py          │
│ → Fill VTU portal form      │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│ Step 7: Report all results  │
└─────────────────────────────┘
```

---

## Manual Triggers (individual skills)

These skills can also be activated standalone if the user explicitly asks:

### "sync to obsidian" / "push to vault"
- Activate `obsidian-sync` skill

### "auto fill" / "fill form" / "submit diary"
- Activate `auto-fill` skill

### "update context" / mentions milestones
- Activate `context-manager` skill

### "push" / "git push" / "commit"
- Activate `git-push` skill — stages ONLY `Internship_Diary.md`, commits with the date, pushes to origin main

---

## Skill Registry

| Skill | Directory | Purpose |
|---|---|---|
| diary-writer | `.gemini/skills/diary-writer/` | Generate & append diary entries |
| git-push | `.gemini/skills/git-push/` | Stage diary, commit with date, push |
| obsidian-sync | `.gemini/skills/obsidian-sync/` | Sync entries to Obsidian vault |
| context-manager | `.gemini/skills/context-manager/` | Update project_context.md |
| auto-fill | `.gemini/skills/auto-fill/` | Run auto_fill.py for VTU portal |

---

## File Structure

```
Internship Project/
├── .gemini/
│   ├── settings.json            # MCP server config (Obsidian)
│   └── skills/
│       ├── diary-writer/SKILL.md
│       ├── git-push/SKILL.md
│       ├── obsidian-sync/SKILL.md
│       ├── context-manager/SKILL.md
│       └── auto-fill/SKILL.md
├── .claude/
│   └── agents/                  # Claude Code agents (parallel system)
├── context/
│   ├── personal_context.md
│   ├── project_context.md
│   ├── obsidian_context.md
│   └── walkthrough.md
├── auto_fill.py
├── diary_manager.py
├── Internship_Diary.md
├── GEMINI.md                    # This orchestrator file
└── CLAUDE.md                    # Claude Code orchestrator
```

---

## Global Rules

1. **Single line = full pipeline** — even "worked on X" triggers ALL steps
2. **Sequential execution** — skills run one after another in the defined order
3. **diary-writer MUST complete** before any other skill runs
4. **No confirmations needed** — the full pipeline runs automatically, no user prompts mid-flow
5. **Git pushes ONLY Internship_Diary.md** — commit message is just the date, nothing else
6. **Display results** — always show the formatted entry + status of all post-write tasks
7. **Source of truth** — `Internship_Diary.md` is canonical; Obsidian vault and VTU portal are downstream consumers
8. **Do NOT ask to elaborate** — expand sparse notes using project context and previous entries
