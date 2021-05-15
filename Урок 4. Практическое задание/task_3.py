"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
from cProfile import run
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    entered_num_str = str(enter_num)
    return ''.join(entered_num_str[i] for i in range(len(entered_num_str) - 1, -1, -1))


def main():
    print(revers_1(123456789))
    print(revers_2(123456789))
    print(revers_3(123456789))
    print(revers_4(123456789))


if __name__ == '__main__':
    run('main()')
    print(timeit('revers_1(123456789)', 'from __main__ import revers_1'))
    print(timeit('revers_2(123456789)', 'from __main__ import revers_2'))
    print(timeit('revers_3(123456789)', 'from __main__ import revers_3'))
    print(timeit('revers_4(123456789)', 'from __main__ import revers_4'))

# 987654321.0
# 987654321.0
# 987654321
# 987654321
#          33 function calls (24 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      10/1    0.000    0.000    0.000    0.000 task_3.py:20(revers_1)
#         1    0.000    0.000    0.000    0.000 task_3.py:30(revers_2)
#         1    0.000    0.000    0.000    0.000 task_3.py:38(revers_3)
#         1    0.000    0.000    0.000    0.000 task_3.py:44(revers_4)
#        10    0.000    0.000    0.000    0.000 task_3.py:46(<genexpr>)  -  рекурсия вызывалась 10 раз
#         1    0.000    0.000    0.000    0.000 task_3.py:49(main)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#
#
# 2.612349307979457 - самый худший метод так как рекурсия
# 1.5964713350113016 - метод лучше так как нет рекурсии есть 1 цикл
# 0.41587080800672993 - лучший метод так как есть перевод в строку и срез
# 1.9734655369829852 - метод хуже 2 и 3 так как есть перевод в строку и 2 цикла (range и join)

