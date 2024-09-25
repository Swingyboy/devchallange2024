from playwright.async_api import Page, expect
from src.page_locators import BASE_PAGE_LOCATORS, SIDE_MENU_LOCATORS

import typing


class SideMenu:
    def __init__(self, page: Page):
        self._page = page
        self._locators = SIDE_MENU_LOCATORS
        self._title = self._page.get_by_text(self._locators["title"]).first
        self._about = self._page.get_by_text(self._locators["about"]).first
        self._judges = self._page.get_by_text(self._locators["judges"]).first
        self._partners = self._page.get_by_text(self._locators["partners"]).first

    async def check_menu_is_opened(self) -> None:
        await expect(self._title).to_be_visible()

    async def open_about(self) -> "MainPage":
        from src.page_objects.main_page import MainPage
        await self._about.click(force=True)
        return MainPage(self._page)

    async def open_judges(self):
        await self._judges.click(force=True)

    async def open_partners(self):
        await self._partners.click(force=True)