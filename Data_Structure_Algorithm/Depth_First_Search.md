## Tree/graph traversal
- Traversal involves exploring every node in a tree or graph, and this can be achieved using depth-first search or breadth-first search methods. These techniques are applicable to both binary trees and graphs.
- Three methods exist for traversing a binary tree with depth-first search: in-order traversal, pre-order traversal, and post-order traversal.

## Depth first search - binary tree
### In-order traversal
- Traverse the left subtree of the current node, followed by the current node, and finally, the right subtree. Its complexity is $O(n)$ where n is the number of nodes.
- In-order traversal is commonly used in binary search trees to obtain the nodes' values in ascending order. 

```
def in_order(self, current_node):
  if current_node:
    self.in_order(current_node.left_child)
    print(current_node.data)
    self.in_order(current_node.right_child)

tree_1.in_order(tree_1.root)
```

### Pre-order traversal
- Traverse the current node, followed by the left subtree of the current node, and finally, the right subtree. Its complexity is $O(n)$ where n is the number of nodes.
- Pre-order is used to create copies of a binary tree and get prefix expressions.

```
def pre_order(self, current_node):
  if current_node:
    print(current_node.data)
    self.pre_order(current_node.left_child)
    self.pre_order(current_node.right_child)

tree_1.pre_order(tree_1.root)
```

### Post-order traversal
- Traverse the left subtree of the current node, followed by the right subtree, and finally, the current node. Its complexity is $O(n)$ where n is the number of nodes.
- Post-order is used to delete binary trees and get postfix expressions.


## Depth first search - graph
- As graphs have cycles, we need to keep track of which vertices have been visited.
- Algorithm: 1) start at any vertex; 2) tracks the current vertex in a list; 3) for each current node's adjacent vertex, if it has been visited, we ignore, but if it hasn't been visited, we recursively perform depth first search.
