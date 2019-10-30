from unittest import main, TestCase

from linked_list import LinkedList, Node


class LinkedListTest(TestCase):
    def _create_ll(self):
        l = LinkedList()
        for i in range(1, 6):
            l.push(i)
        return l

    def test_size(self):
        l = self._create_ll()
        self.assertEqual(l.size, 5)
        self.assertEqual(len(l), 5)

    def test_push(self):
        l = LinkedList()
        self.assertIsNone(l.head)
        l.push(1)
        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.tail.data, 1)
        self.assertIsNone(l.head.next)
        self.assertIsNone(l.head.previous)
        self.assertEqual(l.size, 1)

        l.push(2)
        self.assertEqual(l.head.data, 2)
        self.assertEqual(l.tail.data, 1)
        self.assertEqual(l.head.next, l.tail)
        self.assertEqual(l.tail.previous, l.head)
        self.assertIsNone(l.head.previous)
        self.assertEqual(l.head.next.data, 1)
        self.assertEqual(l.head.next.previous.data, 2)
        self.assertIsNone(l.head.next.next)
        self.assertEqual(l.size, 2)

        """
        1   - tail
        2
        3   - head

        head.next.data = 2
        tail.previous.data = 2
        - head.next == tail.previous
        """
        l.push(3)
        self.assertEqual(l.head.data, 3)
        self.assertEqual(l.tail.data, 1)
        self.assertEqual(l.tail.previous, l.head.next)
        self.assertIsNone(l.head.previous)
        self.assertEqual(l.head.next.data, 2)
        self.assertEqual(l.head.next.next.data, 1)
        self.assertEqual(l.head.next.previous.data, 3)
        self.assertIsNone(l.head.next.next.next)
        self.assertEqual(l.head.next.next.previous.data, 2)
        self.assertEqual(l.size, 3)

    def test_delete(self):
        l = LinkedList()
        l.push(4)
        l.push(3)
        l.push(2)
        l.push(1)

        l.delete(2)

        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next.data, 3)
        self.assertEqual(l.head.next.previous.data, 1)

    def test_delete_head(self):
        l = LinkedList()
        l.push(3)
        l.push(2)
        l.push(1)
        self.assertEqual(l.head.data, 1)

        l.delete(1)

        self.assertEqual(l.head.data, 2)
        self.assertEqual(l.head.next.data, 3)
        self.assertIsNone(l.head.previous)

    def test_delete_key_not_present(self):
        l = LinkedList()
        l.push(1)
        l.push(2)
        l.push(3)

        with self.assertRaises(ValueError):
            l.delete(4)

        l = LinkedList()
        with self.assertRaises(ValueError):
            l.delete(1)

    def test_delete_from_single_item_list(self):
        l = LinkedList()
        l.push(1)

        l.delete(1)

        self.assertEqual(l.size, 0)
        self.assertIsNone(l.head)

    def test_delete_tail(self):
        l = LinkedList()
        l.push(3)
        l.push(2)
        l.push(1)

        l.delete(3)

        self.assertEqual(l.head.data, 1)
        self.assertIsNone(l.head.next.next)
        self.assertIs(l.tail, l.head.next)

    def test_delete_node(self):
        l = LinkedList()
        l.push(2)
        l.push(1)

        l.delete_node(0)

        self.assertEqual(l.size, 1)
        self.assertEqual(l.head.data, 2)
        self.assertIsNone(l.head.previous)

    def test_delete_node_empty_list(self):
        l = LinkedList()

        with self.assertRaises(IndexError):
            l.delete_node(0)

    def test_delete_node_single_item_list(self):
        l = LinkedList()
        l.push(1)

        l.delete_node(0)

        self.assertEqual(l.size, 0)
        self.assertIsNone(l.head)

    def test_delete_node_middle_item(self):
        l = LinkedList()
        l.push(4)
        l.push(3)
        l.push(2)
        l.push(1)

        l.delete_node(1)

        self.assertEqual(l.size, 3)
        self.assertEqual(l.head.next.data, 3)
        self.assertEqual(l.head.next.previous.data, 1)

    def test_delete_node_last_item(self):
        l = LinkedList()
        l.push(3)
        l.push(2)
        l.push(1)

        l.delete_node(2)

        self.assertEqual(l.size, 2)
        self.assertEqual(l.head.next.data, 2)
        self.assertIsNone(l.head.next.next)

    def test_item_in_list(self):
        l = LinkedList()

        self.assertFalse(1 in l)

        l.push(1)

        self.assertFalse(2 in l)
        self.assertTrue(1 in l)

    def test_get_by_index(self):
        l = LinkedList()
        l.push(1)

        ret = l[0]
        self.assertEqual(ret, 1)

    def test_get_by_index_empty_list(self):
        l = LinkedList()

        with self.assertRaises(IndexError):
            l[0]
        l.push(1)
        with self.assertRaises(IndexError):
            l[1]

    def test_get_by_index_more_tests(self):
        l = LinkedList()
        l.push(4)
        l.push(3)
        l.push(2)
        l.push(1)

        self.assertEqual(l[3], 4)
        self.assertEqual(l[2], 3)
        self.assertEqual(l[1], 2)
        self.assertEqual(l[0], 1)

    def test_get_by_negative_index(self):
        l = LinkedList()
        l.push(1)

        self.assertEqual(l[-1], 1)

    def test_get_by_index_key_type_error(self):
        l = LinkedList()
        l.push(1)

        with self.assertRaises(TypeError):
            l['0']

    def test_iter(self):
        l = self._create_ll()

        expected = 5
        for node in l:
            self.assertEqual(node.data, expected)
            expected -= 1
        self.assertEqual(expected, 0)

    def test_reverse(self):
        l = LinkedList()
        l.push(1)
        l.push(2)
        l.push(3)

        l.reverse()

        print()
        for i in l:
            print(i.data)
        print()
        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 2)
        self.assertEqual(l[2], 3)


if __name__ == '__main__':
    main()
