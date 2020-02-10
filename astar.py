import tkinter as tk


class AStar(tk.Frame):
    def __init__(self, parent, width, height, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # Variables for declaring how big generated map will be
        self.width = width
        self.height = height

        # Variables for declaring which color is currently used and if cursor should color Nodes at all
        self.current_color = "white"
        self.color_flag = False

        # Variable for context
        self.context = tk.StringVar(value="Doing nothing")

        # Create map with size of x == width and y == height, weights are used to make this map responsive for all
        # resizing user is doing with the main window
        for row in range(self.width):
            self.rowconfigure(row, weight=1)
            for column in range(self.height):
                self.columnconfigure(column, weight=1)
                btn = tk.Button(self, relief="solid", bg="white", activebackground="white", bd=2)
                btn.bind("<Button-1>", self.color_trigger)
                btn.bind("<Button-2> ", self.color_trigger)
                btn.bind("<Button-3>", self.color_trigger)
                btn.bind("<Enter> ", self.color)
                btn.grid(row=row, column=column, sticky="nsew")

        # Control Panel
        self.control_panel = tk.Frame(self, bg="white")
        self.control_panel.columnconfigure(0, weight=1)
        self.control_panel.columnconfigure(1, weight=1)
        self.control_panel.columnconfigure(2, weight=1)
        self.start_btn = tk.Button(self.control_panel, relief="solid", text="Start", bd=2, bg="white")
        self.context_lbl = tk.Label(self.control_panel, textvariable=self.context, bg="white")
        self.clear_btn = tk.Button(self.control_panel, relief="solid", text="Clear map", bd=2, bg="white")
        self.start_btn.grid(row=0, column=0, sticky="ew")
        self.context_lbl.grid(row=0, column=1, sticky="ew")
        self.clear_btn.grid(row=0, column=2, sticky="ew")

        # Start point of map
        self.grid_slaves(0, 0)[0].configure(bg="green", activebackground="green")

        # End point of map
        self.grid_slaves(self.width - 1, self.height - 1)[0].configure(bg="red", activebackground="red")

        # Control Panel
        self.control_panel.grid(row=20, columnspan=20, sticky="EW")

    def color_trigger(self, event):
        """Method for triggering right color. If scroll is pressed stop coloring map, the left mouse button is used to
        draw walls and the right button is used to clear them. Start and end points cannot be colored or erased"""
        if event.num == 2:
            self.color_flag = False
            self.context.set("Doing nothing")
        else:
            self.color_flag = True
            if event.num == 1:
                self.current_color = "black"
                self.context.set("Drawing walls")
            elif event.num == 3:
                self.current_color = "white"
                self.context.set("Clearing walls")

        # Color currently clicked Node, its added because color function works only when you entering Node and not when
        # you are clicking on it.
        if event.widget.cget("bg") != "green" and event.widget.cget("bg") != "red":
            event.widget.configure(bg=self.current_color)
            event.widget.configure(activebackground=self.current_color)

    def color(self, event):
        """When flag is set, color Node on which mouse is currently hovering on. Start and end points cannot be colored
        or erased"""
        if self.color_flag and event.widget.cget("bg") != "green" and event.widget.cget("bg") != "red":
            event.widget.configure(bg=self.current_color)
            event.widget.configure(activebackground=self.current_color)
