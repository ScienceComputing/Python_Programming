class DivisionError(ValueError):
    pass

class IntegerDivisionError(DivisionError):
    pass

class Divider:
    def divide(self, a, b):
        if b == 0:
            raise DivisionError("Division by zero!")
        if a % b != 0: # Check if the remainder of the division of a by b is not equal to zero. 
            raise IntegerDivisionError("Result is not an integer!")
        return a // b # Floor division: return the largest integer that is less than or equal to the result.

divider = Divider()
result = divider.divide(10, 2)  
result = divider.divide(10, 3)  
# IntegerDivisionError: Result is not an integer!
result = divider.divide(10, 0)  
# DivisionError: Division by zero!
