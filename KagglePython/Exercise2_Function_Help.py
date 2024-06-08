# SETUP
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
    return round(num, 2) # return
    # "pass" is a keyword that does literally nothing. We used it as a placeholder because after we begin a code block, Python requires at least one line of code.
    pass

# Check your answer
q1.check()


## Question 2
# The help for round says that ndigits (the second argument) may be negative. What do you think will happen when it is? Try some examples in the following cell.
round(338424, ndigits = -3)
# As you've seen, ndigits=-1 rounds to the nearest 10, ndigits=-2 rounds to the nearest 100 and so on. Where might this be useful? 
# Suppose we're dealing with large numbers:
# The area of Finland is 338,424 km²
# The area of Greenland is 2,166,086 km²
# We probably don't care whether it's really 338,424, or 338,425, or 338,177. All those digits of accuracy are just distracting. We can chop them off by calling round() with ndigits=-3:
# The area of Finland is 338,000 km²
# The area of Greenland is 2,166,000 km²
