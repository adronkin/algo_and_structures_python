"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from math import inf
from random import randint

MY_LIST = []
MIN_IND, MAX_IND = 0, 0
MIN_NUM, MAX_NUM = float(inf), -float(inf)
MY_SUM = 0

try:
    COUNT_NUM = int(input('Введите кол-во символов для добавления в список: '))

    while len(MY_LIST) < COUNT_NUM:
        MY_LIST.append(randint(1, 15))

    for i in range(len(MY_LIST)):
        if MY_LIST[i] > MAX_NUM:
            MAX_NUM = MY_LIST[i]
            MAX_IND = i
        if MY_LIST[i] < MIN_NUM:
            MIN_NUM = MY_LIST[i]
            MIN_IND = i

    if MAX_IND > MIN_IND:
        for i in range(MIN_IND + 1, MAX_IND):
            MY_SUM += MY_LIST[i]
    else:
        for i in range(MAX_IND + 1, MIN_IND):
            MY_SUM += MY_LIST[i]

    print(MY_LIST)
    print(f'Минимальный элемент "{MIN_NUM}" с индексом "{MIN_IND}"\n'
          f'Максимальный элемент "{MAX_NUM}" с индексом "{MAX_IND}"\n'
          f'Сумма чисел между элементами {MY_SUM}.')
except ValueError:
    print('Необходимо ввести число.')
