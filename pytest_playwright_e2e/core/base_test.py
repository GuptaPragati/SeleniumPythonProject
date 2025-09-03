# core/base_test.py

import pytest
from playwright.sync_api import Page

from pytest_playwright_e2e.core.page_factory import BasePageFactory


@pytest.mark.usefixtures("page")
class BaseTest(BasePageFactory):
    @pytest.fixture(autouse=True)
    def init_pages(self, open_browser):
        """This fixture will automatically run before every test method"""
        self.page = open_browser
        self._initialize_all_pages(self.page)

    def pause_page(self):
        self.page.pause()

    def wait_until_loaded(self, ms):
        self.page.wait_for_timeout(ms)