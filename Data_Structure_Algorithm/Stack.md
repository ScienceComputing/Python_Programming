Last-In-First-Out: the last inserted item will be the first item to be removed

The following `push` and `pop` algorithms have $O(1)$ complexity.
```
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None # No node at the top of the stack
    self.size = 0 # Zero elements in the stack

  # Push an element onto a stack using singly linked lists
  def push(self, data):
    new_node = Node(data) # Create a node with the data
    if self.top:
      new_node.next = self.top
    self.top = new_node # *Set the new node as the top node
    self.size += 1 # Update the size of the stack by one

  # Pop an element from a stack using singly linked lists
  def pop(self):
    if self.top is None: # Check if there is a top element
      return None
    else:
      popped_node = self.top
      self.size -= 1 # Decrement the size of the stack
      self.top = self.top.next # Update the top node with the next node
      popped_node.next = None
      return popped_node.data 
```

Quick way: use the LifeQueue
```
import queue
book_stack = queue.LifoQueue(maxsize=0) # Create an infinite LifoQueue; maxsize = 0 -> the stack will be infinite.
book_stack.put('Olga Dies Dreaming') # Add an element to the stack
book_stack.qsize() # Check the number of elements in the stack
book_stack.get() # Remove an element from the stack
book_stack.empty() # Check if the stack has zero element
```
