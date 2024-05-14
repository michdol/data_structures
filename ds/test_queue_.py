from unittest import TestCase, main

from queue_ import Queue


class QueueTest(TestCase):
    def setUp(self):
        self.q = Queue()
    
    def test_enqueue(self):
        self.q.enqueue(1)
        self.assertEqual(self.q.head.data, 1)
        self.assertEqual(self.q.size, 1)
        self.q.enqueue(2)
        self.assertEqual(self.q.head.next.data, 2)
        self.assertEqual(self.q.head.data, 1)
        self.assertEqual(self.q.size, 2)
        self.q.enqueue(3)
        self.assertEqual(self.q.head.next.next.data, 3)
        self.assertEqual(self.q.size, 3)

    def test_dequeue_single(self):
        self.q.enqueue(1)
        self.assertEqual(self.q.dequeue(), 1)
        self.assertIsNone(self.q.head)
        self.assertEqual(self.q.size, 0)

    def test_dequeue_multiple(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.enqueue(4)

        self.assertEqual(self.q.dequeue(), 1)
        self.assertEqual(self.q.size, 3)
        self.assertEqual(self.q.head.data, 2)

        self.assertEqual(self.q.dequeue(), 2)
        self.assertEqual(self.q.size, 2)
        self.assertEqual(self.q.head.data, 3)

        self.assertEqual(self.q.dequeue(), 3)
        self.assertEqual(self.q.size, 1)
        self.assertEqual(self.q.head.data, 4)

        self.assertEqual(self.q.dequeue(), 4)
        self.assertEqual(self.q.size, 0)
        self.assertIsNone(self.q.head)


if __name__ == "__main__":
    main()
