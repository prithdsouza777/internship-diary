---
description: Unified daily diary entry and auto-fill workflow
---

# Daily Diary Workflow

When the user provides their daily work update, follow these steps:

## 1. Read Context
- Read `context/project_context.md` to understand the current project state.
- Read the last entry in `Internship_Diary.md` to ensure today's entry is distinct.

## 2. Synthesize Entry
Create a structured diary entry with:
- **Date Header**: `## [Day], [Month] [Date], [Year]` (e.g., `## Tuesday, February 4th, 2026`)
- **What I worked on?**: Bullet points of tasks (use bold for emphasis)
- **Learnings / Outcomes**: Key takeaways
- **Blockers / Risks**: Any blockers or `*None reported today.*`
- **Skills Used**: Relevant skills (comma-separated or bullet points)

## 3. Append to Diary
Append the formatted entry to `Internship_Diary.md`.

## 4. Auto-Fill Online Form
// turbo
Run the auto-fill script to submit to the VTU portal:
```
python auto_fill.py
```
Working directory: `c:\Users\prith\Downloads\Internship Project`

## 5. Notify User
Inform the user that:
- The entry has been appended to `Internship_Diary.md`
- The browser has opened and the form is being filled
- They should review and click "Submit" when ready
