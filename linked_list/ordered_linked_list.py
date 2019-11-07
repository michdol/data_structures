from operator import add, sub
from base import Node, BaseLinkedList


class OrderedLinkedList(BaseLinkedList):

    def add(self, item):
        if not self.head:
            self.head = Node(item)
            return

        previous = None
        current = self.head
        while current:
            if current.data > item:
                break
            previous = current
            current = current.next

        new_node = Node(item)
        prev = previous.data if previous else None
        cur = current.data if current else None
        if not current:
            self.head = new_node
        else:
            if previous:
                previous.next = new_node
            new_node.next = current
            if current is self.head:
                self.head = new_node

    def search(self, key):
        current = self.head
        current_idx = 0
        while current:
            if key == current.data:
                return current_idx
            current = current.next
            current_idx += 1
        raise ValueError("{} not in the list".format(key))

    def pop(self, index=None):
        if not self.head:
            raise IndexError("Pop from empty list")
        if not self.head.next:
            self.head = None
            return
        previous = self.head
        current = previous.next
        while current.next:
            previous = current
            current = previous.next
        previous.next = None
        data = current.data
        del current
        return data
