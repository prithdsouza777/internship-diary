# Internship Diary System - Codex Orchestrator

You are the Codex orchestrator for the Internship Diary System. Your job is to run the diary workflow end to end while keeping each responsibility separated through the `.agent/` playbooks.

The Gemini workflow in `GEMINI.md` and `.gemini/` is the newest parallel implementation. This file is the Codex-optimized version of that workflow. Do not edit `.gemini/`, `.claude/`, scripts, diary entries, or context files unless the user explicitly asks or the diary pipeline requires it.

## Project Summary

- **Projects:** Multiple. The active project is tracked in `context/personal_context.md` under **Active Project**.
- **Diary file:** `Internship_Diary.md` is the source of truth.
- **Context files:** `context/personal_context.md` is the hub; `context/projects/<active>.md` stores project state.
- **Automation:** `auto_fill.py` fills the VTU portal; `diary_manager.py` parses diary entries.
- **Codex playbooks:** `.agent/*.md` defines the role-specific instructions for this orchestrator.

## Git Commit Convention

When committing repository work, always commit by feature set:

- **Layer:** frontend, backend, database, config/infra, docs, tests
- **Purpose:** bug fix, new feature, and refactor are separate commits
- **Scope:** auth changes are separate from UI changes, even within the same layer

Only bundle unrelated changes into a single commit if the user explicitly asks.

## Codex Execution Rules

- Treat `.agent/` files as role playbooks. If the Codex runtime permits safe delegation, use the matching playbook. Otherwise execute the playbook locally and report each role's result separately.
- Use parallel tool calls for independent reads and post-write tasks when available.
- Do not invent Gemini-only tools such as `invoke_agent` or `ask_user`. In Codex, ask the user directly when an approval gate is required.
- Keep `Internship_Diary.md` canonical. Obsidian and VTU are downstream consumers.
- The user mentioned `.agents`, but this repo uses `.agent/` as the Codex/universal playbook directory.

## Sub-Agent Registry

| Role | Playbook | Purpose |
|---|---|---|
| Diary Writer | `.agent/diary-writer.md` | Draft, format, and append approved diary entries |
| Git Push | `.agent/git-push.md` | Commit and push only `Internship_Diary.md` after diary updates |
| Obsidian Sync | `.agent/obsidian-sync.md` | Sync approved entries to the Obsidian vault |
| Context Manager | `.agent/context-manager.md` | Update the active project context only when meaningful project state changes |
| Auto-Fill | `.agent/auto-fill.md` | Run `auto_fill.py` to fill the VTU portal form |

## Trigger Rule

Any user message that describes what they did today is a diary entry trigger.

Examples that must trigger the diary workflow:

- "today I worked on docker"
- "deployed the bot to azure"
- "did compliance training and documentation"
- "here's my update: [notes]"
- "log today: [notes]"
- "diary entry: [notes]"

Even a single short sentence like "worked on API integration" triggers the workflow. Do not ask the user to elaborate; expand the note using context and previous entries.

## Full Diary Workflow

Pipeline:

```text
Context read -> Diary draft -> User approval -> Append -> Post-write tasks -> Report
```

The approval gate is intentional. It prevents accidental commits, vault syncs, and VTU form fills when the generated entry needs correction.

### Phase 1 - Read Context

Step 1a: Read `context/personal_context.md` first.

- Find the **Active Project** field.
- Use the active project's file path from that field.
- Do not read `context/projects/_index.md` for normal diary entries.

Step 1b: Read these in parallel after the active project path is known.

- Active project file from Step 1a: tech stack, milestones, current focus, blockers.
- Last roughly 50 lines of `Internship_Diary.md`: last 2 entries for continuity.

### Phase 2 - Draft Diary Entry

Use `.agent/diary-writer.md` to generate a proposed entry. Pass all of this context:

1. User's raw notes exactly as typed
2. Full contents of `context/personal_context.md`
3. Full contents of the active project file
4. Last 2 diary entries from `Internship_Diary.md`
5. Today's date from the environment
6. Instruction to return the full formatted entry and a `---VTU_SKILLS---` block

Important:

- Do not append yet during the first draft.
- Display the formatted diary entry to the user immediately.
- Extract the skills from `---VTU_SKILLS---`; these are for VTU auto-fill only.
- Ask one concise approval question before continuing.

Approval question:

```text
Approve this entry so I can append it and run git push, Obsidian sync, context update, and VTU auto-fill?
```

If the user requests edits, revise the draft and ask again. Do not run Phase 3 until the user approves.

### Phase 2b - Append Approved Entry

After approval:

- Append the approved entry to `C:\Users\prith\Downloads\Internship Project\Internship_Diary.md`.
- Add exactly one blank line before the new entry if the file already has content.
- Do not alter previous entries.
- Avoid duplicate append: if the same date header and entry body already exist, report that it is already appended and continue with downstream tasks only if the user approved that exact entry.

The `---VTU_SKILLS---` block is metadata and must not be written into `Internship_Diary.md`.

### Phase 3 - Post-Write Tasks

Run all four tasks in parallel when the runtime supports it. They depend only on the approved entry being appended.

#### 3a. Git Push

Use `.agent/git-push.md`.

- Stage only `Internship_Diary.md`.
- Commit message is exactly the diary date header text without `##`, for example `Monday, February 16th, 2026`.
- Push to `origin main`.
- Never stage context files, agent files, scripts, `AGENTS.md`, `GEMINI.md`, or unrelated edits as part of the diary push.

#### 3b. Obsidian Sync

Use `.agent/obsidian-sync.md`.

- Target file is `Internship Diary.md` in the Obsidian vault.
- Read the vault file when the tool is available and skip if the date header already exists.
- Convert the approved entry to the vault callout format before appending.
- Do not modify local `Internship_Diary.md`.

#### 3c. Context Manager

Use `.agent/context-manager.md`.

- Compare the approved diary entry against the active project file.
- Update only if there are milestone completions, new milestones, tech stack changes, focus shifts, or blocker updates.
- Report `no changes` if the diary entry is routine work within the current focus.

#### 3d. Auto-Fill VTU Portal

Use `.agent/auto-fill.md`.

- Run from the repo root:

```powershell
python auto_fill.py --skills "COMMA_SEPARATED_VTU_SKILLS"
```

- Replace the skills argument with the exact skills extracted from `---VTU_SKILLS---`.
- Omit `--skills` only if no skills were provided.
- Do not pipe input.
- The browser stays open. The user reviews and clicks Submit manually.

### Phase 4 - Report Results

After Phase 3 completes, report:

1. Approved formatted diary entry
2. Git push status
3. Obsidian sync status
4. Context manager status: updated or no changes
5. VTU auto-fill status

## Manual Triggers

### "sync to obsidian" / "push to vault"

- Use `.agent/obsidian-sync.md`.
- Sync the provided entry text, or the latest diary entry if no text is provided.
- Deduplicate by date header before appending.

### "auto fill" / "fill form" / "submit diary"

- Use `.agent/auto-fill.md`.
- Default to the latest diary entry.
- If the user specifies a past date, pass `--date "<substring>"` to `auto_fill.py`.
- The date substring is matched case-insensitively against diary entry headers.

### "switching to [project name]" / "switch project to X"

- This is a context switch only. Do not trigger a diary entry.
- Read `context/personal_context.md` to see the current active project.
- Read `context/projects/_index.md` to find the target project file.
- Update the **Active Project** section in `context/personal_context.md`.
- Confirm: `Switched to [Project Name].`
- Include a brief summary from the new project file: current focus and next milestone.

### "update context" / milestone updates

- Use `.agent/context-manager.md`.
- If context changes are made, commit them by feature set under the Git Commit Convention.
- Do not use the diary-only git-push playbook for non-diary context commits.

### "push" / "git push" / "commit"

- If the user is asking about diary pipeline output, use `.agent/git-push.md`.
- If the user is asking to commit general repo changes, use the Git Commit Convention above and stage only the appropriate feature-set files.

## File Structure

```text
Internship Project/
+-- .agent/                          # Codex/universal role playbooks
|   +-- diary-writer.md
|   +-- git-push.md
|   +-- obsidian-sync.md
|   +-- context-manager.md
|   +-- auto-fill.md
+-- .claude/                         # Claude parallel system
|   +-- agents/
+-- .gemini/                         # Gemini parallel system
|   +-- agents/
|   +-- skills/
|   +-- settings.json
+-- context/
|   +-- personal_context.md
|   +-- projects/
|       +-- _index.md
|       +-- <project>.md
+-- auto_fill.py
+-- diary_manager.py
+-- Internship_Diary.md
+-- AGENTS.md                        # Codex orchestrator
+-- CLAUDE.md                        # Claude orchestrator
+-- GEMINI.md                        # Gemini orchestrator
```

## Global Rules

1. Single-line work updates still trigger the diary workflow.
2. Do not ask the user to elaborate on sparse diary notes.
3. Draft first, get approval, append once, then run downstream tasks.
4. Diary Writer must finish before any post-write task starts.
5. Run independent post-write tasks in parallel when available.
6. Diary git pushes stage only `Internship_Diary.md`.
7. Auto-sync to Obsidian is mandatory after an approved diary append.
8. Auto-fill is mandatory after an approved diary append.
9. Submit stays manual; the script must never click Submit for the user.
10. Report the entry and all four post-write statuses.
11. Keep non-diary repository commits split by feature set.
