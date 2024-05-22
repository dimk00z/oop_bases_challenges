"Fake helpers."
from faker import Faker


def get_fake(seed: int | None = None) -> Faker:
    "Fake generator."
    if seed:
        Faker.seed(seed)
    return Faker("ru_RU")


def get_py_float(
    fake: Faker,
    min_value: float = 0.1,
    max_value: float = 1_000_000,
    right_digits: int = 2,
) -> float:
    "Get random float number."
    return fake.pyfloat(
        min_value=min_value,
        max_value=max_value,
        right_digits=right_digits,
    )
