# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv
import task_1


if __name__ == '__main__':
    _, *arg = argv

data = '29.02.1999'
print(task_1.check_date(data))
