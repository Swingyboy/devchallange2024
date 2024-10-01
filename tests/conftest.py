import os
from dotenv import load_dotenv
import pytest

from src.page_objects import MainPage
from src.browsers import BrowserFactory

load_dotenv(override=False)

BROWSER_TYPE = os.getenv('BROWSER_TYPE', 'chromium')
BROWSER_TYPE = BROWSER_TYPE.lower() if BROWSER_TYPE else None
BASE_URL = os.getenv('BASE_URL', None)
PLATFORM = os.getenv('PLATFORM', None)
PLATFORM = PLATFORM.lower() if PLATFORM else None
HEADLESS = os.getenv('HEADLESS', "FALSE")
HEADLESS = HEADLESS.lower() in ['true', '1', 't', 'y', 'yes']

@pytest.fixture
def test_context():
    class Context(object):
        pass

    return Context()


@pytest.fixture(scope="session")
def set_platform_context() -> dict:
    platform = PLATFORM
    if platform == "desktop":
        return {"viewport": {"width": 1920, "height": 1080},
                "maximized": True}
    elif platform == "mobile":
        return {"viewport": {"width": 360, "height": 800},
                "user_agent": "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36",
                "maximized": False
                }
    else:
        raise ValueError(f"Unsupported platform: {platform}")


@pytest.fixture(scope="session")
def get_browser(set_platform_context):
    context_args = set_platform_context
    maximazed = context_args.pop("maximized")
    browser = BrowserFactory.create_browser(base_url=BASE_URL, browser_type=BROWSER_TYPE, headless=HEADLESS,
                                            maximized=maximazed)
    page = browser.start(**context_args)
    yield page
    page.close()


@pytest.fixture(scope="function")
def get_starting_page(get_browser):
    page = MainPage(get_browser)
    yield page
    page.goto(BASE_URL)
