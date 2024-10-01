import os
from dotenv import load_dotenv
import pytest

from src.page_objects import MainPage
from src.browsers import BrowserFactory


load_dotenv()

BROWSER_TYPE = os.getenv('BROWSER_TYPE', 'chromium')
BASE_URL = os.getenv('BASE_URL', None)




@pytest.fixture
def test_context():
    class Context(object):
        pass

    return Context()


@pytest.fixture(scope="session")
def get_starting_page():

    print("Starting browser")
    page = BrowserFactory.create_browser(base_url=BASE_URL, browser_type=BROWSER_TYPE, headless=False).start()
    yield MainPage(page)
    page.close()
