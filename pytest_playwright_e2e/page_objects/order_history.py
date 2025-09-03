from playwright.sync_api import expect

from .order_details import OrderDetails


class OrderHistory:
    def __init__(self, page):
        self.page = page

    def verify_and_select_order(self, order_id):
        print(f"order id: {order_id}")
        # oder_row= page.locator("tbody>tr").nth(0)
        oder_row = self.page.locator("tbody>tr").filter(has_text=order_id)
        expect(oder_row).to_contain_text(order_id)
        oder_row.get_by_role("button", name="View").click()
        return OrderDetails(self.page)
