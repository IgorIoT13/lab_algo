def create_adjacency_list(matrix):
    result_list = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                result_list[(i, j)] = []
    return result_list

def build_adjacency_list(matrix):
    adjacency_list = create_adjacency_list(matrix)
    for node in adjacency_list.keys():
        x_position, y_position = node
        for x, y in [(1, 0), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1), (0, -1), (-1, 0)]:
            actual_x, actual_y = x_position + x, y_position + y
            if (0 <= actual_x < len(matrix)) and (0 <= actual_y < len(matrix[0])) and (actual_x, actual_y) in adjacency_list:
                adjacency_list[(x_position, y_position)].append((actual_x, actual_y))

    return adjacency_list


def get_neighbors(adjacency_list, node):
    return adjacency_list[node]

def BFS(a_list, node, visited):
    visited.add(node)
    for neighbor in get_neighbors(a_list, node):
        if neighbor not in visited:
            BFS(a_list, neighbor, visited)

def island(a_list):
    if not a_list:
        return 0
    visited = set()
    count = 0

    for node in a_list.keys():
        if node not in visited:
            BFS(a_list, node, visited)
            count += 1

    return count


def read_matrix_from_stream(stream):
    matrix = []
    for line in stream:
        matrix.append(list(map(int, line.strip().split())))
    return build_adjacency_list(matrix)


def write_result_to_stream(result, file_stream):
    file_stream.write(str(result))



input_file_path = './result/input_mateix.txt'

with open(input_file_path, 'r') as input_file:
    graph = read_matrix_from_stream(input_file)

result = island(graph)


print("Ostrovi :", result)



