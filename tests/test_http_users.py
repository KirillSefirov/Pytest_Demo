import http
import pytest
import allure
from utils import helper


@allure.label("owner", "Dmitry Karasev")
@allure.title("Test Registration")
@allure.tag("API", "Regression", "Registration")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("first_name,last_name,email,password",
                         helper.get_valid_users_raw_info_from_file_as_parameters())
def test_post_register_new_user(base_url_users, first_name, last_name, email, password):
    register_user_response = base_url_users.register_new_user(first_name, last_name, email, password)
    assert register_user_response.status_code == http.HTTPStatus.CREATED, \
        f"response code should be 201, but was ${register_user_response.status_code}"
    user_profile = base_url_users.get_user_profile(email)
    assert user_profile.status_code == http.HTTPStatus.OK
    base_url_users.delete_existing_user(email, password)


@allure.label("owner", "Dmitry Karasev")
@allure.title("Test User Removal")
@allure.tag("API", "Regression")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("first_name,last_name,email,password",
                         helper.get_valid_users_raw_info_from_file_as_parameters())
def test_delete_registered_user(base_url_users, first_name, last_name, email, password):
    base_url_users.register_new_user(first_name, last_name, email, password)
    delete_user_response = base_url_users.delete_existing_user(email, password)
    assert delete_user_response.status_code == http.HTTPStatus.OK
    user_profile = base_url_users.get_user_profile(email)
    assert user_profile.status_code == http.HTTPStatus.UNAUTHORIZED


@allure.label("owner", "Dmitry Karasev")
@allure.title("Test Get User Profile")
@allure.tag("API", "Regression", "Registration")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_user_profile(base_url_users, test_users):
    for user in test_users:
        response = base_url_users.get_user_profile(user['email'])
        assert user['email'] == response.json()['email']


@allure.label("owner", "Dmitry Karasev")
@allure.title("Test Update User Profile")
@allure.tag("API", "Regression")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("new_first_name,new_last_name",
                         helper.get_first_and_last_names_as_parameters())
def test_patch_update_user_profile(base_url_users, test_users, new_first_name, new_last_name):
    for user in test_users:
        user_info = base_url_users.get_user_profile(user["email"])
        assert user_info.json()["firstName"] != new_first_name
        assert user_info.json()["lastName"] != new_last_name
        update_response = base_url_users.update_user_data(new_first_name,
                                                          new_last_name,
                                                          user["email"],
                                                          user["password"])
        assert update_response.status_code == http.HTTPStatus.OK
        assert update_response.json()["firstName"] == new_first_name
        assert update_response.json()["lastName"] == new_last_name
        updated_user_info = base_url_users.get_user_profile(user["email"])
        assert updated_user_info.json()["firstName"] == new_first_name
        assert updated_user_info.json()["lastName"] == new_last_name


def test_put():
    pass
