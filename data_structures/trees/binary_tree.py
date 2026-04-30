from typing import Any
from queue import Queue


class Node:
    def __init__(
        self, data: Any, left: "Node | None" = None, right: "Node | None" = None
    ):
        self.left: Node | None = left
        self.right: Node | None = right
        self.data: Any = data

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, node: Node):
        self.stack.append(node)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.stack.pop()


def build_a_tree() -> Node:
    a = Node(data=1)
    b = Node(data=2)
    c = Node(data=3)
    d = Node(data=4)
    e = Node(data=5)
    f = Node(data=6)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    return a


# ============================
#       DFS using Stack
# ============================


def preorder_traversal(node: Node):
    """
    Process current node first,
    then left,
    then right.
    """
    result = []
    stack = Stack()
    stack.push(node)
    while stack.size > 0:
        current = stack.pop()
        result.append(current.data)
        if current.right:
            stack.push(current.right)
        if current.left:
            stack.push(current.left)
    return result


def inorder_traversal(node: Node) -> list[Any]:
    """
    Process left node first,
    then current,
    then right.
    """
    result = []
    stack = Stack()
    stack.push(node)
    while stack.size > 0:
        node = stack.pop()
        if node.left:
            left = node.left
            stack.push(node)
            stack.push(left)
            node.left = None
            continue
        else:
            result.append(node.data)
            if node.right:
                stack.push(node.right)
                node.right = None

    return result


def postorder_traversal(node: Node) -> list[Any]:
    """
    Process left node first,
    then right,
    then current.
    """
    result = []
    stack = Stack()
    stack.push(node)
    while stack.size > 0:
        node = stack.pop()
        if node.left:
            stack.push(node)
            stack.push(node.left)
            node.left = None
            continue
        if node.right:
            stack.push(node)
            stack.push(node.right)
            node.right = None
            continue
        result.append(node.data)
    return result


# https://www.youtube.com/watch?v=EPwWrs8OtfI


# ============================
#       BFS using Queue
# ============================


def breadth_first_traversal(node: Node) -> list[Any]:
    q = Queue()
    q.put(node)
    result = []
    while not q.empty():
        node = q.get()
        result.append(node.data)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

    return result
