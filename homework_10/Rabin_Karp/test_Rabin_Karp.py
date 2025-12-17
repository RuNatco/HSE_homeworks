import unittest
from Rabin_Karp import rabin_karp

class TestRabinKarp(unittest.TestCase):

    def test_found(self):
        self.assertEqual(rabin_karp("hello world", "world"), 6)

    def test_not_found(self):
        self.assertEqual(rabin_karp("hello world", "42"), -1)

    def test_empty_pattern(self):
        self.assertEqual(rabin_karp("hello world", ""), -1)

    def test_empty_text(self):
        self.assertEqual(rabin_karp("", "world"), -1)

    def test_both_empty(self):
        self.assertEqual(rabin_karp("", ""), -1)

if __name__ == "__main__":
    unittest.main()

