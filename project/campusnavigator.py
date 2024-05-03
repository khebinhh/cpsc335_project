import tkinter as tk
from PIL import Image, ImageTk


class CampusNavigator:
    def __init__(self, master, graph):
        self.master = master
        self.graph = graph
        self.master.title("Campus Navigator")

        #Resizing Map
        """ fix later
        campus_map_image = Image.open("CampusGraph.png")
        width, height = campus_map_image.size
        new_width = 400
        new_height = int(height * (new_width / width))
        resized_campus_map = campus_map_image.resize((new_width, new_height), Image.ANTIALIAS)
        self.CampusGraph = ImageTk.PhotoImage(resized_campus_map)
        """
        
        #Campus Map
        """
        self.CampusGraph = tk.PhotoImage(file="CampusGraph.png")
        self.map_label = tk.Label(master, image=self.CampusGraph)
        self.map_label.grid(row=0, column=0, rowspan=5, padx=10, pady=10)
        """

        #start point

        self.start_label = tk.Label(master, text="Select Start Point:")
        self.start_label.grid(row=0, column=1, sticky="e", padx=10, pady=10)

        self.start_var = tk.StringVar()
        self.start_dropdown = tk.OptionMenu(master, self.start_var, *self.graph.keys())
        self.start_dropdown.grid(row=0, column=2, padx=10, pady=10)

        #end point

        self.end_label = tk.Label(master, text="Select End Point:")
        self.end_label.grid(row=1, column=1, sticky="e", padx=10, pady=10)

        self.end_var = tk.StringVar()
        self.end_dropdown = tk.OptionMenu(master, self.end_var, *self.graph.keys())
        self.end_dropdown.grid(row=1, column=2, padx=10, pady=10)

        #Accessibility Options
        self.accessibility_label = tk.Label(master, text="Accessibility Options:")
        self.accessibility_label.grid(row=2, column=1, sticky="e", padx=10, pady=10)

        self.accessibility_var = tk.BooleanVar()
        self.accessibility_checkbox = tk.Checkbutton(master, text="Wheelchair-friendly routes", variable=self.accessibility_var)
        self.accessibility_checkbox.grid(row=2, column=2, padx=10, pady=10)
       
        #find route

        self.route_button = tk.Button(master, text="Find Route", command=self.find_route)
        self.route_button.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="e")

        self.route_display = tk.Label(master, text="")
        self.route_display.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="e")

    def find_route(self):
        start_point = self.start_var.get()
        end_point = self.end_var.get()
        route = self.calculate_route(start_point, end_point)
        self.route_display.config(text=route)
        wheelchair_friendly = self.accessibility_var.get()

        if wheelchair_friendly:
            pass
        else:
            route = self.bfs_function(self.graph, start_point, end_point)
            self.route_display.config(text=route)


    def calculate_route(self, start, end):
        return f"Route from {start} to {end} found!"

