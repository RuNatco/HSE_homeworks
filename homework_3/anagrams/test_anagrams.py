import unittest
from .anagrams import group_anagram

class TestAnagrams(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(group_anagram(["eat","tea","tan","ate","nat","bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]])
        self.assertEqual(group_anagram([""]), [[""]])
        self.assertEqual(group_anagram(["bla"]), [["bla"]])
        self.assertEqual(group_anagram([42, 24]), [[24, 42]])
        self.assertEqual(group_anagram(["лягушка", "гуляшка", "милашка"]), [["милашка"],["гуляшка", "лягушка"]])
 
if __name__ == '__main__':
    unittest.main()
    