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
