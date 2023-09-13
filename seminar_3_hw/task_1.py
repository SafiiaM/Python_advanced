# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.


# first_lst = [7,7,9,1,2,2,3,4,3,3,5,5,6,13,10]
# dub_lst = []
# res = []
# for item in first_lst:
#     if first_lst.count(item) > 1:
#         dub_lst.append(item)
#     else:
#         res.append(item)
# print(f"Список с дублирующимися элементами: {dub_lst}")
# print(f"Результирующий список (без дубликатов): {res}")

# список для обработки
WORKING_LIST_1 = [1, 1, 2, 3, "F", "T", "F", 3, "o", "0", 0]
WORKING_LIST_2 = [1, 2, 3, 4, "F", "K", "X", "X", "0", 0, 8]


# обработка списка
def double_items(work_list: list) -> list:
    return list(set([i for i in work_list if work_list.count(i) > 1]))


def main():
    print(f"{WORKING_LIST_1} - {double_items(WORKING_LIST_1)}")
    print(f"{WORKING_LIST_2} - {double_items(WORKING_LIST_2)}")


if __name__ == "__main__":
    main()

    # решение 2:

import random

list = [random.randint(0,10)for _ in range(20)]
print(list)

new_list=[]
for item in set(list):
    if not list.count(item) != 1:
        new_list.append(item)
print(new_list)