import pytest

from pytest_playwright_e2e.page_objects.selenium.login import LoginPage
from pytest_playwright_e2e.page_objects.selenium.dashboard import DashboardPage
from pytest_playwright_e2e.page_objects.selenium.radio_checkboxes import RadioCheckboxesPage


class BaseTest:
    def init_pages(self, open_selenium_browser):
        self.driver = open_selenium_browser
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.radio_checkboxes_page = RadioCheckboxesPage(self.driver)

    def navigate(self, url):
        self.driver.get(url)
