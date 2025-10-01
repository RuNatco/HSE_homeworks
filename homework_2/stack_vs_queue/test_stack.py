import unittest
from .stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(42)
        self.assertFalse(self.stack.is_empty())

    def test_push(self):
        self.stack.push(42)
        self.assertEqual(self.stack.peek(), 42)
        self.stack.push(666)
        self.assertEqual(self.stack.peek(), 666)

    def test_pop(self):
        self.stack.push(42)
        self.stack.push(666)
        self.assertEqual(self.stack.pop(), 666)
        self.assertEqual(self.stack.pop(), 42)
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek(self):
        self.stack.push(42)
        self.assertEqual(self.stack.peek(), 42)
        self.stack.push(666)
        self.assertEqual(self.stack.peek(), 666)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 42)
        self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.peek()

if __name__ == '__main__':
    unittest.main()
