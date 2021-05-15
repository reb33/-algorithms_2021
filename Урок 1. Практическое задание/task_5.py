"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
from contextlib import suppress


class StackClass:

    def __init__(self, size):
        self.size = size
        self.memory = [[]]

    def add(self, el):
        if len(self.memory[-1]) < self.size:
            self.memory[-1].append(el)
        else:
            self.memory.append([el])

    def pop(self):
        with suppress(IndexError):
            return self.memory[-1].pop()
        if len(self.memory) > 1:
            self.memory.pop()
            return self.memory[-1].pop()
        else:
            raise IndexError

    def len(self):
        return sum(len(lst) for lst in self.memory)

    def is_empty(self):
        return self.len() == 0

    def __str__(self) -> str:
        return str(self.memory)


if __name__ == '__main__':
    dishes = StackClass(7)
    for i in range(1, 16):
        dishes.add(i)
    print(dishes)
    print('len', dishes.len())
    print('is_empty', dishes.is_empty())
    print(dishes.pop())
    print(dishes.pop())

    print(dishes)
    print('len', dishes.len())
    for i in range(13):
        print(dishes.pop(), end=', ' if i != 12 else '\n')

    print('is_empty', dishes.is_empty())

    try:
        dishes.pop()
    except IndexError:
        print('IndexError')
