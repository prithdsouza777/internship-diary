import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import diary_manager
from selenium.webdriver.support.ui import Select
from datetime import date

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
PASSWORD = "Pritham1*" 

def main():
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
        # options.add_argument("--start-maximized")
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
            email_field.send_keys("22i45.pritham@sjec.ac.in")
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

        # 6. Select Today's Date
        print("Attempting to select Today's Date...")
        try:
            # Custom Date Picker Logic
            # 1. Click the "Pick a Date" button/trigger
            print("Clicking Date picker...")
            try:
                 # Use the specific data attribute from the HTML
                 date_trigger = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-slot='popover-trigger']"))
                 )
                 date_trigger.click()
            except Exception as e:
                 print(f"Could not find Date trigger: {e}")
                 # Fallback (mostly for debug)
                 try:
                    date_trigger = driver.find_element(By.XPATH, "//button[contains(., 'Pick a Date')]")
                    date_trigger.click()
                 except: pass

            # 2. Select Today
            print("Selecting today in calendar...")
            day_num = str(date.today().day)
            
            try:
                # Wait for the popover/calendar to appear
                time.sleep(1) 
                
                # Try finding a button with the exact text of the day number
                # This is common in Shadcn/Radix calendars (e.g. <button ...>4</button>)
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
                    print("Clicked today loop fallback.")
                except:
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
        
        # Keep browser open for user to review
        input("Press Enter to close browser...")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
