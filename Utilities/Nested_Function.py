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

# We can use the nested function to write cleaner codes that can be scaled to a large number of repetitive computations
def mod3plus7(x1, x2, x3, xN):
    """Returns the remainder plus 5 of N values."""
    def inner(x):
        """Returns the remainder plus 5 of a values."""
        return x % 3 + 7 
    return (inner(x1), inner(x2), inner(x3), inner(xN))

print(mod3plus7(9, 3, 27, 90)

# Returning functions - enclosing scope
def raise_val(n):
    """Return the inner function."""
    def inner(x):
        """Raise x to the power of n."""
        raised = x **n
        return raised
    return inner

square_func = raise_val(2)
cube_func = raise_val(3)
print(square_func(3), cube_func(3))  # 9 27

# Use nonlocal keyword to create and change the names in an enclosing scope
# We change the value of k in the inner function and since we use the nonlocal keyword, this change is also effective for the value of k in the enclosing scope.
def outer():
    """Prints the value of n."""
    k = 6
    def inner():
        nonlocal k
        k = 9
        print(k)
    inner()
    print(k) 

outer() # 9 9

def outer2():
    """Prints the value of n."""
    k = 6
    def inner():
        k = 9
        print(k)
    inner()
    print(k) 

outer2() # 9 6
