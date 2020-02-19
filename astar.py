import tkinter as tk
import map as m


class AStar(m.Map):
    def __init__(self, *args, **kwargs):
        m.Map.__init__(self, *args, **kwargs)

    def start(self):
        """A* algorithm implementation"""
        # Change each node parameter to starting one
        self.clear_path()

        for row in self.map:
            for node in row:
                node.g_cost = 10000
                node.h_cost = 0
                node.parent = None

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

                    if neighbour not in open_nodes and neighbour.cget("bg") != "black":
                        open_nodes.append(neighbour)
        else:
            print("No possible path.")

    def retrace_path(self, start, end):
        """Function for drawing  path by retracting it from by to start by parent of each node."""
        path = []
        current_node = end
        while current_node != start:
            path.append(current_node)
            current_node = current_node.parent

        path.reverse()
        for node in path[0:len(path) - 1]:
            self.after(10, node.configure(bg="blue", activebackground="blue"))
            self.update_idletasks()
