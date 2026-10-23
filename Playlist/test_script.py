from playwright.sync_api import Page, expect

def test_verifyPageUrl(page:Page):
    page.goto("https://www.laundrymate.in/") # passing
    #storing in local variable
    myurl = page.url
    print("application URl is: ",myurl)

    # expected result
    expect(page).to_have_url("https://www.laundrymate.in/")

def test_verifyTitalOfPage(page:Page):
    page.goto("https://www.laundrymate.in/")

    pagetital  = page.title()
    print("application tital is: ", pagetital)

    expect(page).to_have_title("Best online Laundry and dry cleaning service in Bangalore | LaundryMate")