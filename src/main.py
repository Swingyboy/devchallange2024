from browsers import BrowserFactory


def main():
    URL = "https://www.devchallenge.it/"
    browser = BrowserFactory.create_browser(base_url=URL, browser_type='chromium', headless=False)
    main_page = browser.start()
    side_menu = main_page.open_side_hamburger_menu()
    side_menu.check_menu_is_opened()
    partners_page = side_menu.open_partners()
    res = partners_page.check_partner_is_present("IPhone")
    print(res)


if __name__ == '__main__':
    main()  # Run the main function
