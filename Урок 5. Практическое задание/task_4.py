"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def dict_fill():
    dct = {}
    for i in range(10):
        dct[i] = i


def dict_get(dct: dict):
    x = dct[50]


def dict_range_items(dct: dict):
    [(k, v) for k, v in dct.items()]


def dict_values(dct: dict):
    dct.values()


def dict_keys(dct: dict):
    dct.keys()


def dict_copy(dct: dict):
    dct.copy()


def dict_pop(dct: dict):
    dct.copy().pop(5)


def orderdict_fill():
    dct = OrderedDict()
    for i in range(10):
        dct[i] = i


if __name__ == '__main__':
    print('\t\t\t\tdict\t\t\tordereddict')
    print('fill\t\t', timeit('dict_fill()', 'from __main__ import dict_fill'), end='\t')
    print(timeit('orderdict_fill()', 'from __main__ import orderdict_fill'))

    dict_1 = {i: i for i in range(100)}
    ordereddict_1 = OrderedDict({i: i for i in range(100)})

    print('get\t\t\t', timeit('dict_get(dict_1)', 'from __main__ import dict_get, dict_1'), end='\t')
    print(timeit('dict_get(ordereddict_1)', 'from __main__ import dict_get, ordereddict_1'))

    print('range_items\t', timeit('dict_range_items(dict_1)', 'from __main__ import dict_range_items, dict_1'),
          end='\t')
    print(timeit('dict_range_items(ordereddict_1)', 'from __main__ import dict_range_items, ordereddict_1'))

    print('values\t', timeit('dict_values(dict_1)', 'from __main__ import dict_values, dict_1'), end='\t')
    print(timeit('dict_values(ordereddict_1)', 'from __main__ import dict_values, ordereddict_1'))

    print('keys\t', timeit('dict_keys(dict_1)', 'from __main__ import dict_keys, dict_1'), end='\t')
    print(timeit('dict_keys(ordereddict_1)', 'from __main__ import dict_keys, ordereddict_1'))

    print('copy\t\t', timeit('dict_copy(dict_1)', 'from __main__ import dict_copy, dict_1'), end='\t')
    print(timeit('dict_copy(ordereddict_1)', 'from __main__ import dict_copy, ordereddict_1'))

    dict_2 = {i: i for i in range(10)}
    ordereddict_2 = OrderedDict({i: i for i in range(10)})

    print('pop\t\t\t', timeit('dict_pop(dict_2)', 'from __main__ import dict_pop, dict_2'), end='\t')
    print(timeit('dict_pop(ordereddict_2)', 'from __main__ import dict_pop, ordereddict_2'))

#   				dict			ordereddict
# fill		     1.1829542470513843	1.4153491759789176
# get			 0.1257730619981885	0.12743454898009077
# range_items	 7.260533020016737	10.224922840017825
# values	     0.1660526919877156	0.1670889129745774
# keys	         0.1705236749839969	0.16555290500400588
# copy		     2.260810127016157	8.505685593001544
# pop			 0.504649921960663	1.0476042620139197
#
# OrderedDict работает чуть медленнее
# это особенно заметно на copy, pop и обходе элемнтов
