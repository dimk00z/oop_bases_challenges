"""
Задания:
    1. Cоздайте экземпляр класса студенда.
    2. Получите его полное имя используя метод get_full_name.
    3. Положите результат вызова метода get_full_name в переменную и распечатайте ее.
"""

from dataclasses import dataclass

from faker import Faker


@dataclass
class Student:
    """Simple student class"""

    name: str
    surname: str
    faculty: str
    course: int

    def get_full_name(self) -> str:
        """Returns student's full name"""
        return f"Student's full name: {self.surname}, {self.name}"


def get_fake_student(fake: Faker) -> Student:
    "Fake student generator."
    return Student(
        name=fake.first_name(),
        surname=fake.last_name(),
        faculty=fake.city(),
        course=fake.pyint(min_value=1, max_value=5),
    )


def main():
    "Main function."

    Faker.seed()
    fake = Faker("ru_RU")
    student: Student = get_fake_student(fake)
    student_full_name = student.get_full_name()
    print(student_full_name)


if __name__ == "__main__":
    main()
