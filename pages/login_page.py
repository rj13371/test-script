from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.submit_button = (By.ID, "login-button")
    
    def open(self, url):
        """Opens the login page."""
        self.driver.get(url)
    
    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()
    
    def login_empty_credentials(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()
        WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-button")))
        
        self.error_button = self.driver.find_elements(By.CLASS_NAME, "error-button")