class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def is_valid_bst(root, low=float('-inf'), high=float('inf')):
	if root is None:
		return True
	if root.val <= low or root.val >= high:
		return False
	return (is_valid_bst(root.left, low, root.val) and
			is_valid_bst(root.right, root.val, high))
