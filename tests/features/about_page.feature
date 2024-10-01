Feature: About Page feature

  @desktop
  Scenario: Open About Page and check email
    Given The main page is open
    When User opens the side menu
    And User opens the About Page
    And User scrolls down to the bottom of the page
    Then Contact mail is hello@devchallenge.it