from base_page import BasePage
from src.page_locators.judges_page_locators import JUDGES_PAGE_LOCATORS


class JudgesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._locators: dict = JUDGES_PAGE_LOCATORS
        self._back_end_judges: "locator" = self._page.get_by_text(self._locators["backend_judges"]).first
        self._front_end_judges: "locator" = self._page.get_by_text(self._locators["frontend_judges"]).first
        self._testing_judges: "locator" = self._page.get_by_text(self._locators["testing_judges"]).first
        self._product_design_judges: "locator" = self._page.get_by_text(self._locators["product_design_judges"]).first
        self._ui_design_judges: "locator" = self._page.get_by_text(self._locators["ui_design_judges"]).first
        self._mac_os_judges: "locator" = self._page.locator(self._locators["mac_os_judges"]).first

    def check_judges_number(self, judges_number: int, judges_type: str) -> bool:
        if judges_type.lower() == "back_end":
            count = self.get_back_end_judges_count()
        elif judges_type.lower() == "front_end":
            count = self.get_front_end_judges_count()
        elif judges_type.lower() == "testing":
            count = self.get_testing_judges_count()
        else:
            raise ValueError(f"Invalid judges type: {judges_type}")
        return count == judges_number

    def get_back_end_judges(self):
        self._back_end_judges.scroll_into_view_if_needed()

    def get_back_end_judges_count(self) -> int:
        self.get_back_end_judges()
        back_end_judges_list = self._back_end_judges.locator(self._locators["team_member"])
        count: int = back_end_judges_list.count()
        return count

    def get_front_end_judges(self):
        self._front_end_judges.scroll_into_view_if_needed()

    def get_front_end_judges_count(self) -> int:
        self.get_front_end_judges()
        front_end_judges_list = self._front_end_judges.locator(self._locators["team_member"])
        count: int = front_end_judges_list.count()
        return count

    def get_testing_judges(self):
        self._testing_judges.scroll_into_view_if_needed()

    def get_testing_judges_count(self) -> int:
        self.get_testing_judges()
        testing_judges_list = self._testing_judges.locator(self._locators["team_member"])
        count: int = testing_judges_list.count()
        return count
