"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from math import inf
from random import randint


def get_expand_matrix(matrix):
    """Разворачивает матрицу на 90 градусов"""
    my_list = []
    for elem in range(0, len(matrix[0])):
        new_list = []
        for num in range(0, len(matrix)):
            new_list.append(matrix[num][elem])
        my_list.append(new_list)
    return my_list


def get_min_col_list(matrix):
    """Возвращает по одному минимальному элементы из каждого столбца матрицы в виде списка"""
    min_list = []
    for elem in matrix:
        min_num = float(inf)
        for num in range(len(elem)):
            if elem[num] < min_num:
                min_num = elem[num]
            if num == len(elem) - 1:
                min_list.append(min_num)
    return min_list


MY_LIST = []
ROW = int(input('Ввидите кол-во строк матрицы: '))
COL = int(input('Ввидите кол-во столбцов матрицы: '))

for i in range(ROW):
    small_list = []
    for j in range(COL):
        small_list.append(randint(-50, 50))
    MY_LIST.append(small_list)

for small in MY_LIST:
    for i in small:
        print(f'{i:4d}', end=' ')
    print()


MIN_LIST = get_min_col_list(get_expand_matrix(MY_LIST))

MAX_ELEM = -float(inf)
for i in MIN_LIST:
    if i > MAX_ELEM:
        MAX_ELEM = i

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы - "{MAX_ELEM}"')
