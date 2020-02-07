import tkinter as tk
import astar as a


class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.astar = a.AStar(self, width=20, height=20, bg='white')
        self.astar.pack(side="left", fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pathfinding")
    root.geometry("800x800")
    Main(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
