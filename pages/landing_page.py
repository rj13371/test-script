from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LandingPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.menu_button = (By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div/button")
        self.logout_button = (By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]")
    def open(self, url):
        self.driver.get(url)
    
    def logout(self):
        self.driver.find_element(*self.menu_button).click()

        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.logout_button)
        )

        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()