"""
У нас есть класс формы и метод для валидации в нем. Мы хотим создать форму для авторизации, где нам важно чтобы юзернэйм
существовал в базе данных

Задания:
    1. Напишите логику метода valid_form в классе AuthorizationFormMixin таким образом, чтобы там была проверка и из
       класса Form и проверка на то что юзернэйм есть в списке USERNAMES_IN_DB. Нужно использовать super() в этом методе
    2. Создайте класс AuthorizationForm, который будет наследником и от Form и от AuthorizationFormMixin
    3. Создайте экземпляр класса AuthorizationForm и вызовите у него метод valid_form. Должны отрабатывать обе проверки:
       и на длину пароля и на наличия юзернэйма в базе
"""

from random import choice
from typing import Protocol

USERNAMES_IN_DB = [
    "Alice_2023",
    "BobTheBuilder",
    "CrazyCoder",
    "DataDiva",
    "EpicGamer",
    "JavaJunkie",
]


class ValidableUserForm(Protocol):
    def valid_form(self) -> bool: ...

    @property
    def username(self) -> str: ...


class Form:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def valid_form(self) -> bool:
        return len(self.password) > 8

    def __str__(self) -> str:
        return self.username


class AuthorizationFormMixin:
    def valid_form(self: ValidableUserForm) -> bool:
        if not super().valid_form():
            return False
        return self.username in USERNAMES_IN_DB


class AuthorizationForm(
    AuthorizationFormMixin,
    Form,
):
    pass


# писать код тут


if __name__ == "__main__":
    correct_password = "password123"
    incorrect_password = "pas"
    for user_name, password in (
        (choice(USERNAMES_IN_DB), correct_password),
        (choice(USERNAMES_IN_DB), incorrect_password),
        ("user", incorrect_password),
        ("user", correct_password),
    ):
        user_info: AuthorizationForm = AuthorizationForm(
            username=user_name,
            password=password,
        )
        print(f"User info {user_info} is correct {user_info.valid_form()}")
