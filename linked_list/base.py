from operator import add, sub

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class BaseLinkedList(object):
    def __init__(self):
        self.head = None

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

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

    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            del current
            return

        previous = None
        while current:
            if current.data == key:
                break
            previous = current
            current = current.next

        if not current:
            raise ValueError("Key not found")

        next_ = current.next
        previous.next = next_
        del current

    def delete_node(self, index):
        previous = None
        current = self.head
        current_index = 0
        while current:
            if current_index == index:
                break
            previous = current
            current = current.next
            current_index += 1

        if not current:
            raise IndexError("Index out of range")

        if current is self.head:
            self.head = current.next
        if previous:
            previous.next = current.next
        del current

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def reverse(self):
        # Empty or single element list
        if not self.head or not self.head.next:
            return
        previous = self.head
        self.tail = previous
        current = previous.next
        next_ = current.next
        previous.next = None
        previous.previous = current
        while current.next:
            current.next = previous
            current.previous = next_
            previous = current
            current = next_
            next_ = current.next
        current.next = previous
        current.previous = next_
        self.head = current

    def index(self, key):
        current = self.head
        current_index = 0
        while current:
            if current.data == key:
                return current_index
            current = current.next
            current_index += 1
        raise ValueError("{} is not in the list".format(key))

    def insert(self, position, key):
        if not self.head:
            self.head = Node(key)
            return

        current = self.head
        current_index = 0

        previous = None
        while current and current_index != position:
            previous = current
            current = current.next
            current_index += 1

        new_node = Node(key)
        if previous:
            previous.next = new_node
        new_node.next = current
        if current is self.head:
            self.head = new_node

    def swap(self, left, right):
        if left == right:
            return

        prevL = None
        currentL = self.head
        while currentL and currentL.data != left:
            prevL = currentL
            currentL = currentL.next

        prevR = None
        currentR = self.head
        while currentR and currentR.data != right:
            prevR = currentR
            currentR = currentR.next

        if not currentL or not currentR:
            return
        
        if prevL:
            prevL.next = currentR
        # Left element is head
        else:
            self.head = currentR

        if prevR:
            prevR.next = currentL
        # Right element is head
        else:
            self.head = currentL

        tmp = currentL.next
        currentL.next = currentR.next
        currentR.next = tmp
