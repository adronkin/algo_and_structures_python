"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def first_formula(num):
    """Возвращает сумму множества по формуле num(num+1)/2"""
    row_amount = num * (num + 1) / 2
    return row_amount


def second_formula(num, my_sum):
    """Возвращает сумму множества 1+2+3+...+num"""
    my_sum += num
    if num <= 0:
        return my_sum
    return second_formula(num - 1, my_sum)


MY_NUM = int(input('Введите число: '))
MY_SUM = 0

print(f'1+2+...+n == n(n+1)/2 == {first_formula(MY_NUM) == second_formula(MY_NUM, MY_SUM)}, '
      f'сумма чисел = {second_formula(MY_NUM, MY_SUM)}')
