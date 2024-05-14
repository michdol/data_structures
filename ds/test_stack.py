from unittest import TestCase, main

from stack import Stack


class StackTest(TestCase):
    def setUp(self):
        self.s = Stack()

    def test_push_peek(self):
        self.s.push(1)
        self.assertEqual(self.s.peek(), 1)
        self.s.push(2)
        self.assertEqual(self.s.peek(), 2)

    def test_pop(self):
        self.s.push(1)

        self.s.push(1)
        self.s.push(2)
        self.s.push(3)
        self.s.push(4)

        self.assertEqual(self.s.pop(), 4)
        self.assertEqual(self.s.pop(), 3)
        self.assertEqual(self.s.pop(), 2)
        self.assertEqual(self.s.pop(), 1)

    def _is_pallindrome(self, string: str) -> bool:
        reversed_string = ""
        for c in string:
            self.s.push(c)
        c = self.s.pop()
        while c:
            reversed_string += c
            c = self.s.pop()
        return reversed_string == string

    def test_is_pallindrome(self):
        string = "kayak"
        self.assertTrue(self._is_pallindrome(string))

    def test_is_not_pallindrom(self):
        string = "mathematics"
        self.assertFalse(self._is_pallindrome(string))


if __name__ == "__main__":
    main()
