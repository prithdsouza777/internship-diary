# Project Context — Teams Sprint Bot

> **Instructions for AI:** This file represents the "current state" of the Teams Sprint Bot project. Update it when significant milestones are reached or the tech stack changes.

## Project Overview
**Project Name:** Teams Sprint Bot
**Description:** A Microsoft Teams bot that automates daily standup meetings using Gemini AI, with dual standup modes (text chat-based and voice via Azure Communication Services). Supports task assignment, proactive scheduled standups, role-based UI, and per-participant coverage tracking. Version 2.0.0.

## Technical Stack
FastAPI + Uvicorn, botbuilder-python, Gemini 3 Flash Preview (structured output), MongoDB (Motor/PyMongo), Firestore (three-tier state fallback), AWS Polly Neural (Matthew voice), Azure Communication Services, Adaptive Cards 1.5, GCP Cloud Run + Cloud Build, Docker, Python 3.13, pydantic-settings, loguru

## Architecture Summary

**Request flow:** Teams messages -> POST /api/messages -> AiohttpRequestWrapper shim -> TeamsBot activity handler -> agent orchestrator (app/agent/graph.py) runs the standup state machine.

**Voice call flow:** Scrum Master triggers "Voice Standup" -> creates ACS group call -> participants join via browser link -> ACS webhooks at /api/voice/callbacks drive the call state machine (greeting -> per-participant Q&A via speech recognition -> summary) -> voice summary card sent to Teams chat.

**Standup flow:** User says "start standup" -> look up user -> check pending tasks -> create AgentState -> run_standup_agent() loops through participants: identify speaker -> fetch tasks -> ask question -> process answer (update MongoDB, track coverage) -> follow-up if tasks remain -> advance to next participant -> summarize when done.

**Task assignment:** Scrum Master triggers "assign task" -> form card -> natural language parsed by Gemini to JSON -> validate assignee in MongoDB -> create_task_for_user() -> confirmation card.

**Proactive standup:** Cloud Scheduler hits /api/scheduled-standup at 9:30 AM IST Mon-Fri -> notify_all_teams() -> sends reminder to each team.

## Current Focus / Active Sprint
Production hardening, deployment refinement, and voice standup polish (v2.0.0 feature-complete)

## Key Milestones & Status
- [x] Milestone 1: Project Introduction
- [x] Milestone 2: Setup & Onboarding
- [x] Milestone 3: Cloud Deployment & Backend Infrastructure (GCP Cloud Run + Cloud Build)
- [x] Milestone 4: Text-based Standup Flow (agent state machine, task coverage tracking, Gemini AI integration)
- [x] Milestone 5: MongoDB CRUD & User/Task Management
- [x] Milestone 6: Adaptive Cards UI & Role-based Flows (12 card factories, Scrum Master vs Member UI)
- [x] Milestone 7: Proactive Scheduled Standups (Cloud Scheduler integration)
- [x] Milestone 8: Voice Standup via Azure Communication Services (ACS calls, speech recognition, TTS with AWS Polly)
- [x] Milestone 9: Firestore Three-tier State Management (memory -> Firestore -> file fallback)
- [ ] Milestone 10: Production Hardening & Final Polish

## Recent Blockers (Context)
- *None recorded.*

## Diary Constraints & Evolution
> **Rule:** ensure that no 2 days in a row are similar.
- **Check Previous Context:** Always review the previous entry to ensure today's update is distinct.
- **One Thing at a Time:** Focus on a specific aspect of development per entry rather than broad repeats.
