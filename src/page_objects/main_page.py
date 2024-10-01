from base_page import BasePage
from src.page_locators.main_page_locators import MAIN_PAGE_LOCATORS


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._locators.update(MAIN_PAGE_LOCATORS)
        self._first_screen: "locator" = self._page.locator(self._locators["first_screen"]).first
