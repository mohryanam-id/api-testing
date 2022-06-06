import pytest
from pytest_bdd import scenarios, given, then
import requests
 
# Scenarios
scenarios('../features/restfulbooker.feature')

# Get Token Scenario
@pytest.mark.xdist_group(name="core1")
@given("I enter username and password for authentication", target_fixture="request_result")
@given("I create token")
def enter_username_and_password():
    url = 'https://restful-booker.herokuapp.com/auth'
    payload = {
        'username' : 'admin',
        'password' : 'password123'
    }
    return requests.post(url, payload)

@pytest.mark.xdist_group(name="core1")
@then("I get token to use in future requests")
def get_token(request_result):
    assert request_result.json()['token'] is not None

# Health Check
@pytest.mark.xdist_group(name="core2")
@given("I do ping", target_fixture="request_result")
def enter_username_and_password():
    url = 'https://restful-booker.herokuapp.com/ping'
    return requests.get(url)

@pytest.mark.xdist_group(name="core2")
@then("I get status code 201")
def get_token(request_result):
    assert request_result.status_code == 201


# Speed Check
@pytest.mark.xdist_group(name="core1")
@then("I get the time of creating token")
def get_token(benchmark):
    result = benchmark(enter_username_and_password)
    assert result.status_code == 201