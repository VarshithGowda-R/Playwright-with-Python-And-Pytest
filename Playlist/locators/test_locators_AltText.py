from playwright.sync_api import Playwright,Page,expect

def test_locator_AltText(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html#")
    page.wait_for_timeout(2000)
    expect(page.get_by_alt_text("logo image")).to_be_visible()
    page.wait_for_timeout(2000)
    page.close()

def test_locator_AltText2(page:Page):
    page.goto("https://www.flipkart.com/")
    page.wait_for_timeout(2000)
    page.get_by_role("button",name="✕").click()
    expect(page.get_by_alt_text("Cart")).to_be_visible()
    page.close()


