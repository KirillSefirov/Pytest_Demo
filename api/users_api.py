import requests
from requests import HTTPError
import allure

user_tokens = {}

s = requests.Session()


@allure.step("API. Registering new user")
def register_new_user(base_url, first_name, last_name, email, password):
    user_data = {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password
    }
    try:
        response = s.post(base_url + "users", json=user_data, timeout=5)
    except HTTPError:
        print("Couldn't register a new user because of an error")
        return None
    user_tokens[email] = response.json()['token']
    print("User tokens from users " + user_tokens[email])
    print(f"user with email = ${email} was created")
    return response

@allure.step("API. Deleting existing user")
def delete_existing_user(base_url, email, password):
    user_data = {
        "email": email,
        "password": password
    }
    headers = {
        "Authorization": "Bearer " + user_tokens[email]
    }
    try:
        response = s.delete(base_url + "users/me", data=user_data, headers=headers, timeout=5)
    except HTTPError:
        print("Couldn't delete existing user because of an error")
        return None
    print(f"User with email = ${email} was deleted")
    return response

@allure.step("API. Logging in by existing user")
def login_by_user(base_url, email, password):
    user_data = {
        'email': email,
        'password': password
    }
    print('Login user data ' + str(user_data))
    try:
        response = s.post(base_url + 'users/login', data=user_data, timeout=5)
        print("Login info status code " + str(response.status_code))
        print("Login info " + response.text)
    except HTTPError:
        print("Couldn't login by user because of an error")
        return None
    print(f"Logging in by user {email}")
    user_tokens[email] = response.json()['token']
    return response

@allure.step("API. Logging out by existing user")
def logout_by_user(base_url, email):
    headers = {
        'Authorization': "Bearer " + user_tokens[email]
    }
    try:
        response = s.post(base_url + "users/logout", headers=headers, timeout=5)
    except HTTPError:
        print("Couldn't log out by the user because of an error")
        return None
    return response

@allure.step("API. Getting existing user profile")
def get_user_profile(base_url, email):
    headers = {
        "Authorization": "Bearer " + user_tokens[email]
    }
    try:
        response = s.get(base_url + "users/me", headers=headers, timeout=5)
    except HTTPError:
        print("Couldn't get user profile because of an error")
        return None
    return response

@allure.step("API. Updating existing user data")
def update_user_data(base_url, new_first_name, new_last_name, email, password):
    print(f"Updating user names to {new_first_name} and {new_last_name}")
    user_data = {
        "firstName": new_first_name,
        "lastName": new_last_name,
        "email": email,
        "password": password
    }
    headers = {
        "Authorization": "Bearer " + user_tokens[email]
    }
    try:
        response = s.patch(base_url + "users/me", data=user_data, headers=headers, timeout=5)
    except HTTPError:
        print("Couldn't update user profile because of an error")
        return None
    nf = response.json()["firstName"]
    nl = response.json()["lastName"]
    print(f"User names were updated to {nf} and {nl}")
    return response
