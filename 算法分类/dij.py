nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

unvisited = {node: None for node in nodes} #把None作为无穷大使用
visited = {}#用来记录已经松弛过的数组
current = 'B' #要找B点到其他点的距离
currentDistance = 0
unvisited[current] = currentDistance#B到B的距离记为0

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue#被访问过了，跳出本次循环
        newDistance = currentDistance + distance#新的距离
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:#如果两个点之间的距离之前是无穷大或者新距离小于原来的距离
            unvisited[neighbour] = newDistance#更新距离
    visited[current] = currentDistance#这个点已经松弛过，记录
    del unvisited[current]#从未访问过的字典中将这个点删除
    if not unvisited: break#如果所有点都松弛过，跳出此次循环
    candidates = [node for node in unvisited.items() if node[1]]#找出目前还有拿些点未松弛过
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]#找出目前可以用来松弛的点

print (visited)
