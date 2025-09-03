from playwright.sync_api import expect


class OrderDetails:
    def __init__(self, page):
        self.page = page

    def verify_order_msg(self, msg:str):
        expect(self.page.locator("body")).to_contain_text(msg)