"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def delete_last_num(num):
    """Возвращает полученное число без последнего символа"""
    if len(str(num)) > 1:
        return (num - (num % 10)) // 10
    return num


def parsing_number(num, even, not_even):
    """Подсчет четных и не четных чисел"""
    if len(str(num)) <= 1:
        if num % 2 == 0:
            even += 1
        else:
            not_even += 1
        print(f'Четных - {even}, не четных - {not_even}')
    else:
        if num % 2 == 0:
            even += 1
        else:
            not_even += 1
        parsing_number(delete_last_num(num), even, not_even)


CALC_EVEN, CALC_NOT_EVEN = 0, 0

NUM = int(input('Введите число: '))

parsing_number(NUM, CALC_EVEN, CALC_NOT_EVEN)
