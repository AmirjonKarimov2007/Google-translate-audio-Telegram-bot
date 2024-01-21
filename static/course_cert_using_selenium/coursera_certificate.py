from selenium import webdriver
import requests
import time


NOPECHA_KEY = 'gidmolwlw9yo55k2'  # Replace with your key.

options = webdriver.chrome.options.Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
# Download the latest NopeCHA crx extension file.
# You can also supply a path to a directory with unpacked extension files.
with open('ext.crx', 'wb') as f:
    f.write(requests.get('https://nopecha.com/f/ext.crx').content)
options.add_extension('extension/NopeCHA-CAPTCHA-Solver.crx')

# Start the driver.
driver = webdriver.Chrome(options=options)

# Set the subscription key for the extension by visiting this URL.
# You can programmatically import all extension settings using this method.
# To learn more, go to "Export Settings" in the extension popup.
driver.get(f"https://nopecha.com/setup#{NOPECHA_KEY}")
time.sleep(2)

# Go to any page with a CAPTCHA and the extension will automatically solve it.
driver.get('https://www.google.com/recaptcha/api2/demo')

time.sleep(100)