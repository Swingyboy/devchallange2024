from browsers import BrowserFactory
import asyncio


async def main():
    URL = "https://www.devchallenge.it/"
    browser = BrowserFactory.create_browser(base_url=URL, browser_type='chromium', headless=False)
    main_page = await browser.start()
    side_menu = await main_page.open_side_hamburger_menu()
    await side_menu.check_menu_is_opened()
    main_page = await side_menu.open_about()
    await main_page.scroll_to_footer()
    contact = await main_page.get_footer_email()
    print(contact)
    await main_page.wait_for_n_seconds(10)


if __name__ == '__main__':
    asyncio.run(main())  # Run the main async function
