"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint
from timeit import Timer


def get_count_num(my_list, num):
    """Возвращает кол-во элементов num в списке"""
    my_count = 0
    for i in my_list:
        if i == num:
            my_count += 1
    return my_count


def test_1():
    my_list = []
    num_count, num = 0, 0
    
    while len(my_list) < 500:
        my_list.append(randint(1, 100))
    
    for num in my_list:
        count_num = get_count_num(my_list, num)
        if count_num > num_count:
            num_count = count_num
            num = num
    
    print(f'В списке - {my_list}\n '
          f'чаще всех встречается "{num}" - {num_count} раз(а).')


# t1 = Timer("test_1()", "from __main__ import test_1")
# print(f'test_1 {t1.timeit(number=1000)} milliseconds')

"""
=========================================================
"""


def get_count_num(my_list, num):
    """Возвращает кол-во элементов num в списке"""
    my_count = 0
    for i in my_list:
        if i == num:
            my_count += 1
    return my_count


def rec_list(my_list):
    if len(my_list) >= 500:
        return my_list
    my_list.append(randint(1, 100))
    return rec_list(my_list)


def test_2():
    my_list = []
    num_count, num = 0, 0

    my_list = rec_list(my_list)

    for num in my_list:
        count_num = get_count_num(my_list, num)
        if count_num > num_count:
            num_count = count_num
            num = num

    print(f'В списке - {my_list}\n '
          f'чаще всех встречается "{num}" - {num_count} раз(а).')


# t2 = Timer("test_2()", "from __main__ import test_2")
# print(f'test_2 {t2.timeit(number=1000)} milliseconds')
"""
=========================================================
"""


def get_count_num(my_list, num):
    """Возвращает кол-во элементов num в списке"""
    my_count = 0
    for i in my_list:
        if i == num:
            my_count += 1
    return my_count


def test_3():
    num_count, num = 0, 0

    my_list = [randint(1, 100) for i in range(500)]
    set_list = set(my_list)

    for num in set_list:
        count_num = get_count_num(my_list, num)
        if count_num > num_count:
            num_count = count_num
            num = num

    print(f'В списке - {my_list}\n '
          f'чаще всех встречается "{num}" - {num_count} раз(а).')


# t3 = Timer("test_3()", "from __main__ import test_3")
# print(f'test_3 {t3.timeit(number=1000)} milliseconds')

"""
test_1 11.500409675 milliseconds
test_2 12.557947164 milliseconds
test_3 3.2712681 milliseconds

test_1
Реализация алгоритма выполненная в рамках ДЗ к уроку 3. Список генерируется при помощи цикла while.
Сложность O(n2). Тк необходимо перебрать каждый элемент в списке + повторный перебор для подсчета 
кол-во вхождений элемента в список.

test_2
Список генерируется при помощи рекурсии. Скорость выполнения незначительно выросла (на 1 сек).
Сложность O(n2)

test_3
Список создается при помощи генератора, что сократило время выполнения примерно на 1 сек (относительно цикла while).
Добавил переменную в которой сохранил множество созданное из списка, это значительно сократило кол-во элементов 
для перебора в цикле while. Не придется считать повторно каждого элемента. Врея выполнения сокращено еще на 8 секунд.
Сложность O(nlogn). Тк для выбора элемента мы используем множество, для подсчета кол-ва вхождений список.
"""
