import unittest
from .AVL import AVLTree

class TestAVL(unittest.TestCase):
    def test_avl_insertion(self):
        tree = AVLTree()
        for number in [30, 20, 40, 10, 25, 35, 50]:
            tree.insert(number)
        self.assertEqual(tree.root.value, 30)
        self.assertEqual(tree.root.left.value, 20)
        self.assertEqual(tree.root.right.value, 40)


    def test_avl_search(self):
        tree = AVLTree()
        for number in [30, 20, 40, 10, 25, 35, 50]:
            tree.insert(number)
        self.assertIsNotNone(tree.search(35))
        self.assertIsNone(tree.search(42))


    def test_avl_deletion(self):
        tree = AVLTree()
        for number in [30, 20, 40, 10, 25, 35, 50]:
            tree.insert(number)
        tree.delete(20)
        self.assertNotEqual(tree.root.left.value, 20)
        self.assertIsNone(tree.search(20))


    def test_avl_duplicate_insertion(self):
        tree = AVLTree()
        tree.insert(30)
        tree.insert(30)
        self.assertIsNotNone(tree.search(30))

        elements = []

        def inorder_traversal(node):
            if node is not None:
                inorder_traversal(node.left)
                elements.append(node.value)
                inorder_traversal(node.right)

        inorder_traversal(tree.root)
        self.assertEqual(elements.count(30), 1)


    def test_avl_delete_non_existent(self):
        tree = AVLTree()
        for number in [30, 20, 40]:
            tree.insert(number)
        tree.delete(99)
        self.assertIsNotNone(tree.search(30))
        self.assertIsNotNone(tree.search(20))
        self.assertIsNotNone(tree.search(40))
        self.assertIsNone(tree.search(99))


if __name__ == "__main__":
    main()
