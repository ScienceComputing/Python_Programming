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
