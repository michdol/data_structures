

class Queue(object):
    def __init__(self):
        print('asd')
        self.items = []

    def is_empty(self):
        try:
            self.items[0]
            return False
        except IndexError:
            return True

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def hot_potato(num):
    names = [1, 2, 3, 4, 5, 6]
    q = Queue()
    for i in names:
        q.enqueue(i)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())

        ret = q.dequeue()
        print("{} goes out".format(ret))

    print(q.dequeue())

