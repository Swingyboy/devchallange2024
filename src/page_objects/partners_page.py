import typing

from base_page import BasePage
from src.page_locators.partners_page_locators import PARTNERS_PAGE_LOCATORS


class PartnersPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._locators.update(PARTNERS_PAGE_LOCATORS)
        self._partners_grid: "locator" = self._page.locator(self._locators["partners_grid"])
        self._first_screen: "locator" = self._page.locator(self._locators["first_screen"]).first

    def check_partner_is_present(self, partner_name: str) -> bool:
        partners: typing.List[typing.Dict[str, typing.Any]] = self.get_partners_list()
        for partner in partners:
            if partner["link"].find(partner_name) != -1:
                return True
        return False

    def get_partners_list(self) -> typing.List[typing.Dict[str, typing.Any]]:
        self._partners_grid.scroll_into_view_if_needed()
        partner_items: typing.List["locator"] = self._partners_grid.locator(
            ".w-dyn-item").all()
        partners: list = []

        for partner in partner_items:
            link = partner.locator("a").get_attribute("href")
            img_src = partner.locator("img").get_attribute("src")
            category_text = partner.locator(".category").inner_text()

            partners.append({"link": link, "img_src": img_src, "category": category_text})

        return partners
