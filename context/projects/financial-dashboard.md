# Project Context — CirrusLabs Financial Dashboard

> **Instructions for AI:** This file represents the "current state" of the CirrusLabs Financial Dashboard project. Update it when significant milestones are reached or the tech stack changes.

## Project Overview
**Project Name:** CirrusLabs Financial Dashboard
**Description:** Internal timesheet analytics dashboard for CirrusLabs. Tracks employee billable/non-billable hours, utilization rates, manager reporting, and P&L ownership. Replaces manual spreadsheet reporting with an interactive analytics layer on top of SQLite timesheet data.

## Technical Stack
Next.js 15 (App Router), React 19, TypeScript, Tailwind CSS v3, shadcn/ui (Radix-based), SQLite via `better-sqlite3`, Recharts + shadcn `ChartContainer`, jspdf + jspdf-autotable, react-hook-form + zod, next-themes

## Architecture Overview
- **Database:** Single SQLite table `timesheet_entries` — server-side only via API routes
- **API layer:** `app/api/` — Next.js route handlers calling `lib/queries.ts`
- **Client hooks:** `hooks/use-dashboard-data.ts` — `useDashboardData<T>(endpoint, params)` pattern
- **Shared components:** `components/shared/` (MetricCard, ChartCard, FilterBar, LoadingSkeleton, PdfExportButton)
- **UI primitives:** `components/ui/` (shadcn/ui), `components/kokonutui/` (Layout, Sidebar, TopNav)
- **Lib:** `lib/db.ts`, `lib/queries.ts`, `lib/types.ts`, `lib/format.ts`, `lib/pdf-export.ts`

## Pages / Routes
| Route | Purpose |
|---|---|
| /dashboard | KPI overview — total hours, billable, utilization, charts |
| /analytics | Tabbed deep-dive: Trends / Distribution / Monthly |
| /projects | Task/project drill-down with detail view |
| /transactions | Paginated raw timesheet table with sort/filter |
| /members | People-centric view — employees, managers, headcount |
| /permissions | Utilization rate analysis by employee/manager/month |
| /search | Global search across employees, managers, tasks |

## Key Milestones & Status
- [ ] Dashboard page — KPI cards, monthly charts, manager/P&L breakdowns
- [ ] Analytics page — Trends, Distribution, Monthly tabs with PDF export
- [ ] Projects page — task list + drill-down detail view
- [ ] Transactions page — paginated table with sorting and filtering
- [ ] Team (Members) page — employee cards, manager breakdowns
- [ ] Utilization page — group-by selector, color-coded rate bars
- [ ] Search page — debounced global search, grouped results
- [ ] Filter bar — shared across all pages, dismissible chips, live DB options
- [ ] PDF export — per-page export with title, filters, KPI summary, tables
- [ ] Dark/light theme — via next-themes

## Recent Blockers (Context)
- *None recorded yet.*

## Diary Constraints & Evolution
> **Rule:** ensure that no 2 days in a row are similar.
- **Check Previous Context:** Always review the previous entry to ensure today's update is distinct.
- **One Thing at a Time:** Focus on a specific aspect of development per entry (e.g., one page, one feature, one bug) rather than broad repeats.
- **PRD Reference:** Feature requirements are in `PRD.md`. Architecture patterns are in `CLAUDE-fdd.md`.
