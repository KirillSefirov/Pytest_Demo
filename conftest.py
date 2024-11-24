import pytest

from utils import helper

user_tokens = {}


@pytest.fixture(scope="session")
def base_url():
    return "https://thinking-tester-contact-list.herokuapp.com/"

@pytest.fixture()
def test_users(base_url):
    helper.create_test_users(base_url)
    yield helper.created_users
    helper.delete_test_users(base_url)
