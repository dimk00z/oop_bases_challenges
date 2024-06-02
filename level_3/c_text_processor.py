"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""

from helpers.fake import get_fake


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f"Total text length: {len(self.text)}"

    @property
    def text_length(self) -> int:
        return len(self.text)


class AdvancedTextProcessor(TextProcessor):
    @property
    def words_number(self) -> int:
        return len(self.text.split())

    def summarize(self):
        return f"Total text length: {self.text_length}, total number of words in the text: {self.words_number}"

    # код писать тут


def main():
    fake = get_fake()
    text = fake.text()

    text_processor = TextProcessor(text)
    print(text_processor.to_upper())
    print(text_processor.summarize())

    advanced_text_processor = AdvancedTextProcessor(text)
    print(advanced_text_processor.to_upper())
    print(advanced_text_processor.summarize())


if __name__ == "__main__":
    main()
