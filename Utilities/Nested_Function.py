# Topic:
# Nested functions
def outer(…):
    """…"""
    x = …

    def inner(…):
        """…"""
        y = x ** 2  
    return … 

# Scenario: do the same process a number of times within a function
def mod3plus7(x1, x2, x3, xN):
    """Returns the remainder plus 5 of N values."""
    new_x1 = x1 % 3 + 7
    new_x2 = x2 % 3 + 7
    new_x3 = x3 % 3 + 7
    """..."""
    new_xN = xN % 3 + 7
    return (new_x1, new_x2, new_x3, new_xN)

# We can use the nested function to write cleaner codes
def mod3plus7(x1, x2, x3, xN):
    """Returns the remainder plus 5 of N values."""
    def inner(x):
        """Returns the remainder plus 5 of a values."""
        return x % 3 + 7 
    return (inner(x1), inner(x2), inner(x3), inner(xN))

print(mod3plus7(9, 3, 27, 90)
