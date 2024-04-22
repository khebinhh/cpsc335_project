# Smart Campus Navigation System
## Overview
This project aims to develop a smart navigation system specifically for a university campus that helps users find the shortest or most optimal paths to different locations on the campus, such as lecture halls, libraries, cafeterias, and administrative buildings. The system will provide routes based on different criteria such as distance, time, and accessibility.
## Objectives
1. Implement a Graph-Based Map of the Campus: Model the campus layout as a graph where locations (nodes) are connected by paths (edges) with attributes such as distance, estimated travel time, and accessibility features.
2. Pathfinding Algorithms Implementation: Utilize BFS, DFS, and Dijkstra's Algorithm to offer different routing options:
```
• BFS to find the shortest path by the number of edges (stops).
• DFS to explore all possible paths and perhaps find paths with specific
characteristics (e.g., scenic routes that pass by certain landmarks).
• Dijkstra's Algorithm to find the shortest path based on weighted criteria such as time or distance.
```