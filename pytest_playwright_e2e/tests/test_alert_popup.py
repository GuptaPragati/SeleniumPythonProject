import pytest

from pytest_playwright_e2e.core.base_test import BaseTest


class TestAlertPopup(BaseTest):
    @pytest.mark.alert
    def test_click_for_js_alert(self):
        '''
            Handle javascript alert pop up
        '''
        self.alert_page.navigate()
        self.alert_page.click_js_alert_btn(self.alert_page.js_alert_btn)
        self.alert_page.accept_js_alert()
        self.alert_page.asert_message("You successfully clicked an alert")

    @pytest.mark.alert
    def test_click_for_js_confirm(self):
        '''
            Handle javascript alert pop up
        '''
        self.alert_page.navigate()
        self.alert_page.click_js_alert_btn(self.alert_page.js_confirm_btn)
        self.alert_page.accept_js_alert()
        self.alert_page.asert_message("You clicked: Cancel")

    @pytest.mark.alert
    def test_click_for_js_prompt(self):
        '''
            Handle javascript alert pop up
        '''
        self.alert_page.navigate()
        self.alert_page.click_js_alert_btn(self.alert_page.js_prompt_btn)
        # self.alert_page.accept_js_prompt_alert()
        self.alert_page.asert_message("You entered: null")

