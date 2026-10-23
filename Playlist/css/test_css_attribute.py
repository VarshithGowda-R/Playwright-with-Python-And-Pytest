from playwright.sync_api import Page,expect

def test_css_attribute(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input[autocomplete=off]").fill("books")
    page.locator("input[value=Search]").click()
    page.close()