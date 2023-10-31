from model.map_reader import MapReader

map = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1]
]
mapreader = MapReader(map)

mapreader.printer()

arr = mapreader.land_finder()
print(len(arr))



