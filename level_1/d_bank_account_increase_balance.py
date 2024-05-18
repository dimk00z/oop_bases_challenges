"""
У нас есть класс банковского аккаунта со свойствами: полное имя владельца и баланс, но не реализован
метод, который увеличивает баланс.

Задания:
    1. Допишите логику в метод increase_balance, который должен увеличивать баланс банковского счета на значение income.
    2. Создайте экземпляр класса банковского счета и распечатайте баланс.
    3. Увеличьте баланс счета у экземпляра класса с помощью метода increase_balance и снова распечатайте текущий баланс.
"""

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


def get_fake_bank_account(fake: Faker) -> BankAccount:
    "Fake bank account generator."
    return BankAccount(owner_full_name=fake.user_name(), balance=get_py_float(fake))


def main():
    "Main function."

    fake: Faker = get_fake()

    bank_account: BankAccount = get_fake_bank_account(fake)
    print(f"{bank_account.balance=}")

    bank_account.increase_balance(get_py_float(fake))

    print(f"{bank_account.balance=}")


if __name__ == "__main__":
    main()
