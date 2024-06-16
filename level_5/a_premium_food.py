"""
У нас есть базовый класс продукта, а так же есть миксин для продуктов питания, но нет класса для продуктов питания.

Задания:
    1. Нужно создать класс FoodProduct, который будет наследовать от классов Product и FoodProductMixin.
    2. У класса FoodProduct переопределить метод get_product_info, таким образом, чтобы если продукт премиальный, то в скобках
       в конце добавлялось слово Premium.
       Например: Product title: Avocado, price: 12 (Premium)'
    3. Создать экземпляр класс FoodProduct с ценой меньше 10 и вызвать у него метод get_product_info.
    4. Создать экземпляр класс FoodProduct с ценой больше 10 и вызвать у него метод get_product_info.
"""

from typing import Protocol


class Priced(Protocol):
    @property
    def price(self) -> float: ...


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_product_info(self):
        return f"Product title: {self.title}, price: {self.price}"


class FoodProductMixin:
    def is_premium_food(self: Priced):
        return self.price > 10


class FoodProduct(FoodProductMixin, Product):
    def get_product_info(self):
        product_info: str = super().get_product_info()
        if not self.is_premium_food():
            return product_info
        return f"{product_info} (Premium)"


if __name__ == "__main__":
    non_premium_product: FoodProduct = FoodProduct(
        "Гречка",
        price=5,
    )
    print(non_premium_product.get_product_info())
    premium_product: FoodProduct = FoodProduct(
        "Гречка элитная в пакете",
        price=11,
    )
    print(premium_product.get_product_info())
