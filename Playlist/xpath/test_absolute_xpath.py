from playwright.sync_api import Page,expect

def test_absolute_xpath(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
