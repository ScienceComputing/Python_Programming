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
```
