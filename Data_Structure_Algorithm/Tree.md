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

def search(self, search_value):
  current_node = self.root
  while current_node:
    if search_value == current_node.data:
      return True
    elif search_value < current_node.data
      current_node = current_node.left_child
    else:
      current_node = current_node.right_child
  return False

def insert(self, data):
    new_node = TreeNode(data)
    if self.root == None:
        self.root = new_node
        return # Finish the execution
    else:
        current_node = self.root
        while True: # Iterate until the new_node is inserted
            if data < current_node.data:
                if current_node.left_child == None:
                    current_node.left_child = new_node
                    return
                else:
                    current_node = current_node.left_child
            elif data > current_node.data:
                if current_node.right_child == None:
                    current_node.right_child = new_node
                    return
                else:
                    current_node = current_node.right_child

```
*The insert() adds a new node to a binary search tree. It begins by creating a new node with the given data. If the tree is currently empty (i.e., the root is None), it sets the new node as the root. Otherwise, it traverses the tree, starting from the root, to find the correct position for the new node. During the traversal, it compares the data of the new node with the current node's data. If the new data is less, it moves to the left child; if greater, to the right child. This process continues until it finds an empty spot where it can insert the new node as a left or right child, depending on the data comparison. The function ends once the new node is inserted.*
