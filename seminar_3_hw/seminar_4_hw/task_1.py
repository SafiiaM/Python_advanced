# Погружение в Python (семинары)
# Урок 4. Функции
# Напишите функцию для транспонирования матрицы

def print_matrix(m):
    for item in m:
        print(item)


def trans_matrix(matrix):
    temp = []
    for i in range(len(matrix[0])):
        temp_col = []
        for j in range(len(matrix)):
            temp_col.append(matrix[j][i])
        temp.append(temp_col)
    return temp


matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [10, 9, 8, 7, 6], [5,4, 3, 2, 1]]
print_matrix(trans_matrix(matrix))