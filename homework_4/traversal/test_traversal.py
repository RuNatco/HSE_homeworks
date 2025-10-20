import unittest
from .traversal import BST

class TestBST(unittest.TestCase):
	def setUp(self):
		self.bst = BST()
		for value in [10, 5, 15, 3, 7, 13, 17]:
			self.bst.insert(value)

	def test_pre_order(self):
		result = self.bst.pre_order(self.bst.root)
		expected = [10, 5, 3, 7, 15, 13, 17]
		self.assertEqual(result, expected)

	def test_in_order(self):
		result = self.bst.in_order(self.bst.root)
		expected = [3, 5, 7, 10, 13, 15, 17]
		self.assertEqual(result, expected)

	def test_post_order(self):
		result = self.bst.post_order(self.bst.root)
		expected = [3, 7, 5, 13, 17, 15, 10]
		self.assertEqual(result, expected)

	def test_reverse_pre_order(self):
		result = self.bst.reverse_pre_order(self.bst.root)
		expected = [10, 15, 17, 13, 5, 7, 3]
		self.assertEqual(result, expected)

	def test_reverse_in_order(self):
		result = self.bst.reverse_in_order(self.bst.root)
		expected = [17, 15, 13, 10, 7, 5, 3]
		self.assertEqual(result, expected)

	def test_reverse_post_order(self):
		result = self.bst.reverse_post_order(self.bst.root)
		expected = [17, 13, 15, 7, 3, 5, 10]
		self.assertEqual(result, expected)
