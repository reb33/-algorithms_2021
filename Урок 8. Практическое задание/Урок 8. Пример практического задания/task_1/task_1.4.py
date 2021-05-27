"""Хаффман через ООП"""

string = "beep boop beer!"
print("Исходная строка: " + string)


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def make_haffman_tree(node, code=""):
    if type(node) is str:
        return {
            node: code
        }

    l, r = node.children()

    result = {}
    # 0 - налево, 1 - направо
    result.update(make_haffman_tree(l, code + "0"))
    result.update(make_haffman_tree(r, code + "1"))

    return result


frequencies = {}
for char in string:
    if char not in frequencies:
        frequencies[char] = 0

    frequencies[char] += 1

tree = frequencies.items()

while len(tree) > 1:
    tree = sorted(tree, reverse=True, key=lambda x: x[1])
    char1, count1 = tree[-1]
    char2, count2 = tree[-2]
    tree = tree[:-2]
    tree.append(
        (Node(char1, char2), count1 + count2)
    )

code_table = make_haffman_tree(tree[0][0])

coded = []
for char in string:
    coded.append(code_table[char])

print("Закодированная строка: %s" % "".join(coded))
