import pytest
from pytest_bdd import scenarios, given, when, then

scenarios("../features/partners_page.feature")


RETRY = 3


@given("The main page is open")
def open_website(get_starting_page, test_context):
    test_context.main_page = get_starting_page


@when("User opens the side menu")
def open_side_menu(test_context):
    main_page = test_context.main_page
    side_menu = main_page.open_side_hamburger_menu()
    test_context.side_menu = side_menu


@when("User opens the Partners Page")
def open_partners_page(test_context):
    side_menu = test_context.side_menu
    partners_page = side_menu.open_partners()
    if partners_page.check_first_screen("OUR PARTNERS"):
        test_context.partners_page = partners_page
    else:
        for _ in range(RETRY):
            partners_page = side_menu.open_partners()
            if partners_page.check_first_screen("OUR PARTNERS"):
                test_context.partners_page = partners_page
                break
        raise AssertionError("First screen text is not equal to expected")


@then("There is no Apple Inc in the partners’ list")
def check_the_absence_of_apple(test_context):
    partners_page = test_context.partners_page
    assert not partners_page.check_partner_is_present("Apple"), "Apple Inc is present in the partners’ list"