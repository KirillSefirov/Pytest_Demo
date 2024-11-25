import pytest

from api.contacts_api import ContactsApiClient
from api.users_api import UsersApiClient
from utils import helper

user_tokens = {}


@pytest.fixture(scope="session")
def base_url_users():
    return UsersApiClient(base_url="https://thinking-tester-contact-list.herokuapp.com/")


@pytest.fixture(scope="session")
def base_url_contacts():
    return ContactsApiClient(base_url="https://thinking-tester-contact-list.herokuapp.com/")


@pytest.fixture()
def test_users(base_url_users):
    helper.create_test_users(base_url_users)
    yield helper.created_users
    helper.delete_test_users(base_url_users)
