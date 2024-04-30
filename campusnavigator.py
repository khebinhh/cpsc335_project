import tkinter as tk

# Dummy campus graph data
campus_graph = {
    #implement graph data here
}

class CampusNavigator:
    def __init__(self, master):
        self.master = master
        self.master.title("Campus Navigator")

        self.start_label = tk.Label(master, text="Select Start Point:")
        self.start_label.grid(row=0, column=0, pady=10)

        self.start_var = tk.StringVar()
        self.start_dropdown = tk.OptionMenu(master, self.start_var, *campus_graph.keys())
        self.start_dropdown.grid(row=0, column=1, pady=10)

        self.end_label = tk.Label(master, text="Select End Point:")
        self.end_label.grid(row=1, column=0, pady=10)

        self.end_var = tk.StringVar()
        self.end_dropdown = tk.OptionMenu(master, self.end_var, *campus_graph.keys())
        self.end_dropdown.grid(row=1, column=1, pady=10)

        self.route_button = tk.Button(master, text="Find Route", command=self.find_route)
        self.route_button.grid(row=2, columnspan=2, pady=10)

        self.route_display = tk.Label(master, text="")
        self.route_display.grid(row=3, columnspan=2, pady=10)

    def find_route(self):
        start_point = self.start_var.get()
        end_point = self.end_var.get()
        route = self.calculate_route(start_point, end_point)
        self.route_display.config(text=route)

    def calculate_route(self, start, end):
        return f"Route from {start} to {end} found!"

def main():
    root = tk.Tk()
    app = CampusNavigator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

