import csv
import os
from dataclasses import astuple

import allure

from api.users_api import UsersApiClient
from utils.user import User

created_users = []


@allure.step("Helper. Getting raw valid user info from file")
def get_valid_users_from_file():
    with open("resources/valid_users_list.csv", newline='') as valid_users_file:
        csv_reader = csv.DictReader(valid_users_file)
        users = [row for row in csv_reader]
    return users


@allure.step("Helper. Getting raw invalid user info from file")
def get_invalid_users_from_file():
    with open("resources/invalid_users_list.csv", newline='') as invalid_users_file:
        csv_reader = csv.DictReader(invalid_users_file)
        users = [row for row in csv_reader]
        return users


@allure.step("Helper. Getting raw valid user info from file as parameter")
def get_valid_users_raw_info_from_file_as_parameters():
    with open("resources/valid_users_list_no_header.csv", newline='') as valid_users_file:
        csv_reader = csv.reader(valid_users_file)
        users = [row for row in csv_reader]
        for i in range(0, len(users)):
            users[i] = tuple(users[i])
    return users


@allure.step("Helper. Getting raw valid user First and Last names from file")
def get_first_and_last_names_as_parameters():
    with open("resources/first_and_last_names.csv", newline='') as first_and_last_names_file:
        csv_reader = csv.reader(first_and_last_names_file)
        names = [row for row in csv_reader]
        for i in range(0, len(names)):
            names[i] = tuple(names[i])
    return names


def get_test_users(usersClient):
    list_of_users_info = get_valid_users_from_file()
    list_of_users = []
    for user_info in list_of_users_info:
        list_of_users.append(User(user_info["first_name"],
                                  user_info["last_name"],
                                  user_info["email"],
                                  user_info["password"]))
    for user in list_of_users:
        response = usersClient.register_new_user(user.first_name, user.last_name, user.email, user.password)
        user.token = response.json()['token']
    return list_of_users


def get_test_users_as_parameters():
    users_client = UsersApiClient(base_url=os.environ['BASE_URL'])
    users = get_test_users(users_client)
    list_of_tuples = []
    for user in users:
        list_of_tuples.append(astuple(user))
    return list_of_tuples


@allure.step("Helper. Deleting test users using api")
def delete_new_test_users(usersClient, users):
    for user in users:
        usersClient.delete_existing_user(email=user.email,
                                         password=user.password,
                                         token=user.token
                                         )
