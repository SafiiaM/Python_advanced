# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random as rnd
import string

letter = string.ascii_lowercase
vowels = 'aeiouy'


def generate_name():
    size = rnd.randint(4,7)
    name = rnd.sample(letter, size-1)
    name.append(rnd.choice(vowels))
    rnd.shuffle(name)
    name=''.join(name).title()
    return name

def write_names_to_file(filename: str, count: int):
    names=[]
    with open(filename,'a+', encoding = 'UTF-8') as file:
        for _ in range(count):
            names.append(generate_name())
        file.write('\n'.join(names))

write_names_to_file('task_2_file.txt', 10)


