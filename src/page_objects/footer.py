from src.page_locators import FOOTER_LOCATORS


class Footer:
    def __init__(self, page):
        self._page = page
        self._locators = FOOTER_LOCATORS
        self._contact = self._page.get_by_role(self._locators["contact"], name="Contact").first
        self._address = self._page.locator(self._locators["address"]).first
        self._email = self._page.locator(self._locators["email"]).first
        
    def check_footer_email(self, email: str) -> bool:
        return self._email.inner_text() == email

    def get_contact(self) -> str:
        return self._contact.inner_text()

    def get_address(self) -> str:
        return self._address.inner_text()

    def get_email(self) -> str:
        return self._email.inner_text()

    def scroll_to_contacts(self) -> None:
        self._contact.scroll_into_view_if_needed()
