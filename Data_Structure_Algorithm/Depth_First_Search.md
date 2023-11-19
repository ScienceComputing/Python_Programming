## Tree/graph traversal
- Traversal involves exploring every node in a tree or graph, and this can be achieved using depth-first search or breadth-first search methods. These techniques are applicable to both binary trees and graphs.
- Three methods exist for traversing a binary tree with depth-first search: in-order traversal, pre-order traversal, and post-order traversal.

## In-order traversal
- Traverse the left subtree of the current node, followed by the current node, and finally,the right subtree. Its complexity is $O(n)$ where n is the number of nodes.

```
def in_order(self, current_node):
  if current_node:
    self.in_order(current_node.left_child)
    print(current_node.data)
    self.in_order(current_node.right_child)

tree_1.in_order(tree_1.root)
```

## Pre-order traversal
- Traverse the current node, followed by the left subtree of the current node, and finally,the right subtree. Its complexity is $O(n)$ where n is the number of nodes.
