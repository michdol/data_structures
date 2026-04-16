from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next: Optional["Node"] = None):
        self.data: Any = data
        self.next: Node | None = next


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self._length: int = 0

    @property
    def length(self) -> int:
        return self._length

    def prepend(self, data: Any):
        node = Node(data=data)
        if self.head:
            node.next = self.head
        self.head = node
        self._length += 1

    def append(self, data: Any):
        node = Node(data=data)
        last = self.get_last()
        if last:
            last.next = node
        else:
            self.head = node
        self._length += 1

    def get_last(self) -> Node | None:
        if not self.head:
            return None
        node = self.head
        while node.next:
            node = node.next
        return node

    def remove_first(self) -> Any:
        if self.head:
            data = self.head.data
            self.head = self.head.next
            self._length -= 1
            return data
        return None

    def pop(self) -> Any:
        if not self.head:
            return None

        if self.length == 1:
            data = self.head.data
            self._length -= 1
            self.head = None
            return data

        node = self.head
        previous = node
        while node.next:
            previous = node
            node = node.next
        previous.next = None
        self._length -= 1
        return node.data

    def remove(self, data: Any) -> Any:
        if not self.head:
            raise ValueError("Value not found")

        if self.head.data == data:
            data = self.head.data
            self.head = self.head.next
            self._length -= 1
            return data

        node = self.head
        previous = node
        while node.next:
            if node.data == data:
                break
            previous = node
            node = node.next

        if node.data != data:
            raise ValueError("Value not found")

        previous.next = node.next
        self._length -= 1
        return node.data

    def contains(self, data: Any) -> bool:
        if not self.head:
            return False
        node = self.head
        while node.next:
            if node.data == data:
                return True
            node = node.next
        return node.data == data

    def peek(self) -> Any:
        return self.head.data if self.head else None

    def peek_last(self) -> Any:
        last = self.get_last()
        return last.data if last else None
