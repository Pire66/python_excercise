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

input_string1 = input().strip().split(' ')
kol_vert = int(input_string1[0])
kol_rebr = int(input_string1[1])
weight_rebr = []
for i in range(kol_rebr):
    vert1, vert2, weight = input().strip().split(' ')
    weight_rebr.append([int(vert1), int(vert2), int(weight)])
input_string1 = input().strip().split(' ')
start_vert = int(input_string1[0])
end_vert = int(input_string1[1])
list_vert = [i+1 for i in range(kol_vert)]
list_vert_temp = {i: float("inf") for i in list_vert}
list_vert_temp[start_vert] = 0
q = list_vert
#visited = {start_vert:0}
visited = {}
path = {}

while len(q)>0:
    u = min(list_vert_temp.values())
    min_node = None
    for node in list_vert_temp:
        if list_vert_temp[node] == u:        
            min_node = node
#            visited.update{min_node:u}
            break
#    -------------------------------    
    for node in list_vert_temp:
         if node in visited:
             if min_node is None:
                 min_node = node
             elif visited[node] < visited[min_node]:
                  min_node = node
    if min_node is None:
        break
    
    list_vert_temp.remove(min_node)
    current_weight = visited[min_node]

    for edge in weight_rebr:
        try:
            weight = current_weight + edge[2]
        except:
            continue
        if edge not in visited or weight < visited[edge]:
            visited[edge] = weight
            path[edge] = min_node

        
    
    print(min_weight, index_min_weight, u)


