# Ваша задача:
#
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях
# (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать исключения
# InvalidNameError и InvalidAgeError, если данные неверные.
#
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер
# (ID). Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
#
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
#
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID
# (по остатку от деления на 7).
#
# Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно
# при передаче неверных данных.
class Errors(ValueError):
    pass


class InvalidNameError(Errors):
    pass


class InvalidAgeError(Errors):
    pass


class Person:

    def __init__(self, name, surname, second_name, age):
        if name == '':
            raise InvalidNameError(f'Invalid name: {name}. Name should be a non-empty string.')
        elif surname == '':
            raise InvalidNameError(f'Invalid name: {name}. Name should be a non-empty string.')
        elif second_name == '':
            raise InvalidNameError(f'Invalid name: {name}. Name should be a non-empty string.')
        else:
            self.mane = name
            self.surname = surname
            self.second_name = second_name
        if age <= 0:
            raise InvalidAgeError(f'Invalid age: {age}. Age should be a positive integer.')
        else:
            self.age = age

    def get_age(self):
        return self.age



class InvalidIdError(Errors):
    pass


class Employee(Person):
    def __init__(self, surname, name, second_name, age, user_id):
        super().__init__(surname, name, second_name, age)
        if user_id < 100000:
            raise InvalidIdError(f'Invalid id: {user_id}. Id should be a 6-digit positive integer between 100000 and 999999.')
        self.user_id = user_id
        self.user_access = int(sum(list(map(int, str(user_id)))) % 7)

    def get_age(self):
        return self.age