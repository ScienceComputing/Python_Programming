import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = [] # Initialize an empty list to store the items in the priority queue
        self._index = 0 # Initialize an index counter to maintain item order
    def push(self, item, priority):
        # Push an item into the priority queue with its priority
        # The priority is negated to simulate a max-heap (higher priority means a smaller value in the heap)
        # _index is used to ensure that items with the same priority are processed in the order they were added
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1] # Return the actual item, which is the third element of the tuple

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)


queue_1 = []
heapq.heappush(queue_1, (-1, 0, "Foo"))
queue_1 # [(-1, 0, 'Foo')]
heapq.heappop(queue_1)[-1] # (-1, 0, 'Foo')[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name) # Return a string in the format 

repr(Item("Tesla"))

x = PriorityQueue()
x.push(Item('Tesla'), 1)
x.push(Item('Aston Martin'), 1)
x.push(Item('Toyota Corolla'), 2)
x.pop() # Item('Toyota Corolla')
x.pop() # Item('Tesla')
x.pop() # Item('Aston Martin')

# Bioinformatics scenarior: determine the order of DNA nucleotides based on the quality scores
class GenomeQueue:
    def __init__(self):
        self._queue = []  # Initialize a priority queue to manage tasks
        self._index = 0   # Initialize an index counter to maintain task order
    def add_sequence(self, sequence, quality_score):
        # Add a DNA sequence to the assembly queue with a priority based on quality score
        # Higher quality scores are given higher priority (negate the score for max-heap behavior)
        heapq.heappush(self._queue, (-quality_score, self._index, sequence))
        self._index += 1
    def process_next_sequence(self):
        # Process the next highest-quality sequence
        if self._queue:
            _, _, sequence = heapq.heappop(self._queue)
            return sequence
        else:
            return None # if next_sequence is None

# Example usage:
genome_queue = GenomeQueue()

# Add DNA sequences with associated quality scores to the queue
genome_queue.add_sequence("AGCTAGCTAGCT", 90)
genome_queue.add_sequence("TTAGCGCTAGTA", 85)
genome_queue.add_sequence("CTAGCTAGCTAG", 95)

# Process sequences based on priority (highest quality first)
while True:
    next_sequence = genome_queue.process_next_sequence()
    if next_sequence is None:
        break
    print("Processing sequence:", next_sequence)
