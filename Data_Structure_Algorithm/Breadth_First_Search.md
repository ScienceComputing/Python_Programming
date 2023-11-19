## Breadth first search - binary tree
- Breadth first search initiates from the root and thoroughly explores all nodes at each level of the tree before progressing to the subsequent level. Its complexity is $O(n)$.

```
import queue

def bfs(self):
    if self.root:
        visited_nodes = []
        bfs_queue = queue.SimpleQueue()
        bfs_queue.put(self.root)
        while not bfs_queue.empty():
            current_node = bfs_queue.get()
            visited_nodes.append(current_node.data)
            if current_node.left:
                bfs_queue.put(current_node.left)
            if current_node.right:
                bfs_queue.put(current_node.right)
        return visited_nodes
```

## Breadth first search - graph
- As graphs have cycles, we need to check if the vertices have already been visited. Its complexity is $O(V + E)$, where V is the number of vertices and E is the number of edges.

```
import queue

def bfs(graph, initial_vertex):
    visited_vertices = []
    bfs_queue = queue.SimpleQueue()
    bfs_queue.put(initial_vertex)
    visited_vertices.append(initial_vertex)
    while not bfs_queue.empty():
        current_vertex = bfs_queue.get()
        for adjacent_vertex in graph[current_vertex]:
            if adjacent_vertex not in visited_vertices:
                visited_vertices.append(adjacent_vertex)
                bfs_queue.put(adjacent_vertex)
    return visited_vertices
```

```
# Search for a given vertex within a graph; vertex in this case is a genetic variant
import queue

def bfs(graph, initial_vertex, search_value):
  visited_vertices = []
  bfs_queue = queue.SimpleQueue()
  visited_vertices.append(initial_vertex)
  bfs_queue.put(initial_vertex)
  while not bfs_queue.empty():
    current_vertex = bfs_queue.get()
    if current_vertex == search_value:
      return True    
    for adjacent_vertex in graph[current_vertex]:
      if adjacent_vertex not in visited_vertices:
        visited_vertices.append(adjacent_vertex)
        bfs_queue.put(adjacent_vertex)
  return False

graph = {
    'Variant1': ['Variant2', 'Variant3'],
    'Variant2': ['Variant1', 'Variant4', 'Variant5'],
    'Variant3': ['Variant1', 'Variant6'],
    'Variant4': ['Variant2'],
    'Variant5': ['Variant2', 'Variant6'],
    'Variant6': ['Variant3', 'Variant5']
}
print(bfs(graph, 'Variant1', 'Variant5'))
# True
```

## Breadth first search vs depth first search
Breadth first search is suitable for targets closer to the starting vertex and is used in applications like web crawling, finding the shortest path in unweighted graphs, locating connected places via GPS, and as a component in more complex algorithms. In contrast, depth first search is better for targets that are far from the starting vertex and is applied in solving puzzles that have a single solution, like mazes, detecting cycles in graphs, finding the shortest path in weighted graphs, and also as part of more sophisticated algorithms.
