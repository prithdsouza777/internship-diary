# Project Context — AI Scrum Bot

> **Instructions for AI:** This file represents the "current state" of the AI Scrum Bot project. Update it when significant milestones are reached or the tech stack changes.

## Project Overview
**Project Name:** AI Scrum Bot
**Description:** Self-hosted conversational AI assistant for Scrum Masters. Connects to Jira or Azure DevOps and answers natural-language questions about sprint progress, blockers, backlog health, and feature status. Supports write-back actions (create issues, transition statuses, assign work, add comments) with user confirmation. Responses stream in real-time via SSE with live data fetched on demand via Gemini function calling. Positioned as a self-hosted, customizable alternative to Atlassian Rovo.

## Technical Stack
Python 3.11, FastAPI, async httpx, Pydantic, Google Gemini 3 Flash Preview (google-genai SDK), Server-Sent Events (SSE), React 19, TypeScript, Vite 5, Tailwind CSS v4, Zustand v4, TanStack Query v5, React Router v7, Docker Compose, Google Cloud Run, Google Secret Manager, Jira REST API, Azure DevOps REST API

## Current Focus / Active Sprint
**Phase 2 — Intelligence (Planned)**
- Per-user OAuth 2.0 (Atlassian 3LO) replacing shared API token
- Redis session store for persistent sessions
- Confluence integration — search and read Confluence pages from chat
- Multi-agent architecture — specialized agents (Backlog Groomer, Sprint Planner, Retro Facilitator, Tech Lead, Onboarding Buddy)
- Enhanced sprint panel — health score, scope change tracker, workload bars, burndown mini-chart

## Key Milestones & Status

### Phase 1 — Core (Complete)
- [x] Chat interface with SSE streaming, markdown rendering, quick prompts
- [x] Sprint panel — status breakdown, blockers, in-progress issues, auto-refresh
- [x] Jira read tools (9 tools: boards, sprints, issues, search, blockers, epics)
- [x] Azure DevOps read tools (9 WIQL-based tools)
- [x] Write-back tools (5: create, transition, assign, comment, update)
- [x] Confirmation flow for all write actions (PendingActionStore)
- [x] Multi-provider architecture (BoardProvider protocol)
- [x] Settings page with credential management (localStorage)
- [x] Docker Compose deployment
- [x] Google Cloud Run deployment

### Phase 2 — Intelligence (Planned)
- [ ] OAuth 2.0 per-user auth (Atlassian 3LO)
- [ ] Redis session store
- [ ] Confluence integration
- [ ] Multi-agent architecture (specialized Scrum agents)
- [ ] Enhanced sprint panel (health score, burndown chart)

### Phase 3 — Automation (Planned)
- [ ] Jira webhook engine (real-time cache invalidation)
- [ ] Proactive notification engine (blockers, sprint-at-risk alerts)
- [ ] Deep research mode (25-step analysis)
- [ ] Velocity analytics & trend analysis

### Phase 4 — Ecosystem (Planned)
- [ ] Chrome extension
- [ ] Jira Forge app (native panel)
- [ ] Slack bot (slash commands via Slack Bolt SDK)
- [ ] PDF export & Confluence page publishing

## Recent Blockers (Context)
- *None recorded yet.*

## Key Architecture Notes
- **AI Loop:** Gemini function calling in `gemini_service.py` — max 10 tool iterations per query
- **Streaming:** FastAPI `StreamingResponse` → SSE → frontend `fetch` + `ReadableStream`
- **Session store:** In-memory `ConversationStore` — resets on server restart (Redis planned Phase 2)
- **Cache:** 5-minute TTL in-memory cache on Jira/ADO responses
- **Write safety:** All write actions queue in `PendingActionStore`, execute only after user confirms
- **Provider abstraction:** `BoardProvider` protocol ensures Jira and ADO share the same AI loop

## Diary Constraints & Evolution
> **Rule:** ensure that no 2 days in a row are similar.
- **Check Previous Context:** Always review the previous entry to ensure today's update is distinct.
- **One Thing at a Time:** Focus on a specific aspect of development per entry rather than broad repeats.
