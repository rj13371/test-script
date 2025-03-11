from selenium.webdriver.common.by import By

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