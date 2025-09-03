import pytest

from pytest_playwright_e2e.tests.selenium.base_test import BaseTest


class TestRadioCheckboxes(BaseTest):
    @pytest.mark.smoke
    def test_radio_checkboxes(self):
        self.navigate("https://www.letskodeit.com/practice")
        self.radio_checkboxes_page.select_radio_checkbox_cars(self.radio_checkboxes_page.cars_radio_btn,"Honda")
        self.radio_checkboxes_page.verify_radio_car_selected(self.radio_checkboxes_page.cars_radio_btn,"Honda")
        self.radio_checkboxes_page.select_radio_checkbox_cars(self.radio_checkboxes_page.cars_checkbox_btn,"Honda")
        self.radio_checkboxes_page.verify_radio_car_selected(self.radio_checkboxes_page.cars_checkbox_btn,"Honda")

