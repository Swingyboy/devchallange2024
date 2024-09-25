from src.browsers import BrowserFactory
import asyncio


async def main():
    browser = BrowserFactory.create_browser('chromium')  # Adjust to use the correct method
    await browser.start()  # Await the start method
    await browser.goto('https://www.google.com')  # Await the goto method
    await asyncio.sleep(5)  # Use asyncio.sleep to wait asynchronously
    await browser.close()  # Await the close method

if __name__ == '__main__':
    asyncio.run(main())  # Run the main async function
