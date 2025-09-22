import unittest
from sum_divisible_by_2 import max_sum_divisible_by_2

class TestMaxSumDivisibleBy2(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_sum_divisible_by_2([5, 7, 13, 2, 14]), 36)
        self.assertEqual(max_sum_divisible_by_2([3]), 0)

    def test_all_even(self):
        self.assertEqual(max_sum_divisible_by_2([2, 4, 6]), 12)

    def test_all_odd(self):
        self.assertEqual(max_sum_divisible_by_2([1, 3, 5]), 8)

    def test_mixed(self):
        self.assertEqual(max_sum_divisible_by_2([1, 2, 3, 4, 5]), 14)

    def test_non_positive_integers(self):
        with self.assertRaises(ValueError):
            max_sum_divisible_by_2([-1, 2, 3])
        with self.assertRaises(ValueError):
            max_sum_divisible_by_2([1.5, 2, 3])
        with self.assertRaises(ValueError):
            max_sum_divisible_by_2(['a', 2, 3])

    def test_zero_included(self):
        self.assertEqual(max_sum_divisible_by_2([0, 2, 4]), 6)
        self.assertEqual(max_sum_divisible_by_2([0, 1, 3]), 4)

if __name__ == '__main__':
    unittest.main()
