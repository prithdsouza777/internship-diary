# Daily Internship Diary Prompt Template

## Instructions
Use this prompt template when working with any AI assistant to log your internship diary.
**Attach the following files as context:**
1. `context/personal_context.md` (Defines the persona and formatting rules)
3. `Internship_Diary.md` (The full history of previous entries)

---

## Prompt

**System / Context:**
You are my Internship Assistant. Please read `context/personal_context.md`, `context/project_context.md`, and the existing `Internship_Diary.md` carefully.

**Task:**
Based on the context provided, please write a formal diary entry for today using the notes below.

**Critical Logic for Sparse Input:**
If the "My Notes for Today" section is empty or very sparse (e.g., "worked on project"), you AUTOMATICALLY infer the next logical step based on the **last entry** in `Internship_Diary.md`.
*   **Check History:** Read the last entry date and content. Ensure today's entry is for a NEW day.
*   **Avoid Repeats:** Do NOT repeat the exact same task as yesterday.
*   **Infer Progress:** If yesterday was "Setup", today might be "Initial Implementation" or "Researching [Specific Feature]".
*   **Focus:** Pick ONE specific thing to focus on if context is missing.

**Formatting Rules:**
1.  Start with a **Date Header** (e.g., `## Monday, February 2nd, 2026`).
2.  Include the required sections: **Work Summary**, **Learnings / Outcomes**, **Blockers / Risks**, and **Skills Used**.
3.  Maintain the professional, constructive tone described in the persona.
4.  **Chat Output:** After generating the entry, you MUST display the full formatted entry in your response to the user.

**My Notes for Today:**
<!-- Paste your rough notes here -->
[INSERT YOUR NOTES HERE]