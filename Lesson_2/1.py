"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


def correct_sign(sign, right_signs):
    """Возвращает True, если sign есть в списке right_signs"""
    if sign in right_signs:
        return True


def check_zero_division(sign, num):
    """Возвращает True, если sign - операция деления, а num = 0"""
    if sign == '/' and num == 0:
        return True


def get_calc_result(num_1, num_2, sign):
    """Возвращает результат вычеслений"""
    if sign == '+':
        return num_1 + num_2
    elif sign == '-':
        return num_1 - num_2
    elif sign == '*':
        return num_1 * num_2
    else:
        return num_1 / num_2


def calc_recursion():
    """Арифмитические операции над числами введенными пользователем"""
    print(MENU)
    num_1 = int(input('Ведите первое число: '))
    operation = input('Ведите арифметическую операцию: ')
    if operation == '0':
        print('Работа программы завершена.')
    else:
        num_2 = int(input('Ведите второе число: '))
        if check_zero_division(operation, num_2):
            print('Ошибка, деление на 0 невозможно.')
        else:
            print(f'{num_1} {operation} {num_2} = {get_calc_result(num_1, num_2, operation)}')
        calc_recursion()


# while OPERATION != 0:
#     print(MENU)
#     OPERATION = input('Ведите арифметическую операцию: ')
#     if correct_sign(OPERATION, SIGN):
#         if OPERATION == '0':
#             print('Работа программы завершена.')
#             break
#         else:
#             NUM_1 = int(input('Ведите первое число: '))
#             NUM_2 = int(input('Ведите второе число: '))
#             if check_zero_division(OPERATION, NUM_2):
#                 print('Ошибка, деление на 0 невозможно.')
#             else:
#                 print(f'{NUM_1} {OPERATION} {NUM_2} = {get_calc_result(NUM_1, NUM_2, OPERATION)}')
#     else:
#         print('Введена некорректная арифметическая операция.')


MENU = """
Выберите операцию и введите 2 числа:
'+' - сложение
'-' - вычитание
'*' - умножение
'/' - деление
'0' - завершить программу
"""

SIGN = ['0', '+', '-', '*', '/']

OPERATION = None

calc_recursion()
