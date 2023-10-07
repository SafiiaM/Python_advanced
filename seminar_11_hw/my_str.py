"""
Задание 1

Создайте класс МояСтрока где будут доступны все возможности str и дополнительно хранится имя автора строки и время
создания (time.time)
"""
from datetime import time


class MyString(str):
    """Extending the str class."""

    def __new__(cls, value: str, author: str):
        """We extend the new method with the value and name parameters."""
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        return instance


def run_mystring():
    mystring = MyString('сама строка', 'доп. параметр')
    print(mystring.author)
    print(mystring.time)
    print(mystring)
    print(mystring.upper())
    print(mystring.title())
    help(mystring)
    help(MyString)


if __name__ == '__main__':
    run_mystring()

"""
Задание 3

# Добавьте к задачам 1 и 2 строки документации для классов.
import time


class MyString(str):
    '''Расширяемый класс str.'''


    def __new__(cls, value: str, name: str):
        '''Расширяеи метод new параметрами value и name.'''
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time.time()
        return instance


if __name__ == '__main__':
    mystr = MyString('САМА строка', 'доп. параметр')
    print(mystr.name)
    print(mystr.created_at)
    print(mystr)
    print(mystr.upper())
    help(mystr)
    help(MyString)
"""

