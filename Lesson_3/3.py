"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from math import inf
from random import randint

COUNT_NUM = int(input('Введите кол-во символов для добавления в список: '))
MY_LIST = []
MAX_NUM, MIN_NUM = -float(inf), float(inf)
MAX_IND, MIN_IND = 0, 0

while len(MY_LIST) < COUNT_NUM:
    MY_LIST.append(randint(1, 100))

for i in range(len(MY_LIST)):
    if MY_LIST[i] > MAX_NUM:
        MAX_NUM, MAX_IND = MY_LIST[i], i
    elif MY_LIST[i] < MIN_NUM:
        MIN_NUM, MIN_IND = MY_LIST[i], i

print(f'Исходный список - {MY_LIST}')
MY_LIST[MAX_IND] = MIN_NUM
MY_LIST[MIN_IND] = MAX_NUM
print(f'После перестановки минимального и максимального элементов - {MY_LIST}')
