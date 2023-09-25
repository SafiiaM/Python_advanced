"""
Задание №7
✔ Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.

✔ Распечатайте его как pickle строку.
"""
import pickle
from pathlib import Path


def reader_csv(file: Path) -> str:
    with open(file, 'r', encoding='utf-8') as f_csv:
        return f_csv.read()


def print_pickle(file_csv: str) -> None:
    print(pickle.dumps(file_csv))


def csv_to_pickle(file_csv: Path):
    print_pickle(reader_csv(file_csv))


if __name__ == '__main__':
    csv_to_pickle(Path('pickle_to_csv.csv'))


# b'\x80\x04\x95\xd7\x00\x00\x00\x00\x00\x00\x00\x8c\xd3level,id,name,hash\n3,0000000001,\xd0\x91\xd1\x80\xd0\xbe\xd0\xbd\xd0\xb8\xd1\x81\xd0\xbb\xd0\xb0\xd0\xb2,-5486534771322081330\n2,0000000022,\xd0\x90\xd0\xbb\xd0\xb5\xd0\xba\xd1\x81\xd0\xb5\xd0\xb9,-655095373610517729\n2,0000000003,\xd0\xa2\xd0\xb0\xd0\xbc\xd0\xb0\xd1\x80\xd0\xb0,2251407046062405999\n4,0000000004,\xd0\xa1\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f,-6580273402405739838\n\x94.'