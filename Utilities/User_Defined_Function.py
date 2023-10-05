# Topic:
# Define functions without parameters/with one parameter/that return a value/with multiple arguments and that return multiple values

def function_name(): # Function header
    new_value = 2 ** 8 # Function body
    print(new_value)
square()


def function_name(parameter): 
    new_value = parameter ** 8 
    print(new_value)

square(2)

# When we define a function, we write parameters in the function header. When we call a function, we pass arguments into the function. 

def function_name(parameter): 
    new_value = parameter ** 8 
    return new_value

result = square(2)
print(result)

# Docstrings serve as documentation of our function so that others who read our function's doctoring understand what our function does, without having to trace through all the code
def function_name(parameter): 
    """Return the 8th power of a number."""
    new_value = parameter ** 8 
    return new_value
