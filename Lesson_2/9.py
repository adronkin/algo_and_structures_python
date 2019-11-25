"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def delete_last_num(num):
    """Возвращает полученное число без последнего символа"""
    if len(str(num)) > 1:
        return (num - (num % 10)) // 10
    return num


def num_sum(num, my_sum):
    my_sum += num % 10
    if len(str(num)) <= 1:
        return my_sum
    return num_sum(delete_last_num(num), my_sum)


NUM_COUNT = int(input('Введите кол-во цифр для ввода: '))
SUM_NUM = 0

for i in range(NUM_COUNT):
    NUM = int(input(f'Введите число номер {i + 1}: '))
    print(f'Сумма цифр числа {NUM} = {num_sum(NUM, SUM_NUM)}')
