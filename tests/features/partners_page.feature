Feature: Partners Page feature

  @mobile
  Scenario: Open Partners Page and check mobile partners
    Given The main page is open
    When User opens the side menu
    And User opens the Partners Page
    Then There is no Apple Inc in the partners’ list
