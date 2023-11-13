- Last-In-First-Out: the last inserted item will be the first item to be removed
```
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None # No node at the top of the stack
    self.size = 0 # Zero elements in the stack

  def push(self, data):
    new_node = Node(data) # Create a node with the data
    if self.top:
      new_node.next = self.top
    self.top = new_node # Set the new node as the top node
    self.size += 1 # Update the size of the stack by one
```
