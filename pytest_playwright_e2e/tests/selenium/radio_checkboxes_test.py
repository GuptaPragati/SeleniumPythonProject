import pytest

from pytest_playwright_e2e.tests.selenium.base_test import BaseTest


class TestRadioCheckboxes(BaseTest):
    @pytest.mark.smoke
    def test_single_radio_button_selection(self):
        """Test selecting a single radio button"""
        # Select Honda radio button
        self.radio_checkboxes_page.select_radio_checkbox_cars(
            self.radio_checkboxes_page.cars_radio_btn, "Honda"
        )

        # Verify Honda is selected
        self.radio_checkboxes_page.verify_radio_car_selected(
            self.radio_checkboxes_page.cars_radio_btn, "Honda"
        )

    @pytest.mark.smoke
    def test_radio_button_selection_changes(self):
        """Test that selecting one radio button deselects the previous one"""
        # First select Honda
        self.radio_checkboxes_page.select_radio_checkbox_cars(
            self.radio_checkboxes_page.cars_radio_btn, "Honda"
        )
        self.radio_checkboxes_page.verify_radio_car_selected(
            self.radio_checkboxes_page.cars_radio_btn, "Honda"
        )

        # Then select BMW (should deselect Honda)
        self.radio_checkboxes_page.select_radio_checkbox_cars(
            self.radio_checkboxes_page.cars_radio_btn, "BMW"
        )
        self.radio_checkboxes_page.verify_radio_car_selected(
            self.radio_checkboxes_page.cars_radio_btn, "BMW"
        )

        # Finally select Benz (should deselect BMW)
        self.radio_checkboxes_page.select_radio_checkbox_cars(
            self.radio_checkboxes_page.cars_radio_btn, "Benz"
        )
        self.radio_checkboxes_page.verify_radio_car_selected(
            self.radio_checkboxes_page.cars_radio_btn, "Benz"
        )

    @pytest.mark.parametrize("car_name", ["Honda", "BMW", "Benz"])
    def test_each_radio_button_individually(self, car_name):
        """Test each radio button option individually"""
        self.radio_checkboxes_page.select_radio_checkbox_cars(
            self.radio_checkboxes_page.cars_radio_btn, car_name
        )
        self.radio_checkboxes_page.verify_radio_car_selected(
            self.radio_checkboxes_page.cars_radio_btn, car_name
        )

    @pytest.mark.smoke
    def test_single_checkbox_selection(self):
        """Test selecting a single checkbox"""
        # Select Honda checkbox
        self.radio_checkboxes_page.select_radio_checkbox_cars(
            self.radio_checkboxes_page.cars_checkbox_btn, "Honda"
        )

        # Verify Honda checkbox is selected
        self.radio_checkboxes_page.verify_radio_car_selected(
            self.radio_checkboxes_page.cars_checkbox_btn, "Honda"
        )

    @pytest.mark.regression
    def test_multiple_checkbox_selections(self):
        """Test selecting multiple checkboxes simultaneously"""
        cars = ["Honda", "BMW", "Benz"]

        # Select all checkboxes
        for car in cars:
            self.radio_checkboxes_page.select_radio_checkbox_cars(
                self.radio_checkboxes_page.cars_checkbox_btn, car
            )

        # Verify all checkboxes are selected
        for car in cars:
            self.radio_checkboxes_page.verify_radio_car_selected(
                self.radio_checkboxes_page.cars_checkbox_btn, car
            )

    def test_checkbox_toggle_behavior(self):
        """Test checkbox toggle behavior (select and deselect)"""
        # Select Honda checkbox first time
        self.radio_checkboxes_page.select_radio_checkbox_cars(
            self.radio_checkboxes_page.cars_checkbox_btn, "Honda"
        )
        self.radio_checkboxes_page.verify_radio_car_selected(
            self.radio_checkboxes_page.cars_checkbox_btn, "Honda"
        )

        # Click Honda checkbox again to deselect it
        self.radio_checkboxes_page.select_radio_checkbox_cars(
            self.radio_checkboxes_page.cars_checkbox_btn, "Honda"
        )
