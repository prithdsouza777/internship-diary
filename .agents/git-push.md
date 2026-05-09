---
name: git-push
description: Commits and pushes only Internship_Diary.md after an approved diary entry has been appended.
tools:
  - shell_command
---

# Codex Subagent: Git Push

You commit and push `Internship_Diary.md` after an approved diary entry has been appended.

This subagent is only for diary pipeline commits. It is not for general repository commits.

## Inputs Required

- Diary date header without `##`, for example `Monday, February 16th, 2026`
- Confirmation that the approved entry has already been appended to `Internship_Diary.md`

## Commands

Run from `C:\Users\prith\Downloads\Internship Project`:

```powershell
git add Internship_Diary.md
git commit -m "[DATE]"
git push origin main
```

Replace `[DATE]` with the exact diary date header text.

## Strict Rules

1. Stage only `Internship_Diary.md`.
2. Do not run `git add .` or `git add -A`.
3. Commit message is only the date string. No prefix, suffix, or trailers.
4. Push to `origin main`.
5. If there is nothing to commit, report `nothing to commit`; this is not a failure.
6. If push fails because remote is ahead, run `git pull --rebase origin main`, then retry the push.
7. If authentication, network, or merge conflicts block the push, report the exact failure.

## Never Stage

- `AGENTS.md`
- `GEMINI.md`
- `CLAUDE.md`
- `.agent/`, `.agents/`, `.gemini/`, `.claude/`
- `context/`
- `auto_fill.py`
- Any unrelated files

## Output

Report:

1. Exact `git add` command used
2. Commit message
3. Push result
