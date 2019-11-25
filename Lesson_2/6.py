"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
from random import random


def random_integer():
    """Возвращает псевдослучайное целое 0 до 100 число"""
    integer = int(random() * (100 + 0))
    return integer


def end_attempts(count):
    """Возвращает True, если кол-во counts >= 10"""
    if count >= 10:
        return True


def guess_the_number(attempts_count, number):
    """Выполнение функции завершается, когда будет отгадано
    число number или будет использовано 10 попыток"""
    user_num = input('Введите число загаданное компьютером (от 1 до 100): ')
    if user_num.isdigit() and 0 < int(user_num) < 101:
        user_num = int(user_num)
        if number == user_num:
            return True
        if end_attempts(attempts_count):
            return False
        print(f'Осталось {10 - attempts_count} попыток.')
        if user_num > number:
            print(f'Выберите число меньше чем {user_num}')
            guess_the_number(attempts_count + 1, number)
        else:
            print(f'Выберите число больше чем {user_num}')
            guess_the_number(attempts_count + 1, number)
    else:
        print('Необходимо ввести число от 10 до 100.')
        guess_the_number(attempts_count, number)


ATTEMPTS = 1
COMP_NUMBER = random_integer()
if guess_the_number(ATTEMPTS, COMP_NUMBER):
    print(f'Вы отгдали загаданное число {COMP_NUMBER}.')
else:
    print(
        f'Игра завершена, использовано 10 попыток. Было загадано число "{COMP_NUMBER}".')
