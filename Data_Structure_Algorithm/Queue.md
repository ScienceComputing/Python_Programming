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

def enqueue(self, data): # O(1) complexity
  new_node = Node(data)
  if self.head == None:
    self.head = new_node
    self.tail = new_node
  else:
    self.tail.next = new_node # The tail's next pointer points to the new_node
    self.tail = new_node

def dequeue(self): # O(1) complexity
  if self.head:
    current_node = self.head
    self.head = current_node.next
    current_node.next = None

    if self.head == None:
      self.tail = None

def has_elements(self):
  return self.head != None
```

```
# Real application
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
  def enqueue(self, data): # O(1) complexity
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node # The tail's next pointer points to the new_node
      self.tail = new_node
  def dequeue(self): # O(1) complexity
    if self.head:
      current_node = self.head
      self.head = current_node.next
      current_node.next = None
      if self.head == None:
        self.tail = None
      return current_node.data
    return None
  def has_elements(self):
    return self.head != None

class print_seq:
  def __init__(self):
    self.queue = Queue()
  def add_base(self, base):
    self.queue.enqueue(base) # Add the base to the queue
  def print_base(self):
    while self.queue.has_elements(): # Iterate over the queue while it has elements
      print("Printing", self.queue.dequeue()) # Remove the base from the queue

seq = print_seq()
# Add some bases to seq
seq.add_base('ACTG')
seq.add_base('TTTTTTT')
seq.add_base('GGGCC')

# Print all the bases in the queue
seq.print_base()
# Printing ACTG
# Printing TTTTTTT
# Printing GGGCC
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
