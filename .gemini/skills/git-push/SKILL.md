---
name: git-push
description: "Use this skill to commit and push Internship_Diary.md to the remote git repository. Runs automatically after diary entries are written. Stages ONLY Internship_Diary.md, commits with the date as the message, pushes to origin main."
---

# Git Push — Diary Only

Your ONLY job is to commit and push `Internship_Diary.md` — nothing else.

## Exact Commands

Run these shell commands in sequence:

```bash
cd "C:\Users\prith\Downloads\Internship Project"
git add Internship_Diary.md
git commit -m "[DATE]"
git push origin main
```

Replace `[DATE]` with the diary entry date (e.g., `Monday, February 16th, 2026`).

## STRICT Rules

1. **ONLY stage `Internship_Diary.md`** — do NOT `git add` any other file
2. **Commit message is ONLY the date** — no prefix, no description, just the date string
3. **No confirmation needed** — just push immediately
4. **Branch** — always push to `origin main`
5. **If push fails** — report the exact error. If remote is ahead, try `git pull --rebase origin main` then push again
6. **If nothing to commit** — report "nothing to commit" — this is not an error

## What NOT to Do

- Do NOT run `git add .` or `git add -A`
- Do NOT stage `context/project_context.md` or any other file
- Do NOT add anything to the commit message beyond the date
- Do NOT add Co-Authored-By or any other trailers
- Do NOT stage untracked files

## Output

Report:
1. The exact `git add` command run
2. Commit message used
3. Push result (success or error)
