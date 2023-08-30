from collections import deque
def search(lines, pattern, history=6): 
    old_lines = deque(maxlen=history) 
    for line in lines:
        if pattern in line:
            yield line, old_lines 
        old_lines.append(line)

with open('sequence_read.fasta') as f:
    for line, old_lines in search(f, 'ATCCCCGGGGTTTTT', 6): 
        for oline in old_lines:
            print(oline, end='') 
        print(line, end='') 
        print('-'*20)

# Bioinformatics senarior 1: calculate the moving average of the quality scores of base calls in DNA sequencing
# Adding items from either end of a queue has O(1) complexity. Whereas in a list, inserting items from the front of the list is O(N).
def calculate_moving_average(seq, window_size):
    moving_average = deque()
    window = deque(maxlen=window_size)
    for value in seq:
        window.append(value)
        if len(window) == window_size:
            avg = sum(window) / window_size
            moving_average.append(avg)
    return moving_average

# Example usage:
quality_scores = [30, 40, 25, 35, 45, 20, 30, 40, 50, 60]
window_size = 3

# Bioinformatics senarior 2: calculate the moving average of the hydrophobicity scores for amino acids
def calculate_hydrophobicity_score(aa):
    """
    This function would calculate the moving average of the hydrophobicity scores for amino acids.
    You can define your own scoring system based on your needs.
    Here, we'll use a psuedo placeholder dictionary for illustration.
    aa: the abbreviation of an amino acid
    """
    hydrophobicity_scores = {'A': 0.5, 'L': 0.8, 'I': 0.7, 'F': 0.9, 'V': 0.6, 'E': 0.2, 'K': 0.3, 'S': 0.4}
    return hydrophobicity_scores.get(aa, 0.0)

def identify_hydrophobic_domains(protein_sequence, window_size, threshold):
    hydrophobic_domains = []
    window = deque(maxlen=window_size)
    current_score = 0.0
    for aa in protein_sequence:
        window.append(aa)
        current_score += calculate_hydrophobicity_score(aa)
        if len(window) == window_size:
            average_score = current_score / window_size
            if average_score >= threshold:
                hydrophobic_domains.append("".join(window))
            first_aa = window.popleft() # Remove the first amino acid in the window to slide it
            current_score -= calculate_hydrophobicity_score(first_aa)
    return hydrophobic_domains

# Example usage:
protein_sequence = "EEEFSEAKLIVSFEKAAAFIVEELII"
window_size = 3
threshold = 0.5

hydrophobic_domains = identify_hydrophobic_domains(protein_sequence, window_size, threshold)
print("Hydrophobic domains:", hydrophobic_domains)
