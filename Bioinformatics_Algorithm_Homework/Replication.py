# Pattern Matching Problem: Find all occurrences of a pattern in a string. 
# Input: Strings Pattern and Genome.
# Output: All starting positions in Genome where Pattern appears as a substring.

def PatternMatching(Pattern, Genome):
    start_pos = []
    start_pos = [pos for pos in range(len(Genome)-len(Pattern)+1) if Genome[pos:pos+len(Pattern)] == Pattern] 
    return start_pos

# Test the function
PatternMatching(Pattern = "ATAT", Genome = "GATATATGCATATACTT")
