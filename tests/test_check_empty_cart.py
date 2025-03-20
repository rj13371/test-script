import pytest
from drivers.driver import get_driver
from pages.checkout_page import CheckoutPage
from config.config import CHECKOUT_PAGE_URL
from utils.screenshot_helper import take_screenshot

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get(CHECKOUT_PAGE_URL)
    yield driver
    driver.quit()

def test_check_empty_cart(setup):
    checkout_page = CheckoutPage(setup)
    checkout_page.checkout()
    
    try:
        assert "/cart.html" not in checkout_page.driver.current_url
    except AssertionError:
        take_screenshot(setup, "test_bad_credentials")
        raise
