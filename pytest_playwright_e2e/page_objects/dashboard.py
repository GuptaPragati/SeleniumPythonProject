from .order_history import OrderHistory


class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.order_btn = page.get_by_role("button", name="ORDERS")

    def openOrders(self):
        self.order_btn.click()
        return OrderHistory(self.page)