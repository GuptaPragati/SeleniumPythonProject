from pytest_playwright_e2e.core.selenium.selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class DropdownPage(SeleniumDriver):
    """Dropdown page for testing dropdown interactions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.dropdown_id = "dropdown"
        self.static_dropdown_id = "staticDropdown"
        self.dynamic_dropdown_class = "dynamic-dropdown"

    def navigate(self):
        """Navigate to dropdown test page"""
        self.driver.get("https://the-internet.herokuapp.com/dropdown")

    def select_by_visible_text(self, dropdown_locator, text, locator_type="id"):
        """Select dropdown option by visible text"""
        element = self.getElement(dropdown_locator, locator_type)
        select = Select(element)
        select.select_by_visible_text(text)

    def select_by_value(self, dropdown_locator, value, locator_type="id"):
        """Select dropdown option by value"""
        element = self.getElement(dropdown_locator, locator_type)
        select = Select(element)
        select.select_by_value(value)

    def select_by_index(self, dropdown_locator, index, locator_type="id"):
        """Select dropdown option by index"""
        element = self.getElement(dropdown_locator, locator_type)
        select = Select(element)
        select.select_by_index(index)

    def get_selected_option_text(self, dropdown_locator, locator_type="id"):
        """Get currently selected option text"""
        element = self.getElement(dropdown_locator, locator_type)
        select = Select(element)
        return select.first_selected_option.text

    def get_all_options(self, dropdown_locator, locator_type="id"):
        """Get all available options"""
        element = self.getElement(dropdown_locator, locator_type)
        select = Select(element)
        return [option.text for option in select.options]
