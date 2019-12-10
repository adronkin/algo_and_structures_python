"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

from random import randint
import timeit


def bubble_sorting(list_for_sorting):
    """
    Принимает list_for_sorting неотсортированный список.
    Возвращает отсортированный пузырьковым алгоритмом список.
    """
    my_list = list_for_sorting
    for _ in range(len(my_list)):
        change = 0
        for i in range(len(my_list) - 1):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                change += 1
        if change == 0:
            return my_list
    return my_list


UNSORTED_LIST = [randint(-100, 100) for i in range(200)]
print(f'UNSORTED_LIST:\n{UNSORTED_LIST}\n')
print(f'SORTED_LIST:\n{bubble_sorting(UNSORTED_LIST)}\n')

print(f'test {timeit.timeit("bubble_sorting(UNSORTED_LIST)", globals=globals(), number=1000)} milliseconds')
"""
Стандартная реализация алгоритма - test 5.776569381 milliseconds
Реализация алгоритма с "change" - test 5.496740742 milliseconds
"""