import unittest
from prime_count import count_primes

class TestCountPrimes(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(count_primes(10), 4)
        self.assertEqual(count_primes(1), 0)

    def test_small_numbers(self):
        self.assertEqual(count_primes(0), 0)
        self.assertEqual(count_primes(2), 0)
        self.assertEqual(count_primes(3), 1)

    def test_larger_numbers(self):
        self.assertEqual(count_primes(20), 8)
        self.assertEqual(count_primes(100), 25)

if __name__ == '__main__':
    unittest.main()
