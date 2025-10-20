class TreeNode:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

class BST:
	def __init__(self):
		self.root = None

	def insert(self, key):
		if self.root is None:
			self.root = TreeNode(key)
			return
		current = self.root
		while True:
			if key < current.val:
				if current.left is None:
					current.left = TreeNode(key)
					break
				else:
					current = current.left
			else:
				if current.right is None:
					current.right = TreeNode(key)
					break
				else:
					current = current.right

	def pre_order(self, node):
		if node is None:
			return []
		result = []
		result.append(node.val)
		result.extend(self.pre_order(node.left))
		result.extend(self.pre_order(node.right))
		return result

	def in_order(self, node):
		if node is None:
			return []
		result = []
		result.extend(self.in_order(node.left))
		result.append(node.val)
		result.extend(self.in_order(node.right))
		return result

	def post_order(self, node):
		if node is None:
			return []
		result = []
		result.extend(self.post_order(node.left))
		result.extend(self.post_order(node.right))
		result.append(node.val)
		return result

	def reverse_pre_order(self, node):
		if node is None:
			return []
		result = []
		result.append(node.val)
		result.extend(self.reverse_pre_order(node.right))
		result.extend(self.reverse_pre_order(node.left))
		return result

	def reverse_in_order(self, node):
		if node is None:
			return []
		result = []
		result.extend(self.reverse_in_order(node.right))
		result.append(node.val)
		result.extend(self.reverse_in_order(node.left))
		return result

	def reverse_post_order(self, node):
		if node is None:
			return []
		result = []
		result.extend(self.reverse_post_order(node.right))
		result.extend(self.reverse_post_order(node.left))
		result.append(node.val)
		return result
