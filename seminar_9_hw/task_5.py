"""
Задание №5

Объедините функции из прошлых задач. Функцию угадайку задекорируйте декораторами для сохранения параметров, декоратором
контроля значений и декоратором для многократного запуска. Выберите верный порядок декораторов.
"""

from task_4 import count
from task_1 import two_numbers
from task_2 import decorate
from task_3 import decorator_json


@count(2)
@decorator_json
def factorial(num: int) -> int:
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


@count(2)
@decorator_json
def product(a: int, b: int, *args, **kwargs):
    return a * b


@count(2)
@decorator_json
@decorate
def two_numbers_two(count_try: int, num: int):
    for i in range(1, count_try + 1):
        user_input = input(' Введите число для отгадывания от 1 до 100: ')
        if int(user_input) == num:
            print(f'Вы угадали с {i} попытки')
            break
    else:
        print('Вы не угадали')


if __name__ == '__main__':
    results = two_numbers(5, 30)
    print(results)
    results()
    two_numbers_two(5, 30)
    product(8, 9, temp=7, res=4, c=6, d=3)
    print(factorial(3))
