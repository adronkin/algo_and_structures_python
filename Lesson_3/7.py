"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from math import inf
from random import randint

MY_LIST = []
MIN_IND_1, MIN_IND_2 = 0, 0
MIN_NUM_1, MIN_NUM_2 = float(inf), float(inf)
COUNT_NUM = int(input('Введите кол-во символов для добавления в список: '))

try:
    for i in range(COUNT_NUM):
        MY_LIST.append(randint(-15, 15))

    for i in range(len(MY_LIST)):
        if MY_LIST[i] < MIN_NUM_1:
            MIN_NUM_2 = MIN_NUM_1
            MIN_NUM_1 = MY_LIST[i]
        elif MY_LIST[i] < MIN_NUM_2:
            MIN_NUM_2 = MY_LIST[i]

    print(MY_LIST)
    print(f'Два минимальных элемента массива {MIN_NUM_1} и {MIN_NUM_2}')
except ValueError:
    print('Необходимо ввести число.')
