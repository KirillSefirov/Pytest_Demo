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


# Fixture below stays as example of a general use of teardown
# @pytest.fixture()
# def test_users(base_url_users):
#     test_users = helper.get_test_users(base_url_users)
#     yield test_users
#     helper.delete_test_users(usersClient=base_url_users, users=test_users)


# Fixture contains finalizer to make sure to remove created test users in case of an error
@pytest.fixture()
def test_users(base_url_users, request):
    test_users = helper.get_test_users(base_url_users)

    def delete_test_users():
        helper.delete_test_users(usersClient=base_url_users, users=test_users)

    request.addfinalizer(delete_test_users)
    return test_users
