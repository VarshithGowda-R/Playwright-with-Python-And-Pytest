from playwright.sync_api import playwright,Page,expect

def test_locator_Lable(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html#")
    page.get_by_label("Email Address:").fill("varshithr567@gmail.com")
    page.wait_for_timeout(1000)
    page.get_by_label("Password:").fill("varshithr567")
    page.wait_for_timeout(1000)
    page.get_by_label("Your Age:").fill("24")
    page.wait_for_timeout(1000)
    page.get_by_label(" Standard").click()
    page.wait_for_timeout(1000)
    page.get_by_label(" Express").click()
    page.wait_for_timeout(1000)
