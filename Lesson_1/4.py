"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

from random import random


def random_integer(min_num, max_num):
    """Возвращает псевдослучайное целое число"""
    integer = int(random() * (max_num - min_num + 1) + min_num)
    return integer


def random_float(min_num, max_num):
    """Возвращает псевдослучайное вещественное число"""
    float_num = random() * (max_num - min_num) + min_num
    return float_num


def get_abc_true(letter):
    """Возвращает True, если введен символ алфавита"""
    abc = 'abcdefghijklmnopqrstuvwxyz'
    if letter in abc:
        return True


def get_letter_num(letter):
    """Возвращает номер символа в алфавите"""
    abc = 'abcdefghijklmnopqrstuvwxyz'
    letter_num = abc.find(letter) + 1
    return letter_num


def get_random_letter(num):
    """Возвращает псевдослучайный символ алфавита"""
    abc = 'abcdefghijklmnopqrstuvwxyz'
    return abc[num - 1]


MIN = int(input('Введите минимальная граница диапазона (число): '))
MAX = int(input('Введите максимальная граница диапазона (число): '))
print(f'Случайное целое число - {random_integer(MIN, MAX)}')
print(f'Случайное вещетвенное число - {random_float(MIN, MAX)}')

MIN_LETTER = input('Введите минимальную граница диапазона (буква): ').lower()
MAX_LETTER = input('Введите максимальная граница диапазона (буква): ').lower()

if get_abc_true(MIN_LETTER) and get_abc_true(MAX_LETTER):
    LET_NUM_1 = get_letter_num(MIN_LETTER)
    LET_NUM_2 = get_letter_num(MAX_LETTER)
    RANDOM_LET_NUM = random_integer(LET_NUM_1, LET_NUM_2)
    print(f'Случайный символ алфавита - {get_random_letter(RANDOM_LET_NUM)}')
else:
    print('Введены не символы алфавита')
