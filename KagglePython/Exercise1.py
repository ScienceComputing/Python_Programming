from learntools.core import binder; binder.bind(globals())
from learntools.python.ex1 import *
print("Setup complete! You're ready to start question 0.")


## Question 0
# create a variable called color with an appropriate value on the line below
# (Remember, strings in Python must be enclosed in 'single' or "double" quotes)
color = "blue"

# Check your answer
q0.check()


## Question 1
pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius = diameter/2

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = pi * (radius ** 2)

# Check your answer
q1.check()
