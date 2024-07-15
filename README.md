# WhatsApp Group Member Adder

This script automates the process of adding members to a WhatsApp group using Selenium. It allows you to add participants by their phone numbers.

## Requirements

- Python 3.x
- Selenium
- Google Chrome
- ChromeDriver

## Installation

### Step 1: Install Python

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
### Step 2: Install ChromeDriver
1. Check your version of Google Chrome by going to chrome://settings/help
2. Download the corresponding version of ChromeDriver from the ChromeDriver download page.
3. Extract the downloaded file and move it to a directory in your PATH using the following commands:
```bash
sudo mv chromedriver /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
```
### Step 3: Install Selenium

You can install Selenium using pip. Open your terminal or command prompt and run:

```bash
pip install selenium
```
### Step 4: Update phone numbers list
1. Replace the placeholder your group name with the actual name of your WhatsApp group in the script.
```python
group_name = "your group name"
```
2. Update the phone_numbers list with the phone numbers you want to add. Ensure that the numbers are in the format with country code (e.g., 94718726588).
```python
phone_numbers = [
    "94718726588",
    # Add more numbers here
]

```
### Step 5: Run the Script

1. Open a terminal or command prompt in the directory where your script is located.

2. Run the script using Python:
```bash
python add_group_members.py
```
3. Scan the QR code to log in to WhatsApp Web when prompted. Once the QR code is scanned and WhatsApp Web is loaded, press Enter to continue.

## Important Notes

- Ensure that your ChromeDriver path is correctly set in the script if it’s not in your system’s PATH.
- This script requires the WhatsApp group to be already created and accessible in your WhatsApp account.
- Be mindful of WhatsApp's terms of service and avoid spamming users.

## Troubleshooting

If you encounter issues:

- Ensure your ChromeDriver version matches your installed Google Chrome version.
- Check the XPath selectors if WhatsApp Web layout changes.
- Make sure you have an active internet connection.


# WhatsApp-Group-Member-Adder
# WhatsApp-Group-Member-Adder
# WhatsApp-Group-Member-Adder
