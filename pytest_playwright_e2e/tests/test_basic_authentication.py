from playwright.sync_api import Playwright, expect


def test_basic_auth(playwright: Playwright, config):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(http_credentials={'username': config['username'], 'password':config['password']})
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/digest_auth")
    result = page.locator("#content p")

    expect(result).to_have_text('Congratulations! You must have the proper credentials.')
    browser.close()