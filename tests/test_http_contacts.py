import http
import allure
from api import contacts_api
import subprocess

@allure.label("owner", "Dmitry Karasev")
@allure.title("Test Post Add New Contact")
@allure.tag("API", "Regression", "Registration")
@allure.severity(allure.severity_level.CRITICAL)
def test_post_add_new_contact(base_url, test_users):
    for user in test_users:
        add_contact_response = contacts_api.add_contact(base_url, user["email"])
        assert add_contact_response.status_code == http.HTTPStatus.CREATED

def test_get():
    assert 0

def test_put():
    assert 0

def test_delete():
    assert 0

def test_patch():
    assert 0
