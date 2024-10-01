from abc import ABC, abstractmethod
from playwright.sync_api import sync_playwright
from typing import Union

from src.page_objects.main_page import MainPage


class BaseBrowser(ABC):
    def __init__(self, base_url: Union[str, None] = None, headless: bool = False, maximized: bool = True):
        self._base_url = base_url
        self._headless = headless
        self._maximized = maximized
        self._playwright = None
        self._browser = None
        self._context = None
        self._page = None

    @abstractmethod
    def _init_browser(self):
        self._playwright = sync_playwright().start()

    @abstractmethod
    def start(self, **context_args):
        self._init_browser()
        if context_args:
            try:
                self._context = self._browser.new_context(**context_args)
            except Exception as e:
                raise ValueError(f"Error while creating context: {e}")
        if not self._context:
            self._context = self._browser.new_context()
        self._page = self._context.new_page()
        if self._base_url:
            self._page.goto(self._base_url)
        return self._page

    def close(self):
        self._browser.close()
        self._playwright.stop()


class ChromiumBrowser(BaseBrowser):
    def _init_browser(self):
        super()._init_browser()
        if self._maximized:
            self._browser = self._playwright.chromium.launch(headless=self._headless, args=["--start-maximized"])
        else:
            self._browser = self._playwright.chromium.launch(headless=self._headless)

    def start(self, **context_args):
        super().start(**context_args)
        return self._page


class FirefoxBrowser(BaseBrowser):
    def _init_browser(self):
        super()._init_browser()
        if self._maximized:
            self._browser = self._playwright.firefox.launch(headless=self._headless, args=["--start-maximized"])
        else:
            self._browser = self._playwright.firefox.launch(headless=self._headless)

    def start(self, **context_args):
        super().start(**context_args)
        return self._page


class WebKitBrowser(BaseBrowser):
    def _init_browser(self):
        super()._init_browser()
        if self._maximized:
            self._browser = self._playwright.webkit.launch(headless=self._headless, args=["--start-maximized"])
        else:
            self._browser = self._playwright.webkit.launch(headless=self._headless)

    def start(self, **context_args):
        super().start(**context_args)
        return self._page


class BrowserFactory:
    @staticmethod
    def create_browser(browser_type: str, base_url: str = None, headless: bool = True,
                       maximized: bool = True) -> BaseBrowser:
        if browser_type.lower() == 'chromium':
            return ChromiumBrowser(base_url, headless, maximized)
        elif browser_type.lower() == 'firefox':
            return FirefoxBrowser(base_url, headless, maximized)
        elif browser_type.lower() == 'webkit':
            return WebKitBrowser(base_url, headless, maximized)
        else:
            raise ValueError(f'Browser "{browser_type}" is not supported')
