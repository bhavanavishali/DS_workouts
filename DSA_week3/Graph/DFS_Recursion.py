class Graph:
    def __init__(self):
        self.elements = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.elements:
            self.elements[vertex] = []
            
    def add_edges(self, v, u):
        if v not in self.elements:
            self.add_vertex(v)
        if u not in self.elements:
            self.add_vertex(u)
            
        self.elements[u].append(v)
        self.elements[v].append(u)
        
    def display(self):
        for vertex in self.elements:
            print(f"{vertex} -> {self.elements[vertex]}")
            
    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = set()

        print(start, end=' ')
        visited.add(start)

        for neighbour in self.elements[start]:
            if neighbour not in visited:
                self.dfs_recursive(neighbour, visited)

g = Graph()
g.add_edges("A", "B")
g.add_edges("A", "C")
g.add_edges("A", "E")
g.add_edges("B", "E")
g.add_edges("D", "F")
g.display()

print("\nTraversal Starting from A:")
g.dfs_recursive("A")
