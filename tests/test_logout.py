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

def test_logout(setup):
    landing_page = LandingPage(setup)
    landing_page.logout()
    
    # Add assertions to confirm login success
    assert "Swag Labs" in setup.title