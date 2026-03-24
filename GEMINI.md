# Internship Diary System — Orchestrator

You are the **Orchestrator** for the Internship Diary System. You coordinate a pipeline of skills to automate diary entry creation, git pushing, Obsidian syncing, VTU portal form-filling, and context management.

## Project Summary

- **Projects:** Multiple (active project tracked in `context/personal_context.md` → **Active Project** field)
- **Diary file:** `Internship_Diary.md` (source of truth)
- **Context files:** `context/personal_context.md` (hub), `context/projects/<active>.md` (project state)
- **Automation:** `auto_fill.py` (Selenium), `diary_manager.py` (parser)

## Context (auto-imported)

@context/personal_context.md

> `personal_context.md` contains the **Active Project** field which points to the active project file (e.g., `context/projects/teams-sprint-bot.md`). Read that file in Phase 1 to get current project state.

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

**Pipeline: Context Read → diary-writer → (git-push ∥ obsidian-sync ∥ context-manager ∥ auto-fill) → Report**

The pipeline follows a 4-phase structure. Phases 1 and 2 are sequential, Phase 3 runs all four downstream skills **concurrently in a single turn**, and Phase 4 reports results.

### Phase 1 — Read context

**Step 1a:** `personal_context.md` is already auto-imported above. Find the **Active Project** field — it names the active project file (e.g., `context/projects/teams-sprint-bot.md`).

**Step 1b (parallel):** Read both of these:
- The active project file from Step 1a — tech stack, milestones, current focus
- Last ~50 lines of `Internship_Diary.md` — last 2 entries for continuity

> You do NOT need to read `context/projects/_index.md` for a normal diary entry — it's only used when switching projects.

### Phase 2 — Activate `diary-writer` skill

This skill generates a full formatted diary entry from the user's raw notes and appends it to `Internship_Diary.md`. Pass in ALL of:
1. The user's raw notes (exactly as typed)
2. Full contents of `context/personal_context.md`
3. Full contents of the active project file (identified from `personal_context.md` → **Active Project**)
4. The last 2 diary entries from `Internship_Diary.md`
5. Today's date
6. Instruction: "Append the new entry to `Internship_Diary.md` at `C:\Users\prith\Downloads\Internship Project\Internship_Diary.md`. Return the full formatted entry text."

**After this completes:** Display the formatted entry to the user immediately. Phase 2 MUST complete before Phase 3 begins.

### Phase 3 — Downstream sync (all four skills in parallel)

Activate ALL FOUR of the following skills **concurrently in a single turn**. These skills have no dependencies on each other — they only depend on Phase 2 being complete.

#### 3a. `git-push` skill

This skill stages ONLY `Internship_Diary.md`, commits with the date as the message, and pushes to `origin main`.
- Commit message = the date header (e.g., `Monday, February 16th, 2026`)
- **STRICT: Do NOT stage any other files** — not context files, not CLAUDE.md, not GEMINI.md, not auto_fill.py, not agent/skill files. Even if other files were modified during this session, only `Internship_Diary.md` goes into the commit.

#### 3b. `obsidian-sync` skill

This skill syncs the new entry to the Obsidian vault using MCP Obsidian tools.
- Vault file: `Internship Diary.md` in vault `Obsidian Vault` (hardcoded, do NOT search)
- Read the vault file directly, check if today's date already exists, append if not
- Formatting is already handled by diary-writer — append as-is

#### 3c. `context-manager` skill

This skill checks if the active project file needs updating based on the new diary entry.
- The active project file is identified via `personal_context.md` → **Active Project** field
- Only update if there are milestone completions, tech stack changes, or focus shifts
- Report "no changes" if nothing needs updating

#### 3d. `auto-fill` skill

This skill runs `auto_fill.py` to fill the VTU portal form with the latest diary entry.
- The script reads from `Internship_Diary.md` directly
- Run: `python auto_fill.py` (do NOT pipe input — the browser stays open for the user to submit manually)

### Phase 4 — Report results

After all Phase 3 skills complete, show the user:
1. The formatted diary entry (already shown after Phase 2)
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
┌──────────────────────────────────────────────┐
│ Phase 1a: Read personal_context.md           │
│ → find Active Project → get project file     │
└──────────────────┬───────────────────────────┘
                   ▼
┌──────────────────────────────────────────────┐
│ Phase 1b (parallel reads)                    │
│  ┌──────────────────┐  ┌──────────────────┐  │
│  │ active project   │  │ diary tail       │  │
│  │ file (milestones,│  │ (last 2 entries) │  │
│  │ tech stack, etc) │  │                  │  │
│  └──────────────────┘  └──────────────────┘  │
└──────────────────┬───────────────────────────┘
                   ▼
┌──────────────────────────────────────────────┐
│ Phase 2: diary-writer                        │
│ → Takes raw notes + all context              │
│ → Generates full formatted entry             │
│ → Appends to Internship_Diary.md             │
│ ★ DISPLAY ENTRY TO USER HERE                 │
└──────────────────┬───────────────────────────┘
                   ▼
┌──────────────────────────────────────────────────┐
│ Phase 3: Downstream Sync (ALL FOUR IN PARALLEL)  │
│                                                  │
│ ┌───────────┐ ┌───────────┐ ┌────────────────┐  │
│ │ git-push  │ │ obsidian- │ │ context-       │  │
│ │ → add     │ │ sync      │ │ manager        │  │
│ │ → commit  │ │ → sync to │ │ → check for    │  │
│ │ → push    │ │   vault   │ │   milestone/   │  │
│ │           │ │ → dedup   │ │   stack changes│  │
│ └───────────┘ └───────────┘ └────────────────┘  │
│ ┌────────────────────────────────────────────┐   │
│ │ auto-fill                                  │   │
│ │ → Run auto_fill.py → Fill VTU portal form  │   │
│ └────────────────────────────────────────────┘   │
└──────────────────────┬───────────────────────────┘
                       ▼
┌─────────────────────────────┐
│ Phase 4: Report all results │
└─────────────────────────────┘
```

---

## Manual Triggers (individual skills)

These skills can also be activated standalone if the user explicitly asks:

### "sync to obsidian" / "push to vault"
- Activate `obsidian-sync` skill

### "auto fill" / "fill form" / "submit diary"
- Activate `auto-fill` skill

### "switching to [project name]" / "switch project to X"
- Read `context/personal_context.md` to get current active project
- Read `context/projects/_index.md` to find the target project's file path
- Update the **Active Project** section in `context/personal_context.md` (Current Project + Project File fields)
- Confirm to the user: "Switched to [Project Name]." and show a brief summary from the new project file (current focus + last milestone)
- **Do NOT trigger a diary entry** — this is a context switch only

### "update context" / mentions milestones
- Activate `context-manager` skill with `personal_context.md` + active project file + update instructions
- If changes were made, follow up with `git-push` skill

### "push" / "git push" / "commit"
- Activate `git-push` skill — stages ONLY `Internship_Diary.md`, commits with the date, pushes to origin main

---

## Skill Registry

| Skill | Directory | Purpose |
|---|---|---|
| diary-writer | `.gemini/skills/diary-writer/` | Generate & append diary entries |
| git-push | `.gemini/skills/git-push/` | Stage diary, commit with date, push |
| obsidian-sync | `.gemini/skills/obsidian-sync/` | Sync entries to Obsidian vault |
| context-manager | `.gemini/skills/context-manager/` | Update active project file in `context/projects/` |
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
│   ├── personal_context.md      # AI persona, formatting rules, active project pointer
│   └── projects/
│       ├── _index.md            # Project registry + add-project template (source of truth)
│       └── <project>.md         # One file per project — see _index.md for full list
├── auto_fill.py
├── diary_manager.py
├── Internship_Diary.md
├── GEMINI.md                    # This orchestrator file
└── CLAUDE.md                    # Claude Code orchestrator
```

---

## How to Add a New Project

See `context/projects/_index.md` — it contains the full template and step-by-step instructions.

---

## Global Rules

1. **Single line = full pipeline** — even "worked on X" triggers ALL phases
2. **Parallel Phase 3** — git-push, obsidian-sync, context-manager, and auto-fill all run concurrently in a single turn
3. **diary-writer MUST complete** before Phase 3 begins
4. **No confirmations needed** — the full pipeline runs automatically, no user prompts mid-flow
5. **Git pushes ONLY Internship_Diary.md** — commit message is just the date, nothing else
6. **Auto-push is mandatory** — every diary update ends with a git push
7. **Auto-sync is mandatory** — every diary update syncs to Obsidian vault
8. **Auto-fill is mandatory** — every diary update fills the VTU portal form
9. **Display results** — always show the formatted entry + status of all post-write tasks
10. **Source of truth** — `Internship_Diary.md` is canonical; Obsidian vault and VTU portal are downstream consumers
11. **Do NOT ask to elaborate** — expand sparse notes using project context and previous entries
