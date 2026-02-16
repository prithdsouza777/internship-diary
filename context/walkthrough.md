# Internship Diary System - Walkthrough

I have set up the "Internship Diary" system to help us maintain context and a high-quality log over the next 4 months.

## File Structure
All files are located in: `c:\Users\prith\Downloads\Internship Project`

1.  **`context/personal_context.md`**
    *   **Purpose:** Defines *who* I am (the Assistant) and *how* to write the diary entries.
    *   **Key Update:** Now includes strict instructions to always begin entries with a **Date Header** and use neat formatting (bullet points, sections) as requested.

2.  **`context/project_context.md`**
    *   **Purpose:** Tracks the technical "State of the Union" for your specific project.
    *   **Usage:** We will update this file whenever you finish a major milestone or change the tech stack. This ensures I never "forget" what we are building, even 3 months from now.

3.  **`Internship_Diary.md`**
    *   **Purpose:** The persistent log file.
    *   **Format:** Standard Markdown (`.md`), which ensures perfectly clean formatting, code highlighting, and is easy for me to read back to maintain context.

## How We Will Use This
1.  **Daily Update:** You simply tell me "Here's my update for today..." with your notes.
2.  **Context Retrieval:** I will read `context/project_context.md` to remember your tech stack and status.
3.  **Drafting:** I will format your notes into the structure defined in `context/personal_context.md`.
4.  **Logging:** I will append the structured entry to `Internship_Diary.md` with the date.

This system guarantees we won't lose context as the diary grows "way behind my context window" because the *important* context is always condensed in the `context/` folder.
