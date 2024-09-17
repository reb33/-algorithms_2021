"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from collections import deque
from contextlib import suppress
from functools import reduce
from math import ceil, sqrt
from random import randint
from timeit import default_timer
from typing import Tuple

import memory_profiler
import numpy
from memory_profiler import profile
from recordclass import recordclass


def measuring(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        res = func(*args, **kwargs)
        time_exec = default_timer() - start_time
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        print(func.__name__)
        print('выполнение заняло памяти', mem_diff)
        print('выполнение заняло времени', time_exec)
        return res

    return wrapper


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other: 'ComplexNumber'):
        # z1=a1+b1i и z2=a2+b2i
        # z=z1⋅z2=(a1a2−b1b2)+(a1b2+b1a2)i
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __str__(self):
        return f'{self.real} + {self.imaginary}i'


class ComplexNumberSlots(ComplexNumber):
    __slots__ = ('real', 'imaginary')


def calc_complex_numbers_1(*nums: Tuple[int, int]):
    complexes = [ComplexNumber(*compl) for compl in nums]
    res = complexes[0]
    for compl in complexes[1:]:
        res += compl
    print(res)


def calc_complex_numbers_slots(*nums: Tuple[int, int]):
    complexes = [ComplexNumberSlots(*compl) for compl in nums]
    res = complexes[0]
    for compl in complexes[1:]:
        res += compl
    print(res)


def calc_complex_numbers_map(*nums: Tuple[int, int]):
    complexes = map(lambda x: ComplexNumber(*x), nums)
    print(reduce(lambda x, y: x + y, complexes))


def get_three_profitable_companies_1(*companies: Tuple[str, int]):
    # Имеется хранилище с информацией о компаниях: название и годовая прибыль.
    # Для реализации хранилища можно применить любой подход,
    # который вы придумаете, например, реализовать словарь.
    # Реализуйте поиск трех компаний с наибольшей годовой прибылью.
    # Выведите результат.
    companies_ = dict(companies)
    max_profs = {}
    for i in range(3):
        max_ = ('', 0)
        for name, prof in companies_.items():
            if prof > max_[1]:
                max_ = (name, prof)
        companies_.pop(max_[0])
        max_profs[max_[0]] = max_[1]
    print(max_profs)


def get_three_profitable_companies_recordclass(*companies: Tuple[str, int]):
    Company = recordclass('Company', ('name', 'profit'))
    companies_ = [Company(c[0], c[1]) for c in companies]
    max_profs = {}
    for i in range(3):
        max_ = ('', 0, None)
        for index, c in enumerate(companies_):
            if c.profit > max_[1]:
                max_ = (c.name, c.profit, index)
        companies_.pop(max_[2])
        max_profs[max_[0]] = max_[1]
    print(max_profs)


def get_three_profitable_companies_tuples(*companies: Tuple[str, int]):
    companies_ = tuple(companies)
    max_profs = {}
    exclude_indexes = []
    for i in range(3):
        max_ = ('', 0, None)
        for index, c in enumerate(companies_):
            if index in exclude_indexes:
                continue
            if c[1] > max_[1]:
                max_ = (c[0], c[1], index)
        exclude_indexes.append(max_[2])
        max_profs[max_[0]] = max_[1]
    print(max_profs)


def get_simple_sieve_of_eratosphenes(num):
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
    print(simples[num])


def get_simple_sieve_of_eratosphenes_numpy(num):
    coef = 10 if num < 6000 else 15
    upper_board = num * coef
    els = numpy.array([True for _ in range(upper_board)])
    for i in range(2, ceil(sqrt(upper_board))):
        if els[i]:
            j = i * i
            while j < upper_board:
                els[j] = False
                j += i
    simples = [i for i, v in enumerate(els) if v]
    print(simples[num + 1])


def get_simple_map(num):
    coef = 10 if num < 6000 else 15
    upper_board = num * coef

    def check_num(els):
        lst, x = els
        if not any(x % el == 0 for el in lst):
            lst.append(x)
            return x

    simples = [2]  # пропускаем 2 элемента
    res = map(check_num, ((simples, x) for x in range(3, upper_board)))  # 2 элемента пропустили в начале
    i = 0
    while i <= num-2:  # 2 элемента пропустили в начале
        i += 1 if next(res) else 0
    print(simples[-1])


def main():
    print('!!!!!!!!!!!!!!!!!!!!!!!!!Задача на вычисление суммы комплексных чисел!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    measuring(calc_complex_numbers_1)(*zip((5, 10) * 50000, (8, 5) * 50000))
    measuring(calc_complex_numbers_slots)(*zip((5, 10) * 50000, (8, 5) * 50000))
    measuring(calc_complex_numbers_map)(*zip((5, 10) * 50000, (8, 5) * 50000))

    print('!!!!!!!!!!!!!!!!!!!!!!!Задача на вычисление 3 самые прибыльные компании!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    def randname():
        return ''.join(chr(randint(66, 122)) for _ in range(5))

    n = 100000
    companies = list(zip((randname() for _ in range(n)), (randint(1, 10000) for _ in range(n))))
    measuring(get_three_profitable_companies_1)(*companies)
    measuring(get_three_profitable_companies_recordclass)(*companies)
    measuring(get_three_profitable_companies_tuples)(*companies)

    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Вычисление решета Эратосфена!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    measuring(get_simple_sieve_of_eratosphenes)(7000)
    measuring(get_simple_sieve_of_eratosphenes_numpy)(7000)
    measuring(get_simple_map)(7000)


if __name__ == '__main__':
    main()

# !!!!!!!!!!!!!!!!!!!!!!!!!Задача на вычисление суммы комплексных чисел!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 750000 + 650000i
# calc_complex_numbers_1
# выполнение заняло памяти 1.30078125
# выполнение заняло времени 0.19030757003929466
#
# 750000 + 650000i
# calc_complex_numbers_slots
# выполнение заняло памяти 1.2421875
# выполнение заняло времени 0.19434969604481012
#
# 750000 + 650000i
# calc_complex_numbers_map
# выполнение заняло памяти 0.0078125
# выполнение заняло времени 0.1642789279576391
#
# выполнение с помощью классов со слотами занимает меньше места чем выполнение через обычные классы
# выполнение через map практически не занимает места, т.к. это генератор
# время работы приблезительно одинаковое


# !!!!!!!!!!!!!!!!!!!!!!!Задача на вычисление 3 самые прибыльные компании!!!!!!!!!!!!!!!!!!!!!!!!!!!
# {'t_obg': 10000, 'EbyVl': 10000, 'ex^HW': 10000}
# get_three_profitable_companies_1
# выполнение заняло памяти 9.046875
# выполнение заняло времени 0.040055315010249615
#
# {'wSwHM': 10000, 'aTKlv': 10000, 'VaNus': 10000}
# get_three_profitable_companies_recordclass
# выполнение заняло памяти 0.5859375
# выполнение заняло времени 0.08031825802754611
#
# {'nLDdh': 10000, 'zgsSK': 10000, 'orgjK': 10000}
# get_three_profitable_companies_tuples
# выполнение заняло памяти 0.59765625
# выполнение заняло времени 0.04912060499191284
#
# выполнение с recordclass и с tuples заняло значительно меньше памяти
# по времени выполнения вариант с recordclass занял больше времени


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Вычисление решета Эратосфена!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 70657
# get_simple_sieve_of_eratosphenes
# выполнение заняло памяти 7.1015625
# выполнение заняло времени 0.04818689508829266
#
# 70657
# get_simple_sieve_of_eratosphenes_numpy
# выполнение заняло памяти 1.2421875
# выполнение заняло времени 0.04008883598726243
#
# 70657
# get_simple_map
# выполнение заняло памяти 0.24609375
# выполнение заняло времени 2.6348919740412384
#
# выполнение через numpy.array заняло меньше памяти через выполнение через dict
# выполнение через map заняло меньше памяти, но время выполнения значительно больше
