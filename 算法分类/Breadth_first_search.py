graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

#print(list(dfs_paths(graph, 'A', 'F')))


paths=list(bfs_paths(graph, 'A', 'F'))
length=999
shortest_path=['']
for path in paths:
    if len(path) < length:
        length=len(path)
        shortest_path=path
print (shortest_path)


# def bfs(graph, start):
#     visited, queue = set(), [start]
#     while queue:
#         vertex = queue.pop(0)
#         if vertex not in visited:
#             visited.add(vertex)
#             queue.extend(graph[vertex] - visited)
#     return visited
#
# bfs(graph, 'A')
# [# 'B', 'C', 'A', 'F', 'D', 'E']
