import requests
import allure
from api.users_api import user_tokens

@allure.step("API. Adding a new contact to existing user")
def add_contact(base_url, user_email):
    contact_info = {
        "firstName": "Kirill",
        "lastName": "Sefirov",
        "birthdate": "1970-01-01",
        "email": "jdoe@fake.com",
        "phone": "8005555555",
        "street1": "1 Main St.",
        "street2": "Apartment A",
        "city": "New York",
        "stateProvince": "KS",
        "postalCode": "12345",
        "country": "USA"
    }
    headers = {
        "Authorization": "Bearer " + user_tokens[user_email]
    }
    print("Contacts user email " + user_email)
    print("Contacts user token " + user_tokens[user_email])
    print("Contact info " + str(contact_info))
    response = requests.post(base_url + "contacts", json=contact_info, headers=headers)
    print("Request info " + str(response.request.body))
    print("Request info " + response.request.url)
    print("Request info " + str(response.request.headers))
    print(response.json())
    return response


class Contacts:
    pass
