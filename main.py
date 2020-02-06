import tkinter as tk


class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pathfinding")
    root.geometry("800x800")
    Main(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
