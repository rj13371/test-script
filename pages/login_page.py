from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver) -> None:

        """
        Initializes the LoginPage object.

        :param driver: WebDriver instance that interacts with the browser
        """

        self.driver = driver

        # Locators for login page elements

        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.submit_button = (By.ID, "login-button")
    
    def open(self, url):
        """Opens the login page."""
        self.driver.get(url)
    
    def login(self, username, password):

        """
        Logs in with the provided username and password.

        :param username: The username to log in with
        :param password: The password to log in with
        """

        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()
    
    def login_empty_credentials(self, username, password):

        """
        Attempts to log in with the provided username and password,
        then waits for the error message to appear when credentials are empty or incorrect.

        :param username: The username to log in with
        :param password: The password to log in with
        """

        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()

        # Wait for the error message to appear when the login fails

        WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-button")))

        # Find the error button that is displayed when credentials are empty/invalid

        self.error_button = self.driver.find_elements(By.CLASS_NAME, "error-button")