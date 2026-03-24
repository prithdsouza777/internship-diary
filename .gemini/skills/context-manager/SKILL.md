---
name: context-manager
description: "Use this skill after a diary entry is written to check if the active project file needs updating. Also activate when the user mentions milestone completions, tech stack changes, or explicitly says 'update context'. Also handles 'switching to [project]' by updating personal_context.md's Active Project field."
---

# Project Context Manager

Your job is to keep the active project file under `context/projects/` up to date so the system maintains long-term memory over a 4-month internship.

## What You Monitor

Review each new diary entry for:

1. **Milestone completions** — if a milestone is done, check it off `[x]`
2. **New milestones** — if new work phases begin, add them as `[ ]`
3. **Tech stack changes** — new tools, services, or frameworks being used
4. **Current focus shifts** — if the active sprint or focus area changed
5. **New blockers** — add to the Recent Blockers section
6. **Resolved blockers** — remove or mark as resolved

## The Files You Manage

**Active project file:** Read `context/personal_context.md` first → find the **Active Project** field → that gives you the file path (e.g., `context/projects/teams-sprint-bot.md`).

All project files live at `C:\Users\prith\Downloads\Internship Project\context\projects\`.

**Never modify** `personal_context.md` (except for project switches) or `_index.md` (except when adding/removing a project).

Each project file has these sections:
- **Project Overview** (name + description)
- **Technical Stack** (comma-separated list)
- **Current Focus / Active Sprint** (what's being worked on now)
- **Key Milestones & Status** (checklist of milestones)
- **Recent Blockers** (active blockers)
- **Diary Constraints & Evolution** (rules — do NOT modify this section)

## Decision Rules

- If the diary entry is routine work within the current focus → **no changes needed**, report "no changes"
- If a new technology/tool appears → **add it** to the Technical Stack
- If work shifts to a new area → **update** Current Focus / Active Sprint
- If a milestone is clearly completed → **check it off** `[x]`
- If a new milestone begins → **add it** as `[ ]`
- Only update when there's a **meaningful change** — do not update for every entry

## How to Update (Normal Diary Entry)

1. Read `context/personal_context.md` to identify the active project file
2. Compare the active project file against the new diary entry
3. If changes needed: edit the project file with minimal, targeted changes
4. Report what was changed and why
5. If no changes needed: report "no changes" — do NOT touch the file

## How to Update (Project Switch)

When the user says "switching to [project]":
1. Read `context/projects/_index.md` to find the target project's file path
2. Update the **Active Project** section in `context/personal_context.md`:
   - `**Current Project:**` → new project name
   - `**Project File:**` → new file path
3. Report: "Switched active project to [Name]. File: [path]."

## What NOT to Do

- Do NOT modify the "Diary Constraints & Evolution" section in any project file
- Do NOT change the Project Overview unless the project fundamentally changes
- Do NOT add redundant or trivial updates
- Do NOT rewrite sections — make minimal, targeted edits
- Do NOT modify `personal_context.md` except during a project switch
