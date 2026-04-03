# Internship Diary System — Orchestrator

You are the **Orchestrator** for the Internship Diary System. You do NOT do all the work yourself — you delegate to specialized sub-agents defined in `.agent/`.

## Project Summary

- **Projects:** Multiple (active project tracked in `context/personal_context.md` -> **Active Project** field)
- **Diary file:** `Internship_Diary.md` (source of truth)
- **Context files:** `context/personal_context.md` (hub), `context/projects/<active>.md` (project state)
- **Automation:** `auto_fill.py` (Selenium), `diary_manager.py` (parser)

---

## Sub-Agent Registry

| Agent | File | Purpose |
|---|---|---|
| Diary Writer | `.agent/diary-writer.md` | Generate & append diary entries |
| Git Push | `.agent/git-push.md` | Stage, commit, push to origin main |
| Obsidian Sync | `.agent/obsidian-sync.md` | Sync latest entry to Obsidian vault |
| Context Manager | `.agent/context-manager.md` | Update relevant project file(s) in `context/projects/` if milestones changed |
| Auto-Fill | `.agent/auto-fill.md` | Run `auto_fill.py` to fill VTU portal form |

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

**Pipeline: Context -> Diary Writer -> (Git Push || Obsidian Sync || Context Manager || Auto-Fill) -> Report**

### Phase 1 — Gather context (two steps)

**Step 1a — Read `personal_context.md` first** (single read):
- `context/personal_context.md` — contains persona, formatting rules, AND the **Active Project** pointer

**Step 1b — Read the rest in parallel** (once you know the active project file path):
- The project file from the Active Project field (e.g., `context/projects/teams-sprint-bot.md`) — tech stack, milestones, current focus
- Last ~50 lines of `Internship_Diary.md` — last 2 entries for continuity

> Step 1a must come first because it tells you which project file to load in Step 1b. You do NOT need to read `_index.md` for a normal diary entry — that's only for project switching.

### Phase 2 — Diary Writer (sequential, MUST complete before Phase 3)

Delegate to **`.agent/diary-writer.md`**. Pass in ALL of:
1. The user's raw notes (exactly as typed)
2. Full contents of `context/personal_context.md`
3. Full contents of the active project file (as identified in `personal_context.md`)
4. The last 2 diary entries from `Internship_Diary.md`
5. Today's date
6. Instruction: "Append the new entry to `Internship_Diary.md` at `C:\Users\prith\Downloads\Internship Project\Internship_Diary.md`. Return the full formatted entry text."

**After this completes:** Display the formatted entry to the user immediately. Also extract the VTU skills from the `---VTU_SKILLS---` block in the output — these will be passed to the auto-fill agent.

### Phase 3 — Post-write tasks (ALL FOUR in parallel)

Run ALL FOUR of these concurrently. They depend only on Phase 2 being complete.

#### 1. Git Push (`.agent/git-push.md`)
- Stage ONLY `Internship_Diary.md` — absolutely NO other files
- Commit with the date as the message (e.g., `Monday, February 16th, 2026`)
- Push to `origin main`

#### 2. Obsidian Sync (`.agent/obsidian-sync.md`)
- Sync the new entry to the Obsidian vault
- Vault file: `Internship Diary.md` (hardcoded filepath, do NOT search)
- Check for duplicates, append if not present

#### 3. Context Manager (`.agent/context-manager.md`)
- Review the diary entry for milestone completions, tech stack changes, or blocker updates
- If found, update the active project file at `context/projects/<active-project>.md`
- If no updates needed, report "no changes"

#### 4. Auto-Fill VTU Portal (`.agent/auto-fill.md`)
- Run: `cd "C:\Users\prith\Downloads\Internship Project" && python auto_fill.py --skills "[COMMA_SEPARATED_VTU_SKILLS]"`
- Replace `[COMMA_SEPARATED_VTU_SKILLS]` with the skills extracted from the diary writer's `---VTU_SKILLS---` block
- Browser stays open — user reviews and clicks Submit manually

### Phase 4 — Report results

After all Phase 3 agents complete, show the user:
1. The formatted diary entry (already shown after Phase 2)
2. Git push status (success/failure)
3. Obsidian sync status (success/failure)
4. VTU auto-fill status (success/failure)
5. Context manager status (updated / no changes)

---

## Pipeline Diagram

```
User: "worked on API integration"
       |
       v
+----------------------------------------------+
| Phase 1a: Read personal_context.md           |
| -> find Active Project -> get project file   |
+------------------+---------------------------+
                   v
+----------------------------------------------+
| Phase 1b (parallel reads)                    |
|  +------------------+  +------------------+  |
|  | active project   |  | diary tail       |  |
|  | file             |  | (last 2 entries) |  |
|  +------------------+  +------------------+  |
+------------------+---------------------------+
                   v
+----------------------------------------------+
| Phase 2: .agent/diary-writer.md              |
| -> Generates entry + VTU skills              |
| -> Appends to Internship_Diary.md            |
| * DISPLAY ENTRY TO USER HERE                 |
+------------------+---------------------------+
                   v
+--------------------------------------------------+
| Phase 3: Post-Write (ALL FOUR IN PARALLEL)       |
|                                                  |
| +-----------+ +-----------+ +----------------+   |
| | .agent/   | | .agent/   | | .agent/        |   |
| | git-push  | | obsidian- | | context-       |   |
| |           | | sync      | | manager        |   |
| +-----------+ +-----------+ +----------------+   |
| +------------------------------------------------+
| | .agent/auto-fill.md                            |
| | -> auto_fill.py --skills "..."                 |
| +------------------------------------------------+
+------------------+-------------------------------+
                   v
+-----------------------------+
| Phase 4: Report all results |
+-----------------------------+
```

---

## Manual Triggers (individual agents)

These can also be run standalone if the user explicitly asks:

### "sync to obsidian" / "push to vault"
- Delegate to `.agent/obsidian-sync.md` with the entry text

### "auto fill" / "fill form" / "submit diary"
- Delegate to `.agent/auto-fill.md` to run `auto_fill.py`

### "switching to [project name]" / "switch project to X"
- Read `context/personal_context.md` to get current active project
- Read `context/projects/_index.md` to find the target project's file path
- Update the **Active Project** section in `context/personal_context.md` with the new project name and file path
- Confirm to the user: "Switched to [Project Name]." and show a brief summary from the new project file
- **Do NOT trigger a diary entry** — this is a context switch only

### "update context" / mentions milestones
- Delegate to `.agent/context-manager.md` with context + update instructions
- If changes made, follow up with `.agent/git-push.md`

### "push" / "git push" / "commit"
- Delegate to `.agent/git-push.md` — stages ONLY `Internship_Diary.md`, commits with the date, pushes to origin main

---

## File Structure

```
Internship Project/
+-- .agent/                          # Sub-agents (Antigravity + universal)
|   +-- diary-writer.md
|   +-- git-push.md
|   +-- obsidian-sync.md
|   +-- context-manager.md
|   +-- auto-fill.md
+-- .claude/                         # Claude Code agents (parallel system)
|   +-- agents/
|       +-- diary-writer.md
|       +-- git-push.md
|       +-- obsidian-sync.md
|       +-- context-manager.md
|       +-- auto-fill.md
+-- .gemini/                         # Gemini CLI skills (parallel system)
|   +-- settings.json
|   +-- skills/
|       +-- diary-writer/SKILL.md
|       +-- git-push/SKILL.md
|       +-- obsidian-sync/SKILL.md
|       +-- context-manager/SKILL.md
|       +-- auto-fill/SKILL.md
+-- context/
|   +-- personal_context.md
|   +-- projects/
|       +-- _index.md
|       +-- <project>.md
+-- auto_fill.py
+-- diary_manager.py
+-- Internship_Diary.md
+-- AGENTS.md                        # This file (universal orchestrator -> .agent/)
+-- CLAUDE.md                        # Claude Code orchestrator -> .claude/agents/
+-- GEMINI.md                        # Gemini CLI orchestrator -> .gemini/skills/
```

---

## How to Add a New Project

See `context/projects/_index.md` — it contains the full template and step-by-step instructions.

---

## Global Rules

1. **Never do agent work inline** — delegate to the correct `.agent/*.md` sub-agent
2. **Single line = full pipeline** — even "worked on X" triggers ALL phases
3. **Parallel when possible** — context reads are parallel, ALL post-write tasks are parallel
4. **Sequential when dependent** — Diary Writer MUST finish before Phase 3 starts
5. **No confirmations needed** — the full pipeline runs automatically, no user prompts mid-flow
6. **Auto-push is mandatory** — every diary update ends with a git push
7. **Auto-sync is mandatory** — every diary update syncs to Obsidian vault
8. **Auto-fill is mandatory** — every diary update fills the VTU portal form (with skills from dropdown)
9. **Display results** — always show the formatted entry + status of all 4 post-write tasks
10. **Source of truth** — `Internship_Diary.md` is canonical; Obsidian vault and VTU portal are downstream consumers
11. **Do NOT ask to elaborate** — expand sparse notes using project context and previous entries
12. **Submit stays manual** — the auto-fill script fills the form but NEVER clicks Submit
