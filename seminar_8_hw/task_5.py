"""
Задание №5

Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle
файлов.
"""
import json
import pickle
from pathlib import Path


def get_pickle(name: dict, json_data: Path) -> None:
    with open(json_data, 'wb') as f_pic:
        pickle.dump(name, f_pic)


def reader_json(file: Path) -> dict[str, str, str]:
    with open(file, 'r', encoding='utf-8') as f_js:
        json_file = json.load(f_js)
    return json_file


def json_to_pickle(file_in: Path, file_out: Path) -> None:
    get_pickle(reader_json(file_in), file_out)


if __name__ == '__main__':
    json_to_pickle(Path('json_in.json'), Path('json_pickle.bin'))