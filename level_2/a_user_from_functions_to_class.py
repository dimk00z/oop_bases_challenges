""" "
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""

from dataclasses import dataclass


@dataclass
class User:
    username: str
    user_id: int
    name: str

    def generate_short_user_description(self) -> str:
        return f"User with id {self.user_id} has {self.username} username and {self.name} name"

    def make_username_capitalized(self):
        self.username = self.username.capitalize()
        return self.username
