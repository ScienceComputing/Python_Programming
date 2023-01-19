# Input:  A string Pattern
# Output: The reverse of Pattern
# First approach
def Reverse(Pattern):
    reversed_Pattern = Pattern[::-1]
    return reversed_Pattern
# Test the function
Reverse("ATCGA")

# Second approach
def Reverse(Pattern):
    reversed_Pattern = ''
    for char in Pattern:
        reversed_Pattern = char + reversed_Pattern
    return reversed_Pattern
# Test the function
Reverse("ATCGA")
