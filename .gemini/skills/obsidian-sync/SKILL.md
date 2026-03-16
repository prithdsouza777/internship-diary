---
name: obsidian-sync
description: "Use this skill to sync diary entries to the user's Obsidian vault. Reads the latest entry from the conversation context and appends it to the Internship Diary file in the Obsidian vault using MCP Obsidian tools. Also activate when user says 'sync to obsidian' or 'push to vault'."
---

# Obsidian Vault Sync

Your job is to sync the latest diary entry to the user's Obsidian vault.

## SAFETY RULE — AVOID DELETING THE WHOLE FILE

Deleting or overwriting the entire Obsidian diary file should be a **last resort only**. It risks data loss.

- **PREFERRED:** Appending a new entry to the end of the file
- **PREFERRED:** Using `obsidian_patch_content` to replace ONLY a specific date's entry
- **LAST RESORT ONLY:** Deleting/overwriting the whole file — only if the file is corrupted or no other method works

Always try append or patch first. Only fall back to full overwrite if absolutely necessary.

## Known Vault Path (hardcoded)

- **Vault:** `Obsidian Vault`
- **File:** `Internship Diary.md`

The file name is stable — do NOT search for it. Go directly to read and append.

## Sync Rules

1. **Read-only on local** — NEVER modify the local `Internship_Diary.md`.
2. **Direct access** — Read `Internship Diary.md` from vault `Obsidian Vault` directly. No searching needed.
3. **Duplicate check** — Read the vault file, check if today's date header already exists. If it does, skip.
4. **Preserve formatting** — Match the EXISTING vault file's formatting exactly (headers, indentation, spacing, bullets). If the entry differs in style, convert it to match.
5. **Scope** — Only touch `Internship Diary.md`. Do not access other vault files.

## How to Sync

### Step 1: Read vault file and check for duplicates
Read `Internship Diary.md` from vault `Obsidian Vault` directly using `obsidian_get_file_contents` (no searching).
- Parse the date headers to check if today's entry already exists
- If it exists, skip (report "already synced")

### Step 2: Append the entry
If the entry does NOT exist yet, use `obsidian_append_content` to add it directly to `Internship Diary.md`.
- Formatting is already handled by the diary-writer — append as-is

### Step 3 (fallback only): If Steps 1-2 fail with "file not found"
- Search for "Internship Diary" by filename in the vault
- Use the found path and retry
- If the file doesn't exist at all, create it

### Step 4: Report
- Confirm entry was synced (by date), skipped (duplicate), or failed (with error)

## Important Notes

- The new diary entry text should be available from the earlier diary-writer step in the conversation
- If MCP Obsidian tools are not available or fail, report the error clearly — do NOT silently fail
