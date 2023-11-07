def lister(matrix):
    moves = [(1, 0), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1), (0, -1), (-1, 0)]
    adjacency_list = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                adjacency_list[(i, j)] = []

    for node in adjacency_list.keys():
        x_node, y_node = node
        for x, y in moves:
            if 0 <= x_node + x < len(matrix) and 0 <= y_node + y < len(matrix[0]):
                if (x_node + x, y_node + y) in adjacency_list.keys():
                    adjacency_list[(x_node, y_node)].append((x_node + x, y_node + y))

    return adjacency_list


def get_neighbors(adjacency_list, node):
    return adjacency_list[node]


def breadth_first_search(a_list, node, visited):
    queue = [node]
    visited.add(node)

    while queue:
        current_node = queue.pop(0)
        for neighbor in get_neighbors(a_list, current_node):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


def ostrovi(a_list):
    if not a_list:
        return 0
    visited = set()
    count = 0

    for node in a_list.keys():
        if node not in visited:
            breadth_first_search(a_list, node, visited)
            count += 1

    return count


def read_matrix_from_stream(file_stream):
    matrix = []
    for line in file_stream:
        matrix.append(list(map(int, line.strip().split())))
        graph = lister(matrix)
    return graph


def write_result_to_stream(result, file_stream):
    file_stream.write(str(result))


input_file_path = './result/input_mateix.txt'
output_file_path = './result/output_result.txt'

with open(input_file_path, 'r') as input_file:
    graph = read_matrix_from_stream(input_file)

result = ostrovi(graph)

with open(output_file_path, 'w') as output_file:
    write_result_to_stream(result, output_file)

print("Graph:", graph)
print("Ostrovi :", result)