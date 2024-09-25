from src.page_locators import HEADER_LOCATORS


class Header:
    def __init__(self, page):
        self._page = page
        self._locators = HEADER_LOCATORS
        self._logo = self._page.locator(self._locators["logo"]).first
        self._register_button = self._page.get_by_role(self._locators["register_button"], name="Register").nth(2)

    async def open_register_page(self):
        await self._register_button.click(force=True)

    async def scroll_to_logo(self) -> None:
        await self._logo.scroll_into_view_if_needed()