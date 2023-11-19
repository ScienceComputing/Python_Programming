## Tree/graph traversal
- Traversal involves exploring every node in a tree or graph, and this can be achieved using depth-first search or breadth-first search methods. These techniques are applicable to both binary trees and graphs.
- Three methods exist for traversing a binary tree with depth-first search: in-order traversal, pre-order traversal, and post-order traversal.

## Depth first search - binary tree
Expression trees are a kind of binary tree that represent arithmetic expressions.

### In-order traversal
- Traverse the left subtree of the current node, followed by the current node, and finally, the right subtree (left -> current -> right). Its complexity is $O(n)$ where n is the number of nodes.
- In-order traversal is commonly used in binary search trees to obtain the nodes' values in ascending order. 

```
def in_order(self, current_node):
  if current_node:
    self.in_order(current_node.left_child)
    print(current_node.data)
    self.in_order(current_node.right_child)

tree_1.in_order(tree_1.root)
```

```
class BinarySearchTree:
  def __init__(self):
    self.root = None

  def in_order(self, current_node):
    if current_node:
      self.in_order(current_node.left_child)
      print(current_node.data)
      self.in_order(current_node.right_child)
```

### Pre-order traversal
- Traverse the current node, followed by the left subtree of the current node, and finally, the right subtree (current -> left -> right). Its complexity is $O(n)$ where n is the number of nodes.
- Pre-order is used to create copies of a binary tree and get prefix expressions.

```
def pre_order(self, current_node):
  if current_node:
    print(current_node.data)
    self.pre_order(current_node.left_child)
    self.pre_order(current_node.right_child)

tree_1.pre_order(tree_1.root)
```

```
import queue

class ExpressionTree:
  def __init__(self):
    self.root = None

  def pre_order(self, current_node):
    if current_node:
      print(current_node.data)
      self.pre_order(current_node.left_child)
      self.pre_order(current_node.right_child)
```

### Post-order traversal
- Traverse the left subtree of the current node, followed by the right subtree, and finally, the current node (left -> right -> current). Its complexity is $O(n)$ where n is the number of nodes.
- Post-order is used to delete binary trees and get postfix expressions.


## Depth first search - graph
- As graphs have cycles, we need to keep track of which vertices have been visited.
- Algorithm: 1) start at any vertex; 2) tracks the current vertex in a visited vertices list; 3) for each current node's adjacent vertex, if it has been visited, we ignore, but if it hasn't been visited, we recursively perform depth first search.
- Its complexity is $O(V + E)$, where V is the number of vertices, and the E is the number of edges.

```
def dfs(visited_vertices, graph, current_vertex):
    if current_vertex not in visited_vertices:
        print(current_vertex)
        visited_vertices.add(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            dfs(visited_vertices, graph, adjacent_vertex)
```
