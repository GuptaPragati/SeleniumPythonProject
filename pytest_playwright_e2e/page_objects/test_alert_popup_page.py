from playwright.sync_api import Page, expect


class AlertPopupPage:
    def __init__(self, page: Page):
        self.page = page
        self.js_alert_btn = self.page.locator("text=Click for JS Alert")
        self.js_confirm_btn = self.page.get_by_text("Click for JS Confirm")
        self.js_prompt_btn = self.page.get_by_text("Click for JS Prompt")
        self.result = self.page.locator("#result")

    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/javascript_alerts")


    def click_js_alert_btn(self, button):
        button.click()

    def accept_js_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())

    def accept_js_prompt_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept(prompt_text="Pragati"))

    def asert_message(self, msg):
        expect(self.result).to_have_text(msg)






