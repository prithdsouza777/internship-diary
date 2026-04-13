# Project Context — AI Scrum Bot

> **Instructions for AI:** This file represents the "current state" of the AI Scrum Bot project. Update it when significant milestones are reached or the tech stack changes.

## Project Overview
**Project Name:** AI Scrum Bot
**Description:** Self-hosted conversational AI assistant for Scrum Masters. Connects to Jira or Azure DevOps and answers natural-language questions about sprint progress, blockers, backlog health, and feature status. Supports write-back actions (create issues, transition statuses, assign work, add comments) with user confirmation. Responses stream in real-time via SSE with live data fetched on demand via Gemini function calling. Positioned as a self-hosted, customizable alternative to Atlassian Rovo.

## Technical Stack
Python 3.11, FastAPI, async httpx, Pydantic v2, MongoDB + Motor (async), Google Gemini 3 Flash Preview (google-genai SDK >=1.69.0), Server-Sent Events (SSE), Gemini Live (WebSocket — real-time bidirectional audio), React 19, TypeScript ~6.0, Vite 8, Tailwind CSS v4, Zustand v5, TanStack Query v5, React Router v7, MSAL Browser (Azure AD frontend auth), @dnd-kit (drag-and-drop), python-jose (JWT validation via JWKS), cryptography (AES-256-GCM per-user credential encryption), SlowAPI (rate limiting), APScheduler (AsyncIOScheduler — per-board hourly dispatcher), MS Graph API (email reports), Docker Compose, Google Cloud Run, Jira REST API, Azure DevOps REST API

## Current Focus / Active Sprint
**v1 Complete — Phase 2–4 Planned**
All core features, voice, kanban DnD, employee portal, analytics, and per-board scheduling are shipped. Next up:
- **Phase 2 (Intelligence):** Confluence integration, multi-agent architecture, glossary tool, deep research mode
- **Phase 3 (Automation):** Jira webhook engine, additional write tools (bulk update, link issues, move to sprint), custom health dimensions
- **Phase 4 (Ecosystem):** Chrome extension, Jira Forge app, Slack bot, knowledge graph

## Key Milestones & Status

### v1 — Core + Chat + Sprint Panel (Complete)
- [x] Chat interface with SSE streaming, markdown rendering, quick prompts
- [x] Sprint panel — status breakdown, blockers, in-progress issues, auto-refresh
- [x] Jira read tools (9 tools: boards, sprints, issues, search, blockers, epics)
- [x] Azure DevOps read tools (9 WIQL-based tools)
- [x] Write-back tools (6: create, transition, assign, comment, update, log_work)
- [x] Confirmation flow for all write actions (PendingActionStore in MongoDB, TTL 5min)
- [x] Multi-provider architecture (BoardProvider protocol)
- [x] Settings page with credential management (encrypted in MongoDB, not localStorage)

### Auth & Security (Complete)
- [x] Microsoft Entra ID (Azure AD) login via MSAL
- [x] Server-side JWT validation (JWKS, audience/issuer/expiry checks)
- [x] Role-based access control (Scrum Master / Employee portals)
- [x] Per-user encrypted credential storage (AES-256-GCM, PBKDF2-derived keys)
- [x] Rate limiting (SlowAPI — 60/min default, 20/min chat, 5/min reports)
- [x] Input validation, CORS hardening, Nginx security headers (CSP, HSTS, X-Frame-Options)

### Standup & Reporting (Complete)
- [x] Standup tracking with submissions and reminders
- [x] DSU dashboard with completion analytics and email reports
- [x] Blocker alerts, notifications, and auto-escalation (3+ days)
- [x] Email reports via Microsoft Graph API + PDF report generation
- [x] CSV export for standup data

### Retrospectives & Analytics (Complete)
- [x] Retrospective management with action item tracking
- [x] Team health surveys (Spotify Squad Health Check model)
- [x] Burndown chart with daily snapshots
- [x] Velocity analytics (sprint-over-sprint trends)

### Employee Portal (Complete)
- [x] Employee async standup form (submit without chat)
- [x] Employee personal kanban board with drag-and-drop transitions (@dnd-kit)
- [x] Employee personal sprint reports
- [x] Employee self-service (transition issues, assign/update own work items)
- [x] Employee-scoped sprint panel (filtered to logged-in user's assignments)

### Voice — Gemini Live (Complete)
- [x] Employee voice standup via Gemini Live WebSocket (browser → Gemini direct)
- [x] Scrum Master voice chat with full tool access (read + write with confirmation)
- [x] Ephemeral token generation (30-min, single-use)
- [x] Multilingual support — auto-detects user language, responds in same language
- [x] Animated voice orb with state-responsive colors and amplitude tracking

### Kanban Drag-and-Drop (Complete)
- [x] Drag-and-drop issue transitions on employee kanban via @dnd-kit
- [x] DSU confirmation modal on column change (prompts for note)
- [x] Micro-DSU auto-logging — transition note appended to today's standup
- [x] Optimistic UI with 15-second TTL reconciliation
- [x] Provider-aware columns (Jira: To Do/In Progress/In Review/Done; ADO: New/In Progress/Done/Removed)

### Per-Board Scheduling (Complete)
- [x] Single hourly dispatcher replaces hardcoded UTC cron jobs
- [x] Per-board timezone-aware schedule execution (defaults to Asia/Kolkata)
- [x] Multi-hour configuration per job type (e.g., reminders at 9 AM and 2 PM)
- [x] Manager assignment with email resolution — reports sent only to designated managers
- [x] Settings UI with timezone picker, multi-hour tag inputs, manager search/picker

### Deployment (Complete)
- [x] Docker Compose with hardened config (multi-stage builds, non-root users, resource limits)
- [x] Google Cloud Run deployment
- [x] MongoDB-backed conversation persistence (TTL 1hr) and pending actions (TTL 5min)

### Phase 2 — Intelligence (Planned)
- [ ] Confluence integration — search and read Confluence pages from chat
- [ ] Multi-agent architecture (Backlog Groomer, Sprint Planner, Tech Lead, Onboarding Buddy)
- [ ] Glossary tool — company-specific terminology lookup
- [ ] Deep research mode — 25-step analysis for structured reports

### Phase 3 — Automation (Planned)
- [ ] Jira webhook engine (real-time cache invalidation and sprint panel updates)
- [ ] Additional write tools (bulk update, link issues, move to sprint)
- [ ] Custom health dimensions — per-team configurable health check categories

### Phase 4 — Ecosystem (Planned)
- [ ] Chrome extension (floating chat widget, context-aware on Jira pages)
- [ ] Jira Forge app (native panel inside Jira issue/board views)
- [ ] Slack bot (slash commands + threaded conversations via Slack Bolt SDK)
- [ ] Knowledge graph (people/project/document relationship mapping)

## Recent Blockers (Context)
- *None active — all v1 features shipped.*

## Key Architecture Notes
- **AI Loop:** Gemini function calling — max 10 tool iterations per query, semaphore (10 concurrent calls), retry with exponential backoff
- **Streaming:** FastAPI `StreamingResponse` → SSE with heartbeat keep-alive → frontend `fetch` + `ReadableStream`
- **Voice:** Gemini Live WebSocket (browser → Gemini direct), ephemeral tokens, Flash Lite handoff for standup intents
- **Session store:** MongoDB-backed conversations (TTL 1hr) — persists across restarts, no Redis needed
- **Cache:** 5-minute TTL in-memory cache on Jira/ADO responses
- **Write safety:** All write actions queue in `PendingActionStore` (MongoDB, TTL 5min), execute only after user confirms
- **Provider abstraction:** `BoardProvider` protocol ensures Jira and ADO share the same AI loop
- **Auth:** Azure AD JWT validation (JWKS), per-user encrypted credentials (AES-256-GCM), role-based access
- **Scheduling:** APScheduler hourly dispatcher with per-board timezone-aware execution, manager-targeted reports
- **Per-user isolation:** Each user's provider, credentials, and board context stored in MongoDB — no global singletons

## Diary Constraints & Evolution
> **Rule:** ensure that no 2 days in a row are similar.
- **Check Previous Context:** Always review the previous entry to ensure today's update is distinct.
- **One Thing at a Time:** Focus on a specific aspect of development per entry rather than broad repeats.
