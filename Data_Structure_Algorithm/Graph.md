- A graph is a data structure formed by a set of nodes (vertices)
- Nodes are connected by links (edges)
- Trees are a type of graph
- Directed and undirected graphs: the relationship between 2 nodes is mutual
- Weighted graphs: numeric values associated with the edges; can be directed or undirected
- Tree vs graph:
  - Trees cannot have cycles: each node cannot reference each other circularly
  - Trees require that all nodes must be connected
- Real application: 1) social networks; 2) drug-drug interaction; 3) location and distance; 4) graph database; 5) search and sort algorithm
```
class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex] = []
    def add_edge(self, source, target):
        self.vertices[source].append(target)

my_graph = Graph()
my_graph.add_vertex('Ann')
my_graph.add_vertex('Ho')
my_graph.add_vertex('Varasa')

my_graph.add_edge('Ann', 'Varasa')
my_graph.add_edge('Ann', 'Ho')
my_graph.add_edge('Ho', 'Varasa')

print(my_graph.vertices)
# {'Ann': ['Varasa', 'Ho'], 'Ho': ['Varasa'], 'Varasa': []}

```
