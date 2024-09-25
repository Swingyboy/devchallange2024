from abc import ABC, abstractmethod
from playwright.async_api import async_playwright
from typing import Union


class BaseBrowser(ABC):
    def __init__(self, base_url: Union[str, None] = None, headless: bool = False):
        self._base_url = base_url
        self._headless = headless
        self._playwright = None
        self._browser = None
        self._page = None

    @abstractmethod
    async def start(self):
        self._playwright = await async_playwright().start()

    async def close(self):
        await self._browser.close()
        await self._playwright.stop()

    async def goto(self, url: str):
        if self._page:
            await self._page.goto(url)
        else:
            self._page = await self._browser.new_page()
            await self._page.goto(url)

    async def wait(self, seconds: int):
        await self._page.wait_for_timeout(seconds * 1000)
