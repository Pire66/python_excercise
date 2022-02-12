# Реализуйте алгоритм Дейкстры поиска кратчайшего пути в графе.
# Входные данные: В первой строке указаны два числа: число вершин и число ребер графа.
# Далее идут строки с описанием ребер. Их количество равно числу ребер. В каждой строке указаны 3 числа: исходящая вершина, входящая вершина, вес ребра. В последней строке указаны 2 номера вершины: начальная и конечная вершина, кратчайший путь между которыми нужно найти.
# Выходные данные: минимальное расстояние между заданными вершинами. Если пути нет, то нужно вернуть -1.
# Sample Input:
# 4 8
# 1 2 6
# 1 3 2
# 1 4 10
# 2 4 4
# 3 1 5
# 3 2 3
# 3 4 8
# 4 2 1
# 1 4
# Sample Output:
# 9


from collections import defaultdict, deque

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    print(visited, paths,full_path,origin, destination)
    try:
        _destination = paths[destination]
        while _destination != origin:
            full_path.appendleft(_destination)
            _destination = paths[_destination]
    except:
        pass
    full_path.appendleft(origin)
    full_path.append(destination)
    try:
        shorter_path = visited[destination]
    except:
        shorter_path = -1
    return shorter_path, list(full_path)

if __name__ == '__main__':
    graph = Graph()
    input_string1 = input().strip().split(' ')
    kol_vert = int(input_string1[0])
    kol_rebr = int(input_string1[1])
    for node in range(kol_vert):
        graph.add_node(node+1)
    for i in range(kol_rebr):
        vert1, vert2, weight = input().strip().split(' ')
        graph.add_edge(int(vert1), int(vert2), int(weight))
    input_string1 = input().strip().split(' ')
    start_vert = int(input_string1[0])
    end_vert = int(input_string1[1])

    unswer,unswer_list  = shortest_path(graph, start_vert, end_vert)
    print(unswer,unswer_list)

