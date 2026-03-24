# Internship Diary System

An AI-powered internship diary automation system that generates structured daily diary entries, syncs them across platforms, and auto-fills the VTU internship portal. Supports **multiple projects** — switch between them with a single command.

## What It Does

1. **Diary Generation** - Takes short daily work notes and expands them into structured diary entries using AI (Claude Code / Gemini CLI)
2. **Multi-Project Support** - Track multiple internship projects; switch active project at any time
3. **VTU Portal Auto-Fill** - Uses Selenium to automatically log in and fill the VTU internship diary form at `vtu.internyet.in`
4. **Obsidian Sync** - Syncs entries to an Obsidian vault for personal knowledge management
5. **Git Auto-Push** - Commits and pushes diary updates to the repository automatically
6. **Context Management** - Automatically updates project context files when milestones or tech stack changes are detected

## How It Works

When you type a work update (e.g. `"worked on API integration"`), the AI orchestrator runs a four-step pipeline:

1. **Read context** — loads your persona, the active project file, and the last two diary entries for continuity
2. **Generate entry** — expands your raw notes into a structured diary entry and appends it to `Internship_Diary.md`
3. **Four tasks run in parallel** — git commit & push, Obsidian vault sync, project context update (if milestones changed), and VTU portal auto-fill
4. **Report** — shows you the formatted entry and the status of all four tasks

The orchestrator is configured for both **Claude Code** (`CLAUDE.md`) and **Gemini CLI** (`GEMINI.md`) — use whichever you prefer.

## Multi-Project Support

The system supports multiple concurrent projects. Each project has its own context file tracking tech stack, milestones, and current focus.

### Switching Projects

```
> switching to CirrusLabs Financial Dashboard
```

This updates `context/personal_context.md` to point to the new project. All future diary entries will use that project's context.

### Adding a New Project

1. Create `context/projects/<project-slug>.md` using the template in `context/projects/_index.md`
2. Add a row to the Active Projects table in `_index.md`
3. Switch to it with `"switching to [project name]"`

### Current Projects

See [`context/projects/_index.md`](context/projects/_index.md) for the full list of active projects.

## Setup

### Prerequisites

- Python 3.8+
- Google Chrome (for Selenium auto-fill)
- [Claude Code](https://claude.com/claude-code) or [Gemini CLI](https://github.com/google-gemini/gemini-cli) as the AI orchestrator

### Installation

```bash
# Clone the repo
git clone <repo-url>
cd "Internship Project"

# Create and activate a virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Credentials

The VTU portal auto-fill script requires your login credentials. These are stored in a `.env` file that is **not committed to git**.

```bash
cp .env.example .env
```

Then edit `.env` and fill in your values:

```
VTU_EMAIL=your_usn.name@college.ac.in
VTU_PASSWORD=your_password_here
```

## Usage

### Logging a diary entry (full pipeline)

Run `claude` (or `gemini`) in the project directory. Any work update triggers the full pipeline:

```
> worked on API integration today
> deployed the bot to Azure
> did compliance training and documentation
```

All four post-write tasks (git push, Obsidian sync, context update, VTU auto-fill) run automatically in parallel.

### Manual commands

| Command | What it does |
|---|---|
| `switching to [project name]` | Switch active project |
| `sync to obsidian` | Re-sync latest entry to Obsidian vault |
| `auto fill` / `fill form` | Run `auto_fill.py` standalone |
| `push` / `git push` | Commit and push `Internship_Diary.md` |
| `update context` | Trigger context manager manually |

### Running scripts standalone

```bash
# Auto-fill VTU portal with the latest diary entry
python auto_fill.py

# Parse and display the latest diary entry
python diary_manager.py
```

## Project Structure

```
Internship Project/
├── .claude/
│   └── agents/
│       ├── diary-writer.md      # Diary Writer sub-agent
│       ├── git-push.md          # Git Push sub-agent
│       ├── obsidian-sync.md     # Obsidian Sync sub-agent
│       ├── context-manager.md   # Context Manager sub-agent
│       └── auto-fill.md         # VTU Auto-Fill sub-agent
├── .gemini/
│   └── skills/                  # Gemini CLI equivalent skills
├── context/
│   ├── personal_context.md      # AI persona, formatting rules, active project pointer
│   └── projects/
│       ├── _index.md            # Project registry + add-project template
│       ├── _index.md            # Project registry (source of truth)
│       └── <project>.md         # One file per project
├── auto_fill.py                 # Selenium VTU portal form filler
├── diary_manager.py             # Diary entry parser
├── Internship_Diary.md          # Main diary file (source of truth)
├── .env.example                 # Credential template (copy to .env)
├── .env                         # Your credentials (git-ignored)
├── .venv/                       # Virtual environment (git-ignored)
├── requirements.txt             # Python dependencies
├── CLAUDE.md                    # Claude Code orchestrator config
└── GEMINI.md                    # Gemini CLI orchestrator config
```

## Notes

- `Internship_Diary.md` is the source of truth — Obsidian vault and VTU portal are downstream consumers
- Only `Internship_Diary.md` is committed on each diary entry; context files are committed separately when updated
- The `.env` file is in `.gitignore` and will never be committed
- Chrome WebDriver is managed automatically by Selenium 4+
- To add a new project, see the template and instructions in `context/projects/_index.md`
