import pytest
import utils.helper as helper

user_tokens = {}


@pytest.fixture(scope="session")
def base_url():
    return "https://thinking-tester-contact-list.herokuapp.com/"


@pytest.fixture(scope="session")
def test_users(base_url):
    helper.create_test_users(base_url)
    yield helper.created_users
    helper.delete_test_users(base_url)


def delete_test_users():
    helper.delete_test_users(base_url)

# TODO fill custom assertion messages
