import pytest
from drivers.driver import get_driver
from pages.checkout_page import CheckoutPage
from config.config import CHECKOUT_PAGE_URL

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get(CHECKOUT_PAGE_URL)
    yield driver
    driver.quit()

def test_check_empty_cart(setup):
    checkout_page = CheckoutPage(setup)
    checkout_page.checkout()
    
    # Add assertions to confirm 
    assert "/cart.html" in checkout_page.driver.current_url, "Did not navigate to the inventory page"