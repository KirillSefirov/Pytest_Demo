from dataclasses import dataclass


@dataclass()
class User:
    first_name: str
    last_name: str
    email: str
    password: str
    token: str = ''
