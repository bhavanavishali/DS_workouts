from collections import deque

class Graph:
    def __init__(self):
        self.elements = {}

    def add_vertex(self, vertex):
        if vertex not in self.elements:
            self.elements[vertex] = []

    def add_edges(self, u, v):
        if u not in self.elements:
            self.add_vertex(u)
        if v not in self.elements:
            self.add_vertex(v)
        self.elements[u].append(v)
        self.elements[v].append(u)  # undirected

    def display(self):
        print("Graph adjacency list:")
        for vertex in self.elements:
            print(f"{vertex} -> {self.elements[vertex]}")

    def bfs_recursive(self, queue, visited):
        if not queue:
            return

        current = queue.popleft()
        print(current, end=" ")
        visited.add(current)

        for neighbor in self.elements[current]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

        # Recursive call on the next node in queue
        self.bfs_recursive(queue, visited)


g = Graph()

g.add_edges("A", "B")
g.add_edges("A", "C")
g.add_edges("B", "D")
g.add_edges("C", "E")
g.add_edges("D", "E")
g.add_edges("E", "F")

g.display()

print("\nBFS Traversal using Recursion:")
start_node = "A"
g.bfs_recursive(deque([start_node]), set())
