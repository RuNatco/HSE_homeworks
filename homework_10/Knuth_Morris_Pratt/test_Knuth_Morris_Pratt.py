import unittest
from Knuth_Morris_Pratt import kmp_search


class TestKMP(unittest.TestCase):
    def test_found(self):
        self.assertEqual(kmp_search("ababcabcab", "abcab"), 2)

    def test_not_found(self):
        self.assertEqual(kmp_search("hello world", "42"), -1)

    def test_empty_pattern(self):
        self.assertEqual(kmp_search("hello", ""), -1)

    def test_empty_text(self):
        self.assertEqual(kmp_search("", "a"), -1)

    def test_pattern_longer_than_text(self):
        self.assertEqual(kmp_search("hi", "hello"), -1)

    def test_overlapping(self):
        self.assertEqual(kmp_search("aaaaa", "aaa"), 0)


if __name__ == "__main__":
    unittest.main()

