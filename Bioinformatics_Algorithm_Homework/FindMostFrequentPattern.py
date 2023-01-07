# Frequent Words Problem: Find the most frequent K-mers in a string. 
# Input: A string Text and an integer k. 
# Output: All most frequent k-mers in Text.


# Find the most frequent 2-mers in a string
seq = "GATCCAGATCCCCATAC"
two_mer = {}
i = 0
for i in range(len(seq)-2+1) : # The last position should be 15; list(range(len(sequence)-2+1))

    now = seq[i: i+2] # When i = 1, [1: 3]extract the first two bases, excluding the third bases
    # print(now)
    if now in two_mer:
        count = two_mer.get(now) # get() return the value
        two_mer[now] = count + 1 # Assign the key as the now and count + 1 as the value
    else:
        two_mer[now] = 1 # Assign now as the key, and 1 as the value
        
print(two_mer)
# {'GA': 2, 'AT': 3, 'TC': 2, 'CC': 4, 'CA': 2, 'AG': 1, 'TA': 1, 'AC': 1}
