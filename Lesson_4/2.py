"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import cProfile
import timeit
from math import sqrt


MY_NUM = int(input('Введите номер простого числа: '))


def test_1(my_num):
    my_list = []
    num, num_number = 2, 0
    while num_number <= my_num:
        if num > 10:
            if num % 2 == 0 or num % 5 == 0:
                pass
        for i in range(2, num):
            if i > sqrt(num):
                my_list.append(num)
                num_number += 1
                break
            if num % i == 0:
                break
        else:
            my_list.append(num)
            num_number += 1
        num += 1
    return my_list[my_num]


# print(test_1(MY_NUM - 1))

print(f'test_1 {timeit.timeit("test_1(MY_NUM)", globals=globals(), number=20)} milliseconds')
cProfile.run('test_1(MY_NUM)')

"""
=========================================================
"""


def test_2_erat(my_num):
    my_list = [i for i in range(100000)]
    my_list[1] = 0
    for num in my_list:
        if num > 1:
            for j in range(num * 2, len(my_list), num):
                my_list[j] = 0
    fin_list = [e for e in my_list if e != 0]
    return fin_list[my_num - 1]


# print(test_2_erat(MY_NUM))

print(f'test_2_erat {timeit.timeit("test_2_erat(MY_NUM)", globals=globals(), number=20)} milliseconds')
cProfile.run('test_2_erat(MY_NUM)')

"""
1.  Найти простое число под номером 10.
test_1 0.0010670900000000483 milliseconds
test_2_erat 0.688657517 milliseconds
Алгоритм с использованием решета в 688 раз медленнее.

2.  Найти простое число под номером 100.
test_1 0.017327596999999972 milliseconds
test_2_erat 0.689248723 milliseconds
Скорости работы алгоритма с использованием решета осталась без изменений. Скорость вычислений по алгоритму номер 1, 
увеличилась примерно в 17 раз.
Алгоритм с использованием решета в 40 раз медленнее.

3.  Найти простое число под номером 1000.
test_1 0.4456654849999997 milliseconds
test_2_erat 0.683860095 milliseconds
Алгоритм с использованием решета в 1.5 раза медленнее.

4.  Найти простое число под номером 9000.
test_1 10.989988778999999 milliseconds
test_2_erat 0.6836636089999999 milliseconds
Скорость работы алгоритма с использованием решета осталась практически без изменений. 
Скорость вычислений по первому алгоритму значительно возрасла.
Алгоритм с использованием решета работает в 16 раз быстрее.

Делаем вывод, что алгоритм с использованием решета становится более эффективен при поиске больших значений (от 1000)
test_1 - алгоритм имеет сложность O(n)
test_2_erat - имеет сложность O(log n)
"""