# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

def parse_row(text: str) -> (int, float):
    text = text.replace(" ", "")
    temp = text.split('|')
    return int(temp[0]), float(temp[1])


def open_files_task3(file_name1: str, file_name2: str, file_name3: str = "task_3_file.txt") -> None:
    with (
            open(file_name1, 'r', encoding='utf-8') as f1,
            open(file_name2, 'r', encoding='utf-8') as f2,
            open(file_name3, 'w', encoding='utf-8') as f3
    ):
        lenf1 = sum(1 for i in f1)
        lenf2 = sum(1 for i in f2)
        for _ in range(max(lenf1, lenf2)):
            text = f2.readline().replace('\n', '')
            if text == "":
                f2.seek(0)
                text = f2.readline().replace('\n', '')
            nums = f1.readline().replace('\n', '')
            if nums == "":
                f1.seek(0)
                nums = f1.readline().replace('\n', '')
            num1, num2 = parse_row(nums)
            if num1 * num2 < 0:
                f3.write(f"{text.lower()}, {abs(num1 * num2)}\n")
            else:
                f3.write(f"{text.upper()}, {round(num1 * num2)}\n")


if __name__ == '__main__':
    open_files_task3("task_1_file.txt", "task_2_file.txt")

