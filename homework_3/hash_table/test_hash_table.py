import unittest
from .hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def test_insert(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        self.assertEqual(hash_table.table[hash_table.polynomial_hash("key1")], [("key1", "value1")])

    def test_search(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        self.assertEqual(hash_table.search("key1"), "value1")

    def test_delete(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        hash_table.delete("key1")
        self.assertEqual(hash_table.search("key1"), None)

    def test_resize(self):
        hash_table = HashTable(size=3)
        keys = [f"key{i}" for i in range(10)]
        for key in keys:
            hash_table.insert(key, f"value{key}")
        self.assertTrue(hash_table.size > 3)

        for key in keys:
            self.assertEqual(hash_table.search(key), f"value{key}")