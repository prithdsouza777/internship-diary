---
name: obsidian-sync
description: "Use this skill to sync diary entries to the user's Obsidian vault. Reads the latest entry from the conversation context and appends it to the Internship Diary file in the Obsidian vault using MCP Obsidian tools. Also activate when user says 'sync to obsidian' or 'push to vault'."
---

# Obsidian Vault Sync

Your job is to sync the latest diary entry to the user's Obsidian vault.

## Sync Rules

1. **Read-only on local** — NEVER modify the local `Internship_Diary.md`. You only read from it.
2. **Update vault** — Append new entries to the Internship Diary file in the Obsidian vault.
3. **Preserve formatting** — Match the EXISTING vault file's formatting exactly (headers, indentation, spacing, bullets).
4. **No duplicates** — Check if the entry date already exists in the vault file. Skip if it does; update only if the local version is newer/more complete.
5. **Scope** — Only touch the Internship Diary file. Do NOT access other vault files.

## How to Sync

### Step 1: Find the vault file
Use the MCP Obsidian tools available via `@obsidian`:
- Use `obsidian_list_files_in_vault` or `obsidian_simple_search` to find the Internship Diary file
- Search for files with `## Monday, February` style date headers or "Internship Diary" in the name

### Step 2: Check for duplicates
- Read the existing vault file content using `obsidian_get_file_contents`
- Parse the date headers to see which entries already exist
- Identify which entries from the new input are missing from the vault

### Step 3: Append new entries
- Use `obsidian_append_content` to add missing entries to the vault file
- Ensure formatting matches the existing vault file exactly
- All 4 sections must be present: What I worked on?, Learnings / Outcomes, Blockers / Risks, Skills Used

### Step 4: Report
- List which entries were synced (by date)
- Note any entries skipped (already existed)
- Report any errors

## Important Notes

- The new diary entry text should be available from the earlier diary-writer step in the conversation
- If MCP Obsidian tools are not available or fail, report the error clearly — do NOT silently fail
- If the vault file doesn't exist yet, create it with the same structure as `Internship_Diary.md`
