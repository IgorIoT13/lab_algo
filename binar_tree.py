class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def find_path_to_element(self, node, target):
        if node is None:
            return None

        if node.value == target:
            return [node.value]  # Знайдено шлях до цільового елементу

        left_path = self.find_path_to_element(node.left, target)
        if left_path is not None:
            return [node.value] + left_path  # Додаємо поточний вузол до шляху

        right_path = self.find_path_to_element(node.right, target)
        if right_path is not None:
            return [node.value] + right_path  # Додаємо поточний вузол до шляху

        return None  # Цільовий елемент не знайдено у піддереві