from base_browser import BaseBrowser


class FirefoxBrowser(BaseBrowser):
    async def start(self):
        await super().start()
        self._browser = await self._playwright.firefox.launch(headless=self._headless)
        if self._base_url:
            self._page = await self._browser.new_page(base_url=self._base_url)
