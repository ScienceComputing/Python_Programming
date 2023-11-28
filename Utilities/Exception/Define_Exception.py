class DivisionError(ValueError):
    pass

class IntegerDivisionError(DivisionError):
    pass

class Divider:
    def divide(self, a, b):
        if b == 0:
            raise DivisionError("Division by zero!")
        if a % b != 0:
            raise IntegerDivisionError("Result is not an integer!")
        return a // b

divider = Divider()
result = divider.divide(10, 2)  
result = divider.divide(10, 3)  
# IntegerDivisionError: Result is not an integer!
result = divider.divide(10, 0)  
# DivisionError: Division by zero!
