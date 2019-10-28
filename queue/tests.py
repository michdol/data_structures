from unittest import main, TestCase

from queue import Queue, hot_potato


class QueueTest(TestCase):

    def test_init(self):
        q = Queue()

        self.assertTrue(q.is_empty())
        self.assertEqual(q.size(), 0)

    def test_hot_potato(self):
        hot_potato(5)


if __name__ == '__main__':
    main()
