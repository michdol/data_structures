from operator import add, sub

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    @property
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __len__(self):
        return self.size

    def __contains__(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Index should be integer")
        # Allow indexing from the end.
        if key >= 0:
            operator_ = add
            current_index = 0
        else:
            operator_ = sub
            current_index = -1
        current = self.head
        while current:
            if current_index == key:
                break
            current = current.next
            current_index = operator_(current_index, 1)
        try:
            return current.data
        # Run out of nodes
        except AttributeError:
            raise IndexError("Index out of range")

    def push(self, item):
        new_node = Node(data=item)
        new_node.next = self.head
        self.head = new_node
        if new_node.next:
            new_node.next.previous = new_node
        if self.tail is None:
            self.tail = new_node

    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            if self.head:
                self.head.previous = None
            del current
            return

        while current:
            if current.data == key:
                break
            current = current.next

        if not current:
            raise ValueError("Key not found")

        previous = current.previous
        next_ = current.next
        if previous:
            previous.next = next_
            if current is self.tail:
                self.tail = previous
        if next_:
            next_.previous = previous
        del current

    def delete_node(self, index):
        current = self.head
        current_index = 0

        if current and current_index == index:
            self.head = current.next
            if self.head:
                self.head.previous = None
            return

        while current:
            if current_index == index:
                break
            current = current.next
            current_index += 1

        if not current:
            raise IndexError("Index out of range")

        previous = current.previous
        next_ = current.next
        if previous:
            previous.next = next_
        if next_:
            next_.previous = previous
        del current

    def __iter__(self):
        return self._generator()

    def _generator(self):
        current = self.head
        while current:
            yield current
            current = current.next
