from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to Chrome for Testing
chrome_path = "/opt/google-chrome-test/chrome"
service = Service("/usr/local/bin/chromedriver")

# Set Chrome options
options = webdriver.ChromeOptions()
options.binary_location = chrome_path

# Start WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open a webpage
driver.get("https://www.google.com")
print(driver.title)

# Close the browser
driver.quit()
