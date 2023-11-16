## Tree
- Trees are node-based data structures
- Each node can have links to more than one node
- Root: the first node of a tree
- Parent nodes and children nodes
- Trees have levels
- **Binary tree**: each node has 0, 1, or 2 children
- Real applications using trees: 1) file system of a computer; 2) structure of an HTML document; 3) in chess, trees store the possible moves that a rival player can make; 3) search and sort algorithms

```
class TreeNode:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left_children = left
    self.right_children = right

node1 = TreeNode('AT')
node2 = TreeNode('CG')
root_node = TreeNode('N', node1, node2)
```

## Binary search tree
- The left subtree of a node contains only nodes with values less than the node itself, whereas the right subtree contains nodes with values greater than the node
- The left and right subtrees must also be binary search trees

```
class TreeNode:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left_children = left
    self.right_children = right

class BinarySearchTree:
  def __init__self():
    self.root = None
```
