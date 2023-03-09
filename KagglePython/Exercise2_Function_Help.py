# SETUP. You don't need to worry for now about what this code does or how it works.
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex2 import *
print('Setup complete.')

## Question 1
# Complete the body of the following function according to its docstring.
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    return(round(num, 2))
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    pass

# Check your answer
q1.check()
