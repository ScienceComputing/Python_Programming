# It's a common practice to use this attribute `__name__` to allow or prevent parts of code from being run when the module is imported versus executed directly.

# touch moduleabc.py
# vim moduleabc.py
# Inside the moduleabc.py, insert the following python code:
def abc_function():
    print("This is a abc function")

if __name__ == '__main__':
    print("This is the main part of the script")

# Open the python from command line interface
# __name__ is set to the name of the module. 
# Hence, as our script is named moduleabc.py, __name__ will be 'moduleabc' when it is imported. 
import moduleabc as mabc
mabc.abc_function()
# This is a abc function
