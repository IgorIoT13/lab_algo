from collections import deque

def is_valid(x, y, N):
    return 0 <= x < N and 0 <= y < N

def min_moves_knight(N, src, dest):

    moves = [
        (2, 1), (1, 2),
        (-1, 2), (-2, 1),
        (-2, -1), (-1, -2),
        (1, -2), (2, -1)
    ]

    visited = [[False for i in range(N)] for i in range(N)]
    path = [[None for i in range(N)] for i in range(N)]

    queue = deque([(src[0], src[1])])

    visited[src[0]][src[1]] = True

    while queue:
        x, y = queue.popleft()

        if x == dest[0] and y == dest[1]:
            path_coordinates = []
            while (x, y) != src:
                path_coordinates.append((x, y))
                x, y = path[x][y]
            path_coordinates.append(src)
            path_coordinates.reverse()
            return path_coordinates

        for move in moves:
            new_x, new_y = x + move[0], y + move[1]

            if is_valid(new_x, new_y, N) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                path[new_x][new_y] = (x, y)
                queue.append((new_x, new_y))

    return []


input_file_path = './result/input_mateix.txt'

with open(input_file_path, 'r') as input_file:
    N = int(input_file.readline().strip())

    src = tuple(map(int, input_file.readline().strip().split()))

    dest = tuple(map(int, input_file.readline().strip().split()))



path = min_moves_knight(N, src, dest)
res = len(path) - 1
print(f"Мінімальна кількість кроків: {res}")
print(f"Шлях: {path}")
