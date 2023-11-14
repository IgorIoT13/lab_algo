class Pinguin:
    def __init__(self, input):
        self.input = input

    def all_City_Storage(self, input):
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

    def BFS_to_Storage(self, graph, first_element):

        city, storage = self.all_City_Storage(graph)
        visited = set()
        result_graph = set()
        result_graph.add(first_element)
        queue = [first_element]

        while queue:
            now_ele = queue.pop(0)
            for f, l in graph:
                if f == now_ele and l not in visited and l not in storage:
                    queue.append(l)
                    result_graph.add(l)

            visited.add(now_ele)

        return result_graph

    def all_storage_graph(self):
        graph = self.input
        city, storage = self.all_City_Storage(graph)

        all_storage = []

        for i in storage:
            curr = self.BFS_to_Storage(graph, i)

            curr_arr = []
            curr_arr.append(f'{i} : ')
            for c in city:
                if c not in curr:
                    curr_arr.append(c)
            all_storage.append(curr_arr)

        return all_storage

