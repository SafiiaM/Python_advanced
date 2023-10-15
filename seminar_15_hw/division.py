"""

Задание 1

Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл. Например отлавливаем
ошибку деления на ноль.
"""
import logging as log


logger1 = r'error1.log'
FORMAT = '{levelname} - {asctime} - {msg} | {name} | {threadName}'
log.basicConfig(level=log.INFO, filename=logger1, datefmt='%Y-%m-%d %H:%M:%S', encoding='utf-8',
                format=FORMAT, style='{')
logger = log.getLogger(__name__)


def division(a: int, b: int) -> float:
    try:
        log.info(f'{a}/{b}')
        return a / b
    except ZeroDivisionError as zd:
        log.error(f'Вы делите на ноль. Ошибка: {zd}')


if __name__ == '__main__':
    division(2, 0)
