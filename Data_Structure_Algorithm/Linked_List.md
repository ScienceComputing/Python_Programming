- A linked list is a sequence of data connected through links.
- Each element is a node, containing data and pointer to the next node. The last link points to null.
- The first node is the head, and the final node is the tail.
- Data does not need to be stored in contiguous blocks of memory.
- Data can be located in any available memory address.
- Singly linked list: each node has one link.
- Doubly linked list: each node has two links in either direction.
- Why use linked lists? Implement other data structures like stacks, queues, and graphs. A common application of a linked list is to access information by navigating backward and forward, such as on a web browser or music playlist.

```
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
```

```
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
```
