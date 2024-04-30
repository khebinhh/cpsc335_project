import heapq


def dijkstra_algo(graph, start_node):
    shortest_distances = {node: float('infinity') for node in graph}
    shortest_distances[start_node] = 0
    nodes_to_explore = [(0, start_node)]

    while nodes_to_explore:
        current_min_distance, min_distance_node = heapq.heappop(
            nodes_to_explore)

        if current_min_distance > shortest_distances[min_distance_node]:
            continue

        for adjacent, weight in graph[min_distance_node].items():
            if weight == float('infinity'):
                continue  # Skip processing if the path is currently unavailable

            path_distance = current_min_distance + weight
            if path_distance < shortest_distances[adjacent]:
                shortest_distances[adjacent] = path_distance
                heapq.heappush(nodes_to_explore, (path_distance, adjacent))

    return shortest_distances
