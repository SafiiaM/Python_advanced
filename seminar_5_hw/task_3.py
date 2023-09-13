# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

#1
# names = ["Alex", "Nikky", "Vlad"]
# stakes = [5000, 21000, 150000]
# bonus = ["15.00%", "10.50%", "10.25%"]
#
# result = {n: (float(b[:-1]) * s) for n, b, s in zip(names, bonus, stakes)}
#
# print(result)
#2

import os


def file_info(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension
def premium(names: list[str], stakes: list[int], bonus: list[str]) -> dict[str:float]:
    return {name: cash / 100 * perc
            for name, cash, perc in zip(names, stakes, (float(i[:-1]) for i in bonus))}

def run():
    print(file_info(r'C: \Users\sonym\new_project\venv\seminar_5_hw\test.json'))
    names = ["Alex", "Nikky", "Vlad"]
    stakes = [5000, 21000, 150000]
    bonus = ["15.00%", "10.50%", "10.25%"]
    print(premium(names, stakes, bonus))



if __name__ == "__main__":
    run()