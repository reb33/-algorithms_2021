"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000

Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""
from math import ceil, sqrt
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def sieve_of_eratosphenes(num):
    coef = 10 if num < 6000 else 15
    upper_board = num * coef
    els = {i: True for i in range(1, upper_board)}
    for i in range(2, ceil(sqrt(upper_board))):
        if els[i]:
            j = i * i
            while j < upper_board:
                els[j] = False
                j += i
    simples = [k for k, v in els.items() if v]
    return simples[num]


# rnd = int(input('Введите порядковый номер искомого простого числа:\n'))
# print(simple(rnd))
# print(sieve_of_eratosphenes(rnd))


print('10 простое число метод перебора ', timeit('simple(10)', 'from __main__ import simple', number=1))
print('10 простое число решето ', timeit('sieve_of_eratosphenes(10)', 'from __main__ import sieve_of_eratosphenes',
                                         number=1))

print('100 простое число метод перебора ', timeit('simple(100)', 'from __main__ import simple', number=1))
print('100 простое число решето ',
      timeit('sieve_of_eratosphenes(100)', 'from __main__ import sieve_of_eratosphenes', number=1))

print('1000 простое число метод перебора ', timeit('simple(1000)', 'from __main__ import simple', number=1))
print('1000 простое число решето ',
      timeit('sieve_of_eratosphenes(1000)', 'from __main__ import sieve_of_eratosphenes', number=1))

# 10 простое число метод перебора       3.358698450028896e-05
# 10 простое число решето               0.000112134002847597
# 100 простое число метод перебора      0.003166925016557798
# 100 простое число решето              0.0003718429943546653
# 1000 простое число метод перебора     0.38552172199706547
# 1000 простое число решето             0.003140006010653451

# при малых числах метод перебора быстрей
# но уже при поиске 100 простого числа решето работает быстрей
# при поиске 1000 простого числа решето работает в 100 раз быстрей
