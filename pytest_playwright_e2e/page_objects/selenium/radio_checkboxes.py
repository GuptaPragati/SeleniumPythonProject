from pytest_playwright_e2e.core.selenium.selenium_driver import SeleniumDriver


class RadioCheckboxesPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cars_radio_btn = "#radio-btn-example >fieldset >label > input"
        self.cars_checkbox_btn = "#checkbox-example-div >fieldset >label > input"

    def __findCar(self, locator, car):
        elms = self.getElements(locator, "css")
        for elem in elms:
            if elem.get_attribute("value").lower() == car.lower():
                return elem
        return None

    def select_radio_checkbox_cars(self, locator, car):
        elem = self.__findCar(locator, car)
        elem.click()

    def verify_radio_car_selected(self, locator, car):
        elem = self.__findCar(locator, car)
        assert elem.is_selected()
