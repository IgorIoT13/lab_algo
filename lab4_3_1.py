STEP = [(1, 0), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1), (0, -1), (-1, 0)]

def get_element_around(matrix, node):
    start_x, start_y = node
    around = set()
    stack = [(start_x, start_y)]
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    while stack:
        x, y = stack.pop()
        around.add((x, y))

        for dx, dy in STEP:
            ax_x, ax_y = x + dx, y + dy
            if (0 <= ax_x < num_rows) and (0 <= ax_y < num_cols) and (ax_x, ax_y) not in around:
                if matrix[x][y] == matrix[ax_x][ax_y]:
                    stack.append((ax_x, ax_y))

    return around

input_file_path = './result/input_mateix.txt'

def paint(color, matrix, node):
    around = get_element_around(matrix, node)

    for x, y in around:
        matrix[x][y] = color

def read_matrix_from_stream(stream):
    matrix = []
    for line in stream:
        matrix.append(list(map(str, line.strip().split())))
    return matrix

with open(input_file_path, 'r') as input_file:
    matrix = read_matrix_from_stream(input_file)
    paint("Y", matrix, (0, 1))

with open(input_file_path, 'w') as output_file:
    for row in matrix:
        output_file.write(' '.join(row) + '\n')

print("File updated with modified data.")
