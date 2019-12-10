"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

from random import uniform
import timeit


def merge_sort(list_for_sorting):
    """
    Принимает list_for_sorting неотсортированный список.
    Возвращает отсортированный список алгоритмом сортировка слиянием.
    """
    len_list = len(list_for_sorting)
    if len_list < 2:
        return list_for_sorting

    left_slice = merge_sort(list_for_sorting[:len_list // 2])
    right_slice = merge_sort(list_for_sorting[len_list // 2:])

    left, right = 0, 0
    result = []
    while left < len(left_slice) or right < len(right_slice):
        if not left < len(left_slice):
            result.append(right_slice[right])
            right += 1
        elif not right < len(right_slice):
            result.append(left_slice[left])
            left += 1
        elif left_slice[left] < right_slice[right]:
            result.append(left_slice[left])
            left += 1
        else:
            result.append(right_slice[right])
            right += 1

    return result


UNSORTED_LIST = [uniform(0, 50) for i in range(9)]
print(f'UNSORTED_LIST:\n{UNSORTED_LIST}\n')
print(f'SORTED_LIST:\n{merge_sort(UNSORTED_LIST)}\n')

print(f'test {timeit.timeit("merge_sort(UNSORTED_LIST)", globals=globals(), number=1000)} milliseconds')
