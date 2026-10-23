import re
from playwright.sync_api import Page,expect

def test_verify_locator_text(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    # Full text matching
    expect(page.get_by_text("Locate elements by their text content.")).to_be_visible()


def test_verify_locator_partialtext(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    # Partial text matching using regex
    expect(page.get_by_text("Locate elements by their text")).to_be_visible()

def test_verify_locator_partialtext2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    expect(page.get_by_text(re.compile(".* for demonstration.*"))).to_be_visible()
