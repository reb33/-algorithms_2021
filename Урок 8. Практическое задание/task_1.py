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
from collections import Counter


class Element:
    __slots__ = ['value', 'num']

    def __init__(self, value, num) -> None:
        self.value = value
        self.num = num


class ListEls:

    def __init__(self, counted_vals: dict) -> None:
        self.els = [Element(*el) for el in sorted(counted_vals.items(), key=lambda x: x[1])]

    def add(self, element=None):
        for i, el in enumerate(self.els):
            if element.num <= el.num:
                self.els.insert(i, element)
                return
        self.els.append(element)

    def arrange(self):
        




class ElTree:

    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


def main(text):
    ListEls(Counter(text))
    print()


if __name__ == '__main__':
    main('beep boop beer!')
