from pytest_playwright_e2e.core.selenium.selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertPage(SeleniumDriver):
    """Alert page for testing JavaScript alerts"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.alert_button = "alertbtn"
        self.confirm_button = "confirmbtn"
        self.prompt_button = "//input[@value='Prompt']"

    def navigate(self):
        """Navigate to alert page"""
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    def click_alert_button(self):
        """Click alert button"""
        self.elementClick(self.alert_button, "id")

    def click_confirm_button(self):
        """Click confirm button"""
        self.elementClick(self.confirm_button, "id")

    def click_prompt_button(self):
        """Click prompt button"""
        self.elementClick(self.prompt_button, "xpath")

    def handle_alert(self, action="accept", text=None):
        """
        Handle JavaScript alert

        Args:
            action: 'accept' or 'dismiss'
            text: Text to enter in prompt (if applicable)
        """
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())

        if text and hasattr(alert, 'send_keys'):
            alert.send_keys(text)

        if action == "accept":
            alert.accept()
        else:
            alert.dismiss()

    def get_alert_text(self):
        """Get alert text"""
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        return alert.text
