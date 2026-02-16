import re
import os

DIARY_FILE = "Internship_Diary.md"

def get_all_entries(file_path):
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex to split entries by Date Header (## ...)
    entry_pattern = r"(## .*?)(?=\n## |\Z)"
    raw_entries = re.findall(entry_pattern, content, re.DOTALL)
    
    parsed_entries = []
    
    # Helper to extract section
    def extract_section(header, text):
        pattern = re.escape(header) + r"\s*\n(.*?)(?=\n### |\Z)"
        match = re.search(pattern, text, re.DOTALL)
        return match.group(1).strip() if match else ""

    for raw_entry in raw_entries:
        # Extract Date
        date_match = re.search(r"## (.*)", raw_entry)
        date = date_match.group(1).strip() if date_match else "Unknown Date"
        
        parsed_entries.append({
            "date": date,
            "work_done": extract_section("### What I worked on?", raw_entry),
            "learnings": extract_section("### Learnings / Outcomes", raw_entry),
            "blockers": extract_section("### Blockers / Risks", raw_entry),
            "skills": extract_section("### Skills Used", raw_entry)
        })
        
    return parsed_entries

def parse_latest_entry(file_path):
    entries = get_all_entries(file_path)
    if not entries:
        return {"error": "No entries found."}
    return entries[-1]

if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), DIARY_FILE)
    data = parse_latest_entry(file_path)
    
    print("-" * 30)
    print(f"LATEST ENTRY PARSED ({data.get('date')})")
    print("-" * 30)
    print(f"WORK DONE:\n{data.get('work_done')}\n")
    print(f"LEARNINGS:\n{data.get('learnings')}\n")
    print(f"SKILLS:\n{data.get('skills')}\n")
    print(f"BLOCKERS:\n{data.get('blockers')}\n")
    print("-" * 30)
