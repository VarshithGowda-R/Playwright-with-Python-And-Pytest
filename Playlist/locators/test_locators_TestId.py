from playwright.sync_api import Playwright,Page,expect

def test_locators_TestId(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html#")
    text_name = page.get_by_test_id("profile-name").text_content()
    print(text_name)
    text_email = page.get_by_test_id("profile-email").text_content()
    print(text_email)
    expect(page.get_by_role("button",name="Edit Profile").click())
    expect(page.get_by_test_id("product-name")).to_have_text("Product A")
    expect(page.get_by_test_id("product-price")).to_have_text("$19.99")
    expect(page.get_by_test_id("product-name")).to_have_text("Product B")
    expect(page.get_by_test_id("product-price")).to_have_text("$29.99")
    expect(page.get_by_test_id("product-name")).to_have_text("Product C")
    expect(page.get_by_test_id("product-price")).to_have_text("$39.99")
