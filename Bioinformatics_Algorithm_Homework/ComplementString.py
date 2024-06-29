# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
# 1st approach
def Complement(Pattern):
    complementary_Pattern = ""
    for char in Pattern:
        if char == "A":
            complementary_Pattern = complementary_Pattern + "T"
        elif char == "T":
            complementary_Pattern = complementary_Pattern + "A"
        elif char == "C":
            complementary_Pattern = complementary_Pattern + "G"
        elif char == "G":
            complementary_Pattern = complementary_Pattern + "C"
    return complementary_Pattern
# Test the function
Complement("CTAG")

# 2nd approach
MAPPING = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}

def Complement(Pattern):
    return ''.join(MAPPING[c] for c in Pattern)
# Test the function
Complement("CTAG")
