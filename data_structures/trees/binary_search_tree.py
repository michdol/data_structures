from typing import Any


class Node:
    def __init__(
        self, data: Any, left: "Node | None" = None, right: "Node | None" = None
    ):
        self.left: Node | None = left
        self.right: Node | None = right
        self.data: Any = data

    def __str__(self):
        return str(self.data)


def build_tree():
    a = Node(data=1)
    b = Node(data=2)
    c = Node(data=3)
    d = Node(data=4)
    e = Node(data=5)
    f = Node(data=6)

    d.left = b
    b.left = a
    b.right = c
    d.right = e
    e.right = f
    return d


def search(root: Node, value: int) -> int | None:
    if not root:
        return None
    node = root
    while node:
        if node.data == value:
            return value
        if node.data > value:
            node = node.left
        else:
            node = node.right
    return None
