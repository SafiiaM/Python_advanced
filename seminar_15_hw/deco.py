"""
Задание 2

На семинаре про декораторы был создан логирующих декоратор. Он сохранял аргументы функции и результат её работы в файл.
Напишите аналогичный декоратор, но внутри используйте модуль logging.
####

Задание 3
Доработаем задачу 2. Сохраняйте в лог файл раздельно: уровень логирования, дату события, имя функции (не декоратора),
аргументы вызова, результат.
"""

import logging
from typing import Callable, Any

logging.basicConfig(filename='info.log', level=logging.INFO, encoding='UTF-8')
logger = logging.getLogger(__name__)


def deco_logger(func: Callable) -> Any:
    def wrapper(*args, **kwargs):
        a, b = args
        res = func(a, b)
        logger.info(f"{a} * {b} = {res}  ")

    return wrapper


@deco_logger
def multy(a: int, b: int, *args, **kwargs) -> int:
    return a * b


if __name__ == '__main__':
    multy(2, 5)

"""
import logging
from typing import Callable

logging.basicConfig(filename='info.log', level=logging.INFO, encoding="UTF-8")
logger = logging.getLogger(__name__)


def deco_logger(func: Callable):
    def wrapper(*args, **kwargs):
        a, b = args
        res = func(a, b)
        logger.info(f"{a} * {b} = {res}  ")

    return wrapper


@deco_logger
def multy(a: int, b: int, *args, **kwargs) -> int:
    return a * b


if __name__ == '__main__':
    multy(2, 5)
"""

"""
import logging
from typing import Callable

FORMAT = "{levelname} - {asctime}: {msg}"
logging.basicConfig(format=FORMAT, style="{", filename='info.log', level=logging.INFO, encoding="UTF-8")

logger = logging.getLogger(__name__)


def deco_logger(func: Callable):
    def wrapper(*args, **kwargs):
        a, b = args
        res = func(a, b)
        logger.info(f"{func.__name__} {a} * {b} = {res}  ")

    return wrapper


@deco_logger
def multy(a: int, b: int, *args, **kwargs) -> int:
    return a * b


if __name__ == '__main__':
    multy(2, 5)
"""