# Topic:
# Scope
# Global scope means a name that is defined in the main body of a script
# Local scope means a name which is defined inside a function, so once the execution of a function is done, any name inside the local scope ceases to exist
# Built-in scope means a name that is defined in the pre-defined built-ins module, such as print and sum
# LEGB rule: when we reference a name in a function call, first of all,  the local scope is searched, then the enclosing scope is searched if there are any nested functions, then the global scope is searched, and last, the built-in scope is searched.
# Assigning names will only create or change local names, unless they are declared in global or nonlocal statements using the keyword global or the keyword nonlocal (in the nested functions).

new_value = 8
def cubic(parameter): 
    """Returns the cubic of a number."""
    new_value = parameter ** 3
    return new_value

cubic(1)
new_value # 8

new_value = 2
def cubic(parameter): 
    """Returns the cubic of a number."""
    new_value_2 = new_value ** 3
    return new_value_2

cubic(1) # 8
new_value_2 # NameError: name 'new_value_2' is not defined.

# Alter the value of a global name within a function call 
new_value = 2
def cubic(parameter): 
    """Returns the cubic of a number."""
    global new_value # Alter the value of a global name  
    new_value = new_value ** 3
    return new_value

cubic(1) # 8
new_value # 8

chemical_perturbation = None
def set_chemical_perturbation(perturbation_name):
    """Set the global variable chemical_perturbation to the specified perturbation."""
    global chemical_perturbation
    chemical_perturbation = perturbation_name

set_chemical_perturbation("Treatment X")
chemical_perturbation # 'Treatment X'

# Print a list of names that are in the built-in scope
Import builtins
dir(builtins)
# sum; range; tuple; False

