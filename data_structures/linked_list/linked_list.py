from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next: Optional["Node"] = None):
        self.data: Any = data
        self.next: Node | None = next


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.length: int = 0

    def prepend(self, data: Any):
        node = Node(data=data)
        if self.head:
            node.next = self.head
        self.head = node
        self.length += 1

    def append(self, data: Any):
        node = Node(data=data)
        last = self.get_last()
        if last:
            last.next = node
        else:
            self.head = node
        self.length += 1

    def get_last(self) -> Node | None:
        node = self.head
        previous = None
        while node:
            previous = node
            node = node.next
        return previous

    def remove_first(self) -> Any:
        if self.head:
            data = self.head.data
            self.head = self.head.next
            self.length -= 1
            return data
        return None

    def pop(self) -> Any:
        if not self.head:
            return None

        if self.length == 1:
            data = self.head.data
            self.length -= 1
            self.head = None
            return data

        node = self.head
        previous = node
        while node.next:
            previous = node
            node = node.next
        previous.next = None
        self.length -= 1
        return node.data

    def remove_all(self, data: Any) -> Any:
        return None

    def remove(self, data: Any) -> Any:
        if not self.head:
            raise ValueError("Value not found")

        if self.head.data == data:
            data = self.head.data
            self.head = self.head.next
            self.length -= 1
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
        self.length -= 1
        return node.data
