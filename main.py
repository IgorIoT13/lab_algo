from collections import deque

def is_valid(x, y, N):
    return 0 <= x < N and 0 <= y < N

def min_moves_knight(N, src, dest):
    # Можливі ходи коня
    moves = [
        (2, 1), (1, 2),
        (-1, 2), (-2, 1),
        (-2, -1), (-1, -2),
        (1, -2), (2, -1)
    ]

    visited = [[False for _ in range(N)] for _ in range(N)]

    queue = deque([(src[0], src[1], 0)])  # (x, y, кількість кроків)

    while queue:
        x, y, steps = queue.popleft()

        if x == dest[0] and y == dest[1]:
            return steps

        for move in moves:
            new_x, new_y = x + move[0], y + move[1]

            if is_valid(new_x, new_y, N) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, steps + 1))

    return -1  # Якщо до кінцевої точки неможливо дістатися

# Приклад використання
N = 8
src = (0, 0)
dest = (1, 2)

result = min_moves_knight(N, src, dest)
print(f"Мінімальна кількість кроків: {result}")
