from typing import Optional, List

from stack import Stack
from queue_ import Queue


class Node():
    def __init__(self, data: int):
        self.data: int = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __str__(self):
        return "Node(%d)" % self.data

    def __repr__(self):
        return "Node(%d)" % self.data


class BinaryTree():
    def __init__(self):
        self.root = None
        self.count = 0

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root

        if node is not None:
            print(" " * (level * 4) + prefix + str(node.data))
            if node.left is not None or node.right is not None:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")

    def insert(self, value: int):
        self.root = self._insert(self.root, value)

    def _insert(self, root: Optional[Node], value: int) -> Optional[Node]:
        if not root:
            return Node(value)
        if root.data < value:
            root.right = self._insert(root.right, value)
        else:
            root.left = self._insert(root.left, value)
        return root

    def search(self, value: int) -> Optional[Node]:
        if type(value) != int:
            raise TypeError("Accepting int only")
        node = self.root
        while node:
            if node.data == value:
                return node
            if node.data > value:
                node = node.left
            else:
                node = node.right
        return None

    def delete(self, value: int):
        node = self.root
        if not node:
            return
        parent = None
        while node and node.data != value:
            if node.data > value:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right

        if not node:
            raise ValueError("Not found")

        if parent:
            # No children
            if all([not node.left, not node.right]):
                if parent.left is node:
                    parent.left = None
                elif parent.right is node:
                    parent.right = None
            # any child
            if any([node.left, node.right]):
                child = node.left or node.right
                if parent.left is node:
                    parent.left = child
                else:
                    parent.right = child
        else:
            child = node.left or node.right
            self.root = child

    def inorder(self) -> List[int]:
        values: List[int] = []
        self._inorder(self.root, values)
        return values

    def _inorder(self, node, values):
        if node:
            self._inorder(node.left, values)
            values.append(node.data)
            self._inorder(node.right, values)

    def preorder(self) -> List[int]:
        values: List[int] = []
        self._preorder(self.root, values)
        return values

    def _preorder(self, node, values):
        if node:
            values.append(node.data)
            self._preorder(node.left, values)
            self._preorder(node.right, values)

    def postorder(self) -> List[int]:
        values: List[int] = []
        self._postorder(self.root, values)
        return values

    def _postorder(self, node, values):
        if node:
            self._postorder(node.left, values)
            self._postorder(node.right, values)
            values.append(node.data)

    def get_leaves(self) -> List[int]:
        values: List[int] = []
        self._get_leaves(self.root, values)
        return values
    
    def _get_leaves(self, node, values):
        if node:
            if not node.left and not node.right:
                values.append(node.data)
            self._get_leaves(node.left, values)
            self._get_leaves(node.right, values)

    def stacked_inorder(self) -> List[int]:
        stack = Stack()
        values: List[int] = []
        current = self.root
        while True:
            if current:
                stack.push(current)
                current = current.left
            if not current and stack.size > 0:
                current = stack.pop()
                values.append(current.data)
                current = current.right
            elif not current and stack.size == 0:
                break
        return values

    def bft(self) -> List[int]:
        values: List[int] = []
        q = Queue()
        q.enqueue(self.root)
        while q.size > 0:
            node = q.dequeue()
            if node:
                values.append(node.data)
                if node.left:
                    q.enqueue(node.left)
                if node.right:
                    q.enqueue(node.right)
        return values

    def max_avg(self):
        values = []
        self._max_avg(self.root, values)
        print(values)
        return max(values)
    
    def _max_avg(self, node, values):
        if node:
            left_avg, left_count = self._max_avg(node.left, values)
            right_avg, right_count = self._max_avg(node.right, values)
            s = sum([left_avg * left_count, right_avg * right_count, node.data])
            count = left_count + right_count + 1
            average = s / count
            values.append(average)
            return average, count
        return 0, 0
