"""
ДЗ_2

Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите
функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.
"""
import csv
import json
import os
from pathlib import Path
from random import choice as c
from random import randint as r
from random import shuffle as s
from random import uniform as u
from typing import TextIO, Any, Dict

__all__ = ["FillFiles", "GenNames", "TwoFilesInOne", "FunctionsToMethods", "JsonToCsv", "GetFromUser"]


class FillFiles:
    __L_LIMIT = -1000
    __H_LIMIT = 1000

    def __init__(self, lines: int, filename: str | Path):
        self.lines = lines
        self.filename = filename

    def fill_files(self) -> None:
        with open(self.filename, 'w', encoding='utf-8') as f:
            for _ in range(self.lines):
                f.write(f'{r(self.__L_LIMIT, self.__H_LIMIT)}|{u(self.__L_LIMIT, self.__H_LIMIT)}\n')

class GenNames:
    __min = 4
    __max = 8

    __VOWELS = 'aeiouy'
    __CONSTANTS = 'bcdfghjklmnqrstvwxz'

    def __init__(self, count: int, str_len_min: int, str_len_max: int, file_2: Path):
        self.count = count
        self.str_len_min = str_len_min
        self.str_len_max = str_len_max
        self.file_2 = file_2

    def generate_names(self) -> None:
        with open(self.file_2, 'a', encoding='utf-8') as f_2:
            for _ in range(self.count):
                rad_string = ''.join(c(self.__VOWELS) if i % 3 == 0 else c(self.__CONSTANTS)
                                     for i in range(r(self.str_len_min, self.str_len_max)))
                f_2.write(f'{rad_string.capitalize()}\n')


class TwoFilesInOne:
    def __init__(self, numbers: Path, words: Path, result: Path):
        self.numbers = numbers
        self.words = words
        self.result = result

    def _read_or_begin(self, fd: TextIO) -> str:
        line = fd.readline()
        if not line:
            fd.seek(0)
            return self._read_or_begin(fd)
        return line[:-1]

    def two_files_in_one(self) -> None:
        with (open(self.numbers, 'r', encoding='utf-8') as f_num,
              open(self.words, 'r', encoding='utf-8') as f_word,
              open(self.result, 'w', encoding='utf-8') as f_res
              ):
            len_numbers = sum(1 for _ in f_num)
            len_word = sum(1 for _ in f_word)
            for _ in range(max(len_numbers, len_word)):
                num = self._read_or_begin(f_num)
                word = self._read_or_begin(f_word)
                num_a, num_b = num.split('|')
                mult = int(num_a) * float(num_b)
                if mult < 0:
                    f_res.write(f'{word.lower()} {abs(mult)}\n')
                elif mult > 0:
                    f_res.write(f'{word.upper()} {round(mult)}\n')


class FunctionsToMethods:
    def __init__(self, file: Path, file_2: Path):
        self.file = file
        self.file_2 = file_2

    def txt_to_json(self) -> None:
        file_data = {}
        with open(self.file, 'r', encoding='utf-8') as f:
            for line in f:
                name, number = line.split(" ")
                file_data[name.capitalize()] = float(number)
        with open(self.file_2, 'w') as f_json:
            json.dump(file_data, f_json, indent=2)


class JsonToCsv:
    def __init__(self, file_in: Path, file_out: Path):
        self.file_in = file_in
        self.file_out = file_out

    def reader_json_to_csv(self) -> None:
        json_file = {}
        if os.path.isfile(self.file_in):
            with open(self.file_in, 'r', encoding='utf-8') as js:
                if os.path.getsize(self.file_in) > 0:
                    json_file = json.load(js)
        rows = []
        for level, value in json_file.items():
            for id, name in value.items():
                rows.append({'level': level, 'user_id': id, 'name': name})
        with open(self.file_out, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['level', 'user_id', 'name']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)


class GetFromUser:
    @classmethod
    def add_data(cls, level: int, person_id: int, name: str) -> dict[int, dict[int, str]]:
        return {level: {person_id: name}}

    @classmethod
    def write_json(cls, data: Dict) -> None:
        file = '../seminar_10_hw/data/data.json'
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @classmethod
    def read_json(cls, file: Path) -> dict[Any, Any] | Any:
        with open(file, "r", encoding='utf-8') as read_file:
            data = read_file.read()
            if data:
                return {}
            data_from_file = json.load(read_file)
        return data_from_file

    @classmethod
    def get_from_user(cls, file: Path):
        base_dict = cls.read_json(file)
        exit_program = False
        print('Добро пожаловать в программу. Введите данные для создания файлов ...')
        while not exit_program:
            level: int = int(input('Введите уровень доступа: '))
            personal_id: int = int(input('Введите id: '))
            name: str = input('Введите имя: ')
            continue_program = input('Хотите продолжить? y/n ')
            if continue_program == 'n':
                exit_program = True
            cls.add_data(level, personal_id, name)
            if level in base_dict:
                base_dict[level].update({personal_id: name})
            else:
                base_dict[level] = {personal_id: name}
        cls.write_json(base_dict)


def run():
    mul = FillFiles(5, Path('data/nums'))
    mul.fill_files()
    print(f'{FillFiles}')

    gn = GenNames(10, 4, 7, Path('data/name_gen'))
    gn.generate_names()
    print(f'{GenNames}')

    tf = TwoFilesInOne(Path('data/nums'), Path('data/name_gen'), Path('data/result'))
    tf.two_files_in_one()
    print(f'{TwoFilesInOne}')

    jsn = FunctionsToMethods(Path('../seminar_10_hw/data/result'), Path('../seminar_10_hw/data/result.json'))
    jsn.txt_to_json()
    print(f'{FunctionsToMethods}')

    gfu = GetFromUser()
    gfu.get_from_user(Path('../seminar_10_hw/data/result.json'))
    print(f'{GetFromUser}')

    jsn_csv = JsonToCsv(Path('../seminar_10_hw/data/data.json'), Path('../seminar_10_hw/data/result.csv'))
    jsn_csv.reader_json_to_csv()
    print(f'{JsonToCsv}')


if __name__ == '__main__':
    run()
