from typing import Optional, Any


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue():
    def __init__(self):
        self.head = None
        self.size = 0

    def enqueue(self, data: Any):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
            self.size += 1
            return

        while current.next:
            current = current.next
        current.next = node
        self.size += 1

    def dequeue(self) -> Optional[Any]:
        node = self.head
        if node:
            next_node = node.next
            self.head = next_node
            self.size -= 1
            return node.data
        return None
