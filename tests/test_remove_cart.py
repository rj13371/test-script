import pytest
from drivers.driver import get_driver
from pages.landing_page import LandingPage
from config.config import LANDING_PAGE_URL

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get(LANDING_PAGE_URL)
    yield driver
    driver.quit()

def test_remove_from_cart(setup):
    landing_page = LandingPage(setup)
    landing_page.remove_from_cart("Sauce Labs Backpack")
    
    # Add assertion to check if cart is empty
    assert landing_page.shopping_cart_badge is None