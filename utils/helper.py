import csv
import utils.api as api

created_users = []


def get_valid_users_from_file():
    with open("resources/valid_users_list.csv", newline='') as valid_users_file:
        csv_reader = csv.DictReader(valid_users_file)
        users = [row for row in csv_reader]
    return users


def get_invalid_users_from_file():
    with open("resources/invalid_users_list.csv", newline='') as invalid_users_file:
        csv_reader = csv.DictReader(invalid_users_file)
        users = [row for row in csv_reader]
        return users


def get_valid_users_from_file_as_parameters():
    with open("resources/valid_users_list_no_header.csv", newline='') as valid_users_file:
        csv_reader = csv.reader(valid_users_file)
        users = [row for row in csv_reader]
        for i in range(0, len(users)):
            users[i] = tuple(users[i])
    return users


def get_first_and_last_names_as_parameters():
    with open("resources/first_and_last_names.csv", newline='') as first_and_last_names_file:
        csv_reader = csv.reader(first_and_last_names_file)
        names = [row for row in csv_reader]
        for i in range(0, len(names)):
            names[i] = tuple(names[i])
    return names


def create_test_users(base_url):
    list_of_users = get_valid_users_from_file_as_parameters()
    for user in list_of_users:
        api.register_new_user(base_url,
                              first_name=user[0],
                              last_name=user[1],
                              email=user[2],
                              password=user[3]
                              )
        print(f"User with email = ${user[2]} was created")
        created_users.append(
            {
                "first_name": user[0],
                "last_name": user[1],
                "email": user[2],
                "password": user[3]
            }
        )


def delete_test_users(base_url):
    list_of_users = get_valid_users_from_file_as_parameters()
    for user in list_of_users:
        api.delete_existing_user(base_url,
                                 email=user[2],
                                 password=user[3]
                                 )
