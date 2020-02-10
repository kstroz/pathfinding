import tkinter as tk
import map as m


class AStar(m.Map):
    def __init__(self, *args, **kwargs):
        m.Map.__init__(self, *args, **kwargs)

    def start(self):
        """A* algorithm implementation"""
        print("Starting A* algorithm")
