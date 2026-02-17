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

## Sync Rules

1. **Read-only on local** — NEVER modify the local `Internship_Diary.md`. You only read from it.
2. **Update vault** — Append new entries to the Internship Diary file in the Obsidian vault.
3. **Preserve formatting** — Match the EXISTING vault file's formatting exactly (headers, indentation, spacing, bullets).
4. **No duplicates** — Check if the entry date already exists in the vault file. Skip if it does; update only if the local version is newer/more complete.
5. **Scope** — Only touch the Internship Diary file. Do NOT access other vault files.
6. **Minimal changes** — Only add or update the SINGLE entry being synced. Never touch other entries.

## How to Sync

### Step 1: Find the vault file
Use the MCP Obsidian tools available via `@obsidian`:
- Use `obsidian_list_files_in_vault` or `obsidian_simple_search` to find the Internship Diary file

### Step 2: Check for duplicates
- Read the existing vault file content using `obsidian_get_file_contents`
- Parse the date headers to see which entries already exist
- Check if today's date entry already exists

### Step 3a: NEW entry (date does NOT exist in vault)
- Use `obsidian_append_content` to add the new entry to the END of the file
- Ensure formatting matches the existing vault file exactly
- All 4 sections must be present

### Step 3b: UPDATE entry (date ALREADY exists in vault)
- Use `obsidian_patch_content` to replace ONLY the specific entry for that date
- Target the text from `## [Date Header]` up to (but not including) the next `## ` header or end of file
- **NEVER delete the whole file to re-add content**

### Step 4: Report
- List which entries were synced (by date)
- Note any entries skipped (already existed and unchanged)
- Report any errors

## Important Notes

- The new diary entry text should be available from the earlier diary-writer step in the conversation
- If MCP Obsidian tools are not available or fail, report the error clearly — do NOT silently fail
- If the vault file doesn't exist yet, create it with the same structure as `Internship_Diary.md`
