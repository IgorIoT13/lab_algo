from binar_tree import BinaryTree
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

        left_height = self.find_height(node.left)
        right_height = self.find_height(node.right)

        left_diameter = self.binary_tree_diameter(node.left)
        right_diameter = self.binary_tree_diameter(node.right)

        return max(left_height + right_height, max(left_diameter, right_diameter))

    def find_tree_height(self):
        return self.binary_tree_diameter(self.root)

    def search(self, node, el):
        if node is None:
            return None
        if node.value is el:
            return node
        right = self.search(node.right, el)
        left = self.search(node.left, el)


        if left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None

    def all_element(self, node, first, last):

        left_fir = self.search(node.left, first)
        left_las = self.search(node.left, last)

        right_fir = self.search(node.right, first)
        right_las = self.search(node.right, last)

        if left_fir is not None and left_las is not None:
            node = self.all_element(node.left, first, last)
            return node
        elif right_fir is not None and right_las is not None:
            node = self.all_element(node.right, first, last)
            return node
        else:
            return node
    def finder(self, node, first, last):
        node = self.all_element(node, first, last)
        tree = BinaryTree(1)

        if(node.value != first and node.value != last):
            return abs(tree.find_length_to_element(node, first) - tree.find_length_to_element(node, last))
        elif node.value == first:
            return tree.find_length_to_element(node, last)
        else:
            return tree.find_length_to_element(node, first)