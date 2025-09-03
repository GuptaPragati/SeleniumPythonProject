from playwright.sync_api import Playwright

class TestNavigation:
    def test_navigation(self, playwright:Playwright):
        browser= playwright.chromium.launch(headless=False, slow_mo=1000, args=['--start-fullscreen'])
        context = browser.new_context()
        page = context.new_page()
        # page.goto("https://playwright.com/")
        page.goto("https://www.google.com/")
        print(page.url)

        # click on Gmail link
        page.locator("text=Gmail").click()
        # Get the url
        print(page.url)
        # Navigate back
        page.go_back()
        print(page.url)
        # Navigate forward
        page.go_forward(wait_until="networkidle")
        print(page.url)