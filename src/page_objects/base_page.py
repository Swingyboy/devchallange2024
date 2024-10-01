from playwright.sync_api import Page
import typing
from src.page_objects.side_menu import SideMenu
from src.page_objects.header import Header
from src.page_objects.footer import Footer
from src.page_locators import BASE_PAGE_LOCATORS


class BasePage:
    def __init__(self, page: Page):
        self._page = page
        self._locators = BASE_PAGE_LOCATORS
        self._hamburger_menu = self._page.locator(self._locators["hamburger_menu"]).first
        self._first_screen = self._page.locator(self._locators["first_screen"]).first
        self._header = Header(self._page)
        self._footer = Footer(self._page)

    def check_first_screen(self, text: str) -> bool:
        inner_text = self._first_screen.inner_text()
        return inner_text == text

    def get_footer_email(self) -> str:
        email =  self._footer.get_email()
        email = email.split(" ")[1]
        return email

    def goto(self, url: str, timeout: typing.Optional[float] = None, wait_until: typing.Optional[str] = None):
        self._page.goto(url, timeout=timeout, wait_until=wait_until)

    def open_side_hamburger_menu(self) -> SideMenu:
        self._hamburger_menu.wait_for(state="visible")
        self._hamburger_menu.click(force=True)
        return SideMenu(self._page)

    def sroll_to_bottom(self) -> None:
        self._page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

    def sroll_to_top(self) -> None:
        self._page.evaluate("window.scrollTo(0, 0);")

    def scroll_to_header(self) -> None:
        self._header.scroll_to_logo()

    def scroll_to_footer(self) -> None:
        self._footer.scroll_to_contacts()

    def get_footer_contact(self) -> str:
        return self._footer.get_contact()

    def sroll_to_element(self, element_name: str) -> None:
        element_name = self._locators.get(element_name)
        if element_name:
            element = self._page.locator(element_name).first
            element.scroll_into_view_if_needed()
        else:
            raise ValueError(f"Element {element_name} not found on the page")

    def wait_for_n_seconds(self, n: int) -> None:
        self._page.wait_for_timeout(n * 1000)
