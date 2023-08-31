list_instance = [7, 8, 2, 1, 6, 9]
iterator_1 = iter(list_instance)
iterator_2 = iter(list_instance)
print(f"A: {next(iterator_1)}")
print(f"A: {next(iterator_1)}")
print(f"A: {next(iterator_1)}")
print(f"A: {next(iterator_1)}")
print(f"B: {next(iterator_2)}")

# Bioinformatics scenarior: define multiple iterators to iterate over different aspects of a sequence, such as nucleotides and codons.
class BioSequenceIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.sequence):
            nucleotide = self.sequence[self.index]
            self.index += 1
            return nucleotide
        else:
            raise StopIteration

class CodonIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.sequence) - 2:
            codon = self.sequence[self.index:self.index + 3]
            self.index += 3
            return codon
        else:
            raise StopIteration

# Example usage:
dna_sequence = "TTGACCGAGCTAGCTGA"

# Iterate over individual nucleotides
nucleotide_iterator = BioSequenceIterator(dna_sequence)
for nucleotide in nucleotide_iterator:
    print(f"Nucleotide: {nucleotide}")

# Iterate over codons
codon_iterator = CodonIterator(dna_sequence)
for codon in codon_iterator:
    print(f"Codon: {codon}")
print(f"Codon: {next(codon_iterator)}")
print(f"Codon: {next(codon_iterator)}")
print(f"Codon: {next(codon_iterator)}")
print(f"Codon: {next(codon_iterator)}")
print(f"Codon: {next(codon_iterator)}")
print(f"Codon: {next(codon_iterator)}")
