class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def find_length_to_element(self, root, target):
        def find_path(node, target):
            if node is None:
                return []
            if node.value == target:
                return [node.value]
            left_path = find_path(node.left, target)
            if left_path:
                return [node.value] + left_path
            right_path = find_path(node.right, target)
            if right_path:
                return [node.value] + right_path
            return []

        path = find_path(root, target)
        if path:
            return len(path) - 1
        else:
            return -1