import pytest
from drivers.driver import get_driver
from config.config import BASE_URL
from pages.login_page import LoginPage

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_bad_credentials(setup):
    login_page = LoginPage(setup)
    login_page.login_empty_credentials("", "")
    
    # Add assertion to confirm on login page
    assert login_page.error_button