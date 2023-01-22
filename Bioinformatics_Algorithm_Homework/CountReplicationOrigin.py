# Research has shown that the region of the bacterial genome encoding ori is typically a few hundred nucleotides long. 
# Our plan is to begin with a bacterium in which ori is known, and then determine what makes this genomic region special，
# in order to design a computational approach for finding ori in other bacteria. 
# Our example is Vibrio cholerae, the pathogenic bacterium that causes cholera.

# First, create a string variable called ori that is equal to the Vibrio cholerae ori. 
# Then, print the length of ori
ori = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
print(len(ori))

# Now use an if statement, to determine whether the Text[i:i+k] matches Pattern; if it does, then we increment count.
if Text[i:i+len(Pattern)] == Pattern:
    count = count+1

# Print all even numbers between 0 and 100
# range(n) runs from 0 to n-1.
for number in range(51): 
    print(2*number)

# In general, the final k-mer of a string of length n begins at position n-k; 
# for example, the final 3-mer of "GACCATACTG", which has length 10, begins at position 10 - 3 = 7. 
# This observation implies that the window should slide between position 0 and position len(Text)-len(Pattern).
# Slide our window from position 0 to len(Text)-len(Pattern)
count = 0
for i in range(len(Text)-len(Pattern)+1):
    if Text[i:i+len(Pattern)] == Pattern:
        count = count+1 

# To put everything together into a function, called PatternCount.
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

# Now, set Text equal to the ori of Vibrio cholerae and Pattern equal to "TGATCA"
print(PatternCount(ori, "TGATCA"))


# How many combined occurrences of "ATGATCAAG" and "CTTGATCAT" in the proposed ori region of Thermotoga petrophila?
Text = "AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGA"

# Estimate the number of times that "ATGATCAAG" occurs in Text.
count_1 = PatternCount(Text = Text, Pattern = "ATGATCAAG")

# Estimate the number of times that "CTTGATCAT" occurs in Text. 
count_2 = PatternCount(Text = Text, Pattern = "CTTGATCAT")

# Estimate the total number of times that "ATGATCAAG" and "CTTGATCAT" occurs in Text. 
print(count_1 + count_2)
