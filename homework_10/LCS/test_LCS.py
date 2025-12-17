import unittest
from LCS import lcs


class TestLCS(unittest.TestCase):
    def test_example(self):
        self.assertEqual(lcs("AGGTAB", "GXTXAYB"), "GTAB")

    def test_no_common(self):
        self.assertEqual(lcs("abc", "xyz"), "")

    def test_full_match(self):
        self.assertEqual(lcs("hello", "hello"), "hello")

    def test_empty_strings(self):
        self.assertEqual(lcs("", "abc"), "")
        self.assertEqual(lcs("abc", ""), "")

    def test_repeated_chars(self):
        self.assertEqual(lcs("aaaa", "aa"), "aa")

    def test_order_matters(self):
        self.assertIn(lcs("abcd", "bdac"), {"bd", "ac"})


if __name__ == "__main__":
    unittest.main()

