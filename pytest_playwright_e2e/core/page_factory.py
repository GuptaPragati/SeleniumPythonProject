from pytest_playwright_e2e.page_objects.angular_dropdown_page import AngularDropdownPage
from pytest_playwright_e2e.page_objects.test_alert_popup_page import AlertPopupPage
from pytest_playwright_e2e.page_objects.test_dynamic_web_table_page import DynamicWebPage
from pytest_playwright_e2e.page_objects.test_sauce_demo_page import LoginPage

class BasePageFactory:
    def _initialize_all_pages(self, page):
        self.page = page
        self._login_page = LoginPage(self.page)  # initialize all required page objects here
        self._alert_page = AlertPopupPage(self.page)
        self._dropdown_page = AngularDropdownPage(self.page)
        self._web_table = DynamicWebPage(self.page)

    @property
    def login_page(self):
        return self._login_page

    @property
    def alert_page(self):
        return self._alert_page

    @property
    def dropdown_page(self):
        return self._dropdown_page

    @property
    def web_table_page(self):
        return self._web_table
    