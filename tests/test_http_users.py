import http

import allure
import pytest

from utils import helper


@allure.label("owner", "Dmitry Karasev")
@allure.title("Test Get User Profile")
@allure.tag("API", "Regression", "Registration")
@allure.severity(allure.severity_level.CRITICAL)
def test_new_get_user_profile(base_url_users, test_users):
    for user in test_users:
        response = base_url_users.get_user_profile(user.token)
        assert user.email == response.json()['email']


@allure.label("owner", "Dmitry Karasev")
@allure.title("Test Update User Profile")
@allure.tag("API", "Regression")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("new_first_name,new_last_name",
                         helper.get_first_and_last_names_as_parameters())
def test_new_patch_update_user_profile(base_url_users, test_users, new_first_name, new_last_name):
    for user in test_users:
        update_response = base_url_users.update_user_data(new_first_name,
                                                          new_last_name,
                                                          user.email,
                                                          user.password,
                                                          user.token)
        updated_user_info = base_url_users.get_user_profile(user.token)
        assert update_response.status_code == http.HTTPStatus.OK
        assert update_response.json()["firstName"] == new_first_name
        assert update_response.json()["lastName"] == new_last_name

        assert updated_user_info.json()["firstName"] == new_first_name
        assert updated_user_info.json()["lastName"] == new_last_name


def test_new_put():
    pass
