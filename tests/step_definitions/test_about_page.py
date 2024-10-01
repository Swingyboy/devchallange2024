import pytest
from pytest_bdd import scenarios, given, when, then

scenarios("../features/about_page.feature")

RETRY = 3

@given("The main page is open")
def open_website(get_starting_page, test_context):
    test_context.main_page = get_starting_page


@when("User opens the side menu")
def open_side_menu(test_context):
    main_page = test_context.main_page
    side_menu = main_page.open_side_hamburger_menu()
    test_context.side_menu = side_menu


@when("User opens the About Page")
def open_about_page(test_context):
    side_menu = test_context.side_menu
    about_page = side_menu.open_about()
    if about_page.check_first_screen("CHALLENGE\nYOURSELF\n& WIN"):
        test_context.about_page = about_page
    else:
        for _ in range(RETRY):
            about_page = side_menu.open_about()
            if about_page.check_first_screen("CHALLENGE\nYOURSELF\n& WIN"):
                test_context.about_page = about_page
                break
        raise AssertionError("First screen text is not equal to expected")


@when("User scrolls down to the bottom of the page")
def scroll_down_to_the_bottom(test_context):
    about_page = test_context.about_page
    about_page.scroll_to_footer()


@then("Contact mail is hello@devchallenge.it")
def check_footer_email(test_context):
    about_page = test_context.about_page
    footer_email = about_page.get_footer_email()
    assert footer_email == "hello@devchallenge.it", f"Footer email {footer_email} is not equal to expected hello@devchallenge.it"