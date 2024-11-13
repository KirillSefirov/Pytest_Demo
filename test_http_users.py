import http
import pytest
import utils.api as api
import utils.helper as helper


@pytest.mark.parametrize("first_name,last_name,email,password", [("kir", "sef", "aasdfzzazsdad@gmail.com", "12345678"),
                                                                 ("sir", "john", "basdfazaaklndvv@yandex.ru", "87654321")
                                                                 ])
def test_post_register_new_usera(first_name, last_name, email, password):
    response = api.register_new_user(first_name, last_name, email, password)
    assert response.status_code == http.HTTPStatus.CREATED


@pytest.mark.parametrize("first_name,last_name,email,password", helper.get_valid_users_from_file_as_parameters())
def test_post_register_new_user(first_name, last_name, email, password):
    response = api.register_new_user(first_name, last_name, email, password)
    assert response.status_code == http.HTTPStatus.CREATED

def test_get():
    return 0


def test_put():
    return 0

def test_delete():
    return 0

def test_patch():
    return 0

