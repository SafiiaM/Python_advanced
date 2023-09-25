"""
Задание №6

✔ Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.

✔ Для тестированию возьмите pickle версию файла из задачи 5 этого семинара.

✔ Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""
import csv
import pickle
from pathlib import Path


# from typing import Dict


def read_pickle(fail: Path) -> list[dict]:
    with open(fail, 'rb') as f_pkl:
        data_lst = pickle.load(f_pkl, encoding='utf-8')
    print(data_lst)
    return data_lst


def form_lst(data_lst: list[dict]) -> list[list[str]]:
    out_lst = [[i_key for i_key in data_lst[0].keys()]]
    for dct in data_lst:
        out_lst.append([*dct.values()])
    return out_lst


def write_csv(pkl_file: list[list[str]], file_out: Path) -> None:
    with open(file_out, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f, dialect='excel')
        csv_writer.writerows(pkl_file)


def pickle_to_csv(fail_in: Path, fail_out: Path) -> None:
    write_csv(form_lst(read_pickle(fail_in)), fail_out)


if __name__ == '__main__':
    pickle_to_csv(Path('json_pickle.bin'), Path('pickle_to_csv.csv'))