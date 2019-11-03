from operator import add, sub
from base import Node, BaseLinkedList


class OrderedLinkedList(BaseLinkedList):

    def add(self, item):
        if not self.head:
            self.head = Node(item)
            return

        previous = self.head
        current = previous.next
        while current:
            if previous.data < item < current.data:
                break
            previous = current
            current = current.next

        new_node = Node(item)
        if not current:
            previous.next = new_node

        previous.next = new_node
        new_node.next = current
