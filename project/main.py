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
def find_shortest_path_using_dijkstra(graph, start_node):
    return dijkstra_algo(graph, start_node)

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
      '''self.route_display.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="e")
      '''

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
      dijkstra_shortest_path = find_shortest_path_using_dijkstra(self.graph, start_point)

      # Displaying results
      result_text = f"BFS Shortest Path: {bfs_shortest_path}\n\nDFS All Paths: {dfs_all_paths}\n\nDijkstra Shortest Path:"
      self.route_display.config(text=result_text)

  def calculate_route(self, start, end):
      return f"Route from {start} to {end} found!"
    
# Create function to initialize GUI and start main loop
if __name__ == "__main__":
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
    root = tk.Tk()
    app = CampusNavigator(root, graph)
    root.mainloop()