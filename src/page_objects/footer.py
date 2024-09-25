from src.page_locators import FOOTER_LOCATORS


class Footer:
    def __init__(self, page):
        self._page = page
        self._locators = FOOTER_LOCATORS
        self._contact = self._page.get_by_role(self._locators["contact"], name="Contact").first
        self._address = self._page.locator(self._locators["address"]).first
        self._email = self._page.locator(self._locators["email"]).first
        
    async def check_footer_email(self, email: str) -> bool:
        return await self._email.inner_text() == email

    async def get_contact(self) -> str:
        return await self._contact.inner_text()

    async def get_address(self) -> str:
        return await self._address.inner_text()

    async def get_email(self) -> str:
        return await self._email.inner_text()

    async def scroll_to_contacts(self) -> None:
        await self._contact.scroll_into_view_if_needed()
