import pytest
import pytest
from selenium import webdriver

from pytest_playwright_e2e.utils.config_reader import ConfigReader


# to run from terminal on specific browser, use this command- pytest test_file.py --browser_name firefox --url
#  playwright show-trace trace.zip
# You can open a saved trace using either the Playwright CLI or in the browser at trace.playwright.dev. Make sure to add the full path to where your trace.zip file is located.
# https://playwright.dev/python/docs/trace-viewer#recording-a-trace

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    # parser.addoption("--url", action="store", default="https://rahulshettyacademy.com/client/")

# https://github.com/automationneemo/PlaywrightDemoYt/blob/main/basics/test_dynamic_web_table.py
@pytest.fixture(scope="session")
def config():
    reader = ConfigReader(env="DEFAULT")
    return {
        "base_url": reader.get_base_url(),
        "browser_name": reader.get_browser_name(),
        "slow": reader.get_browser_slow(),
        "username": reader.get_username(),
        "password": reader.get_password()
    }

@pytest.fixture(autouse=True,scope="function")
def open_selenium_browser(config):
    global driver
    browser_name = config["browser_name"]
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(config["base_url"])
    yield driver
    driver.quit()






