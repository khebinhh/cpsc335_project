import heapq


def dijkstra_algo(graph, start_node, end_node):
    shortest_distances = {node: float('infinity') for node in graph}
    shortest_distances[start_node] = 0
    previous_nodes = {node: None for node in graph}
    nodes_to_explore = [(0, start_node)]

    while nodes_to_explore:
        current_min_distance, min_distance_node = heapq.heappop(
            nodes_to_explore)

        if min_distance_node == end_node:
                path = []
                while min_distance_node is not None:
                    path.append(min_distance_node)
                    min_distance_node = previous_nodes[min_distance_node]
                return path[::-1]  # Return the path in correct order
          
        if current_min_distance > shortest_distances[min_distance_node]:
            continue
        
        for adjacent, weight in graph[min_distance_node].items():
            # Skip processing if the path is currently unavailable
            if weight == float('infinity'):
                continue 
            # Calculating the new distance while considering the weight of the current node being explored.
            path_distance = current_min_distance + weight
            # If a shorter path to the adjacent node is found, update the shortest distances and previous nodes.
            if path_distance < shortest_distances[adjacent]:
                shortest_distances[adjacent] = path_distance
                previous_nodes[adjacent] = min_distance_node
                heapq.heappush(nodes_to_explore, (path_distance, adjacent))
    return []  # In case there's no path from start to end, return an empty list.

'''if current_min_distance > shortest_distances[min_distance_node]:
    continue

for adjacent, weight in graph[min_distance_node].items():
    if weight == float('infinity'):
        continue  # Skip processing if the path is currently unavailable

    path_distance = current_min_distance + weight
    if path_distance < shortest_distances[adjacent]:
        shortest_distances[adjacent] = path_distance
        heapq.heappush(nodes_to_explore, (path_distance, adjacent))

return shortest_distances'''
