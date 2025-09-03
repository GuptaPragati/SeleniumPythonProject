from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select

class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def getElements(self, locator, locatorType="id"):
        elements = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            print("Element Found")
        except:
            print("Element not found")
        return elements

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element not found")
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element = self._wait.until(expected_conditions.element_to_be_clickable(element))
            element.click()
            # select = Select(self.driver.find_element(By.ID, "dropdown-id"))
            print("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            print("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element

    def inputText(self,text, locator, byType="id"):
        element = self.getElement(locator,byType)
        element.send_keys(text)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # alrt1= self.driver.switch_to().alert
        # alrt1.accept()

        # dropdown = wait.until(EC.element_to_be_clickable((By.ID, "country-dropdown")))
        # dropdown.click()
        #
        # # Wait for dynamic list items to load
        # options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='dropdown-options']/li")))
        #
        # # Select the option
        # for option in options:
        #     if option.text.strip() == "India":
        #         option.click()
        #         break

        # main_window = driver.current_window_handle
        # driver.find_element(By.LINK_TEXT, "Open New Window").click()
        # all_windows = driver.window_handles
        # for window in all_windows:
        #     if window != main_window:
        #         driver.switch_to.window(window)
        #         break
        # driver.switch_to.window(main_window)