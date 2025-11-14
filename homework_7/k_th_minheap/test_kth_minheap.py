import unittest
from kth_minheap import kth_largest_custom_heap, kth_largest_heapq


class TestKthLargestMinHeap(unittest.TestCase):
    def test_examples(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(kth_largest_custom_heap(nums.copy(), 2), 5)
        self.assertEqual(kth_largest_heapq(nums.copy(), 2), 5)

        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        self.assertEqual(kth_largest_custom_heap(nums.copy(), 4), 4)
        self.assertEqual(kth_largest_heapq(nums.copy(), 4), 4)

    def test_edges(self):
        self.assertEqual(kth_largest_custom_heap([1], 1), 1)
        self.assertEqual(kth_largest_heapq([1], 1), 1)
        self.assertEqual(kth_largest_custom_heap([2, 1], 1), 2)
        self.assertEqual(kth_largest_heapq([2, 1], 1), 2)

    def test_invalid_k(self):
        with self.assertRaises(ValueError):
            kth_largest_custom_heap([1, 2, 3], 0)
        with self.assertRaises(ValueError):
            kth_largest_heapq([1, 2, 3], 0)
        with self.assertRaises(ValueError):
            kth_largest_custom_heap([1, 2, 3], 4)
        with self.assertRaises(ValueError):
            kth_largest_heapq([1, 2, 3], 4)


if __name__ == '__main__':
    unittest.main()
