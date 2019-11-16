"""
9. Вводятся три разных числа. Найти, какое из них
является средним (больше одного, но меньше другого).
"""


def get_same_numbers(num1, num2, num3):
    """Возвращает True, если числа повторяются"""
    if num1 in (num2, num3) or num2 in (num1, num3):
        return True


def get_big_num(num1, num2, num3):
    """Возвращает среднее число из трех"""
    if num1 > num2 and num1 > num3:
        if num2 > num3:
            return num2
        return num3
    if num2 > num3 and num2 > num1:
        if num1 > num3:
            return num1
        return num3
    if num3 > num1 and num3 > num2:
        if num1 > num2:
            return num1
        return num2


NUM_1 = int(input('Введите число 1: '))
NUM_2 = int(input('Введите число 2: '))
NUM_3 = int(input('Введите число 3: '))

if get_same_numbers(NUM_1, NUM_2, NUM_3):
    print('Среднего числа нет, как минимум, 2 числа равны')
else:
    print(f'Среднее число - {get_big_num(NUM_1, NUM_2, NUM_3)}')
