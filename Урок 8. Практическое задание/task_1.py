"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.


2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""
from collections import Counter, deque


class Element:
    __slots__ = ['value', 'num']

    def __init__(self, value, num) -> None:
        self.value = value
        self.num = num


class ListEls:

    def __init__(self, counted_vals: dict) -> None:
        # сортируем согласно частоте появления и порядку знака
        self.els = [Element(*el) for el in sorted(counted_vals.items(), key=lambda x: (x[1], ord(x[0])*-1))]

    def add(self, element):
        # добавляем элементы в список согласно его числовому значению
        for i, el in enumerate(self.els):
            if element.num <= el.num:
                self.els.insert(i, element)
                return
        self.els.append(element)

    def arrange(self):
        # соединяем элементы в единное дерево
        while len(self.els) > 1:
            left = self.els.pop(0)
            right = self.els.pop(0)
            self.add(Element(ElTree(left.value, right.value), left.num+right.num))

    def get_codes(self):
        self.arrange()
        return self.els[0].value.get_codes()


class ElTree:

    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_codes(self):
        # Горизонтальный обход дерева
        deq = deque([(self, '')])
        values = {}
        while deq:
            cur, s = deq.popleft()
            if isinstance(cur, ElTree):
                deq.appendleft((cur.left, s+'0'))
                deq.appendleft((cur.right, s+'1'))
            if isinstance(cur, str):
                values[cur] = s
        return values


def main(text):
    values = ListEls(Counter(text)).get_codes()
    print(values)


if __name__ == '__main__':
    main('beep boop beer!')


# {'e': '11', 'p': '101', '!': '1001', 'r': '1000', ' ': '011', 'o': '010', 'b': '00'}
