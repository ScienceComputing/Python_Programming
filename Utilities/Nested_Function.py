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
def mod3plus7(x1, x2, x3, xN)
    """Returns the remainder plus 5 of three values."""
    new_x1 = x1 % 3 + 7
    new_x2 = x2 % 3 + 7
    new_x3 = x3 % 3 + 7
    """..."""
    new_xN = xN % 3 + 7
    return (new_x1, new_x2, new_x3, new_xN)
