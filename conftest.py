import os

import pytest

from api.contacts_api import ContactsApiClient
from api.users_api import UsersApiClient
from utils import helper


@pytest.fixture(scope="session")
def base_url_users():
    return UsersApiClient(base_url=os.environ['BASE_URL'])


@pytest.fixture(scope="session")
def base_url_contacts():
    return ContactsApiClient(base_url=os.environ['BASE_URL'])


@pytest.fixture()
def test_users(base_url_users):
    test_users = helper.get_test_users(base_url_users)
    yield test_users
    print("OLOLO TEST USERS EXIST " + str(test_users))
    helper.delete_new_test_users(usersClient=base_url_users, users=test_users)
