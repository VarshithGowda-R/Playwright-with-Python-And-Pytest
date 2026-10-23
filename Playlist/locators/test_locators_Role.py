from playwright.sync_api import sync_playwright, Page, expect


def test_locators_Role_button(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    expect(
            page.get_by_role("button", name="Primary Action")
        ).to_be_visible()
    expect(page.get_by_role("button", name="Toggle Button")
        ).to_be_visible()
    expect(page.get_by_role("button", name="Div with button role")
           ).to_be_visible()

def test_locators_Role(page: Page):
        page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

        page.get_by_role("checkbox", name=" Accept terms ").click()
        page.wait_for_timeout(2000)
        page.get_by_role("textbox",name="Username:").click()
        page.wait_for_timeout(2000)
        page.get_by_role("menuitem",name="Home").click()
        page.wait_for_timeout(2000)
        page.get_by_role("menuitem",name="Products").click()
        page.wait_for_timeout(2000)
        page.get_by_role("menuitem",name="Contact").click()
        page.wait_for_timeout(2000)
