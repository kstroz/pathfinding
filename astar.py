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

        # Start point of map
        self.grid_slaves(0, 0)[0].configure(bg="green", activebackground="green")

        # End point of map
        self.grid_slaves(self.width - 1, self.height - 1)[0].configure(bg="red", activebackground="red")

    def color_trigger(self, event):
        """Method for triggering right color. If scroll is pressed stop coloring map, the left mouse button is used to
        draw walls and the right button is used to clear them. Start and end points cannot be colored or erased"""
        if event.num == 2:
            self.color_flag = False
        else:
            self.color_flag = True
            if event.num == 1:
                self.current_color = "black"
            elif event.num == 3:
                self.current_color = "white"

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
