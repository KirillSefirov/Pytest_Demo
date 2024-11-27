import requests
import allure
from api.users_api import UsersApiClient


class ContactsApiClient(UsersApiClient):

    @allure.step("API. Adding a new contact to existing user")
    def add_contact(self, token):
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
            "Authorization": "Bearer " + token
        }
        response = requests.post(self.base_url + "contacts", json=contact_info, headers=headers)
        return response
