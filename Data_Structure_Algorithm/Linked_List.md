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
    self.data = data # Alternatively, self.value = data
    self.next = None
```

```
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
```

- The methods of the linked lists, as follows:
- insert_at_beginning() - this is $O(1)$ complexity
  ```
  def insert_at_beginning(self, data):
    new_node = Node(data)
    if self.head: # Check if the list is not empty = check whether the linked list has a head node
      new_node.next = self.head # Point the next node to the head
      self.head = new_node
    else:
      self.tail = new_node
      self.head = new_node
  ```
- remove_at_beginning()
  ```
  def remove_at_beginning(self):
    self.head = self.head.next # The "next" node of the head becomes the new head
  ```
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
  ```
  def remove_at_end(self):
    # If the list is empty, there's nothing to remove
    if not self.head:
        return

    # If the list has only one element
    if self.head == self.tail:
        self.head = None
        self.tail = None
        return

    # Traverse the list to find the second-to-last node
    current = self.head
        while current.next != self.tail:
          current = current.next
  
        # Remove the last node
        current.next = None
        self.tail = current
  ```
- insert_at()
  ```
  class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at(self, index, data):
        new_node = Node(data)

        # Case 1: Inserting at the beginning
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            # If the list was empty, update the tail as well
            if self.tail is None:
                self.tail = new_node
            return

        # Case 2: Inserting at an index greater than 0
        current = self.head
        position = 0

        while current is not None and position < index - 1:
            current = current.next
            position += 1

        # If the index is out of bounds
        if current is None:
            print("Index out of bounds")
            return

        # Inserting the new node
        new_node.next = current.next
        current.next = new_node

        # Case 3: Update tail if inserting at the end
        if new_node.next is None:
            self.tail = new_node

  ```
- remove_at()
  ```
  class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove_at(self, index):
        # If the list is empty or index is negative
        if not self.head or index < 0:
            print("Index out of range")
            return

        # Case 1: Removing the first node
        if index == 0:
            self.head = self.head.next
            # If the list becomes empty, update the tail
            if not self.head:
                self.tail = None
            return

        # Case 2: Removing a node from a position other than the first
        current = self.head
        position = 0

        # Traverse the list to find the node before the one to be removed
        while current is not None and position < index - 1:
            current = current.next
            position += 1

        # If the index is out of bounds or points to the last node
        if current is None or current.next is None:
            print("Index out of range")
            return

        # Remove the node
        current.next = current.next.next

        # Case 3: Update tail if removing the last node
        if current.next is None:
            self.tail = current

  ```
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
