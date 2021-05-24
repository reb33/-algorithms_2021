"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from collections import deque
from random import uniform
from timeit import timeit


def merge_sort(lst):
    if len(lst) == 1 or len(lst) == 0:
        return
    left_lst, right_lst = lst[:len(lst) // 2], lst[len(lst) // 2:]
    merge_sort(left_lst)
    merge_sort(right_lst)
    n = m = k = 0
    tmp_lst = [0] * (len(left_lst) + len(right_lst))
    while n < len(left_lst) and m < len(right_lst):
        if left_lst[n] <= right_lst[m]:
            tmp_lst[k] = left_lst[n]
            n += 1
        else:
            tmp_lst[k] = right_lst[m]
            m += 1
        k += 1
    while n < len(left_lst):
        tmp_lst[k], n, k = left_lst[n], n + 1, k + 1
    while m < len(right_lst):
        tmp_lst[k], m, k = right_lst[m], m + 1, k + 1
    for i in range(len(lst)):
        lst[i] = tmp_lst[i]


def merge_sort_stack(lst):
    deq = deque(map(lambda x: [x], lst))
    while len(deq) > 1:
        left = deq.popleft()
        right = deq.popleft()
        n = m = k = 0
        tmp_lst = [0] * (len(left) + len(right))
        while n < len(left) and m < len(right):
            if left[n] <= right[m]:
                tmp_lst[k] = left[n]
                n += 1
            else:
                tmp_lst[k] = right[m]
                m += 1
            k += 1
        while n < len(left):
            tmp_lst[k], n, k = left[n], n + 1, k + 1
        while m < len(right):
            tmp_lst[k], m, k = right[m], m + 1, k + 1
        deq.append(tmp_lst)
    return deq[0]


if __name__ == '__main__':
    lst = [round(uniform(0, 50), 3) for _ in range(10)]
    print(lst)
    lst_copy = lst[:]
    merge_sort(lst_copy)
    print(lst_copy)
    print(merge_sort_stack(lst[:]))
    print(timeit(
        'merge_sort(lst[:])',
        'from __main__ import merge_sort, lst',
        number=100
    ))
    print(timeit(
        'merge_sort_stack(lst[:])',
        'from __main__ import merge_sort_stack, lst',
        number=100
    ))
    lst1 = [round(uniform(0, 50), 3) for _ in range(100)]
    print(timeit(
        'merge_sort(lst1[:])',
        'from __main__ import merge_sort, lst1',
        number=100
    ))
    print(timeit(
        'merge_sort_stack(lst1[:])',
        'from __main__ import merge_sort_stack, lst1',
        number=100
    ))
    lst2 = [round(uniform(0, 50), 3) for _ in range(1000)]
    print(timeit(
        'merge_sort(lst2[:])',
        'from __main__ import merge_sort, lst2',
        number=100
    ))
    print(timeit(
        'merge_sort_stack(lst2[:])',
        'from __main__ import merge_sort_stack, lst2',
        number=100
    ))
    lst3 = [round(uniform(0, 50), 3) for _ in range(10000)]
    print(timeit(
        'merge_sort(lst3[:])',
        'from __main__ import merge_sort, lst3',
        number=100
    ))
    print(timeit(
        'merge_sort_stack(lst3[:])',
        'from __main__ import merge_sort_stack, lst3',
        number=100
    ))

