import unittest
from k_th import kth_largest


class TestKthLargest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_edges(self):
        self.assertEqual(kth_largest([1], 1), 1)
        self.assertEqual(kth_largest([2, 1], 1), 2)
        self.assertEqual(kth_largest([2, 1], 2), 1)
        self.assertEqual(kth_largest([-1, -2, -3, 0], 1), 0)
        self.assertEqual(kth_largest([-1, -2, -3, 0], 4), -3)

    def test_with_duplicates(self):
        nums = [5, 3, 5, 2, 5, 1]
        self.assertEqual(kth_largest(nums.copy(), 1), 5)
        self.assertEqual(kth_largest(nums.copy(), 2), 5)
        self.assertEqual(kth_largest(nums.copy(), 3), 5)
        self.assertEqual(kth_largest(nums.copy(), 4), 3)

    def test_invalid_k(self):
        with self.assertRaises(ValueError):
            kth_largest([1, 2, 3], 0)
        with self.assertRaises(ValueError):
            kth_largest([1, 2, 3], 4)


if __name__ == '__main__':
    unittest.main()
