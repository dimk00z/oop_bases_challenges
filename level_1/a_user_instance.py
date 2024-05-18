"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""

from dataclasses import dataclass
from typing import get_type_hints

from faker import Faker


@dataclass
class User:
    "Simple user class"
    name: str
    username: str
    age: int
    phone: str

    def __str__(self) -> str:
        "String representation of the user."
        user_info = ", ".join((str(getattr(self, key))) for key in get_type_hints(self))
        return f"Информация о пользователе: {user_info}"


def get_fake_user(fake: Faker) -> User:
    "Fake user generator."
    return User(
        name=fake.user_name(),
        username=fake.name(),
        phone=fake.phone_number(),
        age=fake.pyint(min_value=18, max_value=99),
    )


def main() -> None:
    """Main function.

    Example poetry run python level_1/a_user_instance.py
    Информация о пользователе: apotapova, Меркушев Сократ Чеславович, 97, 8 475 938 24 21
    """
    Faker.seed(0)
    fake = Faker("ru_RU")
    user: User = get_fake_user(fake)
    print(user)


if __name__ == "__main__":
    main()
