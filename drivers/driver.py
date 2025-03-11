from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver():
    """Initialize and return a WebDriver instance."""
    
    chrome_path = "/opt/google-chrome-test/chrome"

    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path
    options.add_argument("--incognito")  # Open in incognito mode
   
    # Initialize WebDriver
    service = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver