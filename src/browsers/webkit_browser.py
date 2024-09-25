from base_browser import BaseBrowser


class WebKitBrowser(BaseBrowser):
    async def start(self):
        await super().start()
        self._browser = await self._playwright.webkit.launch(headless=self._headless)
        if self._base_url:
            self._page = await self._browser.new_page(base_url=self._base_url)
