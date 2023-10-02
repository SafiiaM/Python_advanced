"""
Задание 4

Создайте класс Сотрудник. Воспользуйтесь классом человека из прошлого задания. У сотрудника должен быть шестизначный
идентификационный номер и уровень доступа вычисляемый как остаток от деления суммы цифр id на семь).
"""
import random

from Human import Human


def _gen_number():
    MIN_NUM = 100000
    MAX_NUM = 1000000
    return random.randint(MIN_NUM, MAX_NUM)


class Employee(Human):
    def __init__(self, ocupation: str, firstname: str, lastname: str, age: int, gender: str):
        super().__init__(firstname, lastname, age, gender)
        self.emp_id = _gen_number()
        self.sec_level = self._secure_level()
        self.ocupation = ocupation

    @staticmethod
    def _secure_level():
        sec_id = _gen_number()
        LEVEL_NUM = 7
        level_num = 0
        while sec_id > 0:
            last_num = sec_id % 10
            level_num += last_num
            sec_id /= 10
        return int(level_num % LEVEL_NUM)

    def __str__(self):
        return f'ID: {self.emp_id} Уровень доступа: {self.sec_level} {self.firstname} {self.lastname}' \
               f' {self.get_age()} {self.gender} {self.ocupation}'


if __name__ == '__main__':
    emp_1 = Employee('Инженер', 'Алексей', 'Дубровин', 48, 'мужской')
    print(emp_1)


#####

# import random
#
# from Human import Human
#
#
# def _gen_number():
#     MIN_NUM = 100000
#     MAX_NUM = 1000000
#     return random.randint(MIN_NUM, MAX_NUM)
#
#
# class Employee(Human):
#     def __init__(self, ocupation: str, firstname: str, lastname: str, age: int, gender: str):
#         super().__init__(firstname, lastname, age, gender)
#         self.emp_id = _gen_number()
#         self.sec_level = self._secure_level()
#         self.ocupation = ocupation
#
#     @staticmethod
#     def _secure_level():
#         sec_id = _gen_number()
#         LEVEL_NUM = 7
#         level_num = 0
#         while sec_id > 0:
#             last_num = sec_id % 10
#             level_num += last_num
#             sec_id /= 10
#         return int(level_num % LEVEL_NUM)
#
#     def __str__(self):
#         return f'ID: {self.emp_id} Уровень доступа: {self.sec_level} {self.firstname} {self.lastname}' \
#                f' {self.get_age()} {self.gender} {self.ocupation}'
#
#
# if __name__ == '__main__':
#     emp_1 = Employee('Инженер', 'Алексей', 'Дубровин', 48, 'мужской')
#     print(emp_1)
