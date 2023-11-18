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
- Used to order the lists efficiently. When adding or removing elements, there is no need to re-order all of them again.
- **Much faster at searching** than arrays and linked lists
- **Much faster at inserting and deleting** than arrays
- [TD] Used to implement advanced data structures: dynamic sets; lookup tables; priority queues

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
```

### Insert
```
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

*The insert() adds a new node to a binary search tree. It creates the new node and, if the tree is empty, sets this node as the root. Otherwise, it traverses the tree, starting from the root, to find the correct position for the new node. During the traversal, it compares the data of the new node with the current node's data. If the new data is less, it moves to the left child; if greater, to the right child. This process continues until it finds an empty spot where it can insert the new node as a left or right child, depending on the data comparison. The insertion process stops once the new node is correctly placed.*

### Delete
- If the node to delete has no children, it is deleted
- If the [node] to delete has one child, it is deleted and its child node is connected with the [node's] parent
- If the node to delete has 2 children, it is replaced with its successor, which is the smallest value greater than the value of the node to delete
  - To find the successor, we visit the right child of the node to delete, and keep visiting the left nodes until the visited node shows the smallest value greater than the value of the node to delete
  - If the successor has a right child, this child becomes the left child of successor's parent
  
