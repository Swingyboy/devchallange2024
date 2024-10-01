Feature: Judges Page feature

  @desktop
  Scenario: Open Judges Page and check number of testing judges
    Given The main page is open
    When User opens the side menu
    And User opens the Judges Page
    Then Number of testing judges is 7