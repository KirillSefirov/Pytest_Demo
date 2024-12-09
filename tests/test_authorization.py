import http

import allure
import pytest

from utils import helper
from utils.user import User


class TestCreateAccount:

    @pytest.fixture()
    def test_users_list(self):
        test_users = []
        return test_users

    @pytest.fixture()
    def delete_test_users(self, base_url_users, request, test_users_list):
        yield
        helper.delete_test_users(usersClient=base_url_users, users=test_users_list)

    @allure.label("owner", "Dmitry Karasev")
    @allure.title("Test Registration")
    @allure.tag("API", "Regression", "Registration")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("first_name,last_name,email,password",
                             helper.get_valid_users_info(as_parameters=True))
    def test_new_post_register_new_user(self,
                                        test_users_list,
                                        base_url_users,
                                        first_name,
                                        last_name,
                                        email,
                                        password,
                                        delete_test_users):
        register_user_response = base_url_users.register_new_user(first_name,
                                                                  last_name,
                                                                  email,
                                                                  password)
        test_user_token = register_user_response.json()['token']
        test_users_list.append(User(first_name,
                                    last_name,
                                    email,
                                    password,
                                    test_user_token)
                               )
        user_profile = base_url_users.get_user_profile(token=test_user_token)
        assert register_user_response.status_code == http.HTTPStatus.CREATED, \
            f"response code should be 201, but was ${register_user_response.status_code}"
        assert user_profile.status_code == http.HTTPStatus.OK
