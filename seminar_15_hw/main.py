"""
Выбираем логирование в Python:  loguru
"""
from loguru import logger


logger.add("runtime.log", backtrace=True, diagnose=True)
_ANSWEARS = dict()


def new_puzzle(puzzles: dict, count: int):
    for key, val in puzzles.items():
        try_count_1 = puzzle(key, val, count)
        if try_count_1:
            _ANSWEARS[key] = f"Угадано за {try_count_1} раза"
            # print(f"Угадано за {try_count_1} раза")
        else:
            _ANSWEARS[key] = "Не угадали ("
            # print("Не угадали (")


def show_result():
    print(*(f"{key} - {val}\n" for key, val in _ANSWEARS.items()))


def puzzle(text: str, answers: list[str], count: int) -> int:
    print(text)
    logger.info(text)
    count_trying = 1

    while count_trying <= count:
        answer = input("Что это? \n")
        logger.info(answer)
        if answer in answers:
            break
        if count_trying != count:
            print("Не угадали, пробуем еще раз\n")
        count_trying += 1
    else:
        count_trying = 0

    return count_trying


def run():
    return 'start'


if __name__ == '__main__':
    logger.info('start')
    try_count = puzzle("Не лает не кусает, в дом не пускает.", ["замок", "замочек", "засов"], 3)
    # logger.info(try_count)
    if try_count:
        logger.info(f"Угадано за {try_count} раза")
        print(f"Угадано за {try_count} раза")
    else:
        logger.info("Не угадали (")
        print("Не угадали (")
    puzzle_dict = {
        "Не лает не кусает, в дом не пускает.": ["замок", "замочек", "засов"],
        "Красна девица, а коса на улице": ["морковь", "морковка"],
        "два кольца, два конца, в середине гвоздик": ["ножницы"],
    }
    logger.opt(colors=True).info('stop')
