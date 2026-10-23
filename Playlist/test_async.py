#pre-requiste for asynchrouns execution
# install pytest-asyncio
# command pip install pytest-asyncio

from playwright.async_api import async_playwright,Page, expect
import pytest

@pytest.mark.asyncio
async def test_launch_browser():
        async with async_playwright() as p:

            browser = await p.chromium.launch()
            mypage = await browser.new_page()

            await mypage.goto("https://www.laundrymate.in/")
            await expect(mypage).to_have_url("https://www.laundrymate.in/")
            print("url of page! : ",mypage)
            await browser.close()

