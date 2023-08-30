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

# Bioinformatics senarior: calculate the moving average of the quality scores of base calls in DNA sequencing
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
