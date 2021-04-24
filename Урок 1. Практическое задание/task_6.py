"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
from contextlib import suppress


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def __str__(self):
        return str(self.elems)


class Board:
    def __init__(self):
        self.to_do = QueueClass()
        self.in_process = QueueClass()
        self.done = QueueClass()

    def add(self, task):
        self.to_do.to_queue(task)

    def to_work(self):
        with suppress(IndexError):
            task = self.to_do.from_queue()
            print(f'`{task}` взята в работу')
            self.in_process.to_queue(task)
            return
        print('нет доступных задач в to_do list')

    def done_work(self):
        with suppress(IndexError):
            task = self.in_process.from_queue()
            print(f'`{task}` выполнена')
            self.done.to_queue(task)
            return
        print('нет доступных задач в in_process list')

    def count_planned_task(self):
        return self.to_do.size()

    def count_active_task(self):
        return self.in_process.size()

    def count_done_task(self):
        return self.done.size()

    def size(self):
        return self.count_planned_task()+self.count_active_task()+self.count_done_task()

    def __str__(self):
        return f"""
        to_do {self.to_do}
        in_process {self.in_process}
        done {self.done}
        """


if __name__ == '__main__':
    board = Board()
    board.add('помыть посуду')
    board.add('запустить стирку')
    board.add('вымыть полы')
    board.add('помыть кота')
    board.add('покормить кота')
    board.add('выгулять собаку')

    print(board)

    board.to_work()
    board.to_work()
    board.to_work()
    board.to_work()
    board.to_work()

    board.done_work()
    board.done_work()
    board.done_work()
    board.done_work()
    board.done_work()
    board.done_work()

    board.to_work()
    board.to_work()
    board.to_work()

    board.add('оплатить коммуналку')
    board.add('помыть холодильник')
    print(board)
