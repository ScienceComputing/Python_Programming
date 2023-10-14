class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, x):
        self.result += x
        return self.result
    def __call__(self, x):
        return self.add(x)
    
# Create an instance of the Calculator class
calculator = Calculator()

# Call the instance like a function
result1 = calculator(5)
print(result1)

result2 = calculator(20)
print(result2) # Output: 25

# Bioinformatics scenarior: suppose we're working with DNA sequences, and we want to create a class that can perform various operations on DNA sequences, such as calculating GC content, finding open reading frames, and translating sequences into proteins. 
# We can make the class instances callable to easily apply these operations
class DNASequenceProcessor:
    def __init__(self, sequence):
        self.sequence = sequence
    def calculate_gc_content(self):
        gc_count = self.sequence.count('G') + self.sequence.count('C')
        total_bases = len(self.sequence)
        return (gc_count / total_bases) * 100
    def find_orfs(self):
        orf_indices = [(10, 100), (200, 300)]
        return orf_indices
    def translate_to_protein(self):
        codon_table = {
            'TCA': 'S',    # Serina
            'TCC': 'S',    # Serina
            'TCG': 'S',    # Serina
            'TCT': 'S',    # Serina
            'TTC': 'F',    # Fenilalanina
            'TTT': 'F',    # Fenilalanina
            'TTA': 'L',    # Leucina
            'TTG': 'L',    # Leucina
            'TAC': 'Y',    # Tirosina
            'TAT': 'Y',    # Tirosina
            'TAA': '*',    # Stop
            'TAG': '*',    # Stop
            'TGC': 'C',    # Cisteina
            'TGT': 'C',    # Cisteina
            'TGA': '*',    # Stop
            'TGG': 'W',    # Triptofano
            'CTA': 'L',    # Leucina
            'CTC': 'L',    # Leucina
            'CTG': 'L',    # Leucina
            'CTT': 'L',    # Leucina
            'CCA': 'P',    # Prolina
            'CCC': 'P',    # Prolina
            'CCG': 'P',    # Prolina
            'CCT': 'P',    # Prolina
            'CAC': 'H',    # Histidina
            'CAT': 'H',    # Histidina
            'CAA': 'Q',    # Glutamina
            'CAG': 'Q',    # Glutamina
            'CGA': 'R',    # Arginina
            'CGC': 'R',    # Arginina
            'CGG': 'R',    # Arginina
            'CGT': 'R',    # Arginina
            'ATA': 'I',    # Isoleucina
            'ATC': 'I',    # Isoleucina
            'ATT': 'I',    # Isoleucina
            'ATG': 'M',    # Methionina
            'ACA': 'T',    # Treonina
            'ACC': 'T',    # Treonina
            'ACG': 'T',    # Treonina
            'ACT': 'T',    # Treonina
            'AAC': 'N',    # Asparagina
            'AAT': 'N',    # Asparagina
            'AAA': 'K',    # Lisina
            'AAG': 'K',    # Lisina
            'AGC': 'S',    # Serina
            'AGT': 'S',    # Serina
            'AGA': 'R',    # Arginina
            'AGG': 'R',    # Arginina
            'GTA': 'V',    # Valina
            'GTC': 'V',    # Valina
            'GTG': 'V',    # Valina
            'GTT': 'V',    # Valina
            'GCA': 'A',    # Alanina
            'GCC': 'A',    # Alanina
            'GCG': 'A',    # Alanina
            'GCT': 'A',    # Alanina
            'GAC': 'D',    # Acido Aspartico
            'GAT': 'D',    # Acido Aspartico
            'GAA': 'E',    # Acido Glutamico
            'GAG': 'E',    # Acido Glutamico
            'GGA': 'G',    # Glicina
            'GGC': 'G',    # Glicina
            'GGG': 'G',    # Glicina
            'GGT': 'G'     # Glicina
        }
        protein = []
        for i in range(0, len(self.sequence), 3):
            codon = self.sequence[i:i+3]
            amino_acid = codon_table.get(codon, 'X')  # X for unknown codons
            protein.append(amino_acid)
        return ''.join(protein)
    def __call__(self, operation):
        if operation == 'gc_content':
            return self.calculate_gc_content()
        elif operation == 'find_orfs':
            return self.find_orfs()
        elif operation == 'translate':
            return self.translate_to_protein()
        else:
            raise ValueError("Unsupported operation")
        
# Create an instance of DNASequenceProcessor
sequence = "ATGGCTTACGGTAGCTAGCTAGTAA"
sequence_processor = DNASequenceProcessor(sequence)

# Call the instance like a function to perform sequence operations
gc_content = sequence_processor('gc_content')
print(f"GC Content: {gc_content:.2f}%")

orfs = sequence_processor('find_orfs')
print("ORF Indices:", orfs)

protein = sequence_processor('translate')
print("Translated Protein Sequence:", protein)
