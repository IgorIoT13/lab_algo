from collections import deque
from PIL import Image, ImageDraw

class MapReader:
    def __init__(self, map):
        self.map = map
        self.height = len(map)
        self.width = len(map[0])

    def printer(self):

        square_size = 40

        width = len(self.map[0]) * square_size
        height = len(self.map) * square_size

        image = Image.new("RGB", (width, height), "white")

        draw = ImageDraw.Draw(image)

        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                color = (199, 240, 250) if self.map[i][j] == 0 else (215, 255, 10)
                draw.rectangle(
                    [j * square_size, i * square_size, (j + 1) * square_size, (i + 1) * square_size],
                    fill=color,
                )

        image.show()

    def land_finder(self):

        graph = self.map

        def is_valid(x, y):
            return 0 <= x < len(graph) and 0 <= y < len(graph[0])

        def bfs(x, y):
            group = []
            queue = [(x, y)]
            while queue:
                x, y = queue.pop()
                group.append((x, y))
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        new_x, new_y = x + dx, y + dy
                        if is_valid(new_x, new_y) and graph[new_x][new_y] == 1:
                            queue.append((new_x, new_y))
                            graph[new_x][new_y] = 0
            return group

        groups = []
        for x in range(len(graph)):
            for y in range(len(graph[0])):
                if graph[x][y] == 1:
                    group = bfs(x, y)
                    groups.append(group)

        return groups