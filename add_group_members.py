from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Ensure correct path to your ChromeDriver

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for manual login
input("Press Enter after scanning the QR code and WhatsApp Web is fully loaded...")

# List of phone numbers to add
phone_numbers = [
    "94718726588",
]

# Update phone numbers
# add contry code to the begining of the phone number
# phone_numbers = ["94" + number[1:]
#                  if number.startswith("0") else number for number in phone_numbers]

# add your group name here
group_name = "your group name"

try:
    # Search for the group by name
    search_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@contenteditable='true'][@data-tab='3']"))
    )
    search_box.click()
    search_box.clear()
    search_box.send_keys(group_name)
    time.sleep(2)

    # Click on the group chat
    group_chat = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//span[@title='{group_name}']"))
    )
    group_chat.click()
    time.sleep(2)

    # Open group info
    group_info_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@role='button' and @class='_amie']"))
    )
    group_info_button.click()
    time.sleep(2)
    # _ak72 _ak73 _ak76 _ak77
    # Click on add user
    add_user_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(

            (By.XPATH, "//div[@role='button' and contains(@class, '_ak72') and contains(@class, '_ak73') and contains(@class, '_ak77')]"))
    )
    add_user_button.click()
    time.sleep(2)

    # Locate the new search box for adding users
    search_contact_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@contenteditable='true'][@aria-label='Search input textbox']"))
    )

    # Add participants by phone number
    for number in phone_numbers:
        search_contact_box.click()
        search_contact_box.clear()
        search_contact_box.send_keys(number)
        time.sleep(2)

        try:
            # Click on the first user element that appears in search results
            user_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, '_ak72') and contains(@class, '_ak75')]"))
            )
            user_element.click()
            time.sleep(1)
            # Click the Cancel search button to clear the input
            cancel_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(@class, '_ah_y')]"))
            )
            cancel_button.click()
            time.sleep(1)
        except Exception as e:
            print(f"Could not find user for {number}: {e}")

    # Click the Next button to add participants
    next_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@data-icon='checkmark-medium']"))
    )
    next_button.click()
    time.sleep(2)
    # Click the Add Members button
    add_members_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class, 'x889kno') and contains(., 'Add members')]"))
    )
    add_members_button.click()
    time.sleep(20)

    print("Members added to the group successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
