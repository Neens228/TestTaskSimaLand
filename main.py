import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.sima-land.ru/")
    await page.get_by_test_id("nav-item:cabinet").get_by_test_id("link").click()
    await page.get_by_test_id("login-field").get_by_test_id("text-field:field").click()
    await page.get_by_test_id("login-field").get_by_test_id("text-field:field").fill("qa_test@test.ru")
    await page.get_by_test_id("login-field").get_by_test_id("text-field:field").click()
    await page.get_by_test_id("password-field").get_by_test_id("text-field:field").fill("qa_test")
    await page.get_by_test_id("button").click()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
