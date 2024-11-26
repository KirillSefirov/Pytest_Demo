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
        print("User data" + str(user_data))
        response = self.session.post(self.base_url + "users", json=user_data, timeout=5)
        print("Response register new user" + str(response.json()))
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
        print("Delete user response" + str(response.status_code))
        print(f"User with email = ${email} was deleted")
        return response

    @allure.step("API. Logging in by existing user")
    def login_by_user(self, email, password, token):
        user_data = {
            'email': email,
            'password': password
        }
        print('Login user data ' + str(user_data))
        try:
            response = self.session.post(self.base_url + 'users/login', data=user_data, timeout=5)
            print("Login info status code " + str(response.status_code))
            print("Login info " + response.text)
        except HTTPError:
            print("Couldn't login by user because of an error")
            return None
        print(f"Logging in by user {email}")
        return response

    @allure.step("API. Logging out by existing user")
    def logout_by_user(self, email, token):
        headers = {
            'Authorization': "Bearer " + token
        }
        try:
            response = self.session.post(self.base_url + "users/logout", headers=headers, timeout=5)
        except HTTPError:
            print("Couldn't log out by the user because of an error")
            return None
        return response

    @allure.step("API. Getting existing user profile")
    def get_user_profile(self, token):
        headers = {
            "Authorization": "Bearer " + token
        }
        try:
            response = self.session.get(self.base_url + "users/me", headers=headers, timeout=5)
        except HTTPError:
            print("Couldn't get user profile because of an error")
            return None
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
        try:
            response = self.session.patch(self.base_url + "users/me", data=user_data, headers=headers, timeout=5)
        except HTTPError:
            print("Couldn't update user profile because of an error")
            return None
        nf = response.json()["firstName"]
        nl = response.json()["lastName"]
        print(f"User names were updated to {nf} and {nl}")
        return response
