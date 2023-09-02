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

# Bioinformatics scenarior: parse large genomic data files
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
