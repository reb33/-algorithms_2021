"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""
from collections import deque
from timeit import timeit


def deque_append(deq: deque):
    deq.append(1)


def deque_pop(deq: deque):
    deq.pop()


def deque_appendleft(deq: deque):
    deq.appendleft(1)


def deque_popleft(deq: deque):
    deq.popleft()


def deque_remove():
    deque(i for i in range(10)).remove(5)


def deque_fill():
    deque(i for i in range(10))


def deque_get(deq: deque):
    x = deq[15]


def list_append(lst: list):
    lst.append(1)


def list_pop(lst: list):
    lst.pop()


def list_appendleft(lst: list):
    lst.insert(0, 1)


def list_popleft(lst: list):
    lst.pop(0)


def list_remove():
    list(i for i in range(10)).remove(5)


def list_fill():
    list(i for i in range(10))


def list_get(lst):
    x = lst[5]


if __name__ == '__main__':
    print('\t\tlist\t\t\tdeque')
    print('fill', timeit('list_fill()', 'from __main__ import list_fill'), end='\t')
    print(timeit('deque_fill()', 'from __main__ import deque_fill'))

    deq = deque(i for i in range(1000))
    lst = list(i for i in range(1000))

    print('get', timeit('list_get(lst)', 'from __main__ import list_get, lst'), end='\t')
    print(timeit('deque_get(deq)', 'from __main__ import deque_get, deq'))

    print('append', timeit('list_append(lst)', 'from __main__ import list_append, lst'), end='\t')
    print(timeit('deque_append(deq)', 'from __main__ import deque_append, deq'))
    print('pop', timeit('list_pop(lst)', 'from __main__ import list_pop, lst'), end='\t')
    print(timeit('deque_pop(deq)', 'from __main__ import deque_pop, deq'))
    print('appendleft', timeit('list_appendleft(lst)', 'from __main__ import list_appendleft, lst'), end='\t')
    print(timeit('deque_appendleft(deq)', 'from __main__ import deque_appendleft, deq'))
    print('popleft', timeit('list_popleft(lst)', 'from __main__ import list_popleft, lst'), end='\t')
    print(timeit('deque_popleft(deq)', 'from __main__ import deque_popleft, deq'))

    print('remove', timeit('list_remove()', 'from __main__ import list_remove'), end='\t')
    print(timeit('deque_remove()', 'from __main__ import deque_remove'))


# 		list			deque
# fill 1.3543147210148163	1.204766502021812
# get 0.10826835699845105	0.11773397799697705
# append 0.14653991698287427	0.14600678099668585
# pop 0.16743343099369667	0.13992940197931603
# appendleft 250.5061836859968	0.14643970798351802
# popleft 150.46432287900825	0.14291279300232418
# remove 1.3821231479814742	1.395541920006508

# Получение элемента для листа выполняется быстрей
# append, pop и remove выполняется с приблизительно одинаковой скоростью
# но appendleft и popleft выполняются быстрей чем insert(0, x) и pop(0)
