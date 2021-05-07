"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_3():
    m = 0
    num = 0
    count_els = set(array)
    for i in count_els:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(timeit('func_1()', 'from __main__ import func_1'))
print(timeit('func_2()', 'from __main__ import func_2'))
print(timeit('func_3()', 'from __main__ import func_3'))


# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# 1.8374580730160233
# 2.687536692013964 - медленей 1 алгоритма, т.к. есть 2 прохода по циклу (создание цикла new_array и max)
# 1.4838648090080824 - быстрей 1 алгоритма, т.к. не вычисляется количество элементов повторно
#                      для всех повторяющихся элементов
