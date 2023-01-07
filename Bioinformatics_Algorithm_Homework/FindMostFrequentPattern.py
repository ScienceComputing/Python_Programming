# Frequent Words Problem: Find the most frequent K-mers in a string. 
# Input: A string Text and an integer k. 
# Output: All most frequent k-mers in Text.

# Find the most frequent 2-mers in a string (standard)
seq = "GATCCAGATCCCCATAC"
freq = {}
n = len(seq)
for i in range(n-2+1):
    two_mer = seq[i:i+2] # Create a k-mers string
    freq[two_mer] = 0 # key:value: assign the variable k_mer to the key, and 0 to the value
    for i in range(n-2+1):  
        if seq[i:i+2] == two_mer:
            freq[two_mer] = freq[two_mer] + 1
print(freq)
# {'GA': 2, 'AT': 3, 'TC': 2, 'CC': 4, 'CA': 2, 'AG': 1, 'TA': 1, 'AC': 1}


# Find the most frequent 2-mers in a string (variant)
seq = "GATCCAGATCCCCATAC"
two_mer = {}
for i in range(len(seq)-2+1) : # The last position should be 15; list(range(len(sequence)-2+1))
    now = seq[i: i+2] # When i = 1, [1: 3]extract the first two bases, excluding the third bases
    # print(now)
    if now in two_mer:
        count = two_mer.get(now) # get() return the value
        two_mer[now] = count + 1 # key:value: assign the variable now to the key and count + 1 to the value
    else:
        two_mer[now] = 1 # key:value: assign the variable now to the key, and 1 to the value
        
print(two_mer)
# {'GA': 2, 'AT': 3, 'TC': 2, 'CC': 4, 'CA': 2, 'AG': 1, 'TA': 1, 'AC': 1}


# Find the most frequent k-mers in a string (standard)
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    # Step1: loop through the text and assign 0 to the frequency of each k-mers 
    for i in range(n-k+1):
        k_mer = Text[i:i+k] # Create a k-mers string
        freq[k_mer] = 0 # key:value: assign the variable k_mer to the key, and 0 to the value

        # Step2: loop through the text and cumulatively count the frequency of each k-mers
        for i in range(n-k+1):  
            if Text[i:i+k] == k_mer:
                freq[k_mer] = freq[k_mer] + 1
    return freq

FrequencyMap(Text = "GATCCAGATCCCCATAC", k = 2)
# {'GA': 2, 'AT': 3, 'TC': 2, 'CC': 4, 'CA': 2, 'AG': 1, 'TA': 1, 'AC': 1}


# Find the most frequent k-mers in a string (variant 1)
def FrequencyMap2(Text, k):
    k_mer = {}
    for i in range(len(Text)-2+1) : # The last position should be 15; list(range(len(sequence)-2+1))
        now = Text[i: i+2] # When i = 1, [1: 3]extract the first two bases, excluding the third bases
        # print(now)
        if now in k_mer:
            count = k_mer.get(now) # get() return the value
            k_mer[now] = count + 1 # key:value: assign the variable now to the key and count + 1 to the value
        else:
            k_mer[now] = 1 # key:value: assign the variable now to the key, and 1 to the value
    return(k_mer)

FrequencyMap2(Text = "GATCCAGATCCCCATAC", k = 2)
# {'GA': 2, 'AT': 3, 'TC': 2, 'CC': 4, 'CA': 2, 'AG': 1, 'TA': 1, 'AC': 1}


# Find the most frequent k-mers in a string (variant 2)
def FrequencyMap3(Text, k): 
    freq = {}
    for i in range(len(Text)-k+1):
        k_mer = Text[i:i+k]
        if k_mer in freq:
          freq[k_mer] += 1
        else:
          freq[k_mer] = 1
    return freq
FrequencyMap3(Text = "GATCCAGATCCCCATAC", k = 2)
# {'GA': 2, 'AT': 3, 'TC': 2, 'CC': 4, 'CA': 2, 'AG': 1, 'TA': 1, 'AC': 1}


# Find the most frequent k-mers in a string (variant 3)
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i : i+len(Pattern)] == Pattern:
            count += 1
    return count

def FrequencyMap4(Text, k):
    freq = {}
    for i in range(len(Text)-k+1):
        k_mer = Text[i : i+k]
        freq[k_mer] = 0
    for k_mer in freq:
        count = PatternCount(Text, k_mer)
        freq[k_mer] = count
    return freq
# {'GA': 2, 'AT': 3, 'TC': 2, 'CC': 4, 'CA': 2, 'AG': 1, 'TA': 1, 'AC': 1}
