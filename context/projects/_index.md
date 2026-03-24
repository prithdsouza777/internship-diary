# Projects Index

> **Instructions for AI:** This is the project registry. It is NOT read on every diary entry — only consulted when switching projects or adding a new one. The active project is tracked in `context/personal_context.md` under **Active Project**. To switch, update that field and point it to the correct file listed here.

## Active Projects

| Project | File | Brief Description |
|---|---|---|
| Teams Sprint Bot | `context/projects/teams-sprint-bot.md` | Call automation system for Microsoft Teams at Cirruslabs |
| CirrusLabs Financial Dashboard | `context/projects/financial-dashboard.md` | Internal timesheet analytics dashboard — billable/non-billable hours, utilization, P&L reporting |
| SentinelAI | `context/projects/sentinel-ai.md` | Autonomous AI Operations Layer for AWS Connect — 5 AI agents, multi-agent negotiation, real-time chaos simulation, CirrusLabs 2026 Buildathon |
| AI Scrum Bot | `context/projects/ai-scrum-bot.md` | Self-hosted conversational AI assistant for Scrum Masters — Jira/ADO integration, Gemini function calling, SSE streaming, write-back actions with confirmation flow |

## How to Use

- **Diary Writer:** Do NOT read this file during normal diary entries. Read `personal_context.md` → it tells you which project file to load.
- **Switching projects:** Read this index to find the target project's file path, then update the **Active Project** field in `personal_context.md`.
- **Context Manager:** Update only the active project file after a diary entry. Update this index only when a new project is added or one ends.

---

## How to Add a New Project

1. **Create** `context/projects/<project-slug>.md` using this template:

```markdown
# Project Context — [Project Name]

> **Instructions for AI:** This file represents the "current state" of [Project Name]. Update it when significant milestones are reached or the tech stack changes.

## Project Overview
**Project Name:** [Name]
**Description:** [What the project does]

## Technical Stack
[Comma-separated list of tools, languages, frameworks]

## Current Focus / Active Sprint
[What's being actively worked on]

## Key Milestones & Status
- [ ] Milestone 1: [Description]

## Recent Blockers (Context)
- *None recorded yet.*

## Diary Constraints & Evolution
> **Rule:** ensure that no 2 days in a row are similar.
- **Check Previous Context:** Always review the previous entry to ensure today's update is distinct.
- **One Thing at a Time:** Focus on a specific aspect of development per entry rather than broad repeats.
```

2. **Add a row** to the Active Projects table above.

3. **Switch to it** by saying `"switching to [project name]"` — the Active Project field in `personal_context.md` will be updated automatically.
