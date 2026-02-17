---
name: auto-fill
description: "Use this skill to run the VTU internship portal auto-fill script (auto_fill.py). Executes the Selenium-based form filler that reads the latest diary entry from Internship_Diary.md and submits it to the VTU portal. Also activate when user says 'fill form', 'submit diary', or 'auto fill'."
---

# VTU Portal Auto-Fill

Your sole job is to execute the `auto_fill.py` Selenium script that fills the VTU internship diary portal.

## What the Script Does

`auto_fill.py`:
1. Reads the **latest entry** from `Internship_Diary.md` using `diary_manager.py`
2. Opens Chrome browser
3. Navigates to `https://vtu.internyet.in/dashboard/student/create-diary-entry`
4. Logs in with stored credentials
5. Selects "Cirruslabs" as the project
6. Selects today's date
7. Fills in: Work Done, Learnings, Hours (10), Blockers
8. Leaves Skills Used empty (as configured)
9. Waits for user to review and close browser

## How to Run

Execute this shell command:
```bash
cd "C:\Users\prith\Downloads\Internship Project" && python auto_fill.py
```

Do NOT pipe input (e.g., `echo "" |`). The script uses Chrome's `detach` option so the browser **stays open** after the script finishes. The user needs to review the filled form and click Submit manually. The browser must NOT be closed by the script or the agent.

## Important Notes

- This script opens a **real browser** and interacts with a **real portal**
- The script already has credentials hardcoded — do NOT modify them
- The script reads from `Internship_Diary.md` directly — the diary entry MUST be written BEFORE running this
- If Chrome or Selenium is not installed, the script will fail with an error message
- Report the full output of the script back

## Error Handling

- If the script fails, report the exact error output
- Common issues: Chrome not installed, WebDriver mismatch, portal URL changed, already logged out
- Do NOT retry automatically — report the failure and let the user decide
