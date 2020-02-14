import tkinter as tk


class Node(tk.Button):
    def __init__(self, parent, col_pos, row_pos, *args, **kwargs):
        tk.Button.__init__(self, parent, *args, **kwargs)

        # Position of node on map
        self.col_pos = col_pos
        self.row_pos = row_pos

        # Distance from starting node
        self.g_cost = 10000

        # Distance from end node
        self.h_cost = 0

        # Parent of this node
        self.parent = None

    def f_cost(self):
        """Return sum of g cost and h cost"""
        return self.g_cost + self.h_cost
