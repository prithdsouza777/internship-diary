# Obsidian Sync Context

## Known Vault Path (hardcoded)
- **Vault:** `Obsidian Vault`
- **File:** `Internship Diary.md`

The file name is stable. Do NOT search for it — read and append directly.

## Source of Truth
- **Input:** The new diary entry text (provided in the prompt, already formatted by diary-writer).
- **Format:** Consistent date headers (`## Monday, February 2nd, 2026`), subsections (`### What I worked on?`, `### Learnings / Outcomes`, `### Blockers / Risks`, `### Skills Used`), and bullet points.

## SAFETY RULE — AVOID DELETING THE WHOLE FILE
Deleting or overwriting the entire Obsidian diary file should be a **last resort only** (e.g., file is corrupted). Always prefer appending.

## Rules
1. **Read-only on local** — NEVER modify the local `Internship_Diary.md`.
2. **Direct access** — Read `Internship Diary.md` from vault `Obsidian Vault` directly. No searching needed.
3. **Duplicate check** — Read the vault file, check if today's date header already exists. If it does, skip.
4. **Preserve formatting** — Match the EXISTING vault file's formatting exactly (headers, indentation, spacing, bullets). If the entry differs in style, convert it to match.
5. **Scope** — Only touch `Internship Diary.md`. Do not access other vault files.

## Fallback (only if read/append fails with "file not found")
- Search for "Internship Diary" by filename in the vault
- Retry with the found path
- If file doesn't exist at all, create it
