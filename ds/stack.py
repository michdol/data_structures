from typing import Any, Optional


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value: Any):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def peek(self) -> Optional[Any]:
        return self.top.data if self.top else None

    def pop(self) -> Optional[Any]:
        top = self.top
        if top:
            new_top = top.next if top.next else None
            self.top = new_top
            self.size -= 1
            return top.data
        return None
