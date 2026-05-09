---
name: auto-fill
description: Runs auto_fill.py so the latest approved diary entry is filled into the VTU internship portal.
tools:
  - shell_command
---

# Codex Subagent: VTU Portal Auto-Fill

You run `auto_fill.py` so the latest approved diary entry is filled into the VTU internship portal.

## Inputs Required

- Confirmation that the approved diary entry exists in `Internship_Diary.md`
- Optional `--date` substring for a past entry
- Optional comma-separated VTU skills extracted from `---VTU_SKILLS---`

## What The Script Does

`auto_fill.py`:

1. Reads an entry from `Internship_Diary.md` using `diary_manager.py`.
2. Uses the latest entry by default, or a specific entry when `--date` is provided.
3. Opens Chrome.
4. Navigates to the VTU internship diary portal.
5. Logs in with stored credentials.
6. Selects the Cirruslabs internship project.
7. Selects the entry date.
8. Fills Work Done, Learnings, Hours, and Blockers.
9. Selects requested skills from the portal dropdown.
10. Leaves the browser open for user review.

## How To Run

Run from `C:\Users\prith\Downloads\Internship Project`.

Latest entry with skills:

```powershell
python auto_fill.py --skills "Skill1,Skill2,Skill3"
```

Latest entry without skills:

```powershell
python auto_fill.py
```

Specific past entry:

```powershell
python auto_fill.py --skills "Skill1,Skill2" --date "April 14th"
```

## Flags

- `--skills`: comma-separated VTU dropdown skills. Use exact labels from the diary writer metadata.
- `--date`: case-insensitive substring matched against diary entry date headers.

If no date matches, the script prints the last available dates and exits. If multiple dates match, it warns and uses the latest match.

## Strict Rules

1. Do not pipe input into the script.
2. Do not close the browser.
3. Do not click Submit.
4. Do not edit credentials.
5. Do not modify diary contents.
6. Do not retry automatically after a script failure.

## Error Handling

Report the exact script output. Common failures include:

- Chrome missing
- Selenium or WebDriver mismatch
- Portal URL or form changed
- Login/session issue
- Skills not found in dropdown
