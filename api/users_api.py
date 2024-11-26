import logging
from logging import DEBUG

import allure
import requests
from requests import HTTPError


class UsersApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    # s = requests.Session()

    @allure.step("API. Registering new user")
    def register_new_user(self, first_name, last_name, email, password):
        user_data = {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "password": password
        }
        response = self.session.post(self.base_url + "users", json=user_data, timeout=5)
        logging.log(level=logging.DEBUG, msg=response.text)
        print(f"user with email = ${email} was created")
        return response

    @allure.step("API. Deleting existing user")
    def delete_existing_user(self, email, password, token):
        user_data = {
            "email": email,
            "password": password
        }
        headers = {"Authorization": "Bearer " + token}

        response = self.session.delete(self.base_url + "users/me", data=user_data, headers=headers, timeout=5)
        logging.log(level=logging.DEBUG, msg=response.text)
        print(f"User with email = ${email} was deleted")
        return response

    @allure.step("API. Logging in by existing user")
    def login_by_user(self, email, password, token):
        user_data = {
            'email': email,
            'password': password
        }
        response = self.session.post(self.base_url + 'users/login', data=user_data, timeout=5)
        logging.log(level=logging.DEBUG, msg=response.text)
        print(f"Logged in by user {email}")
        return response

    @allure.step("API. Logging out by existing user")
    def logout_by_user(self, token):
        headers = {
            'Authorization': "Bearer " + token
        }
        response = self.session.post(self.base_url + "users/logout", headers=headers, timeout=5)
        logging.log(level=logging.DEBUG, msg=response.text)
        return response

    @allure.step("API. Getting existing user profile")
    def get_user_profile(self, token):
        headers = {
            "Authorization": "Bearer " + token
        }
        response = self.session.get(self.base_url + "users/me", headers=headers, timeout=5)
        logging.log(level=logging.DEBUG, msg=response.text)
        return response

    @allure.step("API. Updating existing user data")
    def update_user_data(self, new_first_name, new_last_name, email, password, token):
        print(f"Updating user names to {new_first_name} and {new_last_name}")
        user_data = {
            "firstName": new_first_name,
            "lastName": new_last_name,
            "email": email,
            "password": password
        }
        headers = {
            "Authorization": "Bearer " + token
        }
        response = self.session.patch(self.base_url + "users/me", data=user_data, headers=headers, timeout=5)
        logging.log(level=logging.DEBUG, msg=response.text)
        nf = response.json()["firstName"]
        nl = response.json()["lastName"]
        print(f"User names were updated to {nf} and {nl}")
        return response
