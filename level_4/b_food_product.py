"""
У нас есть класс Product, который подходит для многих продуктов, но не для еды.
В пищевом продукте нам нужно хранить еще срок годности, который будет влиять и на другие методы

Задания:
    1. Переопределите частично метод __init__ у FoodProduct так, чтобы там хранилось еще свойство expiration_date.
       Используйте super() для этого.
    2. Переопределите у FoodProduct полностью метод get_full_info, чтобы он возвращал еще и информацию о сроке годности
    3. Переопределите частично метод is_available у FoodProduct, чтобы там учитывался еще и срок годности. Если он
       меньше чем текущая дата - то is_available должен возвращать False. Используйте super() для этого.
    3. Создайте экземпляры каждого из двух классов и вызовите у них все доступные методы
"""

from datetime import datetime, timedelta
from pprint import pprint


class Product:
    def __init__(self, title: str, quantity: int) -> None:
        self.title = title
        self.quantity = quantity

    def get_full_info(self) -> str:
        return f"Product {self.title}, {self.quantity} in stock."

    def is_available(self):
        return self.quantity > 0

    def __str__(self) -> str:
        return self.title


class FoodProduct(Product):
    def __init__(self, title: str, quantity: int, expiration_date: datetime):
        super().__init__(
            title,
            quantity,
        )
        self.expiration_date = expiration_date

    def is_available(self):
        return super().is_available() and self.expiration_date >= datetime.now()


def main():
    simple_product: Product = Product(
        title="simple_product",
        quantity=1,
    )
    pprint(f"{simple_product} is available {simple_product.is_available()}")
    simple_product.quantity = 0
    pprint(f"{simple_product} is available {simple_product.is_available()}")

    food_product: Product = FoodProduct(
        title="food_product",
        quantity=1,
        expiration_date=datetime.now() + timedelta(days=3),
    )
    pprint(f"{food_product} is available {food_product.is_available()}")
    food_product.expiration_date = datetime.now()
    pprint(f"{food_product} is available {food_product.is_available()}")


if __name__ == "__main__":
    main()
