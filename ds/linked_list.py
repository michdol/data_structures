from typing import Optional, Any, Generator


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self._size = 0

    def _increment_size(self):
        self._size += 1

    def _deincrement_size(self):
        self._size -= 1

    def append(self, node: Node):
        if not self.head:
            self.head = node
            self._increment_size()
            return
        tmp = self.head
        while True:
            if not tmp.next:
                tmp.next = node
                self._increment_size()
                break
            tmp = tmp.next

    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node
        self._increment_size()

    def pop(self) -> Optional[Node]:
        if not self.head:
            return None
        tmp = self.head
        previous = None
        while tmp.next:
            previous = tmp
            tmp = tmp.next
        if previous:
            previous.next = None
        self._deincrement_size()
        if tmp is self.head:
            self.head = None
        return tmp

    def size(self) -> int:
        return self._size

    def first(self) -> Optional[Node]:
        return self.head

    def last(self) -> Optional[Node]:
        if not self.head:
            return None
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        return tmp

    def find(self, data: Any) -> Optional[Node]:
        tmp = self.head
        while tmp:
            if tmp.data == data:
                return tmp
            tmp = tmp.next
        return None

    def get(self, idx) -> Optional[Node]:
        if idx + 1 > self.size():
            raise IndexError("Index out of range")
        count = 0
        tmp = self.head
        while count != idx:
            tmp = tmp.next
            count += 1
        return tmp

    @property
    def count(self) -> int:
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count
