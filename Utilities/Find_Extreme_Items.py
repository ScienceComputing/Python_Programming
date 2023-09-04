# Heap queue algorithm: https://docs.python.org/3/library/heapq.html
# heapq is good for finding a relatively small number of items
import heapq
num_list = [19, 30, 1, 3, 88, -100, 28, 0.5, 2, 12, 0]
print(heapq.nlargest(3, num_list))
print(heapq.nsmallest(3, num_list))

car_inventory = [
    {'make': 'Toyota', 'model': 'Camry', 'year': 2022, 'price': 25000},
    {'make': 'Honda', 'model': 'Civic', 'year': 2021, 'price': 22000},
    {'make': 'Ford', 'model': 'F-150', 'year': 2023, 'price': 35000},
    {'make': 'Chevrolet', 'model': 'Malibu', 'year': 2020, 'price': 20000},
    {'make': 'Tesla', 'model': 'Model 3', 'year': 2023, 'price': 45000},
    {'make': 'BMW', 'model': 'X5', 'year': 2022, 'price': 55000}
]

cheap_car = heapq.nsmallest(3, car_inventory, key=lambda car: car['price'])
expensive_car = heapq.nlargest(3, car_inventory, key=lambda car: car['price'])

# min() and max() is good for finding only one number of items
print(min(num_list))
print(max(num_list))

min_price_car = min(car_inventory, key=lambda car: car['price'])
print("Car with the minimum price:", min_price_car)
max_price_car = max(car_inventory, key=lambda car: car['price'])
print("Car with the maximum price:", max_price_car)

# If we want to find items with the same size as the collection itself
sorted(num_list) # Sort the items in the ascending order; sorted(num_list)[:len(num_list) + 1]
sorted(num_list, reverse=True) # Sort the items in the decending order

# Transform a populated list into a heap
num_heap = list(num_list)
heapq.heapify(num_heap) 
num_heap
heapq.heappop(num_heap)
heapq.heappop(num_heap)
heapq.heappop(num_heap)
heapq.heappop(num_heap)

# A simple bioinformatics scenarior: suppose we have a list of DNA sequences along with their lengths, and we want to find the top N sequences with the longest lengths
sequences = [('ACGT', 4), ('TTAGCA', 6), ('GATC', 4), ('ATCGG', 5), ('AGT', 3)] # Sample data: list of (sequence, length) tuples
top_n_sequences = heapq.nlargest(3, sequences, key=lambda seq: seq[1]) # Find the top 3 sequences with the longest lengths
for seq, length in top_n_sequences:
    print(f"Sequence: {seq}, Length: {length}") # Print the top N sequences

# A more advanced bioinformatics scenarior 1: 
# we first create a larger dataset of sequences and demonstrate the use of a custom class to store the names, contents, and lengths of sequences
# then we find the top N sequences with the longest length
class Sequence:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence
        self.length = len(sequence) # Calculate the length automatically

sequences = [
    Sequence("Sequence1", "ACGT"),
    Sequence("Sequence2", "TTAGCA"),
    Sequence("Sequence3", "GATC"),
    Sequence("Sequence4", "ATCGG"),
    Sequence("Sequence5", "AGT"),
    Sequence("Sequence6", "TATATA"),
    Sequence("Sequence7", "CGATCGAT"),
    Sequence("Sequence8", "AGCTAGCTAGCT"),
    Sequence("Sequence9", "GCGCGCGCGC"),
    Sequence("Sequence10", "CTCTCTCTCT")
]

# Find the top N sequences with the longest lengths
N = 3
top_n_sequences = heapq.nlargest(N, sequences, key=lambda x: x.length)

# Print the top N sequences
print(f"Top {N} Sequences with Longest Lengths:")
for seq in top_n_sequences:
    print(f"Name: {seq.name}, Sequence: {seq.sequence}, Length: {seq.length}")


# A more advanced bioinformatics scenarior 2: 
# we want to work with sequences imported from different FASTA files and find the top N sequences with the longest lengths
import os
import heapq
from Bio import SeqIO

# Define a custom sequence class to store sequence information
class Sequence:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence
        self.length = len(sequence)

# Directory containing your FASTA files
fasta_dir = '/path/to/your/fasta/files/'

# List to store Sequence objects from all FASTA files
all_sequences = []

# Read sequences from all FASTA files in the directory
for filename in os.listdir(fasta_dir):
    if filename.endswith(".fasta") or filename.endswith(".fa"):
        filepath = os.path.join(fasta_dir, filename)
        for record in SeqIO.parse(filepath, "fasta"):
            sequence_name = record.id
            sequence_data = str(record.seq)
            sequence = Sequence(sequence_name, sequence_data)
            all_sequences.append(sequence)

N = 3
top_n_sequences = heapq.nlargest(N, all_sequences, key=lambda x: x.length)

print(f"Top {N} Sequences with Longest Lengths:")
for seq in top_n_sequences:
    print(f"Name: {seq.name}, Sequence: {seq.sequence}, Length: {seq.length}")
