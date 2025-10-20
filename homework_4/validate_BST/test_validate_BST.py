import unittest
from .validate_BST import TreeNode, is_valid_bst

class TestValidateBST(unittest.TestCase):

	def test_valid_bst(self):
		root = TreeNode(2)
		root.left = TreeNode(1)
		root.right = TreeNode(3)
		self.assertTrue(is_valid_bst(root))

	def test_invalid_bst(self):
		root = TreeNode(5)
		root.left = TreeNode(1)
		root.right = TreeNode(4)
		root.right.left = TreeNode(3)
		root.right.right = TreeNode(6)
		self.assertFalse(is_valid_bst(root))

	def test_single_node(self):
		root = TreeNode(1)
		self.assertTrue(is_valid_bst(root))

	def test_left_heavy(self):
		root = TreeNode(10)
		root.left = TreeNode(5)
		root.left.left = TreeNode(2)
		root.left.left.left = TreeNode(1)
		self.assertTrue(is_valid_bst(root))

	def test_right_heavy(self):
		root = TreeNode(1)
		root.right = TreeNode(2)
		root.right.right = TreeNode(3)
		root.right.right.right = TreeNode(4)
		self.assertTrue(is_valid_bst(root))

	def test_equal_values(self):
		root = TreeNode(1)
		root.left = TreeNode(1)
		self.assertFalse(is_valid_bst(root))
