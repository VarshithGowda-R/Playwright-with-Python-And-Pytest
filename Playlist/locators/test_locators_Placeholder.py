from playwright.sync_api import playwright,Page,expect

def test_locators_Placeholder(page:Page):

      page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html#")
      page.get_by_placeholder("Enter your full name").fill("varshith R")
      page.wait_for_timeout(1000)
      page.get_by_placeholder("Phone number (xxx-xxx-xxxx)").fill("9578963412")
      page.wait_for_timeout(1000)
      page.get_by_placeholder("Type your message here...").fill("i have started working on the playwright")
      page.wait_for_timeout(2000)
      page.get_by_placeholder("Search products...").fill(" Iphone 18 pro max")
      page.wait_for_timeout(2000)
      page.get_by_role("button",name="search").click()

      page.wait_for_timeout(5000)

      page.close()