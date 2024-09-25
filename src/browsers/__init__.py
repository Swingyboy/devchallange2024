import os
import sys

_SRC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from _browsers import BrowserFactory, ChromiumBrowser, FirefoxBrowser, WebKitBrowser

sys.path.pop()
sys.path.pop()
