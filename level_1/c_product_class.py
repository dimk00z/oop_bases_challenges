"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import get_type_hints

from faker import Faker

from helpers.fake import get_fake


@dataclass
class Product:
    "Simple product class"

    name: str
    description: str
    price: Decimal
    weight: float

    def __str__(self) -> str:
        "String representation of the product."
        product_info = ", ".join(
            (str(getattr(self, key))) for key in get_type_hints(self)
        )
        return f"Информация о продукте: {product_info}"


def get_fake_product(fake: Faker) -> Product:
    "Fake product generator."
    return Product(
        name=fake.name(),
        description=fake.text(),
        price=fake.pydecimal(
            positive=True,
            min_value=0.1,
            max_value=1_000_000,
            right_digits=2,
        ),
        weight=fake.pyfloat(
            min_value=0.1,
            max_value=1_000,
            right_digits=2,
        ),
    )


def main():
    "Main function."
    fake: Faker = get_fake()
    product: Product = get_fake_product(fake)
    print(product)


if __name__ == "__main__":
    main()
