import unittest
from homework_5.tracer.tracer import trace_recursive
from .permutations import permute


class TestPermutations(unittest.TestCase):

    @trace_recursive
    def permute_decorated(self, nums):
        return permute(nums)

    def test_permute(self):
        result = self.permute_decorated([1, 2, 3])
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(result, expected)

        result = self.permute_decorated([0, 1])
        expected = [[0, 1], [1, 0]]
        self.assertEqual(result, expected)

        result = self.permute_decorated([1])
        expected = [[1]]
        self.assertEqual(result, expected)

        result = self.permute_decorated([])
        expected = [[]]
        self.assertEqual(result, expected)

        result = self.permute_decorated([1, 1, 2])
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
