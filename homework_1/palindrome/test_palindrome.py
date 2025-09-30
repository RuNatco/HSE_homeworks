import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_positive_palindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(1221))
    
    def test_negative_palindrome(self):
        self.assertFalse(is_palindrome(-121))

    def test_positive_non_palindrome(self):
        self.assertFalse(is_palindrome(31))
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome(10))

    def test_single_digit(self):
        self.assertTrue(is_palindrome(0))
        self.assertTrue(is_palindrome(7))

    

if __name__ == '__main__':
    unittest.main()
