"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

from dataclasses import dataclass

SURNAMES_TO_BAN = ["Vaughn", "Wilhelm", "Santaros", "Porter", "Smith"]


@dataclass
class User:
    name: str
    surname: str
    age: int

    def should_be_banned(self) -> bool:
        return self.surname in SURNAMES_TO_BAN
