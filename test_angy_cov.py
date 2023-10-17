import unittest
from diametr import OperationBinTree
from binar_tree import BinaryTree

class MyTestCase(unittest.TestCase):
    def test_rig_lef(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)
        root.right.right = BinaryTree(10)
        root.right.right.right = BinaryTree(11)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.right.right = BinaryTree(5)
        root.left.left.left.left = BinaryTree(9)
        root.left.right.right.right = BinaryTree(6)

        op_tree = OperationBinTree(root)
        tree_height = op_tree.find_tree_height()

        self.assertEqual(tree_height, 7)

    def test_left_left (self):
            root = BinaryTree(1)
            root.left = BinaryTree(3)
            root.right = BinaryTree(2)
            root.left.left = BinaryTree(7)
            root.left.right = BinaryTree(4)
            root.left.left.left = BinaryTree(8)
            root.left.right.right = BinaryTree(5)
            root.left.left.left.left = BinaryTree(9)
            root.left.right.right.right = BinaryTree(6)

            op_tree = OperationBinTree(root)
            tree_height = op_tree.find_tree_height()
            self.assertEqual(tree_height, 6)
    def test_zero_tree(self):
        root = None
        op_tree = OperationBinTree(root)
        tree_height = op_tree.find_tree_height()
        self.assertEqual(tree_height, 0)


if __name__ == '__main__':
    unittest.main()
