Feature: Login security
    Scenario: Successful login with proper credentials
        Given I am on the login page
        When I login with valid credentials
        Then I should see the homepage title