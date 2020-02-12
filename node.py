import tkinter as tk


class Node(tk.Button):
    def __init__(self, parent, col_pos, row_pos, *args, **kwargs):
        tk.Button.__init__(self, parent, *args, **kwargs)
        self.col_pos = col_pos
        self.row_pos = row_pos
