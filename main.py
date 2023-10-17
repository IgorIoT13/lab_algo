from  diametr import OperationBinTree
from  binar_tree import BinaryTree


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
print("Висота дерева:", tree_height)