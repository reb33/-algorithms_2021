"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    def __init__(self, *nodes):
        # корень
        self.root = nodes[0]
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        if new_node >= self.root:
            print(f'LEFT el must be LESS root arg {self.root}')
            return
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node < self.root:
            print(f'RIGHT el must be GREATER OR EQUAl root arg {self.root}')
            return
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):

        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def __str__(self) -> str:
        return str(self.get_root_val())

    def pprint(self, level=0, prefix=''):
        print('..'*level+prefix+f'{str(self)}')
        if self.left_child:
            self.left_child.pprint(level=level+1, prefix='l-')
        if self.right_child:
            self.right_child.pprint(level=level+1, prefix='r-')


if __name__ == '__main__':
    r = BinaryTree(8)
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left(40)
    print(r.get_left_child())
    # print(r.get_left_child().get_root_val())
    r.insert_right(12)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val(16)
    print(r.get_right_child().get_root_val())
    r.insert_left(5)
    r.insert_left(7)
    r.get_left_child().insert_right(5)
    r.get_left_child().insert_right(7)

    print('Tree:')
    r.pprint()
