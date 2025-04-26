from behave import given, when, then
from pages.login_page import LoginPage
from drivers.driver import get_driver
from config.config import BASE_URL, USERNAME, PASSWORD

@given('I am on the login page')
def step_impl(context):
    context.driver = get_driver()
    context.driver.get(BASE_URL)
    context.login_page = LoginPage(context.driver)

@when('I login with valid credentials')
def step_impl(context):
    context.login_page.login(USERNAME, PASSWORD)

@then('I should see the homepage title')
def step_impl(context):
    assert "Swag Labs" in context.driver.title
    context.driver.quit()
