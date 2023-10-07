"""
Задание 2

Создайте класс Архив, который хранит пару свойств. Например, число и строку. Для нового экземпляра класса, старые данные
из ранее созданных экземпляров сохраняются в пару списков-архивов, которые также являются свойствами экземпляра.
"""

"""
Задание 4 

Доработаем класс Архив из задачи 2. Добавьте методы представления
экземпляра для программиста и для пользователя.
"""


class Archive:
    """ We store the data of each instance of the class in the lists numbers and values. """
    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        """ Overridden the new method to save arguments to lists. """
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        """Defined a method for initializing an instance of a class."""
        self.number = number
        self.value = value

    def __repr__(self):
        return f'Archive({self.number}, "{self.value}")'

    def __str__(self):
        return f'Номер: {self.number}, Значение: "{self.value}"'


def run_archive():
    a_1 = Archive(1, "Один")
    a_2 = Archive(2, "Два")
    print(f'{a_1.numbers} {a_1.values}')
    print(f'{a_2.numbers} {a_2.values}')
    a_3 = Archive(3, "Три")
    print(f'{a_3.numbers} {a_3.values}')
    help(a_1)
    print(a_1.__repr__())
    print(f'{a_1 = }')
    print(a_1)
    help(Archive)


if __name__ == '__main__':
    run_archive()
