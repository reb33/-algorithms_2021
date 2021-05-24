"""Сортировка выбором"""

import timeit
import random


def selection_sort(lst_obj):
    for i in range(len(lst_obj)):
        idx_min = i
        for j in range(i + 1, len(lst_obj)):
            if lst_obj[j] < lst_obj[idx_min]:
                idx_min = j

        tmp = lst_obj[idx_min]
        lst_obj[idx_min] = lst_obj[i]
        lst_obj[i] = tmp

    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "selection_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "selection_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "selection_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.008928599999999995
0.5506933
44.9177326
"""
