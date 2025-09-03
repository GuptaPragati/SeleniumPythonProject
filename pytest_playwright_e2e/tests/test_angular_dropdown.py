from pytest_playwright_e2e.core.base_test import BaseTest


class TestAngularDropdown(BaseTest):
    def test_dropdown_selection(self):
        self.dropdown_page.navigate()
        self.wait_until_loaded(15000)
        self.dropdown_page.click_dropdown()
        self.dropdown_page.select_dropdown("Label 2")
        self.dropdown_page.verify_selected_option("Label 2")
        self.dropdown_page.click_dropdown()
        self.dropdown_page.select_dropdown("Label 1")
        self.dropdown_page.verify_selected_option("Label 1")


