from project.bfs import bfs
from project.dfs import dfs

# Use bsf.py to find the shortest path
def find_shortest_path_using_bfs(graph, start, end):
    for path in bfs(graph, start, end):
        return path

# Use dfs.py to find all possible paths
def find_all_paths_using_dfs(graph, start, end):
    return dfs(graph, start, end)

# Example for now to check functionality
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
end_node = 'F'

shortest_path = find_shortest_path_using_bfs(graph, start_node, end_node)
print(f"Shortest Path using BFS: {shortest_path}")

all_paths = find_all_paths_using_dfs(graph, start_node, end_node)
print(f"All Paths using DFS: {all_paths}")