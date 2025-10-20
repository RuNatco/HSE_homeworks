import unittest
from .balanced_binary_tree import TreeNode, is_balanced

class TestBalancedBinaryTree(unittest.TestCase):

	def test_balanced(self):
		root = TreeNode(1)
		root.left = TreeNode(2)
		root.right = TreeNode(3)
		root.left.left = TreeNode(4)
		root.left.right = TreeNode(5)
		root.right.right = TreeNode(6)
		self.assertTrue(is_balanced(root))

	def test_unbalanced(self):
		root = TreeNode(1)
		root.left = TreeNode(2)
		root.left.left = TreeNode(3)
		root.left.left.left = TreeNode(4)
		self.assertFalse(is_balanced(root))

	def test_empty_tree(self):
		self.assertTrue(is_balanced(None))

	def test_single_node(self):
		self.assertTrue(is_balanced(TreeNode(1)))

	def test_balanced_with_right_heavy(self):
		root = TreeNode(1)
		root.right = TreeNode(2)
		root.right.right = TreeNode(3)
		self.assertFalse(is_balanced(root))

	def test_balanced_with_left_heavy(self):
		root = TreeNode(1)
		root.left = TreeNode(2)
		root.left.left = TreeNode(3)
		self.assertFalse(is_balanced(root))
