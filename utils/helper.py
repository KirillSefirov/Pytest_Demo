import csv


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


# a = get_valid_users_from_file_as_parameters()
# print(a)