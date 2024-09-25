from chromium_browser import ChromiumBrowser
from firefox_browser import FirefoxBrowser
from webkit_browser import WebKitBrowser


class BrowserFactory:
    @staticmethod
    def create_browser(browser_name: str):
        if browser_name.lower() == 'chromium':
            return ChromiumBrowser()
        elif browser_name.lower() == 'firefox':
            return FirefoxBrowser()
        elif browser_name.lower() == 'webkit':
            return WebKitBrowser()
        else:
            raise ValueError(f'Browser "{browser_name}" is not supported')