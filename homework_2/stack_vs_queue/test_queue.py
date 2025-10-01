import unittest
from .queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(42)
        self.assertFalse(self.queue.is_empty())

    def test_enqueue(self):
        self.queue.enqueue(42)
        self.assertEqual(self.queue.peek(), 42)
        self.queue.enqueue(43)
        self.assertEqual(self.queue.peek(), 42)

    def test_dequeue(self):
        self.queue.enqueue(42)
        self.queue.enqueue(43)
        self.assertEqual(self.queue.dequeue(), 42)
        self.assertEqual(self.queue.dequeue(), 43)
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_peek(self):
        self.queue.enqueue(42)
        self.assertEqual(self.queue.peek(), 42)
        self.queue.enqueue(43)
        self.assertEqual(self.queue.peek(), 42)
        self.queue.dequeue()
        self.assertEqual(self.queue.peek(), 43)
        self.queue.dequeue()
        with self.assertRaises(IndexError):
            self.queue.peek()

if __name__ == '__main__':
    unittest.main()
