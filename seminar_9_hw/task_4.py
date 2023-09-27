"""
Задание №4

Создайте декоратор с параметром. Параметр - целое число, количество запусков декорируемой функции.
"""
from typing import Callable



def count(param: int):
    def deco(func: Callable):
        my_list = []

        def wrapper(*args, **kwargs):
            for i in range(param):
                result = func(*args, **kwargs)
                my_list.append(result)
            return my_list

        return wrapper

    return deco


@count(2)
def factorial(num: int) -> int:
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res


if __name__ == '__main__':
    print(factorial(3))
