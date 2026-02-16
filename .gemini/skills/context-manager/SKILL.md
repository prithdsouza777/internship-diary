---
name: context-manager
description: "Use this skill after a diary entry is written to check if context/project_context.md needs updating. Also activate when the user mentions milestone completions, tech stack changes, or explicitly says 'update context'."
---

# Project Context Manager

Your job is to keep `context/project_context.md` up to date so the system maintains long-term memory over a 4-month internship.

## What You Monitor

Review each new diary entry for:

1. **Milestone completions** — if a milestone is done, check it off `[x]`
2. **New milestones** — if new work phases begin, add them as `[ ]`
3. **Tech stack changes** — new tools, services, or frameworks being used
4. **Current focus shifts** — if the active sprint or focus area changed
5. **New blockers** — add to the Recent Blockers section
6. **Resolved blockers** — remove or mark as resolved

## The File You Manage

`context/project_context.md`

This file has these sections:
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

## How to Update

1. Read the current `context/project_context.md`
2. Compare against the new diary entry (available from the earlier diary-writer step)
3. If changes needed: edit the file with minimal, targeted changes
4. Report what was changed and why
5. If no changes needed: report "no changes" — do NOT touch the file

## What NOT to Do

- Do NOT modify the "Diary Constraints & Evolution" section
- Do NOT change the Project Overview unless the project fundamentally changes
- Do NOT add redundant or trivial updates
- Do NOT rewrite sections — make minimal, targeted edits
