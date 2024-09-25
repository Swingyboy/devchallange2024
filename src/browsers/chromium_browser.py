from base_browser import BaseBrowser


class ChromiumBrowser(BaseBrowser):
    async def start(self):
        await super().start()
        self._browser = await self._playwright.chromium.launch(headless=self._headless)
        if self._base_url:
            self._page = await self._browser.new_page(base_url=self._base_url)
