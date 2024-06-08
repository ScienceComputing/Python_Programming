# Topic: 3 types of errors in Python programming
## Syntax Errors
The syntax errors are detected by the compiler or the interpreter.

**Common reasons**: 
- Wrongly written keywords or functions
  ```
  NameError                                 Traceback (most recent call last)
  Cell In[18], line 1
  ----> 1 devide_two(98.920)
  NameError: name 'devide_two' is not defined
  ```
- Setting extra parameters
  ```
  TypeError                                 Traceback (most recent call last)
  Cell In[14], line 4
  2 y = 5
  3 # Which of the two variables above has the smallest absolute value?
  ----> 4 smallest_abs = min(abs(x, y))
  TypeError: abs() takes exactly one argument (2 given)
  ```
- Wrong use of an operator
- Forgetting parentheses in a function call
- Not putting strings in single quotes or double quotes

## Runtime Errors

## Logical Errors

