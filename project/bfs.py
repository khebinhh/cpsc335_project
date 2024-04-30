# Use BFS to find the shortest path by the number of edges (stops).
def bfs(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
