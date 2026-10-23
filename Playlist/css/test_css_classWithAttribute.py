from playwright.sync_api import Page,expect

def test_css_classWithAttribute(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("div.nivo-main-image[style=display: block;]")
    page.wait_for_timeout(2000)
    page.close()
