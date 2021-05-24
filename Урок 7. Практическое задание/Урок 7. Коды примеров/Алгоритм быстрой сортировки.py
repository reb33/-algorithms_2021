"""Быстрая сортировка"""

import timeit
import random


def my_calc(lst_obj):
    def quick_sort(lst_obj):
        if len(lst_obj) <= 1:
            return lst_obj
        else:
            q = random.choice(lst_obj)
            L = []
            M = []
            R = []
            for elem in lst_obj:
                if elem < q:
                    L.append(elem)
                elif elem > q:
                    R.append(elem)
                else:
                    M.append(elem)
            return quick_sort(L) + M + quick_sort(R)
    return quick_sort


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "my_calc(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "my_calc(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "my_calc(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.00031299999999999384
0.0006287000000000098
0.0020312999999999998
"""
