"""
4. Определить, какое число в массиве встречается чаще всего.
"""
from math import inf
from random import randint


def get_max_num(my_list):
    """Возвращает максимальное число в списке"""
    max_num = -float(inf)
    for i in my_list:
        if i > max_num:
            max_num = i
    return max_num


def get_count_num(my_list, num):
    """Возвращает кол-во элементов num в списке"""
    my_count = 0
    for i in my_list:
        if i == num:
            my_count += 1
    return my_count


COUNT_NUM = int(input('Введите кол-во символов для добавления в список: '))
MY_LIST = []

while len(MY_LIST) < COUNT_NUM:
    MY_LIST.append(randint(1, 10))

MAX_ELEM = get_max_num(MY_LIST)

print(f'В списке - {MY_LIST}, \nмаксимальный элемент "{MAX_ELEM}", '
      f'встречается {get_count_num(MY_LIST, MAX_ELEM)} раз(а).')
