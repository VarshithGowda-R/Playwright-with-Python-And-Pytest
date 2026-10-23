from playwright.async_api import Page,expect

def test_css_class(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input.search-box-text").fill("iphone")
    page.locator("input.button-1.search-box-button").click()
    page.wait_for_timeout(3000)
    page.close()
