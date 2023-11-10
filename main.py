from collections import deque

def is_valid(x, y, M, N):
    return 0 <= x < M and 0 <= y < N


def find_shortest_path(matrix, start, end):
    M, N = len(matrix), len(matrix[0])

    if matrix[start[0]][start[1]] == 0 or matrix[end[0]][end[1]] == 0:
        return None

    queue = deque([(start, 0)])
    visited = set()

    while queue:
        (x, y), distance = queue.popleft()
        visited.add((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy

            if is_valid(new_x, new_y, M, N):

                if (new_x, new_y) == end:
                    return distance + 1

                if matrix[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                    queue.append(((new_x, new_y), distance + 1))

    return None

input_file_path = './result/input_mateix.txt'

with open(input_file_path, 'r') as input_file:
    M, N = map(int, input_file.readline().strip().split())
    start = tuple(map(int, input_file.readline().strip().split()))
    end = tuple(map(int, input_file.readline().strip().split()))
    matrix = [list(map(int, input_file.readline().strip().split())) for _ in range(M)]

shortest_path_length = find_shortest_path(matrix, start, end)
if shortest_path_length is not None:
    print(f"Найкоротший шлях: {shortest_path_length} кроків")
else:
    print("Шлях неможливо знайти")
