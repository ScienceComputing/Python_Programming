# Topic:
# Define functions without parameters/with one parameter/that return a value/with multiple arguments and that return multiple values

# 1: functions without parameters
def function_without_parameter(): # Function header
    new_value = 2 ** 8 # Function body
    print(new_value)
square()


# 2: functions with one parameter
def function_with_one_parameter(parameter): 
    new_value = parameter ** 8 
    print(new_value)

square(2)

# When we define a function, we write parameters in the function header. When we call a function, we pass arguments into the function.  . 

# 3: functions that return a value
def function_return_one_value(parameter): 
    new_value = parameter ** 8 
    return new_value

result = square(2)
print(result)

# Docstrings serve as documentation of our function so that others who read our function's doctoring understand what our function does, without having to trace through all the code
def function_with_docstring(parameter): 
    """Return the 8th power of a number."""
    new_value = parameter ** 8 
    return new_value

# 4: function with multiple parameters
# Notice that the order in which the arguments are passed correspond to the order of the parameters in the function header
def function_with_multiple_parameters(parameter_1, parameter_2): 
    """Return the nth power of a number."""
    new_value = parameter_1 ** parameter_2 
    return new_value

result = square(2, 8)
print(result)

# 5: function with multiple parameters that return multiple values 
def function_with_multiple_parameters_return_multiple_values(parameter_1, parameter_2): 
    """Return the nth power of a number, and vice versa."""
    new_value_1 = parameter_1 ** parameter_2 
    new_value_2 = parameter_2 ** parameter_1

    new_tuple  = (new_value_1, new_value_2)

    return new_tuple

result = square(2, 8)
print(result[0])
print(result[1])
