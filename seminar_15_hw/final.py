import os
import logging
from collections import namedtuple

# Конфигурация логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(message)s')

# Определение namedtuple для хранения информации о файлах и директориях
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def process_directory(directory_path, parent_directory=''):
    # Получаем список файлов и поддиректорий в указанной директории
    try:
        items = os.listdir(directory_path)
    except FileNotFoundError:
        logging.warning(f"Директория не найдена: {directory_path}")
        return

    for item in items:
        item_path = os.path.join(directory_path, item)
        is_directory = os.path.isdir(item_path)

        # Получаем имя и расширение (если это файл)
        if is_directory:
            name, extension = item, None
        else:
            name, extension = os.path.splitext(item)

        # Создаем объект FileInfo и записываем информацию в лог-файл
        file_info = FileInfo(name, extension, is_directory, parent_directory)
        logging.info(
            f"Имя: {file_info.name}, Расширение: {file_info.extension}, Каталог: {file_info.is_directory}, Родительский каталог: {file_info.parent_directory}")

        # Если это поддиректория, рекурсивно обрабатываем ее
        if is_directory:
            process_directory(item_path, os.path.join(parent_directory, name))


if __name__ == '__main__':
    # Получаем путь к директории от пользователя
    directory_path = input("Введите путь к директории: ")

    # Проверяем, существует ли указанная директория
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        process_directory(directory_path)
        print("Информация сохранена в directory_info.log")
    else:
        print("Указанная директория не существует.")

# C:\Users\sonym\new_project\venv\seminar_15_hw\final.py
# D:\Business Analyst\Специализация Backend Python\Погружение в Python\Лекции