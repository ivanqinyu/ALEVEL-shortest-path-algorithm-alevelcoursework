'''graph_example_student.py
Shows an example of code to find direct path through a graph
This graph is a simple adjacency list
Jan 2017'''


#graph presented as a dictionary showing connected nodes (vertices)
graph = {'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D', 'F'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']}


def find_path(graph, start, end, path=[]):
    '''works out direct path through graph'''
    path = path + [start]
    if start == end:
        return path
    if start not in graph:      # input error trap (not strictly necessary)
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path) # good old recursion
            if newpath:
                return newpath
    return None

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    
    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path

    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
print("direct path",find_shortest_path(graph, 'A', 'F'))


'''Now your turn. Try to write a second function (based on this) to work out
all the possible paths through the graph.

If you can do this then try the shortest path'''
