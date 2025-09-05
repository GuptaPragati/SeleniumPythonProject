import pytest

from pytest_playwright_e2e.core.selenium.base_test import SeleniumBaseTest


# class BaseTest:
#     def init_pages(self, open_selenium_browser):
#         self.driver = open_selenium_browser
#         self.login_page = LoginPage(self.driver)
#         self.dashboard_page = DashboardPage(self.driver)
#         self.radio_checkboxes_page = RadioCheckboxesPage(self.driver)
#
#     def navigate(self, url):
#         self.driver.get(url)

class BaseTest(SeleniumBaseTest):
    """
    Base test class with auto-setup for test classes
    """

    @pytest.fixture(autouse=True)
    def setup(self, open_selenium_browser):
        """Auto-setup fixture that runs before each test"""
        self.setup_pages(open_selenium_browser)
        yield
        # Cleanup code can go here if needed

    def init_pages(self, driver):
        """
        Legacy method for backward compatibility
        Can be removed once all tests are updated
        """
        self.setup_pages(driver)
