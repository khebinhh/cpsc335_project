from bfs import bfs
from dfs import dfs
from dijkstra import dijkstra_algo
from PIL import Image, ImageTk
import tkinter as tk

# Use bsf.py to find the shortest path
def find_shortest_path_using_bfs(graph, start, end):
    for path in bfs(graph, start, end):
        return path

# Use dfs.py to find all possible paths
def find_all_paths_using_dfs(graph, start, end):
    return dfs(graph, start, end)

# Use dijkstra.py to find the shortest weighted path
def find_shortest_path_using_dijkstra(graph, start_node, end_node):
    shortest_distances = dijkstra_algo(graph, start_node)
    shortest_path = [end_node]
    current_node = end_node
    while current_node != start_node:
        for neighbor, weight in graph[current_node].items():
            if shortest_distances[current_node] == shortest_distances[neighbor] + weight:
                shortest_path.append(neighbor)
                current_node = neighbor
                break
    shortest_path.reverse()
    return shortest_path


# campusnavigator.py moves over here
class CampusNavigator:
  def __init__(self, master, graph):
      self.master = master
      self.graph = graph
      self.master.title("Campus Navigator")

      #Resizing Map

      campus_map_image = Image.open("CampusGraph.png")
      width, height = campus_map_image.size
      new_width = 400
      new_height = int(height * (new_width / width))
      resized_campus_map = campus_map_image.resize((new_width, new_height))
      self.CampusGraph = ImageTk.PhotoImage(resized_campus_map)


      #Campus Map

      self.map_label = tk.Label(master, image=self.CampusGraph)
      self.map_label.grid(row=0, column=1, columnspan=2, padx=10, pady=10)


      #start point

      self.start_label = tk.Label(master, text="Select Start Point:")
      self.start_label.grid(row=1, column=1, sticky="e", padx=10, pady=10)

      self.start_var = tk.StringVar()
      self.start_dropdown = tk.OptionMenu(master, self.start_var, *self.graph.keys())
      self.start_dropdown.grid(row=1, column=2, padx=10, pady=10)

      #end point

      self.end_label = tk.Label(master, text="Select End Point:")
      self.end_label.grid(row=2, column=1, sticky="e", padx=10, pady=10)

      self.end_var = tk.StringVar()
      self.end_dropdown = tk.OptionMenu(master, self.end_var, *self.graph.keys())
      self.end_dropdown.grid(row=2, column=2, padx=10, pady=10)

      #Accessibility Options
      self.accessibility_label = tk.Label(master, text="Accessibility Options:")
      self.accessibility_label.grid(row=3, column=1, sticky="e", padx=10, pady=10)

      self.accessibility_var = tk.BooleanVar()
      self.accessibility_checkbox = tk.Checkbutton(master, text="Wheelchair-friendly routes", variable=self.accessibility_var)
      self.accessibility_checkbox.grid(row=3, column=2, padx=10, pady=10)

      #find route

      self.route_button = tk.Button(master, text="Find Route", command=self.find_route)
      self.route_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="e")

      self.route_display = tk.Label(master, text="")
      self.route_display.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="e")
  
  def find_route(self):
    start_point = self.start_var.get()
    end_point = self.end_var.get()
    
    '''
      route = self.calculate_route(start_point, end_point)
      self.route_display.config(text=route)
      wheelchair_friendly = self.accessibility_var.get()

      if wheelchair_friendly:
          pass
      else:
          route = self.bfs_function(self.graph, start_point, end_point)
          self.route_display.config(text=route)
      '''
      # Implementing algos
    bfs_shortest_path = find_shortest_path_using_bfs(self.graph, start_point, end_point)
    dfs_all_paths = find_all_paths_using_dfs(self.graph, start_point, end_point)
    dijkstra_shortest_path = find_shortest_path_using_dijkstra(self.graph, start_point, end_point)

      # Displaying results
    result_text = f"BFS Shortest Path: {bfs_shortest_path}\n\nDFS All Paths:\n"
    dfs_paths = [', '.join(path) for path in dfs_all_paths]
    result_text += '\n'.join(dfs_paths) + "\n\nDijkstra Shortest Path: {dijkstra_shortest_path}"
    self.route_display.config(text=result_text)

def calculate_route(self, start, end):
      return f"Route from {start} to {end} found!"
    
# Create function to initialize GUI and start main loop
if __name__ == "__main__":
    graph = {
        '1': {'2': 1},
        '2': {'1': 1, '7': 2},
        '3': {'4': 1},
        '4': {'3': 1, '5': 1},
        '5': {'4': 1, '6': 2, '7': 4},
        '6': {'5': 2},
        '7': {'2': 2, '5': 4, '8': 4},
        '8': {'7': 4, '9': 4, '23': 4},
        '9': {'8': 4, '11': 1},
        '10': {'11': 1},
        '11': {'9': 1, '10': 1, '12': 1, '18': 2},
        '12': {'11': 1, '13': 1},
        '13': {'12': 1, '14': 1, '15': 1},
        '14': {'13': 1, '16': 1},
        '15': {'13': 1, '16': 1, '20': 2},
        '16': {'14': 1, '15': 1, '21': 2},
        '17': {'18': 1},
        '18': {'11': 2, '17': 1, '19': 1},
        '19': {'18': 1, '20': 2},
        '20': {'19': 2, '15': 2},
        '21': {'16': 2, '22': 0, '40': 1},
        '22': {'21': 0, '24': 1, '27': 4},
        '23': {'8': 4, '24': 1, '25': 4},
        '24': {'23': 1, '22': 1},
        '25': {'23': 4, '26': 1, '28': 1},
        '26': {'25': 1, '30': 1, '27': 1},
        '27': {'22': 4, '26': 1, '39': 6, '42': 1},
        '28': {'29': 1},
        '29': {'25': 1, '28': 1, '31': 1, '30': 1},
        '30': {'29': 1, '26': 1},
        '31': {'29': 1, '33': 1, '32': 2},
        '32': {'31': 2, '35': 1},
        '33': {'31': 1, '36': 1},
        '35': {'32': 1, '39': 2, '38': 1},
        '36': {'33': 1, '38': 2, '37': 1},
        '37': {'36': 1},
        '38': {'35': 2, '36': 2},
        '39': {'35': 2, '27': 6},
        '40': {'21': 1, '46': 2},
        '41': {'42': 1, '47': 2},
        '42': {'41': 1, '48': 2, '27': 1},
        '43': {'49': 1},
        '44': {'46': 6},
        '46': {'44': 6, '40': 1, '47': 1},
        '47': {'46': 1, '41': 2, '48': 1},
        '48': {'47': 1, '42': 2, '49': 1},
        '49': {'50': 1, '43': 1, '38': 1},
        '50': {'52': 1, '49': 1},
        '51': {'52': 1},
        '52': {'50': 1, '51': 1, '62': 3},
        '53': {'70': 1},
        '54': {'56': 1},
        '55': {'56': 1, '59': 1},
        '56': {'55': 1, '54': 1, '57': 1},
        '57': {'56': 1, '58': 1},
        '58': {'57': 1},
        '59': {'55': 1, '60': 1, '66': 3},
        '60': {'59': 1},
        '62': {'52': 3, '63': 2},
        '63': {'62': 2, '74': 2},
        '64': {'71': 1},
        '65': {'70': 4, '67': 1},
        '66': {'59': 3, '67': 2},
        '67': {'66': 2, '65': 1, '68': 3},
        '68': {'67': 3, '69': 1, '72': 1},
        '69': {'68': 1},
        '70': {'65': 4, '53': 1, '71': 1},
        '71': {'70': 1, '64': 1, '72': 1},
        '72': {'68': 1, '71': 1, '73': 1},
        '73': {'72': 1, '74': 1},
        '74': {'63': 2, '73': 1}
    }

  
    root = tk.Tk()
    app = CampusNavigator(root, graph)
    root.mainloop()