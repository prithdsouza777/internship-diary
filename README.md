# Internship Diary System

An AI-powered internship diary automation system that generates structured daily diary entries, syncs them across platforms, and auto-fills the VTU internship portal.

## What It Does

1. **Diary Generation** - Takes short daily work notes and expands them into structured diary entries using AI (Claude Code / Gemini CLI)
2. **VTU Portal Auto-Fill** - Uses Selenium to automatically log in and fill the VTU internship diary form at `vtu.internyet.in`
3. **Obsidian Sync** - Syncs entries to an Obsidian vault for personal knowledge management
4. **Git Auto-Push** - Commits and pushes diary updates to the repository automatically

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

# Install Python dependencies
pip install selenium python-dotenv
```

### Credentials

The VTU portal auto-fill script requires your login credentials. These are stored in a `.env` file that is **not committed to git**.

```bash
# Copy the example file
cp .env.example .env
```

Then edit `.env` and fill in your values:

```
VTU_EMAIL=your_usn.name@college.ac.in
VTU_PASSWORD=your_password_here
```

## Usage

### With Claude Code

Run `claude` in the project directory. Any work update you type triggers the full pipeline automatically:

```
> worked on API integration today
```

This will:
- Generate a formatted diary entry and append it to `Internship_Diary.md`
- Commit and push to git
- Sync to Obsidian vault
- Auto-fill the VTU portal form

### Running Auto-Fill Standalone

```bash
python auto_fill.py
```

This reads the latest entry from `Internship_Diary.md` and fills the VTU portal form. Make sure your `.env` file is set up first.

### Running the Diary Parser

```bash
python diary_manager.py
```

Parses and displays the latest entry from `Internship_Diary.md`.

## Project Structure

```
Internship Project/
├── .claude/agents/          # Claude Code sub-agent prompts
├── .gemini/skills/          # Gemini CLI equivalent skills
├── context/
│   ├── personal_context.md  # AI persona & formatting rules
│   ├── project_context.md   # Current project state & milestones
│   └── obsidian_context.md  # Obsidian vault sync rules
├── auto_fill.py             # Selenium VTU portal form filler
├── diary_manager.py         # Diary entry parser
├── Internship_Diary.md      # Main diary file (source of truth)
├── .env.example             # Credential template (copy to .env)
├── .env                     # Your credentials (git-ignored)
├── CLAUDE.md                # Claude Code orchestrator config
└── GEMINI.md                # Gemini CLI orchestrator config
```

## Notes

- `Internship_Diary.md` is the source of truth for all entries
- The `.env` file is in `.gitignore` and will never be committed
- Chrome WebDriver is managed automatically by Selenium 4+
