"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def len_num(num):
    """Возвращает кол-во символов числа"""
    return len(str(num))


def delete_last_num(num):
    """Возвращает полученное число без последнего символа"""
    if len_num(num) > 1:
        return (num - (num % 10)) // 10
    return num


def reverse_num(num):
    """Возвращает последнюю цифру num + колво нулей как у num"""
    if len_num(num) <= 1:
        return num
    one_zero_zero = 10 ** (len_num(num) - 1)
    return num % 10 * one_zero_zero + reverse_num((num - num % 10) // 10)


NUM = int(input('Введите число: '))

if NUM >= 0:
    print(f'разворачиваем число {NUM} и получаем {reverse_num(NUM)}')
else:
    print('Введите число больше 0')
