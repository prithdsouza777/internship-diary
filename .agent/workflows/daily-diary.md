---
description: Unified daily diary entry pipeline — context, write, git push, Obsidian sync, context update, VTU auto-fill
---

# Daily Diary Workflow

Any user message describing what they did today triggers this full pipeline. Even a single sentence like "worked on API integration" runs ALL steps below. Do NOT ask the user to elaborate — expand using context files.

---

## Phase 1 — Gather Context (parallel reads)

Read ALL THREE of these in parallel before writing:
- `context/personal_context.md` — formatting rules and persona
- `context/project_context.md` — current project state, milestones, tech stack
- Last ~50 lines of `Internship_Diary.md` — last 2 entries for continuity and deduplication

---

## Phase 2 — Write Diary Entry (sequential, must complete before Phase 3)

Create a structured diary entry using the user's raw notes + all context gathered above.

Format:
- **Date Header**: `## [Day], [Month] [Date], [Year]` (e.g., `## Tuesday, February 4th, 2026`)
- **What I worked on?**: Bullet points of tasks (use bold for key terms)
- **Learnings / Outcomes**: Key takeaways from the day
- **Blockers / Risks**: Any blockers or `*None reported today.*`
- **Skills Used**: Relevant skills (comma-separated or bullet points)

Append the formatted entry to `Internship_Diary.md`.

**Display the formatted entry to the user immediately after writing.**

---

## Phase 3 — Post-Write Tasks (all four in parallel)

Run ALL FOUR of these simultaneously after Phase 2 completes:

### 3a. Git Push
Stage ONLY `Internship_Diary.md`, commit with the date as the message (e.g., `Monday, February 16th, 2026`), and push to origin main.
```
cd "C:\Users\prith\Downloads\Internship Project"
git add Internship_Diary.md
git commit -m "Monday, February 16th, 2026"
git push origin main
```
Do NOT stage any other files. Do NOT add anything to the commit message beyond the date.

### 3b. Obsidian Sync
Sync the new diary entry to the Obsidian vault:
- Read `context/obsidian_context.md` for vault path and sync rules
- Use Obsidian MCP tools (obsidian_get_file_contents, obsidian_append_content) to:
  1. Read the existing vault file
  2. Check for duplicate entries
  3. Match formatting
  4. Append the new entry

### 3c. Context Manager
Review the new diary entry for any:
- Milestone completions
- Tech stack changes
- New tools or frameworks
- Blocker updates

If changes found, update `context/project_context.md`. If no updates needed, report "no changes".

### 3d. Auto-Fill VTU Portal
Run the auto-fill script to submit the entry to the VTU internship portal:
```
cd "C:\Users\prith\Downloads\Internship Project"
echo "" | python auto_fill.py
```
The `echo ""` pipes empty input to handle the "Press Enter to close browser" prompt.

---

## Phase 4 — Report Results

After all Phase 3 tasks complete, show the user:
1. The formatted diary entry (already shown after Phase 2)
2. Git push status (success/failure)
3. Obsidian sync status (success/failure)
4. Context manager status (updated / no changes)
5. VTU auto-fill status (success/failure)

---

## Trigger Rules

**Full pipeline triggers** (any of these):
- "today I worked on docker"
- "deployed the bot to azure"
- "did compliance training and documentation"
- "here's my update: [notes]"
- "log today: [notes]"
- Any sentence describing work done

**No confirmations needed** — the full pipeline runs automatically.

---

## File References

| File | Purpose |
|---|---|
| `Internship_Diary.md` | Source of truth for all entries |
| `context/personal_context.md` | AI persona and formatting rules |
| `context/project_context.md` | Current project state and milestones |
| `context/obsidian_context.md` | Obsidian vault sync rules |
| `auto_fill.py` | Selenium script for VTU portal automation |
| `diary_manager.py` | Diary entry parser (used by auto_fill.py) |
