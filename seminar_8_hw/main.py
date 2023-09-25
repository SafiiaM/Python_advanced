from pathlib import Path

from task_6 import pickle_to_csv
from task_4 import csv_to_json
from task_3 import json_to_csv
from direct_info_hw import direct_info
from task_2 import get_from_user, read_json
from task_1 import txt_to_json

if __name__ == '__main__':
    txt_to_json(Path('../seminar_7/task_3_file.txt'))
    get_from_user(Path('../seminar_8_hw/task_3_file.json'))
    print(type(read_json(Path('../seminar_8_hw/data.json'))))
    json_to_csv(Path('../seminar_8_hw/data.json'), (Path('../seminar_8_hw/file_out.csv')))
    csv_to_json(Path('file_out.csv'), Path('json_in.json'))
    pickle_to_csv(Path('json_pickle.bin'), Path('pickle_to_csv.csv'))
    direct_info(Path(r'C:\Users\sonym\new_project\venv\seminar_8_hw'), 'name')