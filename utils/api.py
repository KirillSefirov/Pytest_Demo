import requests

base_url = "https://thinking-tester-contact-list.herokuapp.com/"


def register_new_user(first_name, last_name, email, password):
    user_data = {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password
    }
    print(user_data)
    response = requests.post(base_url + "users", json=user_data)

    print(response.text)
    return response

