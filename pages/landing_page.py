from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LandingPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.menu_button = (By.XPATH, "//button[text()='Open Menu']")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")
        self.product_label = (By.CLASS_NAME, "product_label")
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

    def add_to_cart(self, item_container):
        self.container = item_container

        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'inventory_item')]//div[contains(text(), '{item_container}')]")))
        
        container = self.driver.find_element(By.XPATH, f"//div[contains(@class, 'inventory_item')]//div[contains(text(), '{item_container}')]")
        button = container.find_element(By.XPATH, "//button[text()='ADD TO CART']")
        button.click()
        self.shopping_cart_badge = (By.CLASS_NAME, "fa-layers-counter shopping_cart_badge")

    def remove_from_cart(self, item_container):
        self.container = item_container

        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'inventory_item')]//div[contains(text(), '{item_container}')]")))
        
        container = self.driver.find_element(By.XPATH, f"//div[contains(@class, 'inventory_item')]//div[contains(text(), '{item_container}')]")
        button = container.find_element(By.XPATH, "//button[text()='ADD TO CART']")
        button.click()

        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, f"//button[text()='REMOVE']")))

        remove_button = container.find_element(By.XPATH, "//button[text()='REMOVE']")
        remove_button.click()

        elements = self.driver.find_elements(By.CLASS_NAME, "fa-layers-counter.shopping_cart_badge")
        
        self.shopping_cart_badge = (By.CLASS_NAME, "fa-layers-counter shopping_cart_badge") if elements else None
