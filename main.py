input_valuer = [
    ['Storage_1', 'Lviv'],
    ['Striy', 'Lviv'],
    ['Storage_2', 'Storage_1'],
    ['Kiyv', 'Lviv'],
    ['Ternopil', 'Harkiv'],
    ['Storage_3', 'Ternopil'],
    ['Ternopil', 'Lviv']
]
def all_City_Storage(input):
    result = set()
    storage = set()

    for first, last in input:

        try:
            ins = first.index("Storage")
            storage.add(first)
        except:
            result.add(first)

        try:
            ins = last.index("Storage")
            storage.add(last)
        except:
            result.add(last)



    return result, storage


def BFS_to_Storage(graph, first_element):

    visited = set()
    result_graph = set()
    result_graph.add(first_element)
    queue = [first_element]

    while queue:
        now_ele = queue.pop(0)
        for f, l in graph:
            if f == now_ele and l not in visited:
                queue.append(l)
                result_graph.add(l)

        visited.add(now_ele)

    return result_graph

def all_storage_graph(graph):
    city, storage = all_City_Storage(graph)

    all_storage = []


    for i in storage:
        curr_arr = []
        curr = BFS_to_Storage(graph, i)
        curr_arr.append(f'{i} : ')
        for c in city:
            if c not in curr:
                curr_arr.append(c)
        all_storage.append(curr_arr)


    return all_storage





print(all_storage_graph(input_valuer))