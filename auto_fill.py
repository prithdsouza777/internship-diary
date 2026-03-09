import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import diary_manager
from selenium.webdriver.support.ui import Select
from datetime import date, datetime
import re

load_dotenv()

def parse_entry_date(date_str):
    """Parse diary date string like 'Monday, March 9th, 2026' into a date object."""
    # Remove ordinal suffixes (1st, 2nd, 3rd, 4th, etc.)
    cleaned = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
    try:
        return datetime.strptime(cleaned.strip(), "%A, %B %d, %Y").date()
    except ValueError:
        try:
            return datetime.strptime(cleaned.strip(), "%B %d, %Y").date()
        except ValueError:
            print(f"Warning: Could not parse diary date '{date_str}', defaulting to today.")
            return date.today()

def clean_text(text):
    """Removes bullet points and formatting like * or - or ** from the text."""
    if not text:
        return ""
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        # Remove all leading bullets/stars
        while line.startswith('*') or line.startswith('-'):
            line = line[1:].strip()
        # Remove bold formatting anywhere in the line
        line = line.replace('**', '')
        # Remove italics if simple * used (optional but safe)
        if line.startswith('_'):
             line = line.lstrip('_').rstrip('_')
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

# --- CONFIGURATION ---
URL = "https://vtu.internyet.in/dashboard/student/create-diary-entry"
DIARY_FILE = "Internship_Diary.md"
EMAIL = os.getenv("VTU_EMAIL")
PASSWORD = os.getenv("VTU_PASSWORD")

def main():
    if not EMAIL or not PASSWORD:
        print("Error: VTU_EMAIL and VTU_PASSWORD must be set in .env file.")
        print("Copy .env.example to .env and fill in your credentials.")
        return

    # 1. Parse Data
    print("Reading diary entries...")
    entries = diary_manager.get_all_entries(DIARY_FILE)

    if not entries:
        print("Error: No entries found in diary.")
        return

    # User requested to ignore Wednesday entry for now.
    # We will pick the latest one, but if the file hasn't been saved/updated, it might be the Tuesday one.
    # To be safe, we just take the last one as per standard operation,
    # assuming the user controls the file content.
    entry_data = entries[-1]

    print(f"\nAuto-selecting latest entry: {entry_data['date']}")
    print("-" * 20)

    # 2. Launch Browser
    print("Launching Chrome...")
    # Using Key error handling to fall back or guide user if drivers missing
    try:
        # Trying Chrome first as it's most common
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        print(f"Could not launch Chrome: {e}")
        print("Please ensure you have Selenium and a WebDriver (Auto-installer? or standard path installed).")
        return

    try:
        driver.get(URL)
        print("Opened page.")

        # --- LOGIN LOGIC ---
        # 3. Attempt to Fill Email & Password
        print("Checking for Login Page...")
        try:
            # Based on HTML analysis:
            # Email: <input ... autocomplete="email" ...>
            # Password: <input ... name="password" ...>
            # Button: <button ... type="submit">Sign In</button>

            print("Looking for email field...")
            email_field = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[autocomplete='email']"))
            )
            email_field.clear()
            email_field.send_keys(EMAIL)
            print("Auto-filled Email.")

            if PASSWORD:
                print("Looking for password field...")
                password_field = driver.find_element(By.NAME, "password")
                password_field.clear()
                password_field.send_keys(PASSWORD)
                print("Auto-filled Password.")

                # Attempt to find and Click Login Button
                print("Attempting to click Login button...")
                try:
                    # Specific selector from HTML: button[type='submit'] with text Sign In
                    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
                    login_btn.click()
                    print("Clicked Login Button.")
                except:
                    print("Could not find Login button. Trying Enter key on password field.")
                    password_field.send_keys(Keys.ENTER)
            else:
                 print("Password variable is empty. Please enter password manually.")

        except Exception as e:
            print(f"Login field detection failed: {e}")
            print("Assuming already logged in OR selectors changed. Please Login manually.")

        # 4. Wait for Login completion & Navigate to Diary
        print("Waiting for Dashboard/Sidebar...")
        try:
            # Wait for URL to change or sidebar to appear
            time.sleep(3)

            # Click "Internship Diary" in sidebar
            print("Navigating to 'Internship Diary'...")
            sidebar_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Internship Diary"))
            )
            sidebar_link.click()
            print("Clicked 'Internship Diary'.")

            # If it's a menu that expands, we might need to click a sub-item.
            # Assuming it goes straight to the page or we need to click "Create Entry"
            # Let's wait a bit to see if we are on the form.
            time.sleep(2)

        except Exception as e:
            print(f"Navigation failed: {e}")
            print("Please navigate manually to the 'Create Diary Entry' page.")

        # Removed manual pause to fully automate
        # input("Press Enter to continue...")

        # --- FORM SELECTION LOGIC ---

        # 5. Select 'Cirrus labs' (Project Selection)
        print("Attempting to select 'Cirrus labs'...")
        try:
            # Custom UI Dropdown Logic
            # 1. Click the trigger button
            print("Clicking Project dropdown...")
            project_trigger = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "internship_id"))
            )
            project_trigger.click()

            # 2. Wait for option to appear and click it
            print("Waiting for 'Cirruslabs' option...")
            # Look for div/span with text inside the dropdown portal
            cirrus_option = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Cirruslabs')] | //span[contains(text(), 'Cirruslabs')]"))
            )
            cirrus_option.click()
            print("Selected 'Cirrus labs'.")

        except Exception as e:
            print(f"Could not select 'Cirrus labs': {e}")
            print("Please select Project manually.")

        # 6. Select Date from Diary Entry
        print("Attempting to select date from diary entry...")
        try:
            # Parse the date from the diary entry itself
            entry_date = parse_entry_date(entry_data['date'])
            print(f"Parsed diary date: {entry_date} (day={entry_date.day}, month={entry_date.month}, year={entry_date.year})")

            # 1. Click the "Pick a Date" button/trigger
            print("Clicking Date picker...")
            try:
                date_trigger = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-slot='popover-trigger']"))
                )
                date_trigger.click()
            except Exception as e:
                print(f"Could not find Date trigger: {e}")
                try:
                    date_trigger = driver.find_element(By.XPATH, "//button[contains(., 'Pick a Date')]")
                    date_trigger.click()
                except:
                    pass

            time.sleep(1)

            # 2. Navigate to the correct month/year if needed
            target_year = entry_date.year
            target_month = entry_date.month
            for _ in range(24):  # max 24 navigation attempts
                try:
                    cal_header = driver.find_element(
                        By.CSS_SELECTOR,
                        "div[role='dialog'] button[name='view_date'], "
                        "[data-slot='caption-label'], "
                        ".rdp-caption_label"
                    )
                    header_text = cal_header.text.strip()
                except Exception:
                    header_text = ""

                current_cal_date = None
                try:
                    current_cal_date = datetime.strptime(header_text, "%B %Y").date().replace(day=1)
                except ValueError:
                    pass

                if current_cal_date and (current_cal_date.year, current_cal_date.month) == (target_year, target_month):
                    break

                if current_cal_date:
                    if (target_year, target_month) < (current_cal_date.year, current_cal_date.month):
                        try:
                            prev_btn = driver.find_element(
                                By.CSS_SELECTOR,
                                "button[name='previous-month'], "
                                "button[aria-label='Go to previous month'], "
                                ".rdp-nav_button_previous"
                            )
                            prev_btn.click()
                        except Exception:
                            break
                    else:
                        try:
                            next_btn = driver.find_element(
                                By.CSS_SELECTOR,
                                "button[name='next-month'], "
                                "button[aria-label='Go to next month'], "
                                ".rdp-nav_button_next"
                            )
                            next_btn.click()
                        except Exception:
                            break
                else:
                    break
                time.sleep(0.3)

            # 3. Click the correct day
            day_num = str(entry_date.day)
            print(f"Selecting day '{day_num}' in calendar...")
            try:
                day_btn = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, f"//div[@role='dialog']//button[text()='{day_num}'] | //button[text()='{day_num}' and @role='gridcell']"))
                )
                day_btn.click()
                print(f"Clicked day '{day_num}'.")
            except Exception as e:
                print(f"Could not click day '{day_num}' in calendar: {e}")
                print("Trying method 2: aria-current='date'...")
                try:
                    today_cell = driver.find_element(By.CSS_SELECTOR, "[aria-current='date']")
                    today_cell.click()
                    print("Clicked today as fallback.")
                except Exception:
                    print("Manual Date selection required.")
                    time.sleep(2)

        except Exception as e:
            print(f"Could not interact with Date picker: {e}. Please verify manually.")

        # --- IMPORTANT: CLICK CONTINUE ---
        print("Attempting to click 'Continue'...")
        try:
            # Wait for button to be enabled
            time.sleep(1.0)
            continue_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue') and @type='submit']"))
            )
            continue_btn.click()
            print("Clicked 'Continue'.")
        except Exception as e:
            print(f"Could not click 'Continue': {e}")
            print("Please click 'Continue' manually.")


        # 7. Fill 'Work Done' (name="description")
        print("Waiting for 'Work Done' field (name='description')...")
        description_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "description"))
        )
        description_field.clear()
        cleaned_work_done = clean_text(entry_data['work_done'])
        description_field.send_keys(cleaned_work_done)
        print("Filled 'Work Done'.")

        # 8. Fill 'Learnings' (name="learnings")
        try:
            learnings_text = clean_text(entry_data.get('learnings', ''))
            learnings_field = driver.find_element(By.NAME, "learnings")
            learnings_field.clear()
            learnings_field.send_keys(learnings_text)
            print("Filled 'Learnings'.")
        except:
             print("Field 'learnings' not found via Name. Skipping.")

        # 9. Fill 'Number of Hours' -> "10"
        try:
            # Look for number input or label "Hours"
            hours_field = driver.find_element(By.XPATH, "//input[@type='number'] | //label[contains(., 'Hours')]/following-sibling::input")
            hours_field.clear()
            hours_field.send_keys("10")
            print("Filled 'Hours' with 10.")
        except Exception as e:
            print(f"Could not fill Hours: {e}")

        # 10. Fill 'Blockers' (name="blockers") -> Default "None"
        try:
            blockers_text = clean_text(entry_data.get('blockers', ''))
            # Check if empty string or just whitespace, or specific "none" phrases
            normalized_blockers = blockers_text.strip().lower()
            if (not normalized_blockers or
                normalized_blockers == "none" or
                "none recorded" in normalized_blockers or
                "none reported" in normalized_blockers):
                blockers_text = "None"

            blockers_field = driver.find_element(By.NAME, "blockers")
            blockers_field.clear()
            blockers_field.send_keys(blockers_text)
            print(f"Filled 'Blockers' with '{blockers_text}'.")
        except:
             print("Field 'blockers' not found.")

        # 11. Fill 'Skills Used'
        # Per user request: Skills used should always remain empty.
        print("Skipping 'Skills Used' as requested (leaving empty).")

        print("-" * 20)
        print("Done! Form is filled. Please review and hit Submit.")
        print("Browser will remain open. Close it manually when you're done.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Browser will remain open. Please complete the form manually.")

if __name__ == "__main__":
    main()
