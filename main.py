from  diametr import OperationBinTree
from  binar_tree import BinaryTree


root = BinaryTree(1)
root.left = BinaryTree(3)
root.right = BinaryTree(2)
root.left.left = BinaryTree(7)
root.left.right = BinaryTree(4)
root.left.left.left = BinaryTree(8)
root.left.left.left.left = BinaryTree(9)

op_tree = OperationBinTree(root)
tree_height = op_tree.find_tree_height()
print(f"Висота дерева: {tree_height}" )

Status = op_tree.finder(root,4, 9)

print(Status)