from unittest import main, TestCase

from linked_list import LinkedList, Node
from ordered_linked_list import OrderedLinkedList
from base import BaseLinkedList


class BaseLinkedListTest(TestCase):
    def _create_ll(self):
        l = BaseLinkedList()
        for i in range(1, 6):
            l.push(i)
        return l

    def test_len(self):
        l = self._create_ll()
        self.assertEqual(len(l), 5)

    def test_push(self):
        l = BaseLinkedList()
        self.assertIsNone(l.head)
        l.push(1)
        self.assertEqual(l.head.data, 1)
        self.assertIsNone(l.head.next)
        self.assertEqual(len(l), 1)

        l.push(2)
        self.assertEqual(l.head.data, 2)
        self.assertEqual(l.head.next.data, 1)
        self.assertIsNone(l.head.next.next)
        self.assertEqual(len(l), 2)

        l.push(3)
        self.assertEqual(l.head.data, 3)
        self.assertEqual(l.head.next.data, 2)
        self.assertEqual(l.head.next.next.data, 1)
        self.assertIsNone(l.head.next.next.next)
        self.assertEqual(len(l), 3)

    def test_delete(self):
        l = BaseLinkedList()
        l.push(4)
        l.push(3)
        l.push(2)
        l.push(1)

        l.delete(2)

        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next.data, 3)

    def test_delete_head(self):
        l = BaseLinkedList()
        l.push(3)
        l.push(2)
        l.push(1)
        self.assertEqual(l.head.data, 1)

        l.delete(1)

        self.assertEqual(l.head.data, 2)
        self.assertEqual(l.head.next.data, 3)

    def test_delete_key_not_present(self):
        l = BaseLinkedList()
        l.push(1)
        l.push(2)
        l.push(3)

        with self.assertRaises(ValueError):
            l.delete(4)

        l = BaseLinkedList()
        with self.assertRaises(ValueError):
            l.delete(1)

    def test_delete_from_single_item_list(self):
        l = BaseLinkedList()
        l.push(1)

        l.delete(1)

        self.assertEqual(len(l), 0)
        self.assertIsNone(l.head)

    def test_delete_tail(self):
        l = BaseLinkedList()
        l.push(3)
        l.push(2)
        l.push(1)

        l.delete(3)

        self.assertEqual(l.head.data, 1)
        self.assertIsNone(l.head.next.next)

    def test_delete_node(self):
        l = BaseLinkedList()
        l.push(2)
        l.push(1)

        l.delete_node(0)

        self.assertEqual(len(l), 1)
        self.assertEqual(l.head.data, 2)

    def test_delete_node_empty_list(self):
        l = BaseLinkedList()

        with self.assertRaises(IndexError):
            l.delete_node(0)

    def test_delete_node_single_item_list(self):
        l = BaseLinkedList()
        l.push(1)

        l.delete_node(0)

        self.assertEqual(len(l), 0)
        self.assertIsNone(l.head)

    def test_delete_node_middle_item(self):
        l = BaseLinkedList()
        l.push(4)
        l.push(3)
        l.push(2)
        l.push(1)

        l.delete_node(1)

        self.assertEqual(len(l), 3)
        self.assertEqual(l.head.next.data, 3)

    def test_delete_node_last_item(self):
        l = BaseLinkedList()
        l.push(3)
        l.push(2)
        l.push(1)

        l.delete_node(2)

        self.assertEqual(len(l), 2)
        self.assertEqual(l.head.next.data, 2)
        self.assertIsNone(l.head.next.next)

    def test_item_in_list(self):
        l = BaseLinkedList()

        self.assertFalse(1 in l)

        l.push(1)

        self.assertFalse(2 in l)
        self.assertTrue(1 in l)

    def test_get_by_index(self):
        l = BaseLinkedList()
        l.push(1)

        ret = l[0]
        self.assertEqual(ret, 1)

    def test_get_by_index_empty_list(self):
        l = BaseLinkedList()

        with self.assertRaises(IndexError):
            l[0]
        l.push(1)
        with self.assertRaises(IndexError):
            l[1]

    def test_get_by_index_more_tests(self):
        l = BaseLinkedList()
        l.push(4)
        l.push(3)
        l.push(2)
        l.push(1)

        self.assertEqual(l[3], 4)
        self.assertEqual(l[2], 3)
        self.assertEqual(l[1], 2)
        self.assertEqual(l[0], 1)

    def test_get_by_negative_index(self):
        l = BaseLinkedList()
        l.push(1)

        self.assertEqual(l[-1], 1)

    def test_get_by_index_key_type_error(self):
        l = BaseLinkedList()
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
        l = BaseLinkedList()
        l.push(1)
        l.push(2)
        l.push(3)
        l.push(4)
        l.push(5)

        l.reverse()

        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 2)
        self.assertEqual(l[2], 3)
        self.assertEqual(l[3], 4)
        self.assertEqual(l[4], 5)

        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next.data, 2)

    def test_reverse_empty_list(self):
        l = BaseLinkedList()
        l.reverse()

    def test_reverse_one_element_list(self):
        l = BaseLinkedList()
        l.push(1)

        l.reverse()

        self.assertEqual(l.head.data, 1)

    def test_reverse_two_elements_list(self):
        l = BaseLinkedList()
        l.push(1)
        l.push(2)

        l.reverse()

        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 2)
        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next.data, 2)

    def test_index(self):
        l = BaseLinkedList()
        l.push(1)
        l.push(2)
        l.push(3)
        l.push(4)

        self.assertEqual(l.index(1), 3)
        self.assertEqual(l.index(2), 2)
        self.assertEqual(l.index(3), 1)
        self.assertEqual(l.index(4), 0)

    def test_index_key_not_in_the_list(self):
        l = BaseLinkedList()
        with self.assertRaises(ValueError):
            l.index(1)

        l.push(1)
        with self.assertRaises(ValueError):
            l.index(2)

    def test_insert(self):
        l = BaseLinkedList()
        l.push(1)

        l.insert(0, 2)
        self.assertEqual(l.head.data, 2)
        self.assertEqual(l.head.next.data, 1)

    def test_insert_empty_list(self):
        l = BaseLinkedList()
        
        l.insert(5, 1)

        self.assertEqual(l.head.data, 1)

    def test_insert_in_the_middle(self):
        l = BaseLinkedList()
        l.push(3)
        l.push(1)

        l.insert(1, 2)

        self.assertEqual(l.head.next.data, 2)
        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 2)
        self.assertEqual(l[2], 3)

    def test_swap_adjacent_head_and_tail(self):
        l = BaseLinkedList()
        l.push(1)
        l.push(2)

        l.swap(2, 1)

        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next.data, 2)
        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 2)

    def test_swap_second_and_fourth_out_of_five(self):
        l = BaseLinkedList()
        l.push(5)
        l.push(4)
        l.push(3)
        l.push(2)
        l.push(1)

        l.swap(2, 4)

        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 4)
        self.assertEqual(l[2], 3)
        self.assertEqual(l[3], 2)
        self.assertEqual(l[4], 5)


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
        l.push(4)
        l.push(5)

        l.reverse()

        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 2)
        self.assertEqual(l[2], 3)
        self.assertEqual(l[3], 4)
        self.assertEqual(l[4], 5)

        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next.data, 2)
        self.assertEqual(l.tail.data, 5)

        self.assertEqual(l.head.next.previous.data, 1)
        self.assertEqual(l.tail.previous.next.data, 5)
        self.assertEqual(l.tail.previous.data, 4)

    def test_reverse_empty_list(self):
        l = LinkedList()
        l.reverse()

    def test_reverse_one_element_list(self):
        l = LinkedList()
        l.push(1)

        l.reverse()

        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.tail.data, 1)

    def test_reverse_two_elements_list(self):
        l = LinkedList()
        l.push(1)
        l.push(2)

        l.reverse()

        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 2)
        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next.data, 2)
        self.assertEqual(l.tail.previous, l.head)

        self.assertEqual(l.head.next, l.tail)

    def test_index(self):
        l = LinkedList()
        l.push(1)
        l.push(2)
        l.push(3)
        l.push(4)

        self.assertEqual(l.index(1), 3)
        self.assertEqual(l.index(2), 2)
        self.assertEqual(l.index(3), 1)
        self.assertEqual(l.index(4), 0)

    def test_index_key_not_in_the_list(self):
        l = LinkedList()
        with self.assertRaises(ValueError):
            l.index(1)

        l.push(1)
        with self.assertRaises(ValueError):
            l.index(2)

    def test_insert(self):
        l = LinkedList()
        l.push(1)

        l.insert(0, 2)
        self.assertEqual(l.head.data, 2)
        self.assertEqual(l.head.next.data, 1)
        self.assertEqual(l.tail.data, 1)
        self.assertIs(l.head.next, l.tail)

    def test_insert_empty_list(self):
        l = LinkedList()
        
        l.insert(5, 1)

        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.tail.data, 1)
        self.assertIs(l.head, l.tail)

    def test_insert_in_the_middle(self):
        l = LinkedList()
        l.push(3)
        l.push(1)

        l.insert(1, 2)

        self.assertEqual(l.head.next.data, 2)
        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 2)
        self.assertEqual(l[2], 3)

        self.assertEqual(l.tail.previous.data, 2)
        self.assertIs(l.head.next.next, l.tail)

    def test_swap_adjacent_head_and_tail(self):
        l = LinkedList()
        l.push(1)
        l.push(2)

        l.swap(2, 1)

        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next.data, 2)
        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 2)

    def test_swap_second_and_fourth_out_of_five(self):
        l = LinkedList()
        l.push(5)
        l.push(4)
        l.push(3)
        l.push(2)
        l.push(1)

        l.swap(2, 4)

        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 4)
        self.assertEqual(l[2], 3)
        self.assertEqual(l[3], 2)
        self.assertEqual(l[4], 5)


class OrderedLinkedListTest(TestCase):

    def test_add(self):
        l = OrderedLinkedList()
        l.add(1)

        self.assertEqual(l.head.data, 1)
        self.assertEqual(l[0], 1)

        l.add(1)   

        self.assertEqual(len(l), 1)
        self.assertEqual(l[0], 1)

        l.add(2)

        self.assertEqual(len(l), 2)
        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 2)


if __name__ == '__main__':
    main()
