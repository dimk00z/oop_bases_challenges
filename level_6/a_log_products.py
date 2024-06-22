"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""

from loguru import logger


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self):
        return f"Product {self.title} with price {self.price}"

    def __str__(self) -> str:
        return self.get_info()


class PrintLoggerMixin:
    def log(self, message: str) -> None:
        logger.info(message)


class PremiumProduct(PrintLoggerMixin, Product):
    def increase_price(self):
        self.price *= 1.2
        self.log(message=f"Price increased, price={self.price}")

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} (Premium)"


class DiscountedProduct(PrintLoggerMixin, Product):
    def decrease_price(self):
        self.price /= 1.2
        self.log(message=f"Price decreased, price={self.price}")

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} (Discounted)"


if __name__ == "__main__":
    premium_product: PremiumProduct = PremiumProduct(
        title="Топовая гречка",
        price=999,
    )
    premium_product.increase_price()

    discounted_product: DiscountedProduct = DiscountedProduct(
        title="Моя гречка",
        price=37,
    )
    discounted_product.decrease_price()
