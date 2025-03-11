from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by, keys

from drivers import chrome_path
# Path to Chrome for Testing
chrome_path = "/opt/google-chrome-test/chrome"
service = Service("/usr/local/bin/chromedriver")

# Set Chrome options
options = webdriver.ChromeOptions()
options.binary_location = chrome_path

# Start WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open a webpage
driver.get("https://ats.rippling.com/playeveryware-careers/jobs/224afeb8-189e-4c29-82ef-27f31f72cf6b/apply?step=application")
element = driver.find_element(by.By.CSS_SELECTOR, "[data-input='first_name']")

element.send_keys("Test input")
element.send_keys(keys.Keys.RETURN)  # Press Enter (if needed)

print(element)

driver.close()