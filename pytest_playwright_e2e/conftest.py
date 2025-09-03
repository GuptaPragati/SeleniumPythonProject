import pytest
import pytest
from .utils.config_reader import ConfigReader

# to run from terminal on specific browser, use this command- pytest test_file.py --browser_name firefox --url
#  playwright show-trace trace.zip
# You can open a saved trace using either the Playwright CLI or in the browser at trace.playwright.dev. Make sure to add the full path to where your trace.zip file is located.
# https://playwright.dev/python/docs/trace-viewer#recording-a-trace

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    # parser.addoption("--url", action="store", default="https://rahulshettyacademy.com/client/")


# session will run once for entire execution
@pytest.fixture
def launch_browser(playwright, request):
    global browser
    browser_name = request.config.getoption("browser_name")
    # url = request.config.getoption("url")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()
    # page.goto(url)
    yield page
    context.tracing.stop(path="trace.zip")
    browser.close()

@pytest.fixture(scope="session")
def config():
    reader = ConfigReader(env="DEFAULT")
    return {
        "base_url": reader.get_base_url(),
        "browser_name": reader.get_browser_name(),
        "username": reader.get_username(),
        "password": reader.get_password()
    }

@pytest.fixture(scope="session")
def open_browser(config, playwright):
    browser_name = config["browser_name"]
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False, slow_mo=config["slow"])
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config["base_url"])
    yield page
    browser.close()



