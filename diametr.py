
class OperationBinTree:

    def __init__(self, root):
        self.root = root

    def find_height(self, node):
        if node is None:
            return 0
        left_height = self.find_height(node.left)
        right_height = self.find_height(node.right)
        return max(left_height, right_height) + 1

    def binary_tree_diameter(self, node):
        if node is None:
            return 0

        left_height = self.find_height(self.node.left)
        right_height = self.find_height(self.node.right)

        left_diameter = self.binary_tree_diameter(self.node.left)
        right_diameter = self.binary_tree_diameterself(self.node.right)

        return max(left_height + right_height, max(left_diameter, right_diameter))

    def find_tree_height(self):
        return self.binary_tree_diameter(self.root)