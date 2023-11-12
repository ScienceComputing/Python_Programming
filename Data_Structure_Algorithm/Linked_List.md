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

- The methods of the linked lists, as follows:
- insert_at_beginning()
  ```
  def insert_at_beginning(self, data):
    new_node = Node(data)
    if self.head: # Check if the list is not empty
      new_node.next = self.head # Next -> point to right
      self.head = new_node
    else:
      self.tail = new_node
      self.head = new_node
  ```
- remove_at_beginning()
- insert_at_end()
  ```
  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head: # Check if the list is not empty
      self.tail.next = new_node # Next -> point to right
      self.tail = new_node
    else:
      self.head = new_node
      self.tail = new_node
  ```
- remove_at_end()
- insert_at()
- remove_at()
- search(): search for a value in a LinkedList
  ```
  def search(self, data):
    current_node = self.head()
    while current_node: # Check if the list is not empty
      if current_node.data == data:
        return True
      else:
        current_node = current_node.next # Search from the left most to the right most
    return False
  ```

  - Example
    ```
    Sequencing = LinkedList()
    Sequencing.insert_at_end('TCGA')
    Sequencing.insert_at_end('AAAGGGGG')
    Sequencing.insert_at_beginning('TGCCCN')
    Sequencing.search('TCGA')
    # True
    Sequencing.search('NNNN')
    # False
    ```
