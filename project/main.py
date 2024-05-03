from bfs import bfs
from dfs import dfs
from dijkstra import dijkstra_algo
import tkinter as tk
from campusnavigator import CampusNavigator

# Use bsf.py to find the shortest path


def find_shortest_path_using_bfs(graph, start, end):
    for path in bfs(graph, start, end):
        return path

# Use dfs.py to find all possible paths


def find_all_paths_using_dfs(graph, start, end):
    return dfs(graph, start, end)

# Use dijkstra.py to find the shortest weighted path


def find_shortest_path_using_dijkstra(graph, start_node):
    return dijkstra_algo(graph, start_node)

# Example for now to check functionality


graph = {
    '1': {'2'},
    '2': {'1', '7'},
    '3': {'4'},
    '4': {'3', '5'},
    '5': {'4', '6', '7'},
    '6': {'5'},
    '7': {'2', '5', '8'},
    '8': {'7', '9', '23'},
    '9': {'8', '11'},
    '10': {'11'},
    '11': {'9', '10', '12', '18'},
    '12': {'11', '13'},
    '13': {'12', '14', '15'},
    '14': {'13', '16'},
    '15': {'13', '16', '20'},
    '16': {'14', '15', '21'},
    '17': {'18'},
    '18': {'11', '17', '19'},
    '19': {'18', '20'},
    '20': {'19', '15'},
    '21': {'16', '22', '40'},
    '22': {'21', '24', '27'},
    '23': {'8', '24', '25'},
    '24': {'23', '22'},
    '25': {'23', '26', '28'},
    '26': {'25', '30', '27'},
    '27': {'22', '26', '39', '42'},
    '28': {'29'},
    '29': {'25', '28', '31', '30'},
    '30': {'29', '26'},
    '31': {'29', '33', '32'},
    '32': {'31', '35'},
    '33': {'31', '36'},
    '35': {'32', '39', '38'},
    '36': {'33', '38', '37'},
    '37': {'36'},
    '38': {'35', '36'},
    '39': {'35', '27'},
    '40': {'21', '46'},
    '41': {'42', '47'},
    '42': {'41', '48', '27'},
    '43': {'49'},
    '44': {'46'},
    '46': {'44', '40', '47'},
    '47': {'46', '41', '48'},
    '48': {'47', '42', '49'},
    '49': {'50', '43', '38'},
    '50': {'52', '49'},
    '51': {'52'},
    '52': {'50', '51', '62'},
    '53': {'70'},
    '54': {'56'},
    '55': {'56', '59'},
    '56': {'55', '54', '57'},
    '57': {'56', '58'},
    '58': {'57'},
    '59': {'55', '60', '66'},
    '60': {'59'},
    '62': {'52', '63'},
    '63': {'62', '74'},
    '64': {'71'},
    '65': {'70', '67'},
    '66': {'59', '67'},
    '67': {'66', '65', '68'},
    '68': {'67', '69', '72'},
    '69': {'68'},
    '70': {'65', '53', '71'},
    '71': {'70', '64', '72'},
    '72': {'68', '71', '73'},
    '73': {'72', '74'},
    '74': {'63', '73'}
}

start_node = '1'
end_node = '74'

shortest_path = find_shortest_path_using_bfs(graph, start_node, end_node)
print(f"Shortest Path using BFS: {shortest_path}")

all_paths = find_all_paths_using_dfs(graph, start_node, end_node)
print(f"All Paths using DFS: {all_paths}")


# Creating an instance of Tk
root = tk.Tk()

# Pass root
app = CampusNavigator(root, graph)

# Start main loop
root.mainloop()