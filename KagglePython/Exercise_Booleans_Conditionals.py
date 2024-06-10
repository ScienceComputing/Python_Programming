## References:
# https://github.com/ScienceComputing/Python_Programming/blob/68201ab5a7ec56c128425f736fd34298c1258548/Utilities/List/*List_Comprehension.py#L87

## Question 1
def sign(num=-1):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    else:
        return 1

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies <= 1:
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")
    # Use a succinct conditional expression
    # print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
    return total_candies % 3

to_smash(91)
to_smash(1)
