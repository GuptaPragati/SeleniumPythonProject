from pytest_playwright_e2e.core.base_test import BaseTest


class TestClearEnteredTest(BaseTest):

    def clear_entered_text(self, locator):
        self.page.locator(locator).press("Control+KeyA")
        self.page.locator(locator).press("Backspace")

    def test_clear_text(self):
        self.page.goto("https://the-internet.herokuapp.com/login")
        self.page.locator("#username").fill("pragati")
        self.page.locator("#username").clear()
        self.page.locator("#password").fill("pragati")
        self.clear_entered_text("#password")

