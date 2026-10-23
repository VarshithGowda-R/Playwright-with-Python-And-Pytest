import p
from playwright.sync_api import Playwright, Page, expect, sync_playwright


def test_title(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(
        page.get_by_title("Home page link")
    ).to_have_text("Home")
    page.close()

def test_title_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

        expect(
            page.get_by_title("Home page link")
        ).to_be_visible()

        browser.close()

