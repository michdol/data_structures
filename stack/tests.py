from unittest import main, TestCase

from stack import Stack, StackLL, convert_decimal_to_binary, StackNode


class StackLLTest(TestCase):
    def test__init__(self):
        s = StackLL()
        self.assertIsNone(s.top)
        self.assertEqual(s.size, 0)
        self.assertTrue(s.is_empty)

    def test_push(self):
        s = StackLL()
        s.push(1)
        self.assertIsInstance(s.top, StackNode)
        self.assertEqual(s.top.data, 1)
        self.assertIsNone(s.top.next)
        self.assertFalse(s.is_empty)
        self.assertEqual(s.peek, 1)

        s.push(2)
        self.assertEqual(s.top.data, 2)
        self.assertIsInstance(s.top.next, StackNode)
        self.assertEqual(s.top.next.data, 1)

    def test_pop(self):
        s = StackLL()
        s.push(1)
        s.push(2)

        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.top.data, 1)
        self.assertIsNone(s.top.next)

        self.assertEqual(s.pop(), 1)
        self.assertIsNone(s.top)
        self.assertTrue(s.is_empty)

    def test_reverse(self):
        s = StackLL()
        s.push(1)
        s.push(2)
        s.push(3)

        s.reverse()

        self.assertEqual(s.top.data, 1)
        self.assertEqual(s.top.next.data, 2)
        self.assertEqual(s.top.next.next.data, 3)
        self.assertIsNone(s.top.next.next.next)


class StackTest(TestCase):
    def test___init__(self):
        s = Stack()
        self.assertIsNone(s.pop())
        self.assertIsNone(s.peek)
        self.assertEqual(s.size, 0)
        self.assertTrue(s.is_empty)

    def test_push_pop(self):
        s = Stack()

        s.push(1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.peek, 1)
        self.assertEqual(s.size, 1)
        self.assertFalse(s.is_empty)

        s.push(2)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.peek, 2)

        # pop
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.size, 1)

        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.size, 0)
        self.assertTrue(s.is_empty)

    def test_reverse(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)

        s.reverse()

        self.assertEqual(s.size, 3)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 3)

    def test_sort(self):
        s = Stack()
        s.push(0)
        s.push(4)
        s.push(1)
        s.push(3)
        s.push(2)

        s.sort()

        self.assertEqual(s.size, 5)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.pop(), 0)

    ### Functions ###

    def test_convert_decimal_to_binary_input_not_int(self):
        with self.assertRaises(AssertionError):
            convert_decimal_to_binary('a')

    def test_convert_decimal_to_binary(self):
        decimal = 0
        binary = convert_decimal_to_binary(decimal)
        self.assertEqual(binary, 0)

        decimal = 1
        binary = convert_decimal_to_binary(decimal)
        self.assertEqual(binary, 1)

        decimal = 256
        binary = convert_decimal_to_binary(decimal)
        self.assertEqual(binary, 100000000)

        decimal = 255
        binary = convert_decimal_to_binary(decimal)
        self.assertEqual(binary, 11111111)


if __name__ == '__main__':
    main()
