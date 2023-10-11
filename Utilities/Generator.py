# List comprehension returns a list; while the generator returns a generator object
# Both can be iterated over
[2 * num for num in range(5)]
(2 * num for num in range(5)) # Create a generator

num_gen = (2 * num for num in range(5))
for num in num_gen:
    print(num)  

print(list(num_gen)) # Convert the generator a list

# Lazy evaluation whereby the evaluation of the expression is delayed until its value is needed.
# We prefer the generator when working with extremely large sequences, as we don't want to store the entire list in memory, which is what comprehensions would do. We want to generate elements of the sequence on the fly.
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))

[2 * num for num in range(2 ** 10000000000)]
(2 * num for num in range(2 ** 10000000000)]

 # Conditionals in the generator
aa = ['histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'phenylalanine', 'threonine', 'tryptophan', 'valine']
aa_target = (x for x in aa if "t" in x)
print(list(aa_target))

# Build the generator function that produces the generator objects when called. 
# This function yields a sequence of values instead of returning a single value, using the keyword `yield`.
def yield_multiple_items():
    yield "The 1st item"
    yield "The 2nd item"  
    yield "The 3rd item"
    yield "The last item. Do not call next again."
example = yield_multiple_items()
print(next(example))
print(next(example))
print(next(example))
print(next(example))
print(next(example))

def num_sequence(n):
    """Generate values from 0 to n."""
    i = 0
    while i < n:
        yield i
        i += 1

result = num_sequence(7)
print(type(result)) # <class 'generator'>
for item in result:
    print(item)

# Bioinformatics scenarior: parse a very large genomic data file
def parse_fasta(file_path):
    with open(file_path, 'r') as fasta_file:
        sequence = ""
        for line in fasta_file:
            if line.startswith(">"): 
                if sequence:
                    yield sequence # Yield the previously read sequence
                    sequence = ""
            else:
                sequence += line.strip() # Concatenate lines of the sequence with leading and trailing whitespace removed
        if sequence:
            yield sequence # Yield the last sequence in the file

# Usage example
fasta_file_path = "large_genomic_data.fasta"
sequences = parse_fasta(fasta_file_path)

# Process sequences one by one using next()
try:
    while True:
        sequence = next(sequences)
        print("Processing sequence:", sequence[:20], "...")
except StopIteration:
    print("Finished processing all sequences.")
