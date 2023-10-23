from binar_tree import BinaryTree

# Створюємо бінарне дерево
root = BinaryTree(1)
root.left = BinaryTree(3)
root.right = BinaryTree(2)
root.left.left = BinaryTree(7)
root.left.right = BinaryTree(11)
root.left.left.left = BinaryTree(8)
root.left.left.left.left = BinaryTree(9)

target_element = 9
path_to_element_1 = root.find_path_to_element(root, target_element)
target_element_2 = 2
path_to_element_2 = root.find_path_to_element(root, target_element_2)


def Fight(fir_arr, last_arr):
    if fir_arr is None or last_arr is None:
        return "Error"

    min_len = len(fir_arr)
    max_len = len(last_arr)

    for i in fir_arr:
        if i in last_arr:
            min_len -= 1
            max_len -= 1

    result = abs(max_len + min_len)

    if min_len <= 1 and min_len == max_len:
        result -= 2

    return result


print(Fight(path_to_element_1, path_to_element_2))