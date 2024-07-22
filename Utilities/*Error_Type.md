# Topic: 3 types of errors in Python programming
## Syntax Errors
The syntax errors are detected by the compiler or the interpreter.

**Common reasons**: 
- Wrongly written keywords
  ```
  Cell In[17], line 3
  return y
  ^
  SyntaxError: 'return' outside function
  ```
- Wrong function names
  ```python
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
- Two starred expressions in assignment
  ```
  SyntaxError: two starred expressions in assignment
  ```
- Wrong use of an operator
- Forgetting parentheses in a function call
- Not putting strings in single quotes or double quotes

## Runtime Errors
- No compatible binary
  ```
  DEBUG [main] Printing verbose output
  Traceback (most recent call last):
    File "/Users/your_name/.pyenv/versions/3.8.18/bin/kb", line 8, in <module>
      sys.exit(main())
    File "/Users/your_name/.pyenv/versions/3.8.18/lib/python3.8/site-packages/ngs_tools/logging.py", line 62, in inner
      return func(*args, **kwargs)
    File "/Users/your_name/.pyenv/versions/3.8.18/lib/python3.8/site-packages/kb_python/main.py", line 1583, in main
      raise UnsupportedOSError(
    kb_python.config.UnsupportedOSError: Failed to find compatible kallisto binary. Provide a compatible binary with the --kallisto option or    run kb compile."
  ```

## Logical Errors


