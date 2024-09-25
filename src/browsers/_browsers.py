from abc import ABC, abstractmethod
from playwright.async_api import async_playwright
from typing import Union

from src.page_objects.main_page import MainPage


class BaseBrowser(ABC):
    def __init__(self, base_url: Union[str, None] = None, headless: bool = False):
        self._base_url = base_url
        self._headless = headless
        self._playwright = None
        self._browser = None
        self._context = None
        self._page = None

    @abstractmethod
    async def _init_browser(self):
        self._playwright = await async_playwright().start()

    @abstractmethod
    async def start(self):
        await self._init_browser()
        self._context = await self._browser.new_context()
        self._page = await self._context.new_page()
        if self._base_url:
            self._page = MainPage(self._page)
            await self._page.goto(self._base_url)
        return self._page

    async def close(self):
        await self._browser.close()
        await self._playwright.stop()


class ChromiumBrowser(BaseBrowser):
    async def _init_browser(self):
        await super()._init_browser()
        self._browser = await self._playwright.chromium.launch(headless=self._headless)

    async def start(self):
        await super().start()
        return self._page


class FirefoxBrowser(BaseBrowser):
    async def _init_browser(self):
        await super()._init_browser()
        self._browser = await self._playwright.firefox.launch(headless=self._headless)

    async def start(self):
        await super().start()
        return self._page


class WebKitBrowser(BaseBrowser):
    async def _init_browser(self):
        await super()._init_browser()
        self._browser = await self._playwright.webkit.launch(headless=self._headless)

    async def start(self):
        await super().start()
        return self._page


class BrowserFactory:
    @staticmethod
    def create_browser(browser_type: str, base_url: str = None, headless: bool = True):
        if browser_type.lower() == 'chromium':
            return ChromiumBrowser(base_url, headless)
        elif browser_type.lower() == 'firefox':
            return FirefoxBrowser(base_url, headless)
        elif browser_type.lower() == 'webkit':
            return WebKitBrowser(base_url, headless)
        else:
            raise ValueError(f'Browser "{browser_type}" is not supported')
