import unittest
from .two_sum import two_sum

class TestTwoSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(two_sum([1, 3, 4, 10], 7), (1, 2))
        self.assertEqual(two_sum([5, 5, 1, 4], 10), (0, 1))

    def test_additional_exampless(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(two_sum([3, 2, 4], 6), (1, 2))
        self.assertEqual(two_sum([1, 2, 3, 4, 5], 9), (3, 4))
        self.assertEqual(two_sum([0, -1, 2, -3, 1], -2), (3, 4))
        self.assertEqual(two_sum([10, 20, 10, 40, 50, 60, 70], 50), (2, 3))

    def test_empty_array(self):
        with self.assertRaises(ValueError):
            two_sum([], 5)

    def test_single_element_array(self):
        with self.assertRaises(ValueError):
            two_sum([1], 1)
    def test_no_solution(self):
        self.assertEqual(two_sum([1, 2, 3, 4, 5], 10), None)

if __name__ == '__main__':
    unittest.main()
