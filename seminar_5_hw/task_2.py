# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

#1
import os


def file_info(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension

#2
def file_info(file_path):
    path = '\\'.join(file_path.split('\\')[:-1])
    *_, filename, extension = file_path.replace('.', '\\').split('\\')
    result = (path, filename, extension)
    return result


print(file_info('C: /Users\sonym\ new_project\ venv\seminar_5_hw\\task_2.py'))


