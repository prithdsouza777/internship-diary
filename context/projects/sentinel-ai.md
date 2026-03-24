# Project Context — SentinelAI

> **Instructions for AI:** This file represents the "current state" of SentinelAI. Update it when significant milestones are reached or the tech stack changes.

## Project Overview
**Project Name:** SentinelAI
**Description:** Autonomous AI Operations Layer for AWS Connect — 5 specialized AI agents that continuously monitor a contact center, detect anomalies, predict cascade failures, and take real-time action with full human-in-the-loop governance. Built for the CirrusLabs 2026 Internal Buildathon.
**Company:** CirrusLabs (cirruslabs.io)
**Event:** Internal Buildathon 2026 — 1 month, 4-6 person team
**Score:** 19/20 (wow factor, business value, technical depth, feasibility)

## Technical Stack
React 18, TypeScript, Zustand 5, TailwindCSS, shadcn/ui, Aceternity UI, Framer Motion (frontend); Python 3.10, FastAPI, LangGraph (parallel agent orchestration); Anthropic Claude (claude-sonnet-4-20250514, primary) + MockLLM (context-aware fallback); WebSocket (bidirectional real-time); Redis (optional, in-memory fallback); AWS Connect (simulation-first architecture)

## Project Structure
```
Sentinel/
├── frontend/          # React + TypeScript (9 pages)
├── backend/           # FastAPI + Python
│   ├── app/agents/    # 5 AI agents + orchestrator + negotiation
│   ├── app/services/  # simulation, anomaly, bedrock, redis
│   ├── app/api/       # WebSocket + REST routes
│   └── tests/         # 19 passing tests
├── docs/              # Architecture, Context, Status, Tasks, Backlog
└── Sentinel/*.md      # Project reference docs (PRD, README, etc.)
```

## The 5 AI Agents
| Agent | Role |
|-------|------|
| Queue Balancer | Detects staffing imbalances, moves agents between queues |
| Predictive Prevention | Identifies cascade failure signatures before they trigger |
| Escalation Handler | Responds to critical alerts, coordinates resolution |
| Skill Router | Zero-LLM latency skill-based contact routing (weighted scoring) |
| Analytics Agent | Powers natural language queries, incident summaries, what-if analysis |

## AI Governance (Human-in-the-Loop)
- `>= 0.9` confidence → AUTO_APPROVE immediately
- `0.7–0.9` confidence → PENDING_HUMAN (auto-approves after 30s in demo mode)
- `< 0.7` confidence → BLOCKED until human reviews

## Architecture Principles
- **3s tick loop** in `backend/app/main.py` drives simulation + agent orchestration
- **Simulation-First:** demo works entirely without AWS Connect (primary path, not fallback)
- **camelCase on the wire:** always `model_dump(by_alias=True, mode="json")` for WS/REST
- **Singletons:** import `simulation_engine`, `anomaly_engine`, `manager`, `orchestrator` — never instantiate new
- **LLM fallback:** Anthropic Claude → MockLLM (context-aware, dynamic responses from live telemetry)

## Key Milestones & Status
- [x] Week 1: Simulation loop + Queue Balancer + Predictive Prevention agents
- [x] Week 2: All 4 agents, negotiation protocol, cost ticker, approve/reject E2E
- [x] Week 3: Bedrock/MockLLM chat, NL policies, AI Governance overlay, scripted scenarios
- [x] Week 4: Demo polish, 3-minute scripted demo scenario, 19/19 tests passing, 0 TS errors
- [x] Full demo: 9 frontend pages, 5 agents, WebSocket real-time, chaos engine live

## Current Focus / Active Sprint
Project is **demo-ready**. All milestones complete. Focus shifts to:
- Presenting / demoing at the 2026 Buildathon
- Any last-minute polish or bug fixes before the presentation
- Potential real AWS Connect integration (Week 4 bonus — optional)

## Recent Blockers (Context)
- *None recorded — project is demo-complete.*

## The 3-Minute Demo Script
| Phase | Timing | What Happens |
|-------|--------|-------------|
| The Calm | 0:00–0:30 | Normal ops, agents observing, cost $0 |
| The Storm | 0:30–1:15 | Chaos inject: Support 4x spike + General agent dropout |
| The Negotiation | 1:15–1:45 | Queue Balancer vs Escalation Handler conflict, approval prompt |
| The Resolution | 1:45–2:30 | Human approves, metrics stabilize, cost ticker $450→$1,240 |
| The Intelligence | 2:30–3:00 | "What just happened?" → AI incident summary |

## Quick Start
```bash
npm install && npm run dev   # frontend :5173, backend :8000
cd backend && .venv310/Scripts/python.exe -m pytest tests/ -v  # 19 tests
```
Set `ANTHROPIC_API_KEY` in `backend/.env` for live AI (falls back to MockLLM without it).

## Diary Constraints & Evolution
> **Rule:** ensure that no 2 days in a row are similar.
- **Check Previous Context:** Always review the previous entry to ensure today's update is distinct.
- **One Thing at a Time:** Focus on a specific aspect of development per entry (e.g., one agent, one frontend page, a specific bug fix, demo prep) rather than broad repeats.
- **Terminology to use:** agents, tick loop, LangGraph, WebSocket broadcast, chaos injection, guardrails, negotiation protocol, confidence scoring, camelCase serialization, MockLLM, simulation engine
