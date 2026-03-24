---
name: obsidian-sync
description: "Use this skill to sync diary entries to the user's Obsidian vault. Reads the latest entry from the conversation context and appends it to the Internship Diary file in the Obsidian vault using MCP Obsidian tools. Also activate when user says 'sync to obsidian' or 'push to vault'."
---

# Obsidian Vault Sync

Your job is to sync the latest diary entry to the user's Obsidian vault.

## IMPORTANT — Obsidian Must Be Running

This skill uses the **Obsidian Local REST API plugin** via `mcp-obsidian`. Obsidian must be open and running for any tool calls to work. If you get a connection error, report it clearly.

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

## MCP Tool Reference (correct tool names)

| Action | Tool |
|---|---|
| Read a file | `mcp__mcp-obsidian__obsidian_get_file_contents` |
| Append to a file | `mcp__mcp-obsidian__obsidian_append_content` |
| Patch/replace content | `mcp__mcp-obsidian__obsidian_patch_content` |
| Search vault | `mcp__mcp-obsidian__obsidian_simple_search` |
| List vault files | `mcp__mcp-obsidian__obsidian_list_files_in_vault` |

> **Do NOT use** `list-available-vaults`, `read-note`, `edit-note`, or `create-note` — those are from the old npm package and will fail.
> **To create a new file:** use `mcp__mcp-obsidian__obsidian_append_content` with the new filepath — Obsidian REST API creates it automatically if it doesn't exist.

## How to Sync

### Step 1: Read vault file and check for duplicates
Use `mcp__mcp-obsidian__obsidian_get_file_contents` with `filepath: "Internship Diary.md"` to read the file directly (no searching).
- Parse the date headers to check if today's entry already exists
- If it exists, skip (report "already synced")

### Step 2: Append the entry
If the entry does NOT exist yet, use `mcp__mcp-obsidian__obsidian_append_content` with `filepath: "Internship Diary.md"` and the entry text as `content`.
- Formatting is already handled by the diary-writer — append as-is

### Step 3 (fallback only): If Step 1 fails with "file not found"
- Use `mcp__mcp-obsidian__obsidian_simple_search` to search for "Internship Diary"
- Use the found path and retry
- If the file doesn't exist at all, use `mcp__mcp-obsidian__obsidian_append_content` with the filepath — Obsidian REST API will create it automatically

### Step 4: Report
- Confirm entry was synced (by date), skipped (duplicate), or failed (with error)

## Important Notes

- The new diary entry text should be available from the earlier diary-writer step in the conversation
- If MCP Obsidian tools are not available or fail, report the error clearly — do NOT silently fail
