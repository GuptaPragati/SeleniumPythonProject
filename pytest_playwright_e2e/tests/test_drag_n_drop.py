from playwright.sync_api import expect

from pytest_playwright_e2e.core.base_test import BaseTest


class TestDragDrop(BaseTest):
    def test_drag_n_drop_approach(self):
        self.page.goto("https://the-internet.herokuapp.com/drag_and_drop")
        src= self.page.locator("#column-a")
        dest = self.page.locator("#column-b")
        src.drag_to(dest)
        expect(dest).to_have_text("A")
        expect(src).to_have_text("B")
        self.page.drag_and_drop("#column-a", "#column-b")
        expect(dest).to_have_text("B")
        expect(src).to_have_text("A")
        src.hover()
        self.page.mouse.down()
        dest.hover()
        self.page.mouse.up()
        expect(dest).to_have_text("A")
        expect(src).to_have_text("B")
