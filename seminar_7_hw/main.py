# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from pathlib import Path
from task_4 import create_file
from task_5 import gen_files
from task_6 import create_dir
from task_7 import group_file_in_dir
from group_rename import group_rename



__all__ = ['create_file', 'gen_files', 'create_dir', 'group_file_in_dir', 'group_rename']

