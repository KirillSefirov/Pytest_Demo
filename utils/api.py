import requests

user_tokens = {}

s = requests.Session()


def register_new_user(base_url, first_name, last_name, email, password):
    user_data = {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password
    }
    response = s.post(base_url + "users", json=user_data, timeout=5)
    user_tokens[email] = response.json()['token']
    print(f"user with email = ${email} was created")
    return response


def delete_existing_user(base_url, email, password):
    user_data = {
        "email": email,
        "password": password
    }
    headers = {
        "Authorization": "Bearer " + user_tokens[email]
    }
    response = s.delete(base_url + "users/me", data=user_data, headers=headers, timeout=5)
    print(f"user with email = ${email} was deleted")
    return response


def login_by_user(base_url, email, password):
    user_data = {
        'email': email,
        'password': password
    }
    response = s.post(base_url + 'users/login', data=user_data, timeout=5)
    user_tokens[email] = response.json()['token']
    return response


def logout_by_user(base_url, email):
    headers = {
        'Authorization': "Bearer " + user_tokens[email]
    }
    response = s.post(base_url + "users/logout", headers=headers, timeout=5)
    return response


def get_user_profile(base_url, email):
    headers = {
        "Authorization": "Bearer " + user_tokens[email]
    }
    response = s.get(base_url + "users/me", headers=headers, timeout=5)
    return response


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

    response = s.patch(base_url + "users/me", data=user_data, headers=headers, timeout=5)
    nf = response.json()["firstName"]
    nl = response.json()["lastName"]
    print(f"User names were updated to {nf} and {nl}")
    return response
