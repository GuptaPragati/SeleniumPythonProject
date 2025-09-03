from pytest_playwright_e2e.core.base_test import BaseTest


class TestDynamicWebTable(BaseTest):
    def test_dynamic_web_table(self):
        self.web_table_page.navigate()
        print(self.web_table_page.get_spec_by_browser("Disk", "System"))