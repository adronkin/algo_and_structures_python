"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def sum_element_mass(start_num, num, sum_elem, elem_num):
    """Возвращает сумму элементов ряда чисел: 1 -0.5 0.25 -0.125 ..."""
    if elem_num == num:
        sum_elem += start_num
        return sum_elem
    elem_num += 1
    sum_elem += start_num
    start_num /= 2
    return sum_element_mass(start_num, NUM, sum_elem, elem_num)


NUM = int(input('Введите число елемента "n": '))
START_NUM = 1
SUM_ELEM = 0
ELEM_NUM = 0

try:
    print(sum_element_mass(START_NUM, NUM, SUM_ELEM, ELEM_NUM))
except RecursionError:
    print('Введено слишком большое значение')
