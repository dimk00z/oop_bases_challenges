"""
Банк позволяет уходить в минус по счету, чтобы клиенты не оказывались в без денег в самый неподходящий момент

Задания:
    1. Напишите логику метода decrease_balance таким образом, чтобы можно было уменьшать баланс, но чтобы он не становился
       меньше чем значение в атрибуте класса min_balance. Если он будет меньше - вызывайте исключение ValueError
    2. Создайте экземпляр класса BankAccount, вызовите у него метод decrease_balance и убедитесь, что баланс уменьшается
       и если он уменьшается больше чем можно, то вызывается исключение
"""


class BankAccount:
    min_balance = -100

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def decrease_balance(self, amount: float):
        decreased_balance = self.balance - amount
        if decreased_balance < BankAccount.min_balance:
            raise ValueError("Couldn't decreased balance")
        self.balance = decreased_balance

    def __str__(self) -> str:
        return f"{self.owner}'s balance - {self.balance}"


if __name__ == "__main__":
    account: BankAccount = BankAccount(
        owner="The Master",
        balance=200,
    )
    print(account)
    for amount in (100, 200, 400):
        try:
            account.decrease_balance(amount)
        except ValueError as ex:
            print(ex)
        finally:
            print(account)
