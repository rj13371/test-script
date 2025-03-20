import pytest
from drivers.driver import get_driver
from config.config import BASE_URL
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_xss_attack(setup):
    login_page = LoginPage(setup)
    malicious_script = "<script>alert('XSS Attack!')</script>"

    login_page.login(malicious_script, "fake_password")
    try:
        WebDriverWait(setup, 2).until(EC.alert_is_present())
        alert = Alert(setup)
        alert_message = alert.text
        alert.accept()
        assert alert_message == "XSS Attack!", "XSS attack was not reflected properly"
    
    except:
        page_source = setup.page_source
        assert malicious_script not in page_source, "XSS script was reflected in the page source!"

    current_url = setup.current_url
    assert BASE_URL in current_url, f"Unexpected navigation. Current URL: {current_url}"

    # Additionally, check if the username field is still present on the login page
    assert login_page.username_field.is_displayed(), "Username field is not visible on the login page"