from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.checkout_button = (By.CLASS_NAME, "checkout_button")
    
    def open(self, url):
        self.driver.get(url)
    
    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        WebDriverWait(self.driver, 2).until(EC.url_contains("/checkout-step-one.html"))
        assert "/cart.html" in self.driver.current_url, "Did not navigate to the inventory page"
    