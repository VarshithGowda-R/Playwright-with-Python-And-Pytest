from  playwright.sync_api import Page,expect

def test_tag_id(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    #tag with id
    page.locator("input#small-searchterms").fill("iphone")
    page.wait_for_timeout(3000)
