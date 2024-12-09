import http

import allure
import pytest

from utils import helper


@allure.label("owner", "Dmitry Karasev")
@allure.title("Test User Removal")
@allure.tag("API", "Regression")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("first_name,last_name,email,password",
                         helper.get_valid_users_info(as_parameters=True))
def test_new_delete_registered_user(base_url_users, first_name, last_name, email, password):
    register_user_response = base_url_users.register_new_user(first_name, last_name, email, password)
    delete_user_response = base_url_users.delete_existing_user(email, password, register_user_response.json()['token'])
    assert delete_user_response.status_code == http.HTTPStatus.OK
    user_profile = base_url_users.get_user_profile(register_user_response.json()['token'])
    assert user_profile.status_code == http.HTTPStatus.UNAUTHORIZED
