# content of restfulbooker.feature
Feature: Restful booker
    Restful booker is a free to use API for practising testing

    Scenario: Create Token
        Given I enter username and password for authentication
        Then I get token to use in future requests

    Scenario: Health Check
        Given I do ping
        Then I get status code 201

    Scenario: Speed check
        Given I create token
        Then I get the time of creating token

