import pytest
from drivers.driver import get_driver
from config.config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage

@pytest.fixture
def setup(driver):
    driver = get_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_login(setup):
    login_page = LoginPage(setup)
    login_page.login(USERNAME, PASSWORD)
    
    # Add assertions to confirm login success
    assert "Swag Labs" in setup.title