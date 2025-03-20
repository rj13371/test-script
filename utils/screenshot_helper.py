import os
import datetime

def take_screenshot(driver, test_name):

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = os.path.join("screenshots", f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)

def pytest_exception_interact(node, call, report):
    """
    Take a screenshot when a test fails.
    """
    if report.failed:
        driver = node.funcargs.get("driver", None)
        if driver:
            take_screenshot(driver, node.nodeid)