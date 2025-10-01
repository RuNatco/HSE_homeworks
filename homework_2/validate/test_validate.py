import unittest
from .validate import validate_stack_sequences

class TestValidateStackSequences(unittest.TestCase):
    def test_example_1(self):
        pushed = [1, 2, 3, 4, 5]
        popped = [1, 3, 5, 4, 2]
        self.assertTrue(validate_stack_sequences(pushed, popped))

    def test_example_2(self):
        pushed = [1, 2, 3]
        popped = [3, 1, 2]
        self.assertFalse(validate_stack_sequences(pushed, popped))

    def test_empty(self):
        pushed = []
        popped = []
        self.assertTrue(validate_stack_sequences(pushed, popped))

    def test_single_element(self):
        pushed = [42]
        popped = [42]
        self.assertTrue(validate_stack_sequences(pushed, popped))
    

if __name__ == '__main__':
    unittest.main()
