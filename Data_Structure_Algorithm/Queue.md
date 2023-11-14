- First-In First-Out: first inserted item is the first to be removed
- Head and tail: the beginning and the end of the queue
- Enqueue: as in stacks, the item can only be inserted at the end of the queue
- Dequeue: unlike stacks, the item can only removed from the head of the queue
- Other types of queues: doubly ended queues; circular queues; priority queues
- Applications: 1) printing task; 2) applications where the order of requests matters (e.g., concert ticket; taxi service)

```
class Node:
  def __init_(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None

def enqueue(self, data):
  new_node = Node(data)
  if self.head == None:
    self.head = new_node
    self.tail = new_node
  else:
    self.tail.next = new_node # The tail's next pointer points to the new_node
    self.tail = new_node

def dequeue(self):
  if self.head:
    current_node = self.head
    self.head = current_node.next
    current_node.next = None

    if self.head == None:
      self.tail = None
```

```
# Use the Queue or SimpleQueue classes from the module queue
import queue
order_queue = queue.SimpleQueue() # Create a SimpleQueue
order_queue.put('Apple Pie') # Add an element to the queue
order_queue.qsize() # Check the number of elements in the queue
order_queue.get() # Remove an element from the queue
order_queue.empty() # Check if the queue has zero element
```
