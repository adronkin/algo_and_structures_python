"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib


def get_unique_str(my_string, my_set, len_string=1):
    """Используя хэш-функцию, возвращает сет с уникальными значениями"""
    if len_string == len(my_string):
        return my_set
    for i in range(len(my_string) - 1):
        temp_string = my_string[i:i + len_string]
        my_set.add(hashlib.sha1(temp_string.encode('UTF-8')).hexdigest())
    return get_unique_str(my_string[:len(my_string)], my_set, len_string+1)


MY_STRING = input('Введите строку, состоящую только из маленьких латинских букв: ')
SET_STRINGS = set()
LEN_STRING = 1

print(f'Кол-во уникальны подстрок в строке "{MY_STRING}" - '
      f'{len(get_unique_str(MY_STRING, SET_STRINGS))} шт.')
