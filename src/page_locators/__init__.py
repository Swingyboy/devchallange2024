import os
import sys

_SRC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from base_page_locators import BASE_PAGE_LOCATORS
from main_page_locators import MAIN_PAGE_LOCATORS
from side_menu_locators import SIDE_MENU_LOCATORS
from header_locators import HEADER_LOCATORS
from footer_locators import FOOTER_LOCATORS


sys.path.pop()
sys.path.pop()
