from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import browser


class DynamicWebPage:
    def __init__(self, page: Page):
        self.page = page
        self.col_header = self.page.locator(".table-striped >thead> tr> th")

    def navigate(self):
        self.page.goto("https://practice.expandtesting.com/dynamic-table")

    def get_spec_by_browser(self, spec, browser:str):
        for index in range(self.col_header.count()):
            if self.col_header.nth(index).text_content() == spec:
                row = self.page.locator("tbody> tr").filter(has_text=browser)
                return row.locator("td").nth(index).text_content()




