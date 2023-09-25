"""
Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON. Имена пишите с большой
буквы. Каждую пару сохраняйте с новой строки.
"""
import json
from pathlib import Path


def txt_to_json(file: Path) -> None:
    file_data = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split(" ")
            file_data[name.capitalize()] = float(number)
    with open(file.stem + '.json', 'w') as f_json:
        json.dump(file_data, f_json, indent=2)


if __name__ == '__main__':

    txt_to_json(Path('C:/Users/sonym/new_project/venv/seminar_7/task_3_file.txt'))







