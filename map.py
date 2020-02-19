import tkinter as tk
import node as n


class Map(tk.Frame):
    def __init__(self, parent, rows, columns, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # Variables for declaring how big generated map will be
        self.rows = rows
        self.columns = columns

        # Variables for declaring colors of map elements
        self.start_color = "lawn green"
        self.end_color = "firebrick1"
        self.wall_color = "gray20"
        self.path_color = "turquoise1"
        self.map_color = "white"

        # Variable for storing reference to each node on map.
        self.map = []

        # Variables for declaring which color is currently used and if cursor should color Nodes at all
        self.current_color = self.map_color
        self.color_flag = False

        # Variable for context
        self.context = tk.StringVar(value="Doing nothing")

        # Create map with size of x == width and y == height, weights are used to make this map responsive for all
        # resizing user is doing with the main window. Save reference from each button in map variable.
        for row in range(self.rows):
            self.rowconfigure(row, weight=1)
            self.tmp = []
            for column in range(self.columns):
                self.columnconfigure(column, weight=1)
                btn = n.Node(self, column, row, relief="solid", bg=self.map_color, activebackground=self.map_color, bd=2)
                btn.bind("<Button-1>", self.color_trigger)
                btn.bind("<Button-2> ", self.color_trigger)
                btn.bind("<Button-3>", self.color_trigger)
                btn.bind("<Enter> ", self.color)
                btn.grid(row=row, column=column, sticky="nsew")
                self.tmp.append(btn)
            self.map.append(self.tmp)

        # Control Panel
        self.control_panel = tk.Frame(self, bg="white")
        self.control_panel.columnconfigure(0, weight=1)
        self.control_panel.columnconfigure(1, weight=1)
        self.control_panel.columnconfigure(2, weight=1)
        self.control_panel.columnconfigure(3, weight=1)
        self.start_btn = tk.Button(self.control_panel, command=self.start,
                                   relief="solid", text="Start", bd=2, height=3, bg="white")
        self.clear_map_btn = tk.Button(self.control_panel, command=self.clear_map,
                                       relief="solid", text="Clear map", height=3, bd=2, bg="white")
        self.clear_path_btn = tk.Button(self.control_panel, command=self.clear_path,
                                        relief="solid", text="Clear road", height=3, bd=2, bg="white")
        self.context_lbl = tk.Label(self.control_panel, width=8, textvariable=self.context, bg="white")
        self.start_btn.grid(row=0, column=0, sticky="ew")
        self.clear_map_btn.grid(row=0, column=1, sticky="ew")
        self.clear_path_btn.grid(row=0, column=2, sticky="ew")
        self.context_lbl.grid(row=0, column=3, sticky="ew")

        # Start point of map
        self.map[0][0].configure(bg=self.start_color, activebackground=self.start_color)

        # End point of map
        self.map[self.rows - 1][self.columns - 1].configure(bg=self.end_color, activebackground=self.end_color)

        # Control Panel
        self.control_panel.grid(row=self.rows, columnspan=self.columns, sticky="EW")

    def color_trigger(self, event):
        """Method for triggering right color. If scroll is pressed stop coloring map, the left mouse button is used to
        draw walls and the right button is used to clear them. Start and end points cannot be colored or erased"""
        if event.num == 2:
            self.color_flag = False
            self.context.set("Doing nothing")
        else:
            self.color_flag = True
            if event.num == 1:
                self.current_color = self.wall_color
                self.context.set("Drawing walls")
            elif event.num == 3:
                self.current_color = self.map_color
                self.context.set("Clearing walls")

        # Color currently clicked Node, its added because color function works only when you entering Node and not when
        # you are clicking on it.
        if event.widget.cget("bg") != self.start_color and event.widget.cget("bg") != self.end_color:
            event.widget.configure(bg=self.current_color, activebackground=self.current_color)

    def color(self, event):
        """When flag is set, color Node on which mouse is currently hovering on. Start and end points cannot be colored
        or erased"""
        if self.color_flag and event.widget.cget("bg") != self.start_color and event.widget.cget("bg") != self.end_color:
            event.widget.configure(bg=self.current_color, activebackground=self.current_color)

    def clear_map(self):
        """Iterate through whole map and clear every wall"""
        for row in self.map:
            for col in row:
                if col.cget("bg") != self.map_color and col.cget("bg") != self.start_color and col.cget("bg") != self.end_color:
                    col.configure(bg=self.map_color, activebackground=self.map_color)

    def clear_path(self):
        for row in self.map:
            for col in row:
                if col.cget("bg") != self.map_color and col.cget("bg") != self.start_color and col.cget("bg") != self.end_color and col.cget(
                        "bg") != self.wall_color:
                    col.configure(bg=self.map_color, activebackground=self.map_color)

    def start(self):
        """Start algorithm depending on implementation"""
        pass

    def get_neighbours(self, node):
        """Return list of all neighbour nodes for the node called in arguments on map"""
        neighbours = []

        # Column index of node
        col = node.col_pos

        # Row index of node
        row = node.row_pos

        for i_row in range(-1, 2):
            for j_col in range(-1, 2):
                # Check for not adding to list of neighbours the node passed as an argument.
                if i_row == 0 and j_col == 0:
                    continue

                # Indexes of row and column of neighbour, if they are negative that means index will be out of bounds,
                # so ignore them in this case otherwise add them to the list of neighbours.
                neighbour_row = row + i_row
                neighbour_col = col + j_col

                if 0 <= neighbour_row < self.rows and 0 <= neighbour_col < self.columns:
                    neighbours.append(self.map[neighbour_row][neighbour_col])

        return neighbours

    @staticmethod
    def get_distance(node1, node2):
        """Method for calculating distance between 2 nodes on map."""
        return max(abs(node2.col_pos - node1.col_pos), abs(node2.row_pos - node1.row_pos))
