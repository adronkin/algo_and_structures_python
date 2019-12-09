"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

from math import sqrt
from memory_profiler import profile

MY_NUM = 5000


@profile
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
    return my_list[my_num - 1]


print(test_1(MY_NUM))

"""
=========================================================
"""


@profile
def test_2_erat(my_num):
    my_list = [i for i in range(100000)]
    my_list[1] = 0
    for num in my_list:
        if num > 1:
            for j in range(num * 2, len(my_list), num):
                my_list[j] = 0
    fin_list = [e for e in my_list if e != 0]
    return fin_list[my_num - 1]


print(test_2_erat(MY_NUM))

"""
Версия Python 3.7.3
MacOS 10.15

test_1
Line #    Mem usage    Increment   Line Contents
================================================
    22     10.4 MiB     10.4 MiB   @profile
    23                             def test_1(my_num):
    24     10.4 MiB      0.0 MiB       my_list = []
    25     10.4 MiB      0.0 MiB       num, num_number = 2, 0
    26     10.6 MiB      0.0 MiB       while num_number <= my_num:
    27     10.6 MiB      0.0 MiB           if num > 10:
    28     10.6 MiB      0.0 MiB               if num % 2 == 0 or num % 5 == 0:
    29                                             pass
    30     10.6 MiB      0.0 MiB           for i in range(2, num):
    31     10.6 MiB      0.0 MiB               if i > sqrt(num):
    32     10.6 MiB      0.0 MiB                   my_list.append(num)
    33     10.6 MiB      0.0 MiB                   num_number += 1
    34     10.6 MiB      0.0 MiB                   break
    35     10.6 MiB      0.0 MiB               if num % i == 0:
    36     10.6 MiB      0.0 MiB                   break
    37                                     else:
    38     10.4 MiB      0.0 MiB               my_list.append(num)
    39     10.4 MiB      0.0 MiB               num_number += 1
    40     10.6 MiB      0.0 MiB           num += 1
    41     10.6 MiB      0.0 MiB       return my_list[my_num - 1]
    
test_2_erat 
Line #    Mem usage    Increment   Line Contents
================================================
    51     10.6 MiB     10.6 MiB   @profile
    52                             def test_2_erat(my_num):
    53     16.6 MiB      0.7 MiB       my_list = [i for i in range(100000)]
    54     16.6 MiB      0.0 MiB       my_list[1] = 0
    55     16.6 MiB      0.0 MiB       for num in my_list:
    56     16.6 MiB      0.0 MiB           if num > 1:
    57     16.6 MiB      0.0 MiB               for j in range(num * 2, len(my_list), num):
    58     16.6 MiB      0.0 MiB                   my_list[j] = 0
    59     11.0 MiB      0.0 MiB       fin_list = [e for e in my_list if e != 0]
    60     11.0 MiB      0.0 MiB       return fin_list[my_num - 1]
    
    
Первый алгоритм нахождения i-го по счёту простого числа использовал 10.4 MiB памяти.
Алгоритм с использованием решета Эратосфена использовал 16.6 MiB памяти, т.е. оказался более затратным.
При нахождении простого числа до 5000 элемента, первый алгоритм значительно более эффективно раходует выделенную память.
Но при работе с большими числами, учитывая выделенную память и скорость работы алгоритма, 
алгоритм с использованием решета Эратосфена менее продолжительное время использует выделенную память, 
а значит более эффективен.
"""