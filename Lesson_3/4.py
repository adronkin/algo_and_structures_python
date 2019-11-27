"""
4. Определить, какое число в массиве встречается чаще всего.
"""
from math import inf
from random import randint


def get_count_num(my_list, num):
    """Возвращает кол-во элементов num в списке"""
    my_count = 0
    for i in my_list:
        if i == num:
            my_count += 1
    return my_count


COUNT_NUM = int(input('Введите кол-во символов для добавления в список: '))
MY_LIST = []
NUM_COUNT, NUM = 0, 0

while len(MY_LIST) < COUNT_NUM:
    MY_LIST.append(randint(1, 10))

for num in MY_LIST:
	count_num = get_count_num(MY_LIST, num)
	if count_num > NUM_COUNT:
		NUM_COUNT = count_num
		NUM = num

print(f'В списке - {MY_LIST}, \n, '
      f'чаще всех встречается "{NUM}" - {NUM_COUNT} раз(а).')
