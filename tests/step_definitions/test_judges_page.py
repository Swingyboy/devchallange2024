import pytest
from pytest_bdd import scenarios, given, when, then

from tests.step_definitions.test_about_page import RETRY

scenarios("../features/judges_page.feature")


RETRY = 3


@given("The main page is open")
def open_website(get_starting_page, test_context):
    test_context.main_page = get_starting_page


@when("User opens the side menu")
def open_side_menu(test_context):
    main_page = test_context.main_page
    side_menu = main_page.open_side_hamburger_menu()
    test_context.side_menu = side_menu


@when("User opens the Judges Page")
def open_judges_page(test_context):
    side_menu = test_context.side_menu
    judges_page = side_menu.open_judges()
    if judges_page.check_first_screen("COMPETITION\nJUDGES"):
        test_context.judges_page = judges_page
    else:
        for _ in range(RETRY):
            judges_page = side_menu.open_judges()
            if judges_page.check_first_screen("JUDGES"):
                test_context.judges_page = judges_page
                break
        raise AssertionError("First screen text is not equal to expected")


@then("Number of testing judges is 6")
def get_testing_judges(test_context):
    judges_page = test_context.judges_page
    assert judges_page.check_judges_number(6, "testing"), "Number of testing judges is not equal to 6"
