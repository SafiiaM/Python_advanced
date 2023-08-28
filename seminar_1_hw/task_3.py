# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

import random
from random import randint

num = random.randint(0, 1000)
guess = None
flag = False
attempts = 0

print("Загадано число от 0 до 1000. У тебя есть 10 попыток, чтобы его угадать.")

while attempts < 10:
    guess = int(input("Введи свой вариант: "))
    attempts += 1
    if guess == num:
        print(f"Ура! Ты угадал число {num} за {attempts} попыток.")
        guess = True
        break
    elif guess < num:
        print(f"Попытка № {attempts}, Загаданное число больше.")
    else:
        print(f"Попытка № {attempts}, Загаданное число меньше.")

print(f"У тебя закончились попытки. Загаданное число было {num}." if not flag else '')