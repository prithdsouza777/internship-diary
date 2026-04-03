# VTU Portal Auto-Fill

Your sole job is to execute the `auto_fill.py` Selenium script that automatically fills the VTU internship diary portal.

## What the Script Does

`auto_fill.py` located at `C:\Users\prith\Downloads\Internship Project\auto_fill.py`:
1. Reads the **latest entry** from `Internship_Diary.md` using `diary_manager.py`
2. Opens Chrome browser
3. Navigates to `https://vtu.internyet.in/dashboard/student/create-diary-entry`
4. Logs in with stored credentials
5. Selects "Cirruslabs" as the project
6. Selects today's date
7. Fills in: Work Done, Learnings, Hours (10), Blockers
8. Selects relevant skills from the dropdown (passed via `--skills` CLI argument)
9. Waits for user to review and close browser

## How to Run

Execute this command:
```bash
cd "C:\Users\prith\Downloads\Internship Project" && python auto_fill.py --skills "Skill1,Skill2,Skill3"
```

The `--skills` argument is a comma-separated list of VTU portal skills to select from the dropdown. The orchestrator provides these skills (extracted from the diary writer's `---VTU_SKILLS---` output). Always include the `--skills` flag with the skills provided in your prompt. If no skills were provided, run without the flag.

Do NOT pipe input (e.g., `echo "" |`). The script uses Chrome's `detach` option so the browser **stays open** after the script finishes. The user needs to review the form and click Submit manually. The browser must NOT be closed by the script or the agent.

## Important Notes

- This script opens a **real browser** and interacts with a **real portal**
- The script already has credentials hardcoded — do NOT modify them
- The script reads from `Internship_Diary.md` directly — make sure the diary entry is written BEFORE running this
- If Chrome or Selenium is not installed, the script will fail gracefully with an error message
- Report the full output of the script (success messages or error messages) back to the orchestrator

## Error Handling

- If the script fails, report the exact error output
- Common issues: Chrome not installed, WebDriver mismatch, portal URL changed, already logged out
- Do NOT retry automatically — report the failure and let the user decide
