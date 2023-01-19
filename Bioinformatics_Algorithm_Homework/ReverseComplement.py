# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):   
    rev = Reverse(Pattern)
    comp = Complement(rev)
    return(comp)

def Reverse(Pattern):
    reversed_Pattern = Pattern[::-1]
    return reversed_Pattern

MAPPING = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}

def Complement(Pattern):
    return ''.join(MAPPING[c] for c in Pattern)

# Test the function
ReverseComplement("ACTG")
