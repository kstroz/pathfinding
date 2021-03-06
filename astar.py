import map as m
from tkinter import messagebox as mbox


class AStar(m.Map):
    def __init__(self, *args, **kwargs):
        m.Map.__init__(self, *args, **kwargs)

    def start(self):
        """A* algorithm implementation"""
        # Change each node parameter and color to starting ones.
        self.clear_path()

        # Start point
        start = self.map[0][0]

        # End point
        goal = self.map[self.rows - 1][self.columns - 1]

        # Nodes that have been visited but not expanded
        open_nodes = []

        # Starting node
        start.g_cost = 0
        open_nodes.append(start)

        while len(open_nodes) > 0:
            current = open_nodes[0]
            for node in open_nodes:
                if current.f_cost() > node.f_cost():
                    current = node

            # If current checking node is goal then break loop and start method for visualizing path.
            if current == goal:
                self.retrace_path(start, goal)
                break

            open_nodes.remove(current)

            for neighbour in self.get_neighbours(current):
                tentative_score = current.g_cost + m.Map.get_distance(neighbour, current)
                if tentative_score < neighbour.g_cost:
                    neighbour.parent = current
                    neighbour.g_cost = tentative_score
                    neighbour.h_cost = m.Map.get_distance(neighbour, goal)

                    if neighbour not in open_nodes and neighbour.cget("bg") != self.wall_color:
                        if neighbour.cget("bg") != self.start_color and neighbour.cget("bg") != self.end_color:
                            self.after(self.reload_time, neighbour.configure(bg=self.neighbour_color,
                                                                             activebackground=self.neighbour_color))

                        open_nodes.append(neighbour)
            self.update_idletasks()
        else:
            mbox.showerror("Error", "There is no path from starting node to end node.")

    def retrace_path(self, start, end):
        """Function for drawing  path by retracting it from by to start by parent of each node."""
        path = []
        current_node = end
        while current_node != start:
            path.append(current_node)
            current_node = current_node.parent

        path.reverse()
        for node in path[0:len(path) - 1]:
            self.after(self.reload_time, node.configure(bg=self.path_color, activebackground=self.path_color))
            self.update_idletasks()
