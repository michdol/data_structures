

class StackNode(object):
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, item):
        self.__next = item


class StackLL(object):
    """
    Linked list style Stack data structure.
    """

    def __init__(self):
        self.__top = None

    @property
    def is_empty(self):
        return self.__top is None

    @property
    def size(self):
        count = 0
        next_ = self.__top

        while next_:
            count += 1
            next_ = self.next
        return count

    @property
    def top(self):
        return self.__top

    @property
    def peek(self):
        return self.__top.data

    def push(self, data):
        if self.__top is None:
            self.__top = StackNode(data)
            return

        new_node = StackNode(data)
        new_node.next = self.__top
        self.__top = new_node

    def pop(self):
        data = self.__top.data
        next_ = self.__top.next
        self.__top = next_
        return data

    def reverse(self):
        current = self.__top
        previous = None

        while current:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_

        self.__top.next = None
        self.__top = previous


class Stack(object):
    def __init__(self):
        self.__items = []
        self.__size = 0

    def push(self, value):
        self.__items.append(value)
        self.__size += 1

    def pop(self):
        try:
            value = self.__items.pop()
        except IndexError:
            return None
        self.__size -= 1
        return value

    @property
    def peek(self):
        try:
            return self.__items[-1]
        except IndexError:
            return None

    @property
    def size(self):
        return self.__size

    @property
    def is_empty(self):
        return self.__size == 0

    def reverse(self):
        if not self.is_empty:
            tmp = self.pop()
            self.reverse()
            self._insert_at_bottom(tmp)

    def _insert_at_bottom(self, item):
        if self.is_empty:
            self.push(item)
        else:
            tmp = self.pop()
            self._insert_at_bottom(item)
            self.push(tmp)

    def sort(self):
        if not self.is_empty:
            tmp = self.pop()
            self.sort()
            self.sorted_insert(tmp)

    def sorted_insert(self, item):
        if self.is_empty or item > self.peek:
            self.push(item)
            return

        tmp = self.pop()
        self.sorted_insert(item)
        self.push(tmp)


def convert_decimal_to_binary(number):
    assert type(number) == int
    if len(str(number)) == 1:
        return number % 2
    s = Stack()

    while number:
        remainder = number % 2
        s.push(remainder)
        number = number // 2

    binary_numbers = []
    while not s.is_empty:
        binary_numbers.append(str(s.pop()))

    return int(''.join(binary_numbers))

