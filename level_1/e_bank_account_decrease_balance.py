"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""

import logging
from dataclasses import dataclass

from faker import Faker

from helpers.fake import get_fake, get_py_float


@dataclass
class BankAccount:
    """Simple bank account class"""

    owner_full_name: str
    balance: float

    def increase_balance(self, income: float) -> None:
        """Increase balance by income"""
        self.balance += income

    def decrease_balance(self, income: float) -> None:
        """Decrease balance by income"""
        balance = self.balance
        balance -= income
        if balance < 0:
            raise ValueError("Balance can't be negative")
        self.balance = balance


def get_fake_bank_account(fake: Faker) -> BankAccount:
    "Fake bank account generator."
    return BankAccount(
        owner_full_name=fake.user_name(),
        balance=get_py_float(fake),
    )


def main():
    "Main function."

    fake: Faker = get_fake()

    bank_account: BankAccount = get_fake_bank_account(fake)
    print(f"{bank_account.balance=}")
    try:
        bank_account.decrease_balance(bank_account.balance + get_py_float(fake))
    except ValueError as ex:
        logging.error(ex)
    print(f"{bank_account.balance=}")


if __name__ == "__main__":
    main()
