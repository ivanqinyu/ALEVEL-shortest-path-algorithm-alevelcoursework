graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

#print(list(dfs_paths(graph, 'A', 'F')))

paths=list(dfs_paths(graph, 'A', 'F'))
length=999
shortest_path=['']
for path in paths:
    if len(path) < length:
        length=len(path)
        shortest_path=path
print (shortest_path)

# def dfs(graph, start):
#     visited, stack = set(), [start]
#     while stack:
#         print(visited, stack)
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             stack.extend(graph[vertex] - visited)
#     return visited
# print (dfs(graph, 'A'))
# {'E', 'D', 'F', 'A', 'C', 'B'}