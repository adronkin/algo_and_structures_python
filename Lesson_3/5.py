"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.
"""

from math import inf
from random import randint

COUNT_NUM = int(input('Введите кол-во символов для добавления в список: '))
MY_LIST = []
MAX_NUM = -float(inf)
MAX_IND = 0

while len(MY_LIST) < COUNT_NUM:
    MY_LIST.append(randint(-10, 10))

for i in range(len(MY_LIST)):
    if 0 > MY_LIST[i] > MAX_NUM:
        MAX_NUM, MAX_IND = MY_LIST[i], i

print(f'В массиве - {MY_LIST}, \n'
      f'максимальным отрицательным элементом с индексом {MAX_IND} является {MAX_NUM}.')
