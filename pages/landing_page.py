from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LandingPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.menu_button = (By.XPATH, "//*[@id='menu_button_container']/div/div[3]/div/button")
        self.logout_button = (By.XPATH, "//*[@id='logout_sidebar_link']")
    def open(self, url):
        self.driver.get(url)
    
    def logout(self):
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(self.menu_button)
        ).click()

        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()